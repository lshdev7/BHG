# BHG

Government portal homepage of the **Baekhyeon Hwarang Special Administrative Region**
(백현화랑특별행정구 / 柏峴화랑特別行政區 / 柏岘화랑特别行政区), in English, Korean, Traditional Chinese and Simplified Chinese.

The layout and information architecture follow the GovHK residents homepage (header, language bar,
search, mega menu, banner carousel, quick links, online services, forms, information & services,
guidebooks, features, footer). No HKSAR assets, logos or text are reused; all content is original.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | Redirects to `en/`, `ko/`, `zh-hant/` or `zh-hans/` by browser language |
| `en/` `ko/` `zh-hant/` `zh-hans/` | Generated pages per language |
| `assets/` | `site.css`, `site.js`, flag image, favicon |
| `tools/build.py` | Generator — **edit content here, then rebuild** |

## Build

```sh
python3 tools/build.py
```

Pure static HTML/CSS/JS, no dependencies. Links without a target page show an "under construction" notice.

## Deploy

Served by GitHub Pages from the `main` branch root (`.nojekyll` is included).
