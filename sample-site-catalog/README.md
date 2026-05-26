# Sample Site Catalog

18 sample websites across 6 niches. Each niche has 3 design directions, built to the Gus Sins 10-Point Sales Page conversion architecture.

By Keyvin Abillon · Built 2026-05-26 with the `tbw-build` skill.

---

## How to share with a client

1. Open `index.html` in any browser — that is the gallery
2. Hover any sample to lift it; click to open the full site in a new tab
3. Click "Per-niche case studies" (top of index) for deeper rationale per niche
4. Send the whole `sample-site-catalog/` folder zipped, OR host it on Netlify drop / GitHub Pages

If client wants their specific niche, jump straight to:

- [Dental](per-niche/dental.html)
- [Real Estate](per-niche/real-estate.html)
- [Legal](per-niche/legal.html)
- [Coaching / Consulting](per-niche/coaching.html)
- [Med Spa / Beauty](per-niche/med-spa.html)
- [HVAC / Home Services](per-niche/hvac.html)

---

## What is in this folder

```
sample-site-catalog/
├── index.html              gallery, 18 thumbnails, click to view
├── README.md               this file
├── _make_thumbs.py         Playwright thumbnail generator (re-run anytime)
├── _gen_niche_pages.py     case study page generator (edit + re-run to update)
├── samples/                18 single-file HTML samples (open in browser)
├── thumbnails/             18 JPEG thumbnails (1440x900 viewport)
└── per-niche/              6 case study pages with rationale + refs + 10-PSP map
```

---

## The six niches

| # | Niche | ROI rank | Why it's there |
|---|---|---|---|
| 01 | Dental Clinic | #1 | $5K-$20K patient LTV; owners pay premium for booking funnels |
| 02 | Real Estate | #2 | Single commission justifies any site spend |
| 03 | Legal | #3 | High-ticket service, status-conscious buyers |
| 04 | Coaching / Consulting | #4 | Info-product margins, audience-driven |
| 05 | Med Spa / Beauty | #5 | High repeat-revenue, visual-heavy, ad-driven |
| 06 | HVAC / Home Services | #6 | Local urgency-driven, lead-gen ROI clear |

---

## The three variants per niche

Each niche ships in the same 12-section, 10-PSP architecture. Only the design language changes:

- **Variant A — Conservative canonical** · the safest client sale, follows niche-canonical palette + hero
- **Variant B — Bolder** · same palette family with an unexpected hero, OR a bolder palette on the same hero
- **Variant C — Editorial** · magazine / luxury restraint treatment for the premium tier (Tatler / Vogue / Vanity Fair positioning)

---

## The conversion architecture

Every variant ships the Gus Sins 10-Point Sales Page in order:

1. **Big Promise** — outcome headline with one italic accent word
2. **Empathy** — mirror the customer struggle before any promise
3. **Opportunity / New Mechanism** — why the old way fails
4. **Before vs After** — sensory contrast (dark vs light columns, or side-by-side)
5. **USP** — single sentence about what makes this practice different
6. **Offer Stack** — itemized deliverables with $ values + total + investment
7. **Social Proof** — magazine asymmetric grid with metric chips
8. **Risk Reversal** — guarantee or no-fee promise
9. **Authority** — credentials, partnerships, press
10. **Urgency + FAQ + Close** — real cap (no fake urgency) + FAQ accordion + final CTA

---

## Quality bar applied to every sample

- 7/7 quality gates passed (anti-slop / 10-PSP / BO patterns / photos / animation / typography / integrity)
- Single-file HTML, GSAP loaded via CDN, mobile responsive at 860px
- Niche-authentic palette (never defaulted to cream+orange unless that's truly the right call)
- Real Unsplash placeholder photos (face-crop avatars, niche-relevant hero shots)
- No emdash, no centered-stack hero (except editorial-text-only magazine archetype), no Inter on hero, no fake urgency
- Demographics in social proof match the actual target customer per niche

---

## Reference research

For each niche, 10 live competitor / inspiration sites were captured via headless Playwright @ 1440×900. Top 2-3 were used to lock the direction. Research artifacts live in:

```
C:/Users/User/.claude/skills/tbw/references/sites-captured/<niche-slug>/
```

Each niche folder has:

- `links.json` — 10 URLs with why-picked notes
- `01.png ... 10.png` — fullpage screenshots
- `01.json ... 10.json` — structured section breakdown per site
- `_capture.py` — the Playwright script (re-run anytime)
- `_capture_summary.json` — final capture summary

INDEX.md at `references/sites-captured/INDEX.md` catalogs every captured niche.

---

## How to extend

To build a sample for a new niche, in Claude Code run:

```
build [niche]
```

Examples:

- `build fitness`
- `build restaurant`
- `build saas`
- `build charity`
- `build [any niche]`

The `tbw-build` skill will:

1. Auto-pick the highest-ROI missing niche (or use yours if specified)
2. Capture 10 reference sites via Playwright
3. Lock 3 variant directions (Conservative / Bolder / Editorial)
4. Build all 3 single-file HTML samples
5. Self-audit each against the 7 quality gates
6. Report a verification table

To re-render this gallery after new builds, run:

```bash
cd tbw-case-studies
python _make_thumbs.py    # regenerate thumbnails
python _gen_niche_pages.py    # add the new niche to NICHES list first, then run
```

The `index.html` is hand-edited — add a new `<section>` for any new niche.

---

## Custom rebrand for a real client

Pick a variant that fits their lane. Tell me:

1. Their niche
2. Variant letter (A/B/C)
3. Brand colors / logo / hero photo
4. Their offer details (price, deliverables, guarantee, FAQ topics)

I will rebuild the chosen variant with their actual brand and ship a single-file HTML you can hand over.

---

## Built with

- Python 3.11 + Playwright + BeautifulSoup
- Claude Code (`tbw-build` orchestrator skill)
- 5 parallel niche orchestrator agents
- The Gus Sins 10-PSP framework (from the 050526 Effective Comms training)
- The TBW skill (`tbw` and `tbw-build`) at `C:/Users/User/.claude/skills/`

Total wall time end-to-end: ~45 minutes for 18 samples + 6 case study pages.
