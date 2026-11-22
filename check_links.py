"""Check the external links of the site.

Run it with `uv run check_links.py`. Add `--markdown` for a report you can paste into a GitHub issue.
The script reads `content/**/*.md` and `site.toml`, fetches each distinct http(s) URL once, and prints a report.
The exit status is 1 when at least one URL failed.
Redirects and blocked URLs are warnings.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import threading
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).parent
TIMEOUT = 20
WORKERS = 8
PER_HOST = 2
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
FALLBACK_STATUSES = {403, 405, 501}
BLOCKED_STATUSES = {403, 429}
CLASSES = ("failed", "blocked", "redirected", "ok")

# A URL inside Markdown link parentheses. One level of nested parentheses is allowed.
MARKDOWN_LINK = re.compile(
    r"\]\(\s*<?(https?://[^\s)<>]*(?:\([^\s)<>]*\)[^\s)<>]*)*)"
)
ATTRIBUTE = re.compile(r"""\b(?:href|src)\s*=\s*["'](https?://[^"']+)["']""", re.I)
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")


@dataclass(frozen=True)
class Source:
    path: str
    line: int

    def __str__(self) -> str:
        return f"{self.path}:{self.line}"


@dataclass
class Result:
    url: str
    sources: list[Source] = field(default_factory=list)
    kind: str = "failed"
    status: str = ""
    final_url: str = ""


def find_urls(line: str) -> list[str]:
    """Return the external URLs on one line of Markdown or HTML."""
    found: list[str] = []
    for pattern in (MARKDOWN_LINK, ATTRIBUTE, AUTOLINK):
        found.extend(html.unescape(m.group(1)) for m in pattern.finditer(line))
    return found


def collect_markdown(root: Path) -> list[tuple[str, Source]]:
    pairs: list[tuple[str, Source]] = []
    for path in sorted((root / "content").rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), start=1):
            for url in dict.fromkeys(find_urls(line)):
                pairs.append((url, Source(rel, number)))
    return pairs


def toml_urls(settings: dict) -> list[str]:
    urls = [item[1] for item in settings.get("nav", [])]
    urls += [card.get("url", "") for card in settings.get("card", [])]
    return [u for u in urls if u.startswith(("http://", "https://"))]


def collect_site_toml(root: Path) -> list[tuple[str, Source]]:
    path = root / "site.toml"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    pairs: list[tuple[str, Source]] = []
    for url in toml_urls(tomllib.loads(text)):
        for number, line in enumerate(lines, start=1):
            if f'"{url}"' in line:
                pairs.append((url, Source("site.toml", number)))
    return pairs


def collect(root: Path) -> dict[str, Result]:
    """Map each distinct URL (fragment removed) to a Result that lists its sources."""
    results: dict[str, Result] = {}
    for url, source in collect_markdown(root) + collect_site_toml(root):
        clean = urllib.parse.urldefrag(url).url
        result = results.setdefault(clean, Result(clean))
        if source not in result.sources:
            result.sources.append(source)
    return results


class HostLimiter:
    """Allow at most `limit` requests at once to each host."""

    def __init__(self, limit: int) -> None:
        self._limit = limit
        self._lock = threading.Lock()
        self._semaphores: dict[str, threading.Semaphore] = {}

    def semaphore(self, url: str) -> threading.Semaphore:
        host = urllib.parse.urlsplit(url).hostname or ""
        with self._lock:
            return self._semaphores.setdefault(host, threading.Semaphore(self._limit))


def request(url: str, method: str) -> tuple[int, str]:
    """Send one request and return (status, final URL). HTTP errors become statuses."""
    req = urllib.request.Request(
        url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "*/*"}
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
            return response.status, response.geturl()
    except urllib.error.HTTPError as error:
        return error.code, error.url or url


def request_with_retry(url: str, method: str) -> tuple[int, str]:
    """Retry once on a timeout or connection error."""
    try:
        return request(url, method)
    except (urllib.error.URLError, OSError):
        return request(url, method)


def fetch(url: str) -> tuple[int, str]:
    status, final = request_with_retry(url, "HEAD")
    if status in FALLBACK_STATUSES:
        status, final = request_with_retry(url, "GET")
    return status, final


def is_youtube_video(url: str) -> bool:
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").removeprefix("www.")
    if host == "youtu.be":
        return True
    return host in ("youtube.com", "m.youtube.com") and parts.path == "/watch"


def check_youtube(result: Result) -> None:
    """YouTube answers 200 for removed videos, so ask the oEmbed endpoint."""
    query = urllib.parse.urlencode({"url": result.url, "format": "json"})
    status, _ = request_with_retry(f"https://www.youtube.com/oembed?{query}", "GET")
    notes = {403: "403 (private video)", 404: "404 (video removed)"}
    result.status = notes.get(status, str(status))
    if status in (200, 401):  # 401: the video exists with embedding turned off
        result.kind = "ok"
    elif status == 429:
        result.kind = "blocked"
    else:
        result.kind = "failed"


def normalize(url: str) -> tuple[str, str]:
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower().removeprefix("www.")
    return host, parts.path.rstrip("/")


def classify(result: Result, status: int, final: str) -> None:
    result.status = str(status)
    if status in BLOCKED_STATUSES:
        result.kind = "blocked"
    elif status >= 400:
        result.kind = "failed"
    elif normalize(result.url) != normalize(final):
        result.kind = "redirected"
        result.final_url = final
    else:
        result.kind = "ok"


def check(result: Result, limiter: HostLimiter) -> Result:
    with limiter.semaphore(result.url):
        try:
            if is_youtube_video(result.url):
                check_youtube(result)
            else:
                classify(result, *fetch(result.url))
        except Exception as error:  # Network failures vary widely; report them all.
            result.kind = "failed"
            result.status = describe_error(error)
    return result


def describe_error(error: Exception) -> str:
    reason = getattr(error, "reason", error)
    if isinstance(reason, TimeoutError):
        return "timeout"
    return f"{type(error).__name__}: {reason}"


def check_all(results: dict[str, Result]) -> list[Result]:
    limiter = HostLimiter(PER_HOST)
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        return list(pool.map(lambda r: check(r, limiter), results.values()))


def group(results: list[Result]) -> dict[str, list[Result]]:
    groups: dict[str, list[Result]] = defaultdict(list)
    for result in results:
        groups[result.kind].append(result)
    return groups


def summary(groups: dict[str, list[Result]]) -> str:
    total = sum(len(items) for items in groups.values())
    counts = ", ".join(f"{len(groups.get(k, []))} {k}" for k in CLASSES)
    return f"Checked {total} URLs: {counts}."


def render_text(groups: dict[str, list[Result]]) -> str:
    lines: list[str] = []
    for kind in CLASSES[:-1]:
        items = groups.get(kind, [])
        if not items:
            continue
        lines += [f"{kind.upper()} ({len(items)})", ""]
        for item in items:
            lines.append(f"  {item.url}")
            lines.append(f"    status: {item.status}")
            if item.final_url:
                lines.append(f"    now:    {item.final_url}")
            lines += [f"    from:   {source}" for source in item.sources]
            lines.append("")
    lines.append(summary(groups))
    return "\n".join(lines)


def render_markdown(groups: dict[str, list[Result]]) -> str:
    titles = {"failed": "Failed", "blocked": "Blocked (check in a browser)",
              "redirected": "Redirected"}
    lines: list[str] = ["# Link check report", ""]
    for kind in CLASSES[:-1]:
        items = groups.get(kind, [])
        if not items:
            continue
        lines += [f"## {titles[kind]} ({len(items)})", ""]
        for item in items:
            where = ", ".join(f"`{source}`" for source in item.sources)
            line = f"- <{item.url}>: {item.status}"
            if item.final_url:
                line += f", now <{item.final_url}>"
            lines.append(f"{line} ({where})")
        lines.append("")
    lines.append(summary(groups))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check the external links of the site.")
    parser.add_argument("--markdown", action="store_true",
                        help="print the report as GitHub-flavored Markdown")
    args = parser.parse_args()

    results = collect(ROOT)
    print(f"Found {len(results)} distinct URLs.", file=sys.stderr)
    groups = group(check_all(results))
    print(render_markdown(groups) if args.markdown else render_text(groups))
    return 1 if groups.get("failed") else 0


if __name__ == "__main__":
    sys.exit(main())
