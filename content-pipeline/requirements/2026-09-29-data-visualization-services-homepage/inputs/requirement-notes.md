# Requirement notes

- **Content type**: Webpage — the homepage for Data Visualization and the services HLB HAMT
  provides around it. Standalone product/service homepage, following the same pattern as the
  already-delivered Power BI services homepage and Advanced Analytics services homepage in this
  repo. Not an industry subpage.

- **Primary keyword**: data visualization services in UAE
- **Secondary keywords**: data visualization services; data analytics and visualization
  software; data visualization experts in UAE; data visualization technologies; data
  visualization consulting services

- **Reference websites (competitors)**: the Content Writer's list mixes page titles and one
  real URL. Only one URL was actually given:
  - https://www.instinctools.com/data-visualization/
  The other five are page titles only, no URL: "Data Visualization Services - Softcrylic",
  "Data Visualization Consulting Services | Interactive Dashboards", "Data Visualization
  Services", "Data Visualization Services | IT IDOL Technologies", "Data Visualization Services
  | Business intelligence Consulting", "Data Visualization Services to Transform Complex Data".
  **Plan should search for each by title to find the real URL** (WebSearch), the same way past
  requirements in this project have resolved incomplete references, and note in the brief which
  were found vs. not found. **Likely copy-paste note**: the Content Writer's message describes
  these as "competitor website who provide Power BI services" — almost certainly meant "Data
  Visualization services" given the rest of the request; treat them as Data Visualization
  competitors, not Power BI ones.
  **Instruction**: "there is more information in competitor webpage. put the content without any
  plagiarism in my page." — same standing rule as the other two sibling pages: competitor
  content may inform substance/structure/gaps, but no sentence, heading, or distinctive phrase
  may be copied or closely paraphrased. This is explicit Content Writer instruction here, not
  just the project's default.

- **Content source (the real substance to draw from)**: `inputs/content-source/` (same Bala
  3-tab draft used for the other two sibling pages, copied here). **Only Tab 1 ("Data
  Visualization") is in scope for this requirement** — ignore Advanced Analytics (Tab 2) and
  Power BI Services (Tab 3) entirely, except to link out to them as sibling pages (see internal
  linking note below).

- **Existing live HLB HAMT page** (uploaded, `inputs/existing-page/data-visualization-services-uae.html`
  + extracted text): HLB HAMT's own existing live "Data Visualization Services" page. Per the
  Advanced Analytics requirement's own research (see
  `content-pipeline/requirements/2026-09-29-advanced-analytics-services-homepage/brief.md`
  Section 12.9/L7), this live page at `/services/data-visualization-uae/` is already linked from
  both the Power BI and Advanced Analytics delivered pages. **Assess overlap the same way the
  other two requirements did**: is this existing page essentially Bala's Tab 1 word for word (as
  happened with both the Power BI partner page and the Advanced Analytics page)? If so, apply
  the same recommendation pattern (replace in place at the existing URL, note reuse limits).
  Cannot fetch hlbhamt.com directly (bot-protected, confirmed repeatedly in this project) — this
  uploaded file is the authoritative copy.
  **Important**: since Power BI's L7 and Advanced Analytics' L3/other links already point to
  `/services/data-visualization-uae/`, replacing that page in place (if recommended) means those
  two already-delivered sibling pages' links will now point to the NEW version automatically —
  flag this clearly in the brief and in the handoff, and note it doesn't require editing the
  other two pages, only confirming their links still make sense.

- **Structural sample (mandatory template)**: `inputs/structural-sample/` — the real live HTML
  of https://hlbhamt.com/sugarai-crm-2/, reused from the Advanced Analytics requirement (same
  file, no new upload this time). Follow the same section-order/type approach as the other two
  sibling pages (hero, credential strip, "Why HLB HAMT" platform positioning, "Explore
  [product]" module block, use-cases/industries grid, offerings, mid-page CTA(s), methodology
  section, packages/engagement-model matrix, "Why UAE Businesses Choose HLB HAMT" tile grid,
  video/demo teaser, FAQ, final contact CTA, footer). Size each section to the real Data
  Visualization content available, not padded to match the template's exact counts.
  **"Why AI Changes CRM" section**: the Content Writer didn't explicitly address this section
  for this requirement (unlike Advanced Analytics, where it was explicitly excluded). Given it's
  CRM/AI-specific and neither of the other two sibling pages built an equivalent, **apply the
  same exclusion by default** (don't build an equivalent section) and note this as an assumed
  default in the brief for the Content Writer to confirm/override.

- **Parent webpage as given**: "Data Visualization Definition and Examples | Microsoft Visio" —
  this is a Microsoft product page for a specific named tool (Visio), not an HLB HAMT page.
  Following the exact same precedent as the Power BI requirement's parent-webpage question
  (which was Microsoft's own product page too): treat this as background/context only, not the
  literal site-hierarchy parent — the real breadcrumb parent should be the live HLB HAMT nav
  chain, consistent with the other two sibling pages. **Also**: per this project's standing
  no-third-party-tool-names rule (established during the Power BI Revision 3 and applied from
  the start on Advanced Analytics), **do not name "Microsoft Visio" or any other specific
  visualization tool anywhere on the page** — flag this explicitly since "data visualization" as
  a topic tends to invite naming specific tools (Tableau, Qlik, Looker, D3.js, Visio, etc.).
  Power BI is the one exception, and only as the HLB HAMT sibling-service cross-link, same as on
  the Advanced Analytics page.

- **Explicit Content Writer instructions**:
  1. **HLB HAMT branding** — same standing preference as the other two sibling pages: HLB HAMT
     is the actor/provider, the technology is what it delivers on, not the reverse. Apply from
     the start.
  2. **"The page should talk about the data visualization service"** — keep the page focused on
     data visualization as HLB HAMT's own service offering, not a generic explainer of what data
     visualization is as a concept.
  3. **No plagiarism** from the competitor pages (see Reference websites note above).
  4. **"The content flow should be systematic"** — the section order and progression should read
     as a clear, logical build (what data visualization is and why it matters → HLB HAMT's
     platform/approach → capabilities → use cases → services → proof/methodology → engagement →
     FAQ → contact), mirroring the structural sample's own logical flow rather than a loose
     grab-bag of sections.

- **Internal linking**: to the Power BI services homepage (delivered, find current details from
  `content-pipeline/requirements/2026-09-28-power-bi-services-homepage/`) and to the Advanced
  Analytics services homepage (delivered, find current details from
  `content-pipeline/requirements/2026-09-29-advanced-analytics-services-homepage/`, published at
  `/services/advanced-data-analytics-uae/`) as separate sibling pages, per the Content Writer's
  instruction "while giving internal links to Power BI and Advanced analytics as separate
  pages". Both sibling pages already exist and are delivered, so these can be real links, not
  placeholders (unlike the placeholder situation the other two pages had for each other/for this
  page before it existed).

- **No call transcript provided.**
- **No explicit word count or CTA count given** — size the word count the same way the other two
  sibling pages did (estimate template scale, competitor lengths, real content available). For
  CTA count, the Advanced Analytics page used 3-4 CTAs placed across the page per explicit
  instruction; no such instruction was given here, so **default to the same 3-4 CTA convention**
  established across the sibling pages unless Plan finds a reason to differ, and note this as an
  assumed default for Content Writer confirmation.
