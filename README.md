# SCIL Machinery website

Static bilingual site (English + Arabic RTL) for [SCIL Machinery](https://scil-machinery.com/), beverage packaging lines from preform to pallet.

- English pages: repository root (`index.html`, `equipment.html`, `equipment/*.html`, …)
- Arabic pages: `ar/` (`dir="rtl"`)
- Styles and behaviour: `assets/css/site.css`, `assets/js/site.js`

## Editing content

Pages are generated once from Python data files and committed as plain HTML, so hosting needs no build step.

- English content: `_src/data.py`
- Arabic content: `_src/ar_data.py`
- Shared header, footer, form and UI strings: `_src/parts.py`

Regenerate both languages after editing:

```bash
python _src/build.py
```

## Deployment

Every push to `main` publishes the site files to GitHub Pages through `.github/workflows/pages.yml`.

Design system: see `DESIGN.md`.
