# BHG

Government portal (**GovBHG**) of the **Baekhyeon Hwarang Special Administrative Region**
(백현화랑특별행정구 / 柏峴화랑特別行政區 / 柏岘화랑特别行政区), in English, Korean, Traditional Chinese and Simplified Chinese.

The layout, information architecture and visual design follow the GovHK portal: home pages for
*Residents*, *Business & Trade* and *Non-Residents*, category / topic pages with the left-hand menu,
and service pages such as *Online Application for BHG SAR Passport*. No HKSAR logos, images or text are
reused; all code, artwork and wording are original.

## Structure

| Path | Purpose |
|---|---|
| `index.html` | Redirects to a language folder by browser language |
| `en/` `ko/` `zh-hant/` `zh-hans/` | Generated site per language (267 pages each) |
| `assets/` | `site.css`, `site.js`, flag image, favicon, generated skyline art |
| `tools/data.py` | **All content** (site tree, home sections, passport page text) in 3 languages |
| `tools/build.py` | Page templates and generator |
| `tools/gen_t2s.py` | Regenerates the Traditional to Simplified map (needs OpenCC; only when Chinese text changes) |

Simplified Chinese is derived from the Traditional text, so only English, Korean and Traditional are written by hand.

## Build

```sh
python3 tools/build.py
```

Pure static HTML/CSS/JS, no runtime dependencies (Python 3.6+).

## Deploy

Served by GitHub Pages from the `main` branch root (`.nojekyll` is included).
