# uapl-drill

## What this is
Public, standalone self-study quiz for the Singapore UAPL drone theory test. A single static HTML page with the
question bank embedded; no backend, no accounts. Unofficial; sourced only from public law, CAAS circulars,
ICAO/WMO and FAA material.

## Stack
- Vanilla HTML/CSS/JS, no build tooling beyond `src/build.py` (Python 3 stdlib)
- Progress in browser localStorage (key `uapl-drill-v1`), per device
- PWA: `docs/manifest.webmanifest` + `docs/sw.js` (offline cache, works only over http(s))
- Hosting: GitHub Pages, branch `main`, folder `/docs` (pushing main redeploys)
- Google Fonts is the only external load; it falls back to system fonts offline

## Structure
```
uapl-drill/
├── uapl-drill.html      # built single-file app (share this)
├── docs/                # built PWA, published by GitHub Pages at royhew.github.io/uapl-drill
├── questions/q_*.json   # question bank, one file per module (q_extra.json = extra Air Law permit/licence set)
└── src/
    ├── template.html    # page shell; /*__DATA__*/ and /*__FISH__*/ placeholders
    ├── build.py         # validates questions, writes uapl-drill.html and docs/
    └── sw.js, manifest.webmanifest, icons, fish160.png
```

## Build / Run / Deploy
```bash
python3 src/build.py          # rebuild after editing questions/ or src/
xdg-open uapl-drill.html      # run locally
python3 -m http.server -d docs 8000   # test the installable/offline version
```

## Conventions
- Question schema: id, module, topic, difficulty (medium|hard), question, options[4]{text,correct,why}, source, note?
- Exactly one correct option; every option needs a specific `why`. The UI shuffles option order.
- Sources must be public (ANA, ANR-101, CAAS ACs, ICAO/WMO, FAA, GPS.gov). No private course material.
- Update `VERIFIED` in src/template.html and the date in README.md when facts are re-checked.

## Gotchas
- Never edit `uapl-drill.html` or `docs/` by hand; they are overwritten by build.py.
- `sw.js` version is a content hash: rebuild after any change or installed copies keep the old cache.
- The built HTML must keep `<meta charset="utf-8">`; without it symbols render garbled from file://.
- GitHub Pages only serves from repo root or `/docs`; don't rename `docs/`.
