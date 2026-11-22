# MindView web site

A redesign of [MindviewLLC.com](https://www.mindviewllc.com), generated from Markdown by one Python script.
Trial site: <https://mindviewllc-site.netlify.app/>

## Edit

- Each page is `content/<name>/index.md`, with a `title` and a `weight` in its front matter.
  `weight` sets the order of the Previous and Next links.
- A file placed beside `index.md`, such as `content/about/W9.pdf`, is published in that page's folder.
- A line that reads `<!-- include: bio.md -->` is replaced by the text of that file from the page's folder.
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

## Moving to the custom domain

The trial site carries a `noindex` tag. To go live:

1. Set `preview = false` in `site.toml` and push.
2. In Netlify, move the `www.mindviewllc.com` domain from the old site to this one.
