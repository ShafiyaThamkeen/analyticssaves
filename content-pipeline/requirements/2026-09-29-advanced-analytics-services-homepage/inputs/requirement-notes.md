# Requirement notes

- **Content type**: Webpage — the homepage for Advanced Analytics and the services HLB HAMT
  provides around it. This is a standalone product/service homepage, following the same
  pattern as the already-delivered Power BI services homepage
  (`content-pipeline/requirements/2026-09-28-power-bi-services-homepage/`) and the live SugarAI
  CRM homepage. Not an industry subpage.

- **Primary keyword**: advanced analytics services in UAE
- **Secondary keywords**: Advanced analytics services; advanced analytics company in UAE; data
  analytics and automation

- **CTAs**: the Content Writer asked for **3-4 CTAs** placed across the page (not just one at
  the end). Plan should identify natural CTA placement points across the section skeleton
  (e.g. mid-page CTA(s), plus the final contact CTA), matching how the SugarAI/Power BI
  homepages already place multiple CTAs through the page rather than only at the bottom.

- **Reference websites** (competitor Advanced Analytics service pages — for positioning/gaps,
  nothing may be copied or paraphrased):
  - https://www.drcsystems.com/us/advanced-analytics-and-insights/
  - https://ometis.co.uk/services/data-analytics
  - https://www.protiviti.com/uk-en/advanced-analytics-services
  - https://insightconsulting.co.uk/services/advanced-data-analytics/
  - https://www.apexon.com/our-services/data-analytics/advanced-analytics-and-ai-ml-services/
  - https://www.softcrylic.com/advanced-analytics-services/

- **Content source (the real substance to draw from)**: `inputs/content-source/` (same files
  used for the Power BI homepage requirement, copied here — this is Bala's 3-tab draft).
  **Only the Advanced Analytics tab (Tab 2) is in scope for this requirement** — ignore the
  Data Visualization (Tab 1) and Power BI Services (Tab 3) tabs entirely, except to link out to
  them as sibling pages (see internal linking note below).
  - `hlb-data-viz-v4 (1).html` — read only Tab 2 ("Advanced Analytics" / similar heading —
    locate it the same way Plan located Tab 3 for the Power BI requirement).
  - `HLB_HAMT_Data_Viz_Content_Documentation (1).docx` / `data-viz-documentation-extracted.md`
    — the developer/content documentation behind that HTML. Find Tab 2's section (parallel to
    how Section 6 covered Tab 3 for Power BI).

- **Existing live HLB HAMT page** (uploaded, `inputs/existing-page/advanced-data-analytics-services-uae.html`
  + extracted text): this is HLB HAMT's own existing live "Advanced Data Analytics Services in
  UAE" page. Treat it as a real, authoritative HLB HAMT source, similar to how the Power BI
  homepage requirement folded in HLB HAMT's other live sibling pages
  (`2026-09-28-power-bi-services-homepage/inputs/hlbhamt-sibling-pages/`). Real service detail,
  credentials and positioning language may be drawn from it directly (not just inspiration).
  **Important — flag and reconcile:** this page's URL/positioning may substantially overlap
  with the new homepage being planned here (the same situation as the Power BI partner page,
  which turned out to be near-duplicate of Bala's draft). Plan must explicitly assess: is this
  existing page essentially the same content as Bala's Tab 2 draft (in which case, treat it as
  a redirect candidate and note the reuse-limit question for the Content Writer, same as the
  Power BI requirement's R2-1), or is it materially different content that should be preserved/
  merged? Do not assume; check both and report findings plus a recommendation in the brief's
  open questions, exactly as was done for the Power BI requirement's sibling-page analysis.
  Cannot fetch hlbhamt.com directly (bot-protected, confirmed repeatedly in this project) — this
  uploaded file is the authoritative copy.

- **Structural sample (mandatory template)**: `inputs/structural-sample/` — the real live HTML
  of https://hlbhamt.com/sugarai-crm-2/ (uploaded as `sugarai-crm-hlbhamt-homepage.html`, same
  file used for the Power BI homepage requirement, re-uploaded here). A cleaned plain-text
  extraction is saved alongside it as `sugarai-crm-homepage-extracted-text.txt`.
  - **Content Writer's instruction**: "use as the structural sample — same section order — for
    ALL sections EXCEPT 'Why AI Changes CRM'." That section is CRM/AI-specific and doesn't
    apply to an Advanced Analytics page. Plan should map or drop it, the same way the Power BI
    homepage requirement handled/removed the analogous "AI Insights" section relative to this
    same template (see that requirement's brief.md Section 12.2 for precedent, though note: for
    THIS requirement the instruction is to exclude it from the start, not remove it after a
    revision — so Plan should simply not include an equivalent section in the initial skeleton,
    with a one-line note on why, rather than building it and removing it later).
  - Otherwise, follow the real template's actual section order and types (hero, credential
    strip, "Why HLB HAMT" platform positioning, "Explore [product]" module block, industries/
    use-cases grid, offerings, mid-page CTA(s), methodology/onboarding section, packages/
    engagement-model matrix, "Why UAE Businesses Choose HLB HAMT" tile grid, video/demo teaser,
    FAQ, final contact CTA, footer) — same approach as the Power BI homepage requirement's
    Section 3a mapping. Size each section to the real Advanced Analytics content available
    rather than padding to match the SugarAI page's exact counts.

- **Internal linking**: this page should link out to **Power BI Services** (already live/built
  — link to the real delivered Power BI homepage once Plan confirms its current state/URL from
  the other requirement folder) and **Data Visualization services** (not yet built — link as a
  placeholder, same placeholder-link convention used in the Power BI requirement for its own
  not-yet-built siblings).

- **No call transcript provided.**
- **No explicit word count given** — size it the same way the Power BI homepage requirement
  did: estimate the template's real body-copy word count, look at competitor page lengths, and
  size to the real Advanced Analytics content available (see that requirement's brief.md
  Section 1 "Word count" row for the methodology to replicate).

- **Branding note (carry over from the Power BI revision)**: the Content Writer's standing
  preference, established during the Power BI homepage revision, is HLB HAMT-led branding
  throughout (HLB HAMT as the actor/provider, the technology as what it delivers on, not the
  reverse) and no named competitor or third-party tool/product names beyond what's essential to
  describe HLB HAMT's own service. Plan should apply the same branding posture from the start
  this time, rather than needing a later revision to fix it, and should flag in the brief if a
  specific competitor tool name (e.g. a named analytics/ML platform) seems necessary for
  technical accuracy so the Content Writer can decide up front.
