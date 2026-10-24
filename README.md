# UAPL Theory Drill

Free, unofficial practice questions for the **Singapore Unmanned Aircraft Pilot Licence (UAPL) theory test**.
258 multiple-choice questions across the six syllabus modules. Every option, right or wrong, explains why.

> **Unofficial.** Not made, checked or endorsed by the Civil Aviation Authority of Singapore (CAAS) or any
> training organisation, and these are not the real test questions. Facts were checked against public sources
> on **24 October 2026**. Rules change, so confirm anything that matters on
> [caas.gov.sg](https://www.caas.gov.sg/unmanned-aircraft/).

## Use it

**Easiest: one file, nothing to install.**
Download [`uapl-drill.html`](uapl-drill.html) (click it, then the download button) and open it in any browser,
on a phone or a computer. It works offline. Your progress is saved in that browser only.

**Or clone the repo:**
```bash
git clone https://github.com/RoyHew/uapl-drill.git
```
then open `uapl-drill/uapl-drill.html`.

**Host it as an installable app:** upload the `site/` folder to any static host (GitHub Pages, Cloudflare Pages,
Netlify). Served over https it can be installed to a phone's home screen and works fully offline.

## What's inside

| Mode | What it does |
|---|---|
| Practice | Questions from the modules you pick, with explanations after each answer |
| Mock exam | 50 questions, 90-minute clock, scored against the 75% pass mark |
| Weak spots | Questions you got wrong, until you answer each right twice in a row |

| Module | Questions |
|---|---|
| General UAS Knowledge | 35 |
| Principles of Flight | 35 |
| Air Law | 88 |
| Navigation & Meteorology | 40 |
| Human Factors | 25 |
| Safety & Operations | 35 |

Sources are public only: the Air Navigation Act 1966, the Air Navigation (101 – Unmanned Aircraft Operations)
Regulations 2019, CAAS advisory circulars, ICAO/WMO weather-code standards, GPS.gov and FAA study guides.
Each question shows its source.

## Edit or add questions

Questions live in `questions/*.json`. Each has exactly 4 options, one marked `"correct": true`, and a `why` for
every option. After editing, rebuild:

```bash
python3 src/build.py
```

This regenerates `uapl-drill.html` and `site/`.

## Found a mistake?

Open an issue with the question id (shown on each question, e.g. `AL-033`) and the source that shows the
correct answer.
