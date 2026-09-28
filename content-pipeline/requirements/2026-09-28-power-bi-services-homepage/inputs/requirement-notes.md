# Requirement notes

- **Content type**: Webpage — the homepage for Power BI and the services HLB HAMT provides
  around it. This is a standalone product/service homepage (like the SugarAI CRM homepage),
  not an industry subpage in an existing series.
- **Primary keyword**: Power BI service
- **Secondary keywords**: Certified Power BI Partner in UAE; Power BI consulting company;
  Power BI solutions expert; Power BI Services

- **Reference websites** (competitor Power BI service pages — for positioning/gaps, nothing
  may be copied or paraphrased):
  - https://yesdynamic.com/solutions/power-platform/power-bi/
  - https://zenzero.co.uk/power-bi
  - https://www.dsp.co.uk/power-bi-services
  - https://bcn.co.uk/data-and-ai/power-bi-services/
  - https://www.ranosys.com/uk/platforms/microsoft-power-bi-consulting/

- **Content source (the real substance to draw from)**: `inputs/content-source/`
  - `hlb-data-viz-v4 (1).html` — a 3-tab internal draft page (Data Visualization / Advanced
    Analytics / Power BI Services) prepared for HLB HAMT by Bala. **Only the Power BI tab
    (Tab 3, "Microsoft Power BI Services") is in scope for this requirement** — ignore the
    Data Visualization and Advanced Analytics tabs entirely, except where the Content Writer
    says below to link out to them as future sibling pages.
  - `HLB_HAMT_Data_Viz_Content_Documentation (1).docx` (and its extracted text,
    `data-viz-documentation-extracted.md`) — the developer/content documentation behind that
    HTML. Section 6 ("Tab 3 — Microsoft Power BI Services", starting around line 644 of the
    extracted text) is the relevant part. It matches the HTML exactly; the doc adds a
    suggested target URL (`hlbhamt.com/services/microsoft-power-bi-consulting-in-dubai-uae/`,
    for the original combined 3-tab page — treat as a data point, not necessarily this new
    standalone page's final slug) and PPC keyword notes.
  - **What the Power BI tab actually contains** (real, usable content, not to be reinvented):
    a "Why Power BI?" 4-pillar grid (Self-Service BI & Data Visualization; 360-Degree Business
    Visibility; Seamless Ecosystem Integration; Decision-Making on the Go); a "Power BI and
    HLB HAMT" positioning paragraph naming HLB HAMT as a Power BI implementation partner; a
    4-step "Power BI Service Portfolio" (Consulting & Discovery Workshops; Data Enrichment &
    ETL Kickstart; Data Visualization & Dashboards; Training & Continuous Support); a
    "Power BI Imperatives for Key Buyer Roles" section with bullet lists for Chief Data
    Officer, Chief Marketing Officer, and Chief Analytics Officer; an "Engage HLB HAMT" section
    with 4 engagement models (live demo, proof of concept, connector help, augmented
    expertise); a highlighted "Microsoft Power BI PowerUP!" fixed-price offer ($4,500,
    terms/deliverables in two columns); a "5-Step Power BI Proof of Concept" methodology; and
    a large FAQ (20 Q&As across 4 tabs: Power BI Basics, UAE & GCC, Technical & Integration,
    Why HLB HAMT).
  - **Shared hero stats** (from the combined page's hero, used across all 3 tabs, genuinely
    relevant to Power BI specifically): 200+ Connectors; 33x Faster Reports; 7 Days Proof of
    Concept; 14+ Yrs Gartner #1 (leader). These are legitimate to reuse for this page's hero
    or credential strip.
  - **Content Writer's instruction on scope**: use only the Power BI material from this
    source. Where the source content would naturally reference "Data Visualization" or
    "Advanced Analytics" as related capabilities, treat those as **separate sibling pages to
    be built later** and add internal-link placeholders to them (e.g. an internal link
    anchor like "data visualization services" or "advanced analytics services" pointing to a
    placeholder path), rather than absorbing that content into this Power BI page or
    pretending those pages already exist with real URLs.

- **Structural sample (mandatory template)**: `inputs/structural-sample/`
  - `sugarai-crm-hlbhamt-homepage.html` — the actual live HTML of
    https://hlbhamt.com/sugarai-crm-2/, HLB HAMT's real SugarAI CRM homepage (a WordPress/
    Elementor export, so the markup is heavy; a cleaned plain-text extraction of its visible
    content, in reading order, is saved alongside it as
    `sugarai-crm-homepage-extracted-text.txt` — start from that for structure and copy, refer
    to the raw HTML only for exact markup/classes when needed).
  - **Content Writer's instruction**: "use as the structural sample — same section order:
    Hero, Why PowerBI (dark band, stats), The platform, credential strip, Proven section with
    stats, FAQs and all other sections in it."
  - **Important discrepancy for the Plan agent to reconcile**: the Content Writer's named
    section list (Hero → Why-product dark stats band → platform → credential strip → proven
    stats → FAQ) matches the pattern used on the *industry subpages* built earlier in this
    project (Insurance, Field Service Management, etc.), which are shorter, single-purpose
    pages. The actual uploaded structural sample is different: it's the real SugarAI **homepage**
    section order is: Hero → credential strip (4 stats + a Nucleus Research recognition badge)
    right after the hero → "Why HLB HAMT" deep-dive (platform positioning, 5 sub-points) →
    "Explore SugarAI" (3 product modules table + an AI-layer block + a 3-point "Predicts /
    Summarises / Guides" AI-benefits block) → industries grid (12 cards) → offerings (6
    numbered items) → mid-page CTA → "Guided Low-Touch Onboarding" highlighted methodology
    section → "Packages" (6-category tabbed engagement-model matrix) → "Why UAE Businesses
    Choose HLB HAMT" (6-tile differentiator grid, credential-style, not numeric stats) → a
    short video/demo teaser → mid-page CTA → FAQ (7 Q&As) → final contact-form CTA → footer.
    There is no separate numbered "Proven section with stats" distinct from the credential
    strip on the real page. The Plan agent should follow the **actual uploaded homepage's**
    real section order and section types as the mandatory template (since it's the real,
    uploaded, authoritative sample), using the Content Writer's named list as a rough guide to
    intent (dark stats band early, credential strip, platform, proof, FAQ) rather than a
    literal checklist, and should explicitly note in the brief how it mapped the Content
    Writer's named sections onto the real template's actual sections.
  - **Scale note**: the real SugarAI homepage is far larger and more elaborate than the
    industry subpages built earlier in this project (it is not a 1,500-1,700 word page; the
    Plan agent should estimate its actual approximate word count from the extracted text and
    propose a comprehens, homepage-appropriate word count for this Power BI page instead of
    reusing the subpage convention). The Power BI content source (see above) is rich enough to
    fill a homepage of comparable depth, but does not have to match the SugarAI page's exact
    sub-item counts everywhere (e.g. it does not need 12 industry cards if Power BI content
    doesn't support that many distinct ones) — the Plan agent should size each section to the
    real content available, not pad to match counts.
  - **Real breadcrumb/parent chain**, confirmed from the structural sample's own nav menu:
    Home › Services › Technology Consulting Services › Digital Transformation & Analytics ›
    "Data Analytics & Business Intelligence (Power BI)". This is the real, current nav path on
    hlbhamt.com and should be used for the breadcrumb and parent link, in preference to the
    Microsoft URL given as "parent webpage" below (see open question).
  - **Cross-link opportunity found in the real homepage**: the SugarAI homepage's own "Why UAE
    Businesses Choose HLB HAMT" section already claims "Dual AI intelligence: SugarAI
    prediction plus Power BI analytics, from one partner" — confirming HLB HAMT already
    positions Power BI and SugarAI CRM together. This page and the SugarAI CRM homepage should
    cross-link to each other where natural.

- **Parent webpage as given**: https://www.microsoft.com/en-in/power-platform/products/power-bi
  — this is Microsoft's own Power BI product page, not an HLB HAMT page. Given the real
  breadcrumb chain found in the structural sample (see above), this is likely meant as
  background/context (what Power BI is, per its vendor) rather than the literal site-hierarchy
  parent. Flag this as an open question rather than guessing which the Content Writer intends
  for the breadcrumb.

- **No call transcript provided.**
- **No explicit word count given** — the Plan agent should propose one based on the real
  homepage's scale and the available Power BI content (see Scale note above).
