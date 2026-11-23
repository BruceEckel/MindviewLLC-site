# MindView web site

The source of [MindviewLLC.com](https://www.mindviewllc.com), generated from Markdown by one Python script.

## Edit

- Each page is `content/<name>.md`, with a `title` and a `weight` in its front matter.
  `weight` sets the order of the Previous and Next links.
- A page that needs other files keeps them in a folder with the page's name.
  `content/about/W9.pdf` is published at `/about/W9.pdf`, so `about.md` links to it as `W9.pdf`.
- A line that reads `<!-- include: bio.md -->` is replaced by the text of that file from the page's folder, `content/about/bio.md` for `about.md`.
- The menu and the home page cards are in `site.toml`.
- Write a link to another page from the site root: `[Speaking](/speaking)`.
  The build stops with an error if a link matches no page.
- For an email address, write `<button type="button" class="email-button" data-to="mindview">Show email address</button>`.
  `data-to` is `mindview` or `bruce`; the addresses are encoded in `static/js/site.js`.

## Build

Install [uv](https://docs.astral.sh/uv/), then:

```
uv run build.py --serve    # Preview at http://localhost:8000, rebuilds when a file changes
uv run build.py            # Build into dist/
uv run pytest              # Check the build
```

## Check links

```
uv run check_links.py             # Check every external link
uv run check_links.py --markdown  # Print the report as Markdown
```

The script reads `content/` and `site.toml` and requests each external URL once.
It groups the report as failed, blocked, and redirected.
A blocked URL answered 403 or 429, so open it in a browser to decide.
The exit status is 1 when a URL failed.

The `Links` workflow runs the check every Monday and on demand from the Actions tab.
If any URL failed, it opens an issue titled "Broken links found" with the report.
If that issue is already open, it adds the report as a comment.
The check stays out of `pytest` and out of the Netlify build.

## Deploy

Netlify builds and publishes the site on every push to `main`, using the command in `netlify.toml`.
A GitHub Actions workflow runs the tests on the same push.

## Layout

| Path | Contents |
|---|---|
| `build.py` | The generator |
| `site.toml` | Settings, menu, and home page cards |
| `content/` | The pages, in Markdown, with the files they link to |
| `templates/` | Jinja2 page templates |
| `static/` | CSS, JavaScript, and images, copied as they are |

## Domains

Netlify serves the site at `www.mindviewllc.com`, the primary domain, with `mindviewllc.com` and `www.mindviewinc.com` as aliases.
All three use Netlify DNS.
`static/_redirects` sends the project's `mindviewllc-site.netlify.app` address to the primary domain.

`preview = false` in `site.toml` lets search engines index the site.
Setting it to `true` adds a `noindex` tag to every page, for a trial copy.
