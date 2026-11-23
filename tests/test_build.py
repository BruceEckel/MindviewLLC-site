import re
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
import build  # noqa: E402

BASE = "/MindviewLLC-site"
SLUGS = [
    "about",
    "bibliography",
    "devretreat",
    "media",
    "mindview",
    "quicklinks",
    "speaking",
]


@pytest.fixture(scope="module")
def dist(tmp_path_factory) -> Path:
    out = tmp_path_factory.mktemp("site") / "dist"
    build.build(out, base=BASE)
    return out


def pages(dist: Path) -> list[Path]:
    return sorted(dist.rglob("*.html"))


def read(dist: Path, slug: str) -> str:
    return (dist / slug / "index.html").read_text(encoding="utf-8")


def test_every_content_page_is_built(dist):
    sources = sorted(p.stem for p in build.CONTENT.glob("*.md"))
    assert sources == SLUGS
    for slug in SLUGS:
        assert (dist / slug / "index.html").is_file()
    assert (dist / "index.html").is_file()
    assert (dist / "404.html").is_file()


def test_internal_links_carry_the_base_and_resolve(dist):
    for page in pages(dist):
        html = page.read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="(/[^"]*)"', html):
            assert target.startswith(BASE + "/"), (page, target)
            path = target.removeprefix(BASE).split("#")[0].split("?")[0]
            found = dist / path.lstrip("/")
            assert found.is_file() or (found / "index.html").is_file(), (page, target)


def test_relative_links_resolve(dist):
    for page in pages(dist):
        html = page.read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="([^"/#][^":]*)"', html):
            assert (page.parent / target).is_file(), (page, target)


def test_home_page_shows_the_cards(dist):
    html = (dist / "index.html").read_text(encoding="utf-8")
    assert html.count('class="card"') == 9
    assert "Exceptional Learning Experiences</h1>" in html


def test_files_beside_a_page_are_published(dist):
    for name in ("W9.pdf", "MidEngrCoverHi.JPG", "UnixReviewCoverHi.JPG"):
        assert (dist / "about" / name).is_file()
    assert not list(dist.rglob("*.md"))


def test_the_redirects_are_published(dist):
    rules = (dist / "_redirects").read_text(encoding="utf-8")
    assert "/events/  /quicklinks/#conferences  301" in rules
    assert 'id="conferences"' in read(dist, "quicklinks")
    for address in ("/categories/", "/tags/"):
        assert f"{address}  /  301" in rules
    for host in ("mindviewllc-site.netlify.app", "www.mindviewinc.com"):
        for scheme in ("https", "http"):
            rule = f"{scheme}://{host}/*  https://www.mindviewllc.com/:splat  301!"
            assert rule in rules


def test_the_bio_is_included_in_the_about_page(dist):
    assert "Very Short Bio" in read(dist, "about")
    assert "include:" not in read(dist, "about")
    assert not (dist / "about" / "bio").exists()


def test_no_published_file_exposes_an_email_address(dist):
    address = re.compile(r"[\w.+-]+@[\w-]+\.[a-z]{2,}|mailto:|&#\d+;", re.IGNORECASE)
    texts = [p for p in dist.rglob("*") if p.suffix in {".html", ".js", ".css", ".xml"}]
    assert len(texts) >= 12
    for path in texts:
        assert not address.search(path.read_text(encoding="utf-8")), path
    for slug in ("about", "mindview", "devretreat", "quicklinks", "speaking"):
        assert 'class="email-button"' in read(dist, slug)


def test_stylesheet_and_script_addresses_carry_a_version(dist):
    html = read(dist, "about")
    assert re.search(r'/css/site\.css\?v=[0-9a-f]{10}"', html)
    assert re.search(r'/js/site\.js\?v=[0-9a-f]{10}"', html)


def test_each_page_carries_its_own_description(dist):
    found = set()
    for slug in SLUGS:
        html = read(dist, slug)
        match = re.search(r'<meta name="description" content="([^"]+)">', html)
        assert match, slug
        assert f'<meta property="og:description" content="{match[1]}">' in html
        found.add(match[1])
    assert len(found) == len(SLUGS)


def test_the_media_page_is_grouped_by_year(dist):
    html = read(dist, "media")
    for heading in ("start-here", "2026", "2000-to-2009"):
        assert f'id="{heading}"' in html, heading
    assert "On this page" in html
