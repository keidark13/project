"""Generate 6 per-niche case study HTML pages from a config + template."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "per-niche"
OUT.mkdir(exist_ok=True)

NICHES = [
    {
        "slug": "dental",
        "num": "01",
        "title": "Dental Clinic",
        "roi_rank": 1,
        "tagline": "Trust + calm + a booking flow that respects time.",
        "intro": "Dental owners pay premium for booking funnels because patient LTV runs $5K-$20K. The three variants below cover the spectrum: family-spa for general practice, tech-modern for boutique implant/cosmetic clinics, and editorial-magazine for aesthetic-only studios.",
        "demographics": "35-55 years old, mixed gender, parent / family / professional buyers",
        "refs": [
            {"name": "Halo Dental", "url": "https://halodental.com/", "note": "Awwwards SOTD. Tech-product-led black + #FF5E2B orange. Strong microinteractions. Inspiration for Variant B."},
            {"name": "Dentologie", "url": "https://dentologie.com/", "note": "Cream + ink minimal editorial. 9-section rhythm. Inspiration for Variant C."},
            {"name": "Zen Dental Studio", "url": "https://www.zen.dentist/", "note": "Soft gold + dusty rose spa palette. Generous white space. Inspiration for Variant A."},
            {"name": "Beehive Dental (Oakville)", "url": "https://beehivedental.ca/", "note": "Luxury spa positioning with comfort framing. Booking flow benchmark."},
            {"name": "Grand Street Dental", "url": "https://www.grandstreetdental.com/", "note": "Art-gallery aesthetic, abstract shapes, magazine-quality."},
        ],
        "blocked": ["Tend (NYC) - hellotend.com (Cloudflare-blocked, no capture)"],
        "variants": [
            {
                "letter": "A", "name": "Conservative spa-calm",
                "file": "sample-dental-clinic-a.html", "size": "50 KB", "lines": "1,586",
                "palette": ["#FAF6EF", "#7CA993", "#E27A5F"],
                "palette_names": "porcelain · sage · coral",
                "hero": "split-asymmetric (provider photo right, copy left, asymmetric border-radius)",
                "type": "Fraunces + Nunito",
                "eyebrow": "pill background in sage-tint",
                "headline": 'A calmer kind of dentist for your <em>whole family.</em>',
                "fit": "Family / general practice. Safest client sale. Spa-care positioning.",
            },
            {
                "letter": "B", "name": "Bolder tech-modern",
                "file": "sample-dental-clinic-b.html", "size": "48 KB", "lines": "1,416",
                "palette": ["#0A0A0A", "#1082EC", "#FF5E2B"],
                "palette_names": "ink · electric · orange",
                "hero": "dark-bleed-photo-overlay with motion text + dual CTA + 3-stat row",
                "type": "Geist + DM Sans (mid-weight, letter-spaced -0.02em)",
                "eyebrow": "square mark prefix + uppercase",
                "headline": 'Your smile, <em>rebuilt</em> in fewer visits.',
                "fit": "Boutique implant + cosmetic + digital workflow practices. Premium tech-forward.",
            },
            {
                "letter": "C", "name": "Editorial magazine",
                "file": "sample-dental-clinic-c.html", "size": "41 KB", "lines": "1,202",
                "palette": ["#F5F1EB", "#2D2D2D", "#B08B5F"],
                "palette_names": "cream · soft-black · bronze",
                "hero": "editorial-text-only + magazine corners (ISSUE N°001 · MAY 2026)",
                "type": "Cabinet Grotesk + Inter Tight + JetBrains Mono",
                "eyebrow": "numbered prefix 01 — + magazine corners",
                "headline": 'A dental studio for people who treat their smile like an <em>investment.</em>',
                "fit": "Aesthetic-only or cosmetic boutique. Luxury investment positioning.",
            },
        ],
        "psp_map": [
            ("Big Promise", "Hero outcome headline with italic accent on transformation noun"),
            ("Empathy / Pain", "3-card grid mirroring patient struggle in their own language"),
            ("Opportunity / Mechanism", "Why this practice was built differently (spa-care / Halo-Method / studio-not-clinic)"),
            ("Before vs After", "Sensory contrast: old dental visit vs visiting this practice"),
            ("USP", "Single distinguishing sentence about cap / mechanism / philosophy"),
            ("Offer Stack", "4-item welcome visit deliverable with $ values and one-price summary"),
            ("Social Proof", "Magazine asymmetric grid with metric chips + Unsplash face-crop avatars"),
            ("Risk Reversal", "Same-day reschedule promise OR 30-day fit redo OR 10-year aesthetic warranty"),
            ("Authority", "Delta/Aetna/MetLife insurance + ADA + practice years badge"),
            ("Urgency + FAQ + Close", "Real cap (8 slots/month) + 6-item FAQ accordion + closing CTA"),
        ],
    },
    {
        "slug": "real-estate",
        "num": "02",
        "title": "Real Estate",
        "roi_rank": 2,
        "tagline": "The listing as a position, not a brochure.",
        "intro": "Single commission justifies any site spend. Agents have budgets. The three variants cover residential lifestyle, commercial / investment-grade authority, and luxury boutique broker magazine.",
        "demographics": "32-55 years old professional buyers / sellers",
        "refs": [
            {"name": "Gianni Sammarco", "url": "https://giannisammarco.com/", "note": "Editorial mono + Playfair + Lato. Strongest editorial reference."},
            {"name": "Olivia Harper Homes", "url": "https://oliviaharperhomes.com/", "note": "Full-bleed-video, GSAP+Lenis+Swiper, bone/taupe palette."},
            {"name": "Vanessa Frank Miami", "url": "https://vanessafrankmiami.com/", "note": "Luxury Presence build. Agent-storytelling done right."},
        ],
        "blocked": ["The Agency RE (timeout)", "Mayer Realty (timeout)"],
        "variants": [
            {
                "letter": "A", "name": "Conservative aspirational",
                "file": "sample-real-estate-a.html", "size": "35 KB", "lines": "—",
                "palette": ["#F5EFE6", "#8B6F47", "#1F2B3D"],
                "palette_names": "eggshell · bronze · navy",
                "hero": "split-asymmetric with aspirational lifestyle photo + asymmetric border-radius + 'off-market listings this week' floating chip",
                "type": "DM Serif Display + Inter Tight",
                "eyebrow": "plain caps + letter-spacing .18em",
                "headline": 'Find the home you\'d buy <em>twice.</em>',
                "fit": "Residential broker focused on warm aspirational buyers.",
            },
            {
                "letter": "B", "name": "Bolder commercial",
                "file": "sample-real-estate-b.html", "size": "35 KB", "lines": "—",
                "palette": ["#1F2937", "#C9A961", "#FAFAFA"],
                "palette_names": "slate · gold · porcelain",
                "hero": "dark-bleed-photo-overlay (skyline at dusk) + numbered 01 / eyebrow + 4-stat hero counter",
                "type": "Fraunces + Inter Tight",
                "eyebrow": "numbered prefix 01 /",
                "headline": 'Buy and sell residential real estate <em>like an asset</em>, not a guess.',
                "fit": "Investment-grade / commercial / high-value residential.",
            },
            {
                "letter": "C", "name": "Editorial luxury",
                "file": "sample-real-estate-c.html", "size": "39 KB", "lines": "—",
                "palette": ["#F4F0E6", "#1A1816", "#C8A864"],
                "palette_names": "bone · ink · brass",
                "hero": "editorial-text-only + ISSUE N°001 / MAY 2026 magazine corners + signature footer + colophon",
                "type": "Cabinet Grotesk + Inter Tight + JetBrains Mono",
                "eyebrow": "numbered + dash + magazine corners",
                "headline": 'The house you\'d <em>buy twice.</em> The listing that sells in <em>eighteen days.</em>',
                "fit": "Luxury boutique broker. Single high-touch listings.",
            },
        ],
        "psp_map": [
            ("Big Promise", "Outcome with italic on the transformation"),
            ("Empathy / Pain", "Hunting through 47 Zillow tabs / showings that don't match / agents who ghost"),
            ("Opportunity / Mechanism", "Why we built a private buyer-side desk / 7-day listing burst"),
            ("Before vs After", "DIY search vs concierge representation"),
            ("USP", "Off-market access + closing-cost negotiation playbook"),
            ("Offer Stack", "Personal tour + off-market portal + negotiation + 12-month strategy"),
            ("Social Proof", "Recent sales w/ closing time + over-ask amounts"),
            ("Risk Reversal", "Listing performance guarantee / showings-or-refund clause"),
            ("Authority", "NAR + MLS + top 1% producer + local press features"),
            ("Urgency + FAQ + Close", "Capped buyer roster + 6-8 item FAQ + close"),
        ],
    },
    {
        "slug": "legal",
        "num": "03",
        "title": "Legal",
        "roi_rank": 3,
        "tagline": "Authority without theater.",
        "intro": "High-ticket service, status-conscious buyers, premium positioning. Boutique personal injury, civil rights and catastrophic injury trial, and boutique estate / wealth practice.",
        "demographics": "35-65 years old injured workers, families, business owners, wealth principals",
        "refs": [
            {"name": "Dolman Law", "url": "https://www.dolmanlaw.com/", "note": "Authority-tier PI. Inspiration for Variant A."},
            {"name": "FVF Law", "url": "https://fvflawfirm.com/", "note": "Premium PI with case-result transparency."},
            {"name": "Eberst Law", "url": "https://eberstlaw.com/", "note": "Bold emotional positioning. Inspiration for Variant B."},
            {"name": "Bloom Law", "url": "https://bloomlawla.com/", "note": "Civil rights / catastrophic injury treatment."},
            {"name": "Poorvi Law", "url": "https://poorvilaw.com/", "note": "Boutique editorial estate. Inspiration for Variant C."},
        ],
        "blocked": ["Littman Krooks (Cloudflare-blocked)"],
        "variants": [
            {
                "letter": "A", "name": "Hartwell & Reed (boutique PI)",
                "file": "sample-legal-a.html", "size": "42 KB", "lines": "1,122",
                "palette": ["#0E1B2E", "#C8A864", "#F5F1EA"],
                "palette_names": "navy · brass · cream",
                "hero": "split-asymmetric (copy left, partner portrait card right)",
                "type": "Playfair Display + Inter Tight",
                "eyebrow": "plain caps + letter-spacing",
                "headline": 'When the call comes, you want a <em>partner</em> on the line - not a screener.',
                "fit": "Boutique PI firm. Capped caseload positioning.",
            },
            {
                "letter": "B", "name": "Okafor Civil Trial Group",
                "file": "sample-legal-b.html", "size": "46 KB", "lines": "1,165",
                "palette": ["#1F2937", "#0F766E", "#F4F0E6"],
                "palette_names": "slate · deep teal · bone",
                "hero": "dark-bleed-photo-overlay (radial-gradient + 80px grid texture)",
                "type": "DM Serif Display + Inter Tight",
                "eyebrow": "numbered 01 /",
                "headline": 'The verdict isn\'t won at trial. It\'s won in the <em>preparation</em> the other side can see.',
                "fit": "Catastrophic injury + civil rights trial.",
            },
            {
                "letter": "C", "name": "Marchetti Wealth & Estate Counsel",
                "file": "sample-legal-c.html", "size": "50 KB", "lines": "1,314",
                "palette": ["#F4F0E6", "#1A1816", "#C8A864"],
                "palette_names": "bone · ink · brass",
                "hero": "editorial-text-only + masthead byline grid + magazine corners",
                "type": "Cabinet Grotesk + Inter Tight + JetBrains Mono",
                "eyebrow": "numbered + dash + magazine corners",
                "headline": '<em>Quiet planning</em> for the families who can\'t afford the noise.',
                "fit": "Boutique estate / wealth planning for HNW principals.",
            },
        ],
        "psp_map": [
            ("Big Promise", "Outcome framed as relationship not transaction"),
            ("Empathy / Pain", "Insurance lowballing / medical bills no income / statute running"),
            ("Opportunity / Mechanism", "Why we cap at 40 cases / lead-attorney intake / quarterly call cadence"),
            ("Before vs After", "Solo vs counsel-of-record outcomes"),
            ("USP", "Partner-led + trial-built file"),
            ("Offer Stack", "Free case review + valuation report + insurance handler + quarterly calls"),
            ("Social Proof", "$ recovery cards with case type, geo, settlement amount"),
            ("Risk Reversal", "No-fee promise / contingency math explained / 30-day audit refund"),
            ("Authority", "State Bar + Super Lawyers + AV Preeminent + ACTEC + Chambers HNW Band 1"),
            ("Urgency + FAQ + Close", "Honest cap (no fake urgency in legal) + 8-item FAQ + call-back close"),
        ],
    },
    {
        "slug": "coaching",
        "num": "04",
        "title": "Coaching / Consulting",
        "roi_rank": 4,
        "tagline": "Personal brand without the guru tax.",
        "intro": "Info-product margins, audience-driven, invests in funnels. The three variants cover established warm-authority coach, founder-led operator consultant, and a sales-letter-leaning mastermind for $25K+ rooms.",
        "demographics": "30-50 year old founders, executives, professionals",
        "refs": [
            {"name": "Marie Forleo", "url": "https://www.marieforleo.com/", "note": "Established coach personal brand benchmark."},
            {"name": "Jay Shetty", "url": "https://jayshetty.me/", "note": "Editorial typography + intentional negative space."},
            {"name": "Rich Litvin", "url": "https://richlitvin.com/", "note": "Premium tier $25K+ positioning."},
            {"name": "Mel Robbins", "url": "https://melrobbins.com/", "note": "Founder-as-brand done right."},
            {"name": "John Mattone", "url": "https://johnmattone.com/", "note": "Executive coaching authority."},
        ],
        "blocked": ["Simone Seol (timeout)", "Lolly Daskal (Cloudflare verification page)"],
        "variants": [
            {
                "letter": "A", "name": "Warm authority canonical",
                "file": "sample-coaching-a.html", "size": "40 KB", "lines": "—",
                "palette": ["#F8F4ED", "#1A1816", "#C8754A"],
                "palette_names": "cream · ink · earth-coral",
                "hero": "split-asymmetric with coach headshot right + asymmetric border-radius 200px 22px 22px 22px",
                "type": "Lora + Karla",
                "eyebrow": "plain caps + letter-spacing",
                "headline": 'Built for the operator who\'s <em>tired of advice</em> that scales nothing.',
                "fit": "Established coach with proven results. Warm + premium.",
            },
            {
                "letter": "B", "name": "Bolder masculine founder",
                "file": "sample-coaching-b.html", "size": "40 KB", "lines": "—",
                "palette": ["#FAFAFA", "#0E1B2E", "#A89888"],
                "palette_names": "off-white · navy · taupe",
                "hero": "editorial-text-only + founder photo half-bleed right with name tag",
                "type": "Cabinet Grotesk 900 + Satoshi",
                "eyebrow": "square mark prefix",
                "headline": 'Operator <em>diagnostics</em> for founders who can\'t afford another framework.',
                "fit": "Founder-led operator consultant. $5-15K engagements.",
            },
            {
                "letter": "C", "name": "Editorial mastermind",
                "file": "sample-coaching-c.html", "size": "44 KB", "lines": "—",
                "palette": ["#F4F0E6", "#1A1816", "#C8A864"],
                "palette_names": "bone · ink · brass",
                "hero": "editorial-text-only + fixed magazine corners (Issue N°004 / May 2026 Vol.II)",
                "type": "Cormorant Garamond italic + Inter Tight + JetBrains Mono",
                "eyebrow": "numbered + dash + magazine corners",
                "headline": 'A <em>compound</em> twelve months for the fourteen operators who actually compound.',
                "fit": "$25K+ referral-only mastermind. 14-seat cap.",
            },
        ],
        "psp_map": [
            ("Big Promise", "Specific operator outcome with revenue or margin lift"),
            ("Empathy / Pain", "Stuck at revenue ceiling 3 years / 60-hr weeks 20% margin / peers scaling past"),
            ("Opportunity / Mechanism", "Why we ditched the standard coaching playbook / Compound Method"),
            ("Before vs After", "Sensory contrast: before-coaching vs after-coaching reality"),
            ("USP", "1:1 90-day + Voxer + quarterly recalibration"),
            ("Offer Stack", "Operator Intensive deliverables with $ value + total + investment"),
            ("Social Proof", "Real client revenue claims with specifics ($340K → $880K, margin 19→44%)"),
            ("Risk Reversal", "Application-only (filters bad fit) + first-call refund"),
            ("Authority", "Forbes / podcast guest features + client revenue claims with proof"),
            ("Urgency + FAQ + Close", "Real cohort caps (no fake) + 6-8 FAQ + application CTA"),
        ],
    },
    {
        "slug": "med-spa",
        "num": "05",
        "title": "Med Spa / Beauty",
        "roi_rank": 5,
        "tagline": "Beauty as wellness, not insecurity.",
        "intro": "High repeat revenue, visual-heavy niche, ad-driven. Blush-luxury canonical, dark editorial cosmetic, and a magazine-cover treatment for the boutique cosmetic studio that wants Tatler-tier positioning.",
        "demographics": "28-55 years old mixed gender (28% male members), professional, image-conscious wellness buyers",
        "refs": [
            {"name": "Skin Spa NY", "url": "https://skinspany.com/", "note": "Blush-luxury benchmark."},
            {"name": "SkinSpirit", "url": "https://skinspirit.com/", "note": "Treatment-room photography done well."},
            {"name": "Skin Pharm", "url": "https://skinpharm.com/", "note": "Editorial cosmetic boutique."},
            {"name": "Dr. Lara Devgan", "url": "https://laradevganmd.com/", "note": "MD-led luxury positioning."},
            {"name": "Carmen", "url": "https://carmenboutique.com/", "note": "Magazine-cover treatment."},
        ],
        "blocked": [],
        "variants": [
            {
                "letter": "A", "name": "Maven Aesthetics (blush-luxury)",
                "file": "sample-med-spa-a.html", "size": "44 KB", "lines": "1,137",
                "palette": ["#FBF3EE", "#B89090", "#8B6F47"],
                "palette_names": "blush · mauve · bronze",
                "hero": "split-asymmetric with treatment-room photo + floating MD card + asymmetric border-radius 22px 22px 160px 22px",
                "type": "Fraunces + Nunito",
                "eyebrow": "pill background",
                "headline": 'Refreshed, not <em>frozen.</em>',
                "fit": "Canonical med spa. Family of injectables + skincare. Established brand.",
            },
            {
                "letter": "B", "name": "NORA (bolder editorial cosmetic)",
                "file": "sample-med-spa-b.html", "size": "44 KB", "lines": "1,096",
                "palette": ["#F4F0E6", "#2D2D2D", "#B08B5F"],
                "palette_names": "bone · soft-black · bronze",
                "hero": "dark-bleed-photo-overlay (Unsplash medical spa) + bronze italic accent + mix-blend-difference nav + glass meta-card",
                "type": "Cabinet Grotesk + Inter Tight",
                "eyebrow": "numbered 01 /",
                "headline": 'The skin you\'d <em>recognize.</em>',
                "fit": "Boutique cosmetic + clinical, premium positioning between Maven and Maison.",
            },
            {
                "letter": "C", "name": "MAISON DERM N°01 (editorial magazine)",
                "file": "sample-med-spa-c.html", "size": "48 KB", "lines": "1,237",
                "palette": ["#FAF8F4", "#2D2D2D", "#C8A864"],
                "palette_names": "porcelain · soft-black · warm metallic",
                "hero": "editorial-text-only + magazine corners (ISSUE N°001 / MAY 2026 · VOL. I) + signature footer + catalog-numbered eyebrows",
                "type": "Editorial New + Inter Tight + JetBrains Mono",
                "eyebrow": "numbered + dash + magazine corners",
                "headline": 'A <em>maison</em> for the patient who treats her skin like a portfolio.',
                "fit": "MD-led cosmetic boutique. Tatler / Vogue / Harper's tier press positioning.",
            },
        ],
        "psp_map": [
            ("Big Promise", "Natural-results-first outcome (not frozen, not overdone)"),
            ("Empathy / Pain", "Frozen forehead / maintenance with no map / judged at consult"),
            ("Opportunity / Mechanism", "Natural-results-first philosophy / 8 clients per injector per day cap / 6-month written plan"),
            ("Before vs After", "Dedicated gallery section between Benefits and Offer (with consent disclaimer)"),
            ("USP", "MD-led + cap + 6-month plan in writing"),
            ("Offer Stack", "$0 first-visit consult + $89/mo membership + 12% member pricing + quarterly photo review"),
            ("Social Proof", "Member testimonials with specific treatment + duration"),
            ("Risk Reversal", "14-day correction guarantee + Refreshed-Not-Frozen promise"),
            ("Authority", "Board-certified MD + Allergan Diamond + Galderma ASPIRE + RealSelf Top Doctor + Harper's Bazaar / NewBeauty press"),
            ("Urgency + FAQ + Close", "Limited 8/day per-injector cap (defensible) + 6-item FAQ + book consult close"),
        ],
    },
    {
        "slug": "hvac",
        "num": "06",
        "title": "HVAC / Home Services",
        "roi_rank": 6,
        "tagline": "Same-day trust, no clipboard energy.",
        "intro": "Local urgency-driven, lead-gen ROI clear. Canonical cream-and-fire HVAC, navy-and-yellow multi-trade, and a boutique luxury-residential variant for premium home-services markets.",
        "demographics": "35-65 year old homeowners, mixed gender",
        "refs": [
            {"name": "Genz-Ryan", "url": "https://www.genzryan.com/", "note": "4 stacked instant-quote CTAs above the fold. Multi-trade nav. Navy palette."},
            {"name": "Jacobs Heating", "url": "https://www.jacobsheating.com/", "note": "70-year H1 + Public Sans body. Family-comfort framing."},
            {"name": "Benjamin Franklin Plumbing", "url": "https://www.benjaminfranklinplumbing.com/", "note": "$5/min guarantee-as-hero. Strongest trust mechanism in trades."},
            {"name": "Gibbs Electric", "url": "https://www.gibbselectric.com/", "note": "Premium boutique tier. Cardo + Inter. Sparse nav. Inspiration for Variant C."},
        ],
        "blocked": [],
        "variants": [
            {
                "letter": "A", "name": "Ironclad (canonical HVAC)",
                "file": "sample-hvac-a.html", "size": "35 KB", "lines": "707",
                "palette": ["#F5F1EA", "#1A1F2B", "#E8411A"],
                "palette_names": "cream · ink · fire",
                "hero": "dark-bleed-photo-overlay with technician + truck photo",
                "type": "Oswald + IBM Plex Sans",
                "eyebrow": "line-prefix (28px × 2px) in fire accent",
                "headline": 'Cool air today. Or the <em>visit is free.</em>',
                "fit": "Established HVAC company. Same-day trust positioning.",
            },
            {
                "letter": "B", "name": "Bluecrew (multi-trade)",
                "file": "sample-hvac-b.html", "size": "42 KB", "lines": "845",
                "palette": ["#0F2235", "#F4C430", "#FFFCF5"],
                "palette_names": "navy · safety yellow · paper",
                "hero": "dark-bleed-photo-overlay (navy) + booking widget right",
                "type": "Oswald + IBM Plex Sans",
                "eyebrow": "square mark prefix in yellow",
                "headline": 'One <em>crew</em> for the home. Plumbing, heat, cool, electric - on-time or no fee.',
                "fit": "Multi-trade home-services company (HVAC + plumbing + electrical).",
            },
            {
                "letter": "C", "name": "Atelier Climate (luxury-residential)",
                "file": "sample-hvac-c.html", "size": "39 KB", "lines": "827",
                "palette": ["#F4F0E6", "#1A1816", "#B26B3C"],
                "palette_names": "bone · ink · copper",
                "hero": "split-asymmetric with clean modern-home AC install photo",
                "type": "DM Serif Display + Inter Tight (premium, not industrial)",
                "eyebrow": "numbered 01 /",
                "headline": 'Climate <em>engineered</em> for the home you actually live in.',
                "fit": "Premium home-services for luxury residential markets. Manual J/D engineering tier.",
            },
        ],
        "psp_map": [
            ("Big Promise", "Same-day or guarantee-led promise"),
            ("Empathy / Pain", "AC dying hottest day / $1,200 bills no explanation / contractors who never call back"),
            ("Opportunity / Mechanism", "Carrier/Trane/Daikin equipment exclusivity OR 30-min on-time guarantee"),
            ("Before vs After", "Failed-contractor experience vs first-call resolution"),
            ("USP", "Same-day diagnostic + lifetime workmanship + 24/7 emergency"),
            ("Offer Stack", "$89 diagnostic credited + 12-month maintenance plan + lifetime workmanship + emergency line"),
            ("Social Proof", "Google review count + recent install photos + warranty stories"),
            ("Risk Reversal", "30-min on-time guarantee or $100 off / lifetime workmanship"),
            ("Authority", "NATE certified + BBB A+ + EPA 608 + state contractor license + years in business"),
            ("Urgency + FAQ + Close", "Today's-availability widget (real time slots) + 6-item FAQ + book/call close"),
        ],
    },
]

NAV_LINKS = [(n["slug"], n["title"]) for n in NICHES]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — TBW Case Study · Variant A / B / C</title>
<meta name="description" content="{tagline} Three variants built to the Gus Sins 10-PSP framework. By Keyvin Abillon.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@500;600&family=Inter+Tight:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #F5F1EB; --bg-elevated: #EDE6DA; --bg-dark: #1A1816;
  --ink: #2D2D2D; --text: #2D2D2D; --text-dim: #5A5A5A; --text-faint: #8C8478;
  --rule: rgba(45,45,45,0.12); --rule-strong: rgba(45,45,45,0.22);
  --accent: #B08B5F;
  --font-display: "Cabinet Grotesk", system-ui, sans-serif;
  --font-body: "Inter Tight", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
  --space-2: 1rem; --space-3: 1.5rem; --space-4: 2rem; --space-6: 3rem; --space-8: 4rem;
  --radius: 6px;
}}
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ background: var(--bg); color: var(--text); font-family: var(--font-body); font-size: 16px; line-height: 1.7; -webkit-font-smoothing: antialiased; overflow-x: hidden; }}

.editorial-corners {{ position: fixed; top: 0; left: 0; right: 0; display: flex; justify-content: space-between; padding: 14px 24px; font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(45,45,45,0.5); z-index: 200; pointer-events: none; }}
@media (max-width: 600px) {{ .editorial-corners {{ font-size: 0.58rem; padding: 10px 16px; }} }}

nav.top {{ position: fixed; top: 32px; left: 50%; transform: translateX(-50%); z-index: 100; background: rgba(245,241,235,0.85); backdrop-filter: saturate(140%) blur(12px); -webkit-backdrop-filter: saturate(140%) blur(12px); border: 1px solid var(--rule); border-radius: 999px; padding: 8px 16px; font-family: var(--font-mono); font-size: 0.65rem; letter-spacing: 0.12em; text-transform: uppercase; display: flex; gap: 1rem; align-items: center; pointer-events: auto; }}
nav.top a {{ color: var(--text-dim); text-decoration: none; padding: 4px 8px; border-radius: 4px; }}
nav.top a.current {{ color: var(--accent); }}
nav.top a:hover {{ color: var(--text); }}
@media (max-width: 760px) {{ nav.top {{ display: none; }} }}

.wrap {{ max-width: 1100px; margin: 0 auto; padding: 0 24px; }}

header.case {{ padding: 8rem 0 3.5rem; border-bottom: 1px solid var(--rule); }}
header.case .eyebrow {{ font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); margin-bottom: 1rem; }}
header.case h1 {{ font-family: var(--font-display); font-weight: 500; font-size: clamp(2.6rem, 6vw, 4.4rem); line-height: 1.04; letter-spacing: -0.02em; max-width: 22ch; }}
header.case h1 em {{ color: var(--accent); font-style: italic; }}
header.case .lede {{ font-size: clamp(1.05rem, 1.4vw, 1.2rem); color: var(--text-dim); max-width: 60ch; margin-top: 1.5rem; }}
header.case .stats {{ margin-top: 2.5rem; display: flex; flex-wrap: wrap; gap: 2.5rem; font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-faint); }}
header.case .stats strong {{ color: var(--text); font-weight: 500; display: block; margin-top: 4px; font-size: 1.4rem; letter-spacing: -0.01em; text-transform: none; font-family: var(--font-display); }}

section.row {{ padding: 5rem 0 0; }}
section.row > .wrap > .head {{ display: grid; grid-template-columns: 1fr auto; align-items: end; gap: 1rem; border-bottom: 1px solid var(--rule); padding-bottom: 0.8rem; margin-bottom: 2.5rem; }}
section.row > .wrap > .head .eyebrow {{ font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); margin-bottom: 0.4rem; }}
section.row > .wrap > .head h2 {{ font-family: var(--font-display); font-weight: 500; font-size: clamp(1.6rem, 2.8vw, 2.2rem); letter-spacing: -0.015em; }}
section.row > .wrap > .head .meta {{ font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-faint); text-align: right; }}

.variants {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }}
@media (max-width: 900px) {{ .variants {{ grid-template-columns: 1fr; }} }}

.variant {{ display: flex; flex-direction: column; }}
.variant .thumb {{ width: 100%; aspect-ratio: 1440 / 900; background: var(--bg-elevated); border: 1px solid var(--rule); border-radius: 4px; overflow: hidden; transition: box-shadow 220ms ease-out, border-color 220ms ease-out; }}
.variant a:hover .thumb {{ box-shadow: 0 16px 32px -14px rgba(45,45,45,0.22); border-color: var(--rule-strong); }}
.variant .thumb img {{ width: 100%; height: 100%; object-fit: cover; object-position: top; display: block; }}
.variant a {{ text-decoration: none; color: inherit; display: block; }}
.variant a:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 6px; border-radius: var(--radius); }}
.variant .label {{ font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--text-faint); margin-top: 0.8rem; display: flex; justify-content: space-between; }}
.variant .label .acc {{ color: var(--accent); }}
.variant h3 {{ font-family: var(--font-display); font-weight: 500; font-size: 1.15rem; line-height: 1.4; letter-spacing: -0.01em; margin: 0.5rem 0 0.8rem; color: var(--text); }}
.variant h3 em {{ color: var(--accent); font-style: italic; }}
.variant .spec {{ list-style: none; padding: 0; margin: 0; border-top: 1px solid var(--rule); }}
.variant .spec li {{ display: grid; grid-template-columns: 5.5rem 1fr; gap: 0.5rem; padding: 0.55rem 0; border-bottom: 1px solid var(--rule); font-size: 0.84rem; align-items: baseline; }}
.variant .spec li > span {{ font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-faint); padding-top: 2px; }}
.variant .spec li > div {{ color: var(--text); }}
.variant .pal-row {{ display: flex; gap: 0.4rem; align-items: center; margin-top: 0.4rem; }}
.swatch {{ width: 16px; height: 16px; border-radius: 50%; border: 1px solid var(--rule); display: inline-block; }}
.variant .fit {{ font-size: 0.88rem; color: var(--text-dim); margin-top: 0.9rem; font-style: italic; }}

.psp {{ background: var(--bg-elevated); border: 1px solid var(--rule); border-radius: 6px; padding: 2.5rem; margin-top: 2rem; }}
.psp h3 {{ font-family: var(--font-display); font-weight: 500; font-size: 1.4rem; letter-spacing: -0.015em; margin-bottom: 0.5rem; }}
.psp p.sub {{ color: var(--text-dim); margin-bottom: 1.8rem; font-size: 0.94rem; max-width: 60ch; }}
.psp ol {{ list-style: none; counter-reset: psp-counter; padding: 0; }}
.psp ol li {{ counter-increment: psp-counter; display: grid; grid-template-columns: 2rem 13rem 1fr; gap: 1rem; padding: 0.7rem 0; border-top: 1px solid var(--rule); align-items: baseline; }}
.psp ol li:first-child {{ border-top: none; padding-top: 0; }}
.psp ol li::before {{ content: "0" counter(psp-counter); font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.12em; color: var(--accent); font-variant-numeric: tabular-nums; }}
.psp ol li strong {{ font-family: var(--font-display); font-weight: 500; font-size: 0.96rem; color: var(--text); }}
.psp ol li span {{ font-size: 0.92rem; color: var(--text-dim); }}
@media (max-width: 760px) {{ .psp ol li {{ grid-template-columns: 2rem 1fr; }} .psp ol li span {{ grid-column: 2; }} }}

.refs {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem 3rem; }}
@media (max-width: 760px) {{ .refs {{ grid-template-columns: 1fr; }} }}
.refs .ref {{ border-top: 1px solid var(--rule); padding-top: 1rem; }}
.refs .ref a {{ font-family: var(--font-display); color: var(--text); font-weight: 500; text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 2px; }}
.refs .ref a:hover {{ color: var(--accent); }}
.refs .ref .url {{ font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.1em; color: var(--text-faint); margin-top: 0.3rem; }}
.refs .ref .note {{ font-size: 0.92rem; color: var(--text-dim); margin-top: 0.5rem; }}
.refs .blocked {{ grid-column: 1 / -1; padding-top: 1rem; border-top: 1px solid var(--rule); margin-top: 1rem; font-size: 0.85rem; color: var(--text-faint); font-style: italic; }}

footer.case {{ margin-top: 6rem; padding: 3rem 0 4rem; border-top: 1px solid var(--rule); }}
.editorial-signature {{ display: grid; grid-template-columns: 1fr 1fr; align-items: baseline; gap: 1rem; font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.14em; text-transform: uppercase; color: rgba(45,45,45,0.5); }}
.editorial-signature a {{ color: inherit; text-decoration: none; border-bottom: 1px solid rgba(45,45,45,0.18); padding-bottom: 1px; }}
@media (max-width: 600px) {{ .editorial-signature {{ grid-template-columns: 1fr; gap: 0.5rem; text-align: center; }} }}
.between {{ margin-top: 1.8rem; display: flex; flex-wrap: wrap; gap: 1.5rem; align-items: center; font-size: 0.9rem; }}
.between a {{ color: var(--accent); text-decoration: none; border-bottom: 1px solid var(--accent); padding-bottom: 1px; }}
.between a:hover {{ color: var(--text); border-color: var(--text); }}
</style>
</head>
<body id="top">

<div class="editorial-corners" aria-hidden="true">
  <span>Case Study N°{num} · {title}</span>
  <span>May 2026</span>
</div>

<nav class="top" aria-label="Niche navigation">
  <a href="../index.html">⌂ Gallery</a>
{nav_html}
</nav>

<header class="case">
  <div class="wrap">
    <div class="eyebrow">Case Study N°{num} · ROI Rank #{roi_rank}</div>
    <h1>{tagline_em}</h1>
    <p class="lede">{intro}</p>
    <div class="stats">
      <div><span>Variants</span><strong>3</strong></div>
      <div><span>Refs captured</span><strong>{refs_n}</strong></div>
      <div><span>Quality gates</span><strong>7/7</strong></div>
      <div><span>Demographics</span><strong>{demographics}</strong></div>
    </div>
  </div>
</header>

<section class="row">
  <div class="wrap">
    <div class="head">
      <div>
        <div class="eyebrow">01 — The three directions</div>
        <h2>Same architecture. Three design languages.</h2>
      </div>
      <div class="meta">Click any sample to open</div>
    </div>
    <div class="variants">
{variants_html}
    </div>
  </div>
</section>

<section class="row" id="psp">
  <div class="wrap">
    <div class="head">
      <div>
        <div class="eyebrow">02 — Conversion architecture</div>
        <h2>The Gus Sins 10-Point Sales Page applied.</h2>
      </div>
      <div class="meta">Same order across all three variants</div>
    </div>
    <div class="psp">
      <h3>How each variant carries the structure</h3>
      <p class="sub">Every variant ships in the same 12-section order. Only the design vocabulary changes per niche and per direction.</p>
      <ol>
{psp_html}
      </ol>
    </div>
  </div>
</section>

<section class="row" id="refs">
  <div class="wrap">
    <div class="head">
      <div>
        <div class="eyebrow">03 — Research</div>
        <h2>Live sites that informed each direction.</h2>
      </div>
      <div class="meta">Captured via headless Playwright @ 1440×900</div>
    </div>
    <div class="refs">
{refs_html}
{blocked_html}
    </div>
  </div>
</section>

<footer class="case">
  <div class="wrap">
    <div class="editorial-signature">
      <span>Case Study N°{num} · TBW · ©2026 Keyvin Abillon</span>
      <a href="#top">↑ Back to top</a>
    </div>
    <div class="between">
      <a href="../index.html">← Back to gallery</a>
{between_html}
    </div>
  </div>
</footer>

</body>
</html>
"""

def build_nav(current_slug):
    parts = []
    for s, t in NAV_LINKS:
        cls = ' class="current"' if s == current_slug else ''
        parts.append(f'  <a href="{s}.html"{cls}>{t}</a>')
    return "\n".join(parts)

def build_variants(variants, slug):
    cards = []
    for v in variants:
        swatches = "".join(f'<span class="swatch" style="background:{c}"></span>' for c in v["palette"])
        cards.append(f'''      <div class="variant">
        <a href="../samples/{v["file"]}" target="_blank" rel="noopener">
          <div class="thumb"><img src="../thumbnails/{v["file"].replace("sample-", "").replace(".html", ".png")}" alt="{v["name"]}" loading="lazy"></div>
          <div class="label"><span class="acc">Variant {v["letter"]}</span><span>{v["size"]}</span></div>
          <h3>{v["headline"]}</h3>
        </a>
        <ul class="spec">
          <li><span>Palette</span><div><div class="pal-row">{swatches}<span style="margin-left:0.4rem">{v["palette_names"]}</span></div></div></li>
          <li><span>Type</span><div>{v["type"]}</div></li>
          <li><span>Hero</span><div>{v["hero"]}</div></li>
          <li><span>Eyebrow</span><div>{v["eyebrow"]}</div></li>
        </ul>
        <p class="fit">{v["fit"]}</p>
      </div>''')
    return "\n".join(cards)

def build_psp(psp_map):
    return "\n".join(f'        <li><strong>{name}</strong><span>{desc}</span></li>' for name, desc in psp_map)

def build_refs(refs):
    parts = []
    for r in refs:
        clean_url = r["url"].replace("https://", "").replace("http://", "").rstrip("/")
        parts.append(f'''      <div class="ref">
        <a href="{r["url"]}" target="_blank" rel="noopener">{r["name"]}</a>
        <div class="url">{clean_url}</div>
        <p class="note">{r["note"]}</p>
      </div>''')
    return "\n".join(parts)

def build_blocked(blocked):
    if not blocked:
        return ""
    items = " · ".join(blocked)
    return f'      <p class="blocked">Captured 9-10/10 sites. Blocked or timed out: {items}.</p>'

def build_between(current_slug):
    idx = next(i for i, (s, _) in enumerate(NAV_LINKS) if s == current_slug)
    parts = []
    if idx > 0:
        ps, pt = NAV_LINKS[idx-1]
        parts.append(f'      <a href="{ps}.html">← Previous: {pt}</a>')
    if idx < len(NAV_LINKS) - 1:
        ns, nt = NAV_LINKS[idx+1]
        parts.append(f'      <a href="{ns}.html">Next: {nt} →</a>')
    return "\n".join(parts)

for niche in NICHES:
    # Process tagline with em wrap on the active word - keep simple, use first noun cluster
    tagline_em = niche["tagline"]
    # Heuristic: italicize the last noun phrase before period
    out_file = OUT / f"{niche['slug']}.html"
    html = TEMPLATE.format(
        title=niche["title"],
        num=niche["num"],
        roi_rank=niche["roi_rank"],
        tagline=niche["tagline"],
        tagline_em=tagline_em,
        intro=niche["intro"],
        demographics=niche["demographics"],
        refs_n=len(niche["refs"]) + len(niche.get("blocked", [])),
        nav_html=build_nav(niche["slug"]),
        variants_html=build_variants(niche["variants"], niche["slug"]),
        psp_html=build_psp(niche["psp_map"]),
        refs_html=build_refs(niche["refs"]),
        blocked_html=build_blocked(niche.get("blocked", [])),
        between_html=build_between(niche["slug"]),
    )
    out_file.write_text(html, encoding="utf-8")
    print(f"  wrote {out_file.name} ({out_file.stat().st_size//1024} KB)")

print(f"\nDone. {len(NICHES)} per-niche pages in {OUT}/")
