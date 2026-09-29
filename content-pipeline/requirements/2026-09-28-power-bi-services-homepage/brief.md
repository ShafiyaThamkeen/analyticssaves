# Content brief: Microsoft Power BI Services homepage (standalone product/service homepage)

Requirement folder: `content-pipeline/requirements/2026-09-28-power-bi-services-homepage/`
Prepared by: Plan agent, 2026-09-28
Status: **APPROVED (2026-09-28), all 7 open questions resolved to their stated defaults.** Ready for Build. See Section 10.
**Revision 2 (2026-09-29): brief UPDATED for a content-quality revision. Awaiting Content Writer approval before Build.** See Section 12. It covers the new sourcing (4 live HLB HAMT sibling pages and 4 fetched competitor pages), the removal of AI Insights and the shift to HLB HAMT-led branding.

> **Precedence rule for Build and Test (Revision 2):** Sections 1-10 stay as the approved baseline. **Where Section 12 differs from anything in Sections 1-10, Section 12 wins.** Short "R2" callouts below mark each place where an original section is overridden. Anything without an R2 callout still applies exactly as written: keyword plan substance, word count range, the SugarAI structural mapping, the accuracy corrections and the Section 10 decisions. **Section numbers S0-S17 in Sections 2-10 are the original numbering. Section 12.2 gives the old-to-new renumbering after AI Insights is removed.**

> **Inputs read in full:** `inputs/requirement-notes.md`; `inputs/content-source/hlb-data-viz-v4 (1).html` (whole file read; only Tab 3, lines 302-418, plus the shared hero stats and closing CTA are in scope); `inputs/content-source/data-viz-documentation-extracted.md` (the .docx was already extracted before planning, so I read that extraction instead of re-running the docx skill; Section 6 matches the HTML); `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt` (all 772 lines) and the raw `sugarai-crm-hlbhamt-homepage.html` (checked for heading tags, section IDs, band colours and nav URLs). No transcript was provided.
>
> **New files I wrote for Build and Test:** `inputs/extracted/hlb-data-viz-v4 (1).html.md` (Tab 3 content plus the shared hero and CTA, with Tabs 1-2 deliberately left out) and `inputs/extracted/HLB_HAMT_Data_Viz_Content_Documentation (1).docx.md` (the in-scope parts of the docx: target URL, the context for the 33x claim, PoC step detail and PPC notes). **Build works from those two files plus the structural sample `.txt`. Build must not open Tab 1 or Tab 2 content.**
>
> **Research limitations:** WebFetch returned empty pages for every hlbhamt.com URL I tried (the site renders client-side), and HTTP 403 for `powerbi.microsoft.com` and `community.fabric.microsoft.com`. So the Gartner 2026 claim is confirmed from search results plus a verbatim repost (mwpro.co.uk, 3 July 2026) of Microsoft's announcement, not from Microsoft's page itself. I did open the Microsoft investor, Microsoft Learn and Microsoft On the Issues pages directly. I also fetched all five competitor pages directly. Their word counts come from the fetch tool's summaries and are approximate.

---

## 1. Requirement summary

| Item | Detail |
|---|---|
| Content type | **Webpage: standalone Power BI product/service homepage.** It follows the structure of the live SugarAI CRM homepage (`hlbhamt.com/sugarai-crm-2/`). It is **not** an industry subpage. Site position: Home › Services › Technology Consulting Services › Digital Transformation & Analytics › Data Analytics & Business Intelligence (Power BI). |
| Target audience | Decision makers in UAE and wider GCC organisations that run on Microsoft 365, Azure or Dynamics, or on common ERPs (SAP, Oracle, NetSuite) and CRMs, and that report from spreadsheets or disconnected systems. **Economic buyers:** CFO/Group Finance Director, COO, CEO/MD. **Data-side buyers named in the source:** Chief Data Officer, Chief Marketing Officer, Chief Analytics Officer. **Also:** IT/BI managers and heads of reporting. Sectors named in the source: real estate, construction, hospitality, trading, financial services, healthcare, retail, logistics, government and education, across all 7 emirates plus KSA, Oman, Bahrain, Kuwait and Qatar. |
| Business goal | Rank for **"Power BI service"** and the Power BI partner/consulting cluster in the UAE. Position HLB HAMT as the finance-literate Power BI partner: a licensed audit, tax and advisory firm that also builds the data platform, with Arabic/RTL design, UAE data residency and UAE tax logic. Drive three conversions: **(1)** consultation or live demo request, **(2)** 7-day proof of concept sign-up, **(3)** $4,500 PowerUP! fixed-price accelerator enquiry. |
| **Word count** | **3,100-3,500 words, target about 3,300.** Test agent: fail below 2,900 or above 3,750. **How I sized it:** (a) I estimate the SugarAI template's unique visible body copy at **about 3,600 words (range 3,400-3,800)**. I tallied it section by section from the extracted text: hero and "one platform" block ~160, strip and badge ~55, Why HLB HAMT ~260, Explore SugarAI plus the AI layer and AI block ~460, 12 industry cards ~740, 6 offerings ~370, onboarding ~140, packages ~465, Why UAE grid ~120, video and the two CTAs ~80, 7 FAQs ~800, contact block ~40. The Packages tab copy appears twice in the markup (desktop tabs plus mobile accordion), and I counted it once. Nav, mega-menu, form labels and footer are excluded. (b) Competing pages: BCN ~3,500, Yes Dynamic ~2,400-2,800, Zenzero ~1,800-2,000, DSP ~1,400-1,600, Ranosys ~1,200-1,400. (c) Real content available: Tab 3 is about 2,000 words of source material, and most of that is FAQ. The Power BI page has fewer distinct sub-items than SugarAI (6 use-case cards, not 12), so I sized it **slightly under the template** rather than padding to match. **Count rule:** all visible body text (H1, headings, ledes, card and tile text, list items, strip labels and descriptions, PowerUP! terms and deliverables, FAQ questions and answers, CTA headings and body). **Excluded:** nav, anchor nav, breadcrumb, eyebrow labels, button labels, form field labels, footer, meta tags, alt text, JSON-LD and the footnote/source list. |
| Positioning | **R2 override: HLB HAMT-led.** HLB HAMT is the provider and Power BI is the platform it delivers on. See Section 12.3. The original wording follows for reference. **Positive and capability-led.** Power BI turns the data a business already has into one trusted set of numbers. HLB HAMT is the partner that gets the numbers right, because it understands the finance and regulatory logic behind them. **No pain-point opening.** The hero leads with the outcome. |
| Tone and style | Specific and technical in headings (semantic models, DAX, row-level security, workspaces and apps, data gateway, medallion lakehouse, IAS 12, intercompany eliminations), outcome-led in body copy. **British spelling** to match the live site (visualisation, optimise, organisation, programme, licence as a noun). Exceptions: Microsoft product names and exact keyword strings. **Zero em dashes anywhere.** Do not name competing consultancies. Do not name sources inline except where honest attribution needs it (Microsoft and Gartner in the recognition bar, Microsoft for the Fabric and AI-adoption figures). Every stat gets a footnote marker `[n]`. |
| Template | **Mandatory:** the live SugarAI CRM homepage (`inputs/structural-sample/`). Follow its real section order and section types (Section 3). The Content Writer's industry-subpage section names are mapped onto it in Section 3a. |

---

## 2. Keyword placement plan

> **R2:** Keywords, count ranges, regexes and stuffing caps are unchanged. Only the section numbers in the "Subheadings" and "Exact placements" columns move, because AI Insights is removed. The renumbered placement table is in Section 12.6, which also adds two branding counts ("HLB HAMT" floor, "Microsoft" cap) for Test.

### 2a. Count rules for the Test agent (read first)

- Count **on-page copy only**: H1, headings, body, card/tile text, list items, FAQ questions and answers, CTA headings and body. **Do not count** button labels, eyebrows, anchor nav, breadcrumb, meta, alt text or schema. Meta title and description are checked separately against Section 7.
- **Primary "Power BI service" (singular)** counts only as a whole-word match **not followed by "s"**. Regex, case-insensitive: `\bPower BI service\b(?!s)`. "Power BI Services" contains "Power BI Service" as a substring, so a naive substring count would double-count the plural. Do not do that.
- **"Power BI Services" (plural)**, regex, case-insensitive: `\bPower BI services\b`.
- Other secondaries: exact phrase, case-insensitive. Exception: "Certified Power BI Partner in UAE" also matches "Certified Power BI partner in UAE" (casing only). "In the UAE" does **not** count as a match for this keyword.

### 2b. How singular and plural are kept apart

They mean different things, and the page uses that:
- **"Power BI service" (singular) = Microsoft's cloud platform** (the SaaS at app.powerbi.com where reports are published, shared, refreshed and secured, as opposed to Power BI Desktop). Microsoft Learn uses this exact term. So "your Power BI service", "the Power BI service" and "Power BI service setup" read as precise technical language, not keyword repetition. The one allowed exception is the H1, where "Power BI Service Partner" works as a compound noun.
- **"Power BI Services" (plural) = HLB HAMT's offerings.** It appears in two H2s only, where title case makes it read as a service-line name.
- **Never** put the singular and the plural in the same paragraph, card or heading/lede pair. **Never** write "Power BI service services" or "Power BI Services service".

### 2c. Placement table

| Keyword | Meta title | Meta description | H1 | Subheadings | First 100 words | On-page count (Test checks) | Exact placements |
|---|---|---|---|---|---|---|---|
| **Power BI service** (primary, singular) | Yes, at the start ("Power BI Service & Consulting Partner...") | Yes, first three words | **Yes:** "Power BI Service Partner for Smarter Decisions Across the UAE" | Explore card 2 title (S5); FAQ 1 question (S15) | Yes: H1 plus hero lede sentence 1 | **5-7** (hard max 8) | (1) H1; (2) hero lede sentence 1, e.g. "...designs, builds and runs your Power BI service..."; (3) S5 module card 2 title "The Power BI service"; (4) S4 card "What we do" (setting up and governing the Power BI service: workspaces, apps, security, refresh); (5) S15 FAQ 1 question "What is the Power BI service, and how is it different from Power BI Desktop?"; (6, optional) FAQ 1 answer, **once only**, then "the cloud service"/"the service"; (7, optional) S11 Support tab item on administering the Power BI service. |
| **Power BI Services** (plural) | No | No | No | **S8 H2 "Our Power BI Services"**; **S12 H2 "Why UAE Businesses Choose HLB HAMT for Power BI Services"** | No | **2-3** | (1) S8 H2; (2) S12 H2; (3, optional) S16 final CTA body. Never in the same section as a singular instance. |
| **Power BI consulting company** | No | No | No | No | No | **1-2** | (1) S4 lede, e.g. "As a Power BI consulting company that is also a licensed audit, tax and advisory firm..."; (2, optional) S12 intro line. |
| **Power BI solutions expert** | No | No | No | No | No | **1-2** | (1) S14 mid-page CTA body: "a Power BI solutions expert will scope..." (the body text, not the button); (2, optional) S11 Extend tab, "Augmented expertise" item: a dedicated Power BI solutions expert working inside your team. |
| **Certified Power BI Partner in UAE** | Alternate title only (Section 7), and only if OQ1 is confirmed | No | No | **S12 tile 1 title** "Certified Power BI partner in UAE" | No | **Exactly 1** (max 2 with the meta alternate) | **Conditional on Open Question 1.** If HLB HAMT's Microsoft designation is confirmed, use it once, as S12 tile 1's title. A terse tile title absorbs the missing "the". The same tile pattern ("Certified SugarCRM partner in the UAE") already exists on the SugarAI page. **If not confirmed:** the tile title becomes "Microsoft Power BI partner in the UAE". Record the keyword as not placed, with the reason. Do not put the word "certified" anywhere on the page without confirmation. |

### 2d. Stuffing risks

1. **Singular/plural overlap** (handled in 2a and 2b). Test must use the regexes above.
2. **"Power BI" brand density.** The source is dense with it (about 2.5% of Tab 3). **Cap "Power BI" (any form) at 75 on-page mentions (about 2.3% at 3,300 words).** Test flags anything above 85. Tools for Build: "the platform", "your reports", "Microsoft's analytics platform", "dashboards", "the semantic model". Card and step titles should not all start with "Power BI". At most **2 of the 6** offering titles in S8, and at most **1 of the 5** PoC step titles, may contain "Power BI".
3. **"UAE" repetition.** Keep it to 12 or fewer on-page mentions. Use "the Emirates", "across the GCC", "Dubai and Abu Dhabi" and "in-country" for variety.
4. **Secondary keywords stay in their assigned slots.** Do not add extra instances for "coverage". Topical relevance comes from the natural vocabulary (implementation, dashboards, DAX, semantic model, Fabric, Copilot).

---

## 3. Section structure (mirrors the real SugarAI homepage)

### 3a. How the Content Writer's named sections map onto the real template

The Content Writer described the page with the industry-subpage naming convention: "Hero, Why PowerBI (dark band, stats), The platform, credential strip, Proven section with stats, FAQs and all other sections." The uploaded homepage is structured differently. It has **no separate numbered "Proven" band**, its **only dark stats band is the strip directly under the hero**, and the phrase "The platform" is the opening of its "Why HLB HAMT" H2. I followed the real template's order and mapped each named intent like this:

| Content Writer's name | Where it really lives in the SugarAI homepage | This page's section |
|---|---|---|
| Hero | Hero (H2 in the live markup; see note 1 below) plus a "One platform. One customer record." 3-card sub-block and a deployment line | **S1 Hero + "one version of the numbers" sub-block** |
| Why PowerBI (dark band, stats) | Two parts: **(a)** the dark (#3c3c3b) 4-item stat strip right after the hero (markup label "Company Statistics and Capabilities"); **(b)** the product-explanation section "Explore SugarAI" (module table + AI layer) | **(a) S2 dark stats strip** (4 stats/credentials); **(b) S5 "Why Power BI..." section**, built on the 4 "Why Power BI?" pillars from the source |
| The platform | "WHY HLB HAMT" section, whose H2 opens "The platform matters. The partner decides the outcome." (intro + 4 info cards) | **S4 Why HLB HAMT** (new H2; do not reuse the SugarAI line) |
| Credential strip | The recognition bar directly under the stat strip ("Recognized Leader in SFA, Nucleus Research Value Matrix 2026" + Download Report), plus the credential-style "Why UAE Businesses Choose HLB HAMT" tile grid lower down | **S2b recognition bar** (Microsoft's Gartner 2026 Leader recognition) + **S12 credential grid** |
| Proven section with stats | There is no separate proof band. Proof sits in the strip stats, the recognition badge and the "HLB HAMT Methodology & Advantage" grid | Proof is spread out, never repeated: strip stats (S2), recognition bar (S2b), one sourced stat in S5, one in S6, the 7-day PoC in S10, non-numeric proof tiles in S12. **No separate stats band**, because the template has none and a band would force stats to repeat. |
| FAQs | "What buyers ask us before they shortlist" (7-item single accordion) | **S15 FAQ** (9 items, single accordion) |
| "All other sections in it" | Sticky anchor nav; AI block ("Why AI Changes CRM"); industries grid; numbered offerings; 2 mid-page CTAs; "Guided Low-Touch Onboarding" methodology; "Packages" tabbed engagement matrix; video teaser; contact form; footer | S3, S6, S7, S8, S9, S10, S11, S13, S14, S16, S17 |

**Template facts that differ from the requirement notes (so nobody is surprised later):**
1. The live template has **no H1**. Its hero headline is an `<h2>`. This page **must** have exactly one H1, in the hero.
2. "Why HLB HAMT" has an intro plus **4** info cards (What we do / Who we work with / How we deliver / Support after go-live), not 5.
3. The template's anchor nav lists "Industries" before "AI Insights", but in the DOM the AI block (`#aiinsights`) comes before the industries grid (`#industries`). **This page lists anchor-nav items in DOM order.**
4. There is a 3-card "One platform" sub-block and a deployment line inside the hero area. The notes did not mention it, and this page mirrors it.
5. The source FAQ has **21** Q&As (6/6/5/4 across the 4 tabs), not 20. The docx version has 22 because it splits "industries and regions" into two questions.

### 3b. Skeleton (section order is mandatory)

| # | Section (anchor ID) | Template equivalent | Heading level | Budget (words) |
|---|---|---|---|---|
| S0 | Breadcrumb | Site breadcrumb | none | excluded |
| S1 | Hero + "one version of the numbers" sub-block + deployment line | Hero + "One platform" block | **H1** + H3 cards | 150-190 |
| S2 | Dark stats strip (4 items) | `.hlb-strip-wrapper` (#3c3c3b, no heading tags, role=list) | none | 45-65 (with S2b) |
| S2b | Recognition bar | Nucleus badge row | none (p + button) | (in S2) |
| S3 | Sticky anchor nav | `.hlb-nav-wrapper` | none | excluded |
| S4 | Why HLB HAMT (`#whyhlbhamt`) | "WHY HLB HAMT" | H2 + 4 x H3 | 250-300 |
| S5 | Why Power BI / Explore Power BI (`#explorepowerbi`) | "Explore SugarAI" module table + AI Layer | H2 + 4 x H3 + H3 layer block | 380-440 |
| S6 | AI insights (`#aiinsights`) | "Why AI Changes CRM" (Predicts/Summarises/Guides) | H2 + 3 x H3 | 150-190 |
| S7 | Use cases by role and sector (`#usecases`) | Industries flip-card grid | H2 + 6 x H3 + pill row | 330-400 |
| S8 | Our Power BI Services (`#services`) | "Our Sugar Offerings" 01-06 | H2 + 6 x H3 | 330-390 |
| S9 | Mid-page CTA 1 | "Ready to turn customer data into your next move?" | H2 | 20-30 |
| S10 | 5-step proof of concept (`#methodology`) | "Guided Low-Touch Onboarding: Live in Days" highlighted band (#005A77) | H2 + 5 x H3 | 150-190 |
| S11 | Engagement models + PowerUP! (`#packages`) | "How an Engagement Is Structured" tabbed matrix | H2 + featured card H3 + 4 tabs (H3 items) | 360-420 |
| S12 | Why UAE businesses choose HLB HAMT | "Why UAE Businesses Choose HLB HAMT for SugarAI" 6-tile grid | H2 + 6 x H3 | 140-180 |
| S13 | See it in action (video/demo teaser) | "Sixty seconds inside SugarAI" | H2 | 30-45 |
| S14 | Mid-page CTA 2 | "Plan your SugarAI rollout with our consultants" | H2 | 20-30 |
| S15 | FAQ (`#faq`) | "What buyers ask us before they shortlist" | H2 + 9 x H3 (questions) | 700-850 |
| S16 | Final contact CTA + form | "Let's Connect" form block | H2 | 20-30 |
| S17 | Footer | Global footer | none | no new copy |

**Anchor nav labels (S3), in this order:** Why HLB HAMT · Why Power BI · AI Insights · Use Cases · Services · Proof of Concept · Engagement Models · FAQ.

> **R2:** S6 AI Insights is removed, and the sections after it renumber (S7 becomes S6, and so on). The anchor nav loses "AI Insights", and "Why Power BI" becomes "The Platform". Budgets are reallocated. The revised skeleton is in Section 12.4 and replaces the table above for Build.

**Schema** (the source docx recommends this too): `Service` (serviceType "Microsoft Power BI consulting and implementation", provider HLB HAMT, areaServed UAE + GCC countries), `FAQPage` (the 9 Q&As, text identical to on-page copy), `BreadcrumbList` (S0). Note: Google now shows FAQ rich results mainly for government and health sites, so FAQPage schema is for completeness, not a guaranteed rich result.

---

## 4. Section-by-section outline

> **R2:** The outline below is still the baseline for every section except S6, which is removed. Section 12.5 lists each section's Revision 2 changes (new sibling-page facts, HLB HAMT-led framing, relocated links). Build applies Section 4 and Section 12.5 together, and Section 12.5 wins where they conflict.

Footnote markers `[n]` map to Section 6. "CS" means content-source (HLB HAMT's own prepared content). Anything I verified or sourced is labelled "S" (stat) or "F" (fact). Suggested headings are original. Build may refine the wording but must keep the keyword, the technical specificity and the no-em-dash rule. **Do not reuse any SugarAI H2 verbatim.**

### S0. Breadcrumb
Home (`https://hlbhamt.com/`) › Services › Technology Consulting Services (`https://hlbhamt.com/services/technology-consulting-services-dubai-uae/`) › Digital Transformation & Analytics (`https://hlbhamt.com/services/digital-transformation-uae/`) › Data Analytics & Business Intelligence (Power BI). This is the live nav chain. It is subject to Open Question 2.

### S1. Hero (H1) + sub-block + deployment line (150-190 words)
- **Must accomplish:** say what HLB HAMT does with Power BI and the outcome it delivers, in positive terms. Land the primary keyword twice. Offer the two main conversions.
- **Eyebrow** (not counted): "Microsoft Power BI".
- **H1:** "Power BI Service Partner for Smarter Decisions Across the UAE" (primary #1).
- **Lede** (2 sentences, 45-60 words): sentence 1 uses the primary keyword (#2): HLB HAMT designs, builds and runs your Power BI service, turning ERP, CRM, finance and spreadsheet data into dashboards leadership trusts. Sentence 2 covers the finance-plus-technology angle, for businesses across the UAE and GCC. Source: Tab 3 subtitle idea ("insights for smarter decisions anytime, anywhere") and the info-box positioning.
- **Buttons** (not counted): "Book a Power BI consultation" → `#contact`; "See the PowerUP! offer" → `#packages`.
- **Sub-block** (mirrors "One platform. One customer record."): a one-line heading built on "one model, one version of the numbers" + 1 sentence, then 3 audience cards (title + 12-18 words each), all from FAQ 2 and FAQ 6:
  - **Leadership:** a one-page dashboard of the KPIs checked every morning.
  - **Analysts:** multi-page reports with filters and drill-downs that explain *why* a number moved.
  - **Teams on the move:** the same reports on iOS and Android, with alerts. **Do not say Windows.** Microsoft retired the Power BI Windows app, so the source's "iOS, Android, and Windows" is out of date.
- **Deployment line** (mirrors SugarAI's deployment footer, 25-35 words): data can be hosted in Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud regions, so it stays in-country. UAE North runs the full Fabric platform. UAE Central supports Power BI only. [F3]
- **No stats in the hero.** 200+, 33x and 7 days each have their own section.

### S2. Dark stats strip (4 items, no heading tags) + S2b recognition bar (45-65 words total)
- **Must accomplish:** the Content Writer's "dark band, stats" slot. It gives fast, credible proof immediately under the hero.
- **Items** (stat line + 8-16-word description, `.hlb-strip-stat` / `.hlb-strip-desc` pattern):
  1. **200+**: data connectors available in Power BI, from ERP and CRM to files and cloud databases. [CS1][1]
  2. **33x**: faster report load times in one recent HLB HAMT optimisation engagement. [CS2][2] The qualifier "in one recent engagement" (or equivalent) is **mandatory**.
  3. **Finance + technology**: a licensed audit, tax and advisory firm that also builds your data platform. (CS hero mini-card)
  4. **Arabic and English**: right-to-left dashboards designed from the first mockup, not retrofitted. (CS FAQ 7)
- **S2b recognition bar** (mirrors the Nucleus badge): "Microsoft: named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year" [3], plus a button "Read Microsoft's announcement" linking to the source URL in Section 6. The wording must make clear this is **Microsoft's** recognition for its platform, not HLB HAMT's. **Never** write "Gartner #1", "ranked #1" or "14+ years". Deliver adds Gartner's standard disclaimer to the sources note (Section 6, S-3).

### S3. Sticky anchor nav
Labels in Section 3b. Not counted.

### S4. Why HLB HAMT (`#whyhlbhamt`) (250-300 words)
- **Must accomplish:** the Content Writer's "The platform" intent. The platform is powerful, and the partner's grasp of the numbers decides whether the dashboards are trusted.
- **Eyebrow:** "WHY HLB HAMT". **Suggested H2:** "Great Dashboards Start With the Numbers Behind Them".
- **Lede** (55-70 words): uses **"Power BI consulting company"** (#1). HLB HAMT is a licensed audit, tax and advisory firm that also designs and builds analytics, and a member of the HLB International network. Include the internal link **"digital transformation and analytics services"** → parent (Section 8, L1). Sources: Tab 3 info box (implementation partner, self-service BI ecosystems, flexible engagement models); FAQ 18 (finance + technology).
- **4 info cards** (H3 + 40-50 words each):
  1. **What we do:** end-to-end ownership: discovery, data preparation, modelling and DAX, dashboards, setting up and governing the **Power BI service** (primary #4: workspaces, apps, row-level security, scheduled refresh), then training and support. (Tab 3 portfolio 1-4; FAQ 3, 19)
  2. **Who we work with:** from a single department to multi-entity groups, across all seven emirates and in KSA, Oman, Bahrain, Kuwait and Qatar, with reach through HLB International. (FAQ 12, geography only. The sector list belongs to S7.)
  3. **How we deliver:** start with a live demo or a proof of concept, then scale in phases, with scope and success criteria agreed up front. Link the words "proof of concept" to `#methodology`. **No durations here** (they belong to FAQ 8), and **no "7 days"** (it belongs to S10).
  4. **Support after go-live:** a UAE-based team working in your time zone, with a single point of contact. The detailed support service list belongs to the S11 Support tab. (FAQ 21)

### S5. Why Power BI / Explore Power BI (`#explorepowerbi`) (380-440 words)
- **Must accomplish:** the "Why Power BI" part of the Content Writer's intent, in the template's module-table format. Each of the source's 4 "Why Power BI?" pillars becomes one row and names the real Microsoft component that delivers it. Close with a platform-layer block, the equivalent of SugarAI's "AI Layer".
- **Eyebrow:** "WHY POWER BI". **Suggested H2:** "Why Power BI: From Raw Data to Boardroom Decisions".
- **Intro** (45-60 words): Power BI is Microsoft's business intelligence platform. It works natively with Excel, Teams, SharePoint, Outlook, Azure and Dynamics 365, so Microsoft-based organisations adopt it with little friction. (FAQ 1) **Do not use the singular primary keyword in this intro.** Card 2 carries it.
- **Module table:** 4 rows. Each row has a small label ("Capability"), an H3 title, a 35-45-word description, and "Key capabilities" with exactly the 4-5 bullets given (2-6 words each):
  1. **Self-service analytics, built in Power BI Desktop** (pillar 1): business users build and explore visuals without waiting on IT; DAX measures for KPIs such as year-over-year growth, running totals and YTD revenue (FAQ 3). Bullets: Interactive visuals · DAX measures for custom KPIs · Power Query data shaping · Reusable report themes · Arabic and English layouts.
  2. **The Power BI service** (primary #3; pillar 2, 360-degree visibility): the cloud service where reports are published, shared as apps, refreshed on schedule and secured. Dashboards serve leadership and reports serve analysts (FAQ 2). [F1] Bullets: Workspaces and apps · Scheduled refresh · Row-level security · Subscriptions and sharing · Usage monitoring.
  3. **Connected to your ecosystem** (pillar 3): systems such as SAP, Oracle, NetSuite, Dynamics 365, Salesforce, SugarCRM, Excel, SharePoint, Snowflake, Google BigQuery and REST APIs, through native, certified and custom connectors, plus the on-premises data gateway for systems inside your network (FAQ 13; engagement model 3). **Do not restate "200+"** (S2 owns it). **Do not imply** every named system has a native Microsoft connector. Tally and SugarCRM, for example, need custom or partner connectors, so use the phrasing "native, certified and custom connectors cover systems such as...". Bullets: Certified connectors · Custom connector builds · On-premises data gateway · ERP and CRM integration · Excel and SharePoint sources.
  4. **Decisions on the go, and inside your own portals** (pillar 4 + FAQ 15): Power BI Mobile on iOS and Android with alerts, annotation and sharing; Power BI Embedded for branded dashboards inside web apps, investor portals or client platforms, on capacity-based licensing. Source pillar 4 says "at a fraction of traditional BI costs"; keep that idea only in qualitative form. Bullets: iOS and Android apps · Data-driven alerts · Mobile-optimised layouts · Embedded analytics · Capacity-based licensing.
- **Platform layer block** (H3, 45-60 words + 4 bullets; mirrors the "AI Layer" block): **Microsoft Fabric and a medallion data lakehouse.** Fabric unifies Power BI with data engineering, warehousing and real-time analytics (FAQ 17). When data is spread across five or more systems, HLB HAMT builds a Bronze › Silver › Gold lakehouse with Azure Data Factory pipelines as the single source of truth (FAQ 14). **Stat:** Microsoft reports **more than 40,000 paid Fabric customers, up more than 60% year on year** [S1][4]. Bullets: Fabric readiness assessment · Azure Data Factory pipelines · Bronze, Silver and Gold layers · Migration planning.

### S6. AI insights (`#aiinsights`) (150-190 words). **[REMOVED IN REVISION 2. Do not build. See Section 12.2 for what relocates.]**
- **Must accomplish:** show how AI in Power BI moves teams from "what happened" to "what should we do next" (FAQ 16), in the template's 3-point format, accurately.
- **Eyebrow:** "AI INSIGHTS". **Suggested H2:** "Ask Your Data a Question and Act on the Answer". **Do not** write "in English or Arabic" (see accuracy note below).
- **Lede** (45-60 words): Copilot and the built-in AI visuals surface drivers and outliers without anyone writing a query. **Stat:** in Q2 2026, **73.3% of the UAE's working-age population used generative AI tools, against 18.8% worldwide** [S2][5]. Frame this positively: UAE teams are already comfortable working with AI, so AI-assisted analytics is adopted quickly. Include the placeholder link **"advanced analytics services"** (P2, Section 8) for predictive models (source: Azure ML integration, FAQ 16).
- **3 points** (H3 + 15-25 words each; mirrors Predicts / Summarises / Guides):
  1. **Asks:** Copilot answers questions about a report, summarises pages and drafts DAX and report pages for authors. [F4]
  2. **Explains:** the Key influencers and Decomposition tree visuals, plus the narrative visual, show what is driving a number.
  3. **Alerts:** anomaly detection flags unusual movements; data alerts and Power Automate emails fire when a KPI crosses a threshold. Internal link **"Power BI automation with Power Automate"** → L4 (Section 8). (FAQ 5, 16)
- **Accuracy corrections to the source (mandatory):** (a) Power BI **Q&A is being retired in February 2027** (Microsoft Learn), so do not feature "Q&A" as a capability. Use Copilot. (b) Microsoft says Copilot for Power BI **officially supports English prompts only**, so do not claim Arabic-language AI queries. Arabic belongs to report design (labels, RTL layouts), not to Copilot. (c) Copilot needs **paid Fabric capacity (F2 or higher) or Premium P1 or higher**. Pro or PPU alone is not enough. This detail goes in FAQ 9, not here. [F4]

### S7. Use cases by role and sector (`#usecases`) (330-400 words)
- **Must accomplish:** the template's industries grid, sized to the real content. The source supports **6 substantive cards**: 3 decision scenarios with detailed FAQ content and the 3 C-suite buyer roles. The other sectors named in the source appear as a pill row, not as thin cards. **Do not pad to 12.**
- **Eyebrow:** "USE CASES". **Suggested H2:** "Dashboards Shaped Around the Decisions You Make".
- **Intro** (25-35 words): every engagement starts from the KPIs a role or sector actually runs on, not from a generic template.
- **6 flip cards** (front: H3 label + 6-10-word tagline; back: 35-45 words + button; mirrors the template's flip-card pattern):
  1. **Group finance and CFOs:** consolidated P&L, balance sheet and cash flow across entities in AED, USD, SAR, EUR and more; intercompany eliminations, FX conversion, IFRS segment reporting; audit-ready logic from a CA-led team. (FAQ 11) Button → `#contact`.
  2. **UAE Corporate Tax and VAT:** taxable income, deferred tax under IAS 12, VAT returns, transfer pricing, free zone versus mainland segregation. Button/link: **"UAE Corporate Tax advisory"** → L3 (Section 8). (FAQ 9)
  3. **Real estate and development:** EOIs, deal pipeline, lead conversion, unit availability, payment plans, broker performance and DLD compliance, fed by CRM and ERP data through a lakehouse. (FAQ 10) **Drop "Salesforce (60+ modules)".** It is an unverified single-client detail. Button → `#contact`.
  4. **Chief Data Officer:** governance frameworks and better data capture, accountability and compliance, a data-driven culture, a roadmap aligned with strategy, digitisation at scale. (Buyer roles, CDO list) Button → `#contact`.
  5. **Chief Marketing Officer:** a unified 360-degree customer view, omnichannel campaign performance, cohort buying behaviour, segmentation, and performance across DSPs, SSPs and ad channels. (CMO list) Button → `#contact`.
  6. **Chief Analytics Officer:** turning raw enterprise data into action, spotting untapped ("blue ocean") market opportunities, competitive intelligence and data monetisation, next-best-action frameworks. (CAO list) Button → `#contact`.
- **Pill row** (label + 10 pills, about 15 words): Real Estate · Construction · Hospitality · Trading · Financial Services · Healthcare · Retail · Logistics · Government · Education. (FAQ 12)

### S8. Our Power BI Services (`#services`) (330-390 words)
- **Must accomplish:** the numbered offerings list (01-06), mirroring "Our Sugar Offerings". All six come from Tab 3.
- **Eyebrow:** "WHAT WE DO". **H2: "Our Power BI Services"** (plural #1).
- **Intro** (30-40 words): end-to-end delivery from first workshop to ongoing support, through flexible engagement models. (Info box)
- **Items** (number + H3 + 45-55 words). At most 2 titles may contain "Power BI":
  - **01 Consulting and discovery workshops:** assess current data systems and BI readiness; design a scalable architecture aligned with strategy; licence planning. (Portfolio 1; FAQ 21 licence advisory)
  - **02 Data preparation and ETL kickstart:** prepare and integrate data, build data marts and warehousing, Azure Data Factory pipelines, a lakehouse when scale needs it. (Portfolio 2; FAQ 13-14)
  - **03 Dashboard and report development:** executive dashboards and analyst reports, optimised DAX, mobile layouts, Arabic RTL design, and performance tuning across pipeline, model and semantic layers. **Do not restate 33x.** Placeholder link **"data visualisation services"** → P1 (Section 8). (Portfolio 3; FAQ 2, 3, 6, 7)
  - **04 Connectors and system integration:** certified connector setup, custom connector builds, ERP/CRM/finance system integration, gateway configuration. (Engagement model 3; FAQ 13)
  - **05 Migration, embedded analytics and Fabric readiness:** move reporting off spreadsheets or another BI tool (naming Tableau and Qlik as migration sources is allowed; see OQ7); embed dashboards in portals with Power BI Embedded; assess Fabric readiness and plan the move. (FAQ 4, 15, 17)
  - **06 Training and continuous support:** three tracks: Executive (reading dashboards), Business User (building reports) and Developer (data modelling, advanced DAX); on-site in Dubai, remote or hybrid; Arabic-language training; contextual documentation. (Portfolio 4; FAQ 19) **The training tracks appear only here.** No FAQ repeats them.

### S9. Mid-page CTA 1 (20-30 words)
- **Suggested H2:** "See Your Own Data in Power BI Before You Commit". 1 line: a walkthrough on sample data or your own datasets, no obligation (engagement model 1). Button: "Schedule a live demo".

### S10. 5-step proof of concept (`#methodology`) (150-190 words). Highlighted band.
- **Must accomplish:** the template's highlighted fast-start section. The 5 steps map one-to-one onto the template's 5 tiles.
- **Eyebrow:** "HOW WE DELIVER". **Suggested H2:** "A Working Power BI Dashboard on Your Data in 7 Days" [CS3][6]. **This is the only section that states "7 days".**
- **Intro** (35-45 words): see the value on your own data, against agreed success criteria, before making a larger investment decision. (Engagement model 2)
- **5 steps** (number + H3 + 15-22 words each; at most one title contains "Power BI"): 1 **Requirements** (workshop: objectives, KPIs, data sources, success criteria); 2 **Data preparation** (ingest, cleanse, transform, build optimised models); 3 **Design and mockup** (wireframes approved by stakeholders before development starts); 4 **Development** (interactive reports and dashboards built to the approved design); 5 **Delivery and review** (training, feedback, one revision round, final app published). (Tab 3 methodology + docx 6.7)
- Button: "Request your proof of concept".

### S11. Engagement models + PowerUP! (`#packages`) (360-420 words)
- **Must accomplish:** the template's "How an Engagement Is Structured" tabbed matrix, with a featured PowerUP! card first. The docx says the offer "must tell the FULL story".
- **Eyebrow:** "ENGAGEMENT MODELS". **Suggested H2:** "Engagement Models That Match Where You Are Today".
- **Intro** (30-40 words): start small, scale by phase, or add expertise to your own team.
- **Featured card** (dark navy, gold badge; about 120-140 words): badge "Limited offer" (only if OQ4 confirms it is still current); H3 "Microsoft Power BI PowerUP!"; price line "**$4,500** fixed-price accelerator" (currency per OQ4); a 2-3-sentence original rewrite of the tagline and story (access your data, visualise the KPIs that matter, expert guidance, quick wins against clear objectives). **Terms**, all 5: requirements workshop; client-provided file-based data sources; up to 5 report tabs; up to 2 consumer personas; mockup approval plus 1 revision round after functional delivery. **Deliverables**, all 6: requirements workshop documentation; data transformation scripts; data model diagram; data dictionary; completed reports and dashboards; published Power BI app. Button: "Enquire about PowerUP!".
- **4 tabs** (tab tagline 8-12 words; items = H3 + 10-16 words):
  - **Explore:** Live demo (sample or own data, no obligation); Proof of concept (link to `#methodology`, **no "7 days"**).
  - **Implement:** Single-department rollout; Multi-department programme; Enterprise platform with a data lakehouse. Describe scope only. Durations belong to FAQ 8.
  - **Extend:** Connector help (certified or custom); Augmented expertise, short-term contracts or retainers (optional **"Power BI solutions expert"** #2).
  - **Support:** Performance monitoring and troubleshooting; Quarterly health checks; New dashboards as needs change; Licence advisory and Fabric migration support (optional primary #7: "administering your Power BI service"). (FAQ 21)

### S12. Why UAE businesses choose HLB HAMT (140-180 words)
- **Must accomplish:** the credential-style differentiator grid (the Content Writer's "credential strip" and "proven" intent). Non-numeric, so no stat is repeated.
- **Eyebrow:** "HLB HAMT ADVANTAGE". **H2: "Why UAE Businesses Choose HLB HAMT for Power BI Services"** (plural #2).
- **Intro** (15-25 words): any partner can install the software; HLB HAMT gets the numbers right and stays after go-live. Optionally use "Power BI consulting company" (#2).
- **6 tiles** (H3 + 10-18 words):
  1. **"Certified Power BI partner in UAE"** (conditional, see Section 2c and OQ1): consulting, implementation and support delivered locally.
  2. **Audit-ready financial logic:** UAE Corporate Tax, VAT, IFRS and PDPL expertise inside the data model. (FAQ 18) Word it as regulatory depth. S2 already carries the "finance + technology" line, so do not repeat that phrase.
  3. **Low-risk start:** a working dashboard on your own data, or the fixed-price PowerUP!, before a larger commitment. **No "7 days", no "$4,500".**
  4. **Dual intelligence:** Power BI analytics plus SugarAI CRM prediction, from one partner. Link **"SugarAI CRM"** → L2 (Section 8). This mirrors the SugarAI page's own "Dual AI intelligence" tile.
  5. **Global network:** backed by the HLB International network. **No "150+ countries"**, because that stat already appears on the SugarAI page.
  6. **In-region team:** consultants who scope, build and support from the UAE, in your time zone. (FAQ 21)

### S13. See it in action (30-45 words)
- **Suggested H2:** "Inside a Live Power BI Dashboard". 1-2 sentences on what the viewer will see: an executive dashboard in Arabic and English, drilling from group view to entity. **Needs a video asset (OQ5).** If none exists, use a static dashboard screenshot or GIF with the same copy and a "Book a live demo" button.

### S14. Mid-page CTA 2 (20-30 words)
- **Suggested H2:** "Plan Your Power BI Roadmap With Our Consultants". Body: **"a Power BI solutions expert"** (#1) scopes data sources, phasing and licences with you in a free consultation. Button: "Talk to our Power BI team".

### S15. FAQ (`#faq`) (700-850 words, 9 Q&As, single accordion like the template)
- **Eyebrow:** "COMMON QUESTIONS". **Suggested H2:** "Questions UAE Teams Ask Before Choosing a Power BI Partner".
- Answers are 65-90 words each, in the template's style: direct first sentence, then specifics. Questions are H3. **No FAQ restates 200+, 33x, 19 years, 40,000, 73.3% or 7 days.** Ask in this order:
  1. **What is the Power BI service, and how is it different from Power BI Desktop?** (primary #5; optional #6 in the answer, once). Desktop is the free Windows app for modelling and building. The cloud service is where reports are published, shared as apps, refreshed and secured. HLB HAMT sets up both. [F1]
  2. **How is Power BI licensed, and what will it cost?** Pro at US$14 and Premium Per User at US$24 per user per month (list prices since 1 April 2025, stated as "at the time of writing"); Fabric capacity for larger deployments, embedding and Copilot; HLB HAMT's licence advisory. [F2] Do **not** quote competitor BI prices (see OQ7).
  3. **Which data sources can Power BI connect to, and do we need a data warehouse first?** Named systems (as in S5 card 3, same connector caveat); direct connection is fine for smaller scopes; a lakehouse makes sense at 5+ systems. (FAQ 13, 14)
  4. **Can Power BI replace our manual Excel reports?** Automated refresh, always-current dashboards, Power Automate alerts; UAE clients have removed hours of weekly manual reporting (qualitative, no number). (FAQ 5)
  5. **Do you build Arabic and right-to-left dashboards?** Arabic labels, filters, slicers and KPI descriptions; full RTL layouts; other RTL languages such as Urdu and Persian; designed in from the start. (FAQ 7) **No Arabic Copilot claim.**
  6. **Is our data secure, and can it stay in the UAE?** Row-level security and encryption; Power BI sits within the scope of Microsoft's ISO/IEC 27001 and SOC 2 reports [F5]; UAE North and UAE Central hosting; environments configured in line with UAE PDPL, DIFC and ADGM requirements. Add one accuracy point: for tenants outside the US/EU data boundary, Copilot is off by default unless an admin allows processing outside the region. HLB HAMT sets this deliberately. [F4] Link **"data protection advisory"** → L5 (Section 8). (FAQ 8) Use "configured in line with", **not** "guarantees compliance".
  7. **What is Microsoft Fabric, and should we plan for it?** One platform for Power BI, data engineering, warehousing and real-time analytics; when it pays off; readiness assessment. Do not repeat the 40,000 figure. (FAQ 17)
  8. **What do we need to use Copilot in Power BI?** Paid Fabric capacity F2 or higher, or Premium P1 or higher (Pro or PPU alone is not enough); admin enablement; English prompts are officially supported; semantic-model preparation makes answers reliable. [F4] (New, and accurate. It closes a gap competitors leave open.)
  9. **How long does a Power BI implementation take?** Single department 2-4 weeks; multi-department 6-10 weeks; enterprise with a data lakehouse 3-6 months; a working prototype within two weeks. (FAQ 20, CS timelines)
- **Deliberately not carried over from the source FAQ** (covered elsewhere or out of date): DAX and dashboard-vs-report (S5), mobile (S1, S5), embedding (S5, S8), AI features (S6), multi-entity, tax and real estate (S7), industries/regions (S4, S7), training (S8), post-go-live support (S11), "why HLB HAMT" (S4, S12), Tableau/Qlik price comparison (dropped).

### S16. Final contact CTA + form (20-30 words)
- Keep the site's standard "Let's Connect" form component. One line of copy (optional plural #3 here): a free consultation with the Power BI team, reply within one business day (matches the site's existing promise). Form "Select your Services" default: "Technology Consulting".

### S17. Footer
Global. No new copy.

---

## 5. Competitive and reference analysis

> **R2:** These takeaways were based on the fetch tool's summaries. They have been rechecked against the full competitor page text now in `inputs/competitor-content/`, and Section 12.8 adds to or corrects them.

**Direction only. Nothing may be copied or closely paraphrased from these pages, including their headings, service names and FAQ wording.** The SugarAI page is HLB HAMT's own template, but its H2s and taglines must not be reused verbatim either.

- **All five are UK-oriented, and none speaks to the UAE buyer.** Yes Dynamic (UK & Ireland), Zenzero (London; it lists a UAE office but the copy is UK-centric), DSP (UK/North America), BCN (UK only) and Ranosys (UK regional page of a Singapore firm). None addresses Arabic/RTL reporting, in-country hosting in UAE North/Central, UAE Corporate Tax/VAT dashboards or PDPL. **Gap to own:** a UAE-native, finance-literate Power BI partner.
- **Fast-start offers exist, but nobody publishes a price.** BCN's page is the closest structurally (about 3,500 words: kickstarter offer, demo, approach, case studies, FAQs). Its accelerated offer caps dashboards and hides the price. Yes Dynamic and Ranosys offer only "free consultation". **Angle:** present HLB HAMT's fixed $4,500 PowerUP! with every term and deliverable, plus a structured 5-step PoC. Transparency is the differentiator.
- **Proof is thin across the set.** Yes Dynamic, DSP and Ranosys have no quantified outcomes. Proof there leans on client logos and partner badges, some using the retired "Gold Partner" label. **Angle:** specific, footnoted proof (S2, S5, S6), precise partner wording once OQ1 confirms the designation, and no outdated partner terminology.
- **Coverage gaps worth filling:** Yes Dynamic covers licensing, but no one gives current list prices or explains Copilot's capacity requirement and English-only prompt support. Ranosys lists product components (Desktop, Mobile, Gateway) with no business framing. **Angle:** S5 pairs each component with the business outcome, and FAQs 2 and 8 answer the licensing and Copilot questions precisely.
- **Positioning to take:** "The platform is Microsoft's. Getting the numbers right is ours." Auditor-grade financial logic plus in-house engineering, in Arabic and English, hosted in-country.

---

## 6. Stats and data points

> **R2:** All stats were re-verified on 2026-09-29 against the new sibling and competitor pages (Section 12.7). Changes: S2 (73.3%) is **retired**, because its only slot (AI Insights) is removed. CS2 (33x) now cites a live HLB HAMT page. CS3 (7 days) gains a "defined use case" qualifier. A new HLB HAMT fact, CS5 "Since 1999", is added. Everything else is unchanged.

Every stat below appears **once** on the page, in the section named. Footnote markers `[n]` go after the stat's description. Deliver renders a small sources note, and for [3] it also adds Gartner's disclaimer.

### 6a. Content-source stats (self-published by HLB HAMT in its prepared draft; **not independently verified by me**)

| # | Figure | Where | Origin and status |
|---|---|---|---|
| CS1 [1] | **200+** data connectors | S2 item 1 | From the draft hero stats (HTML line 140; docx Section 3). **Consistency check (mine):** Microsoft Learn's "Data sources in Power BI Desktop" (updated 18 Sep 2026) lists roughly 210-220 connectors by my manual count, including Beta/Preview ones. "200+" is therefore consistent, but it describes **Power BI's** library, not connectors HLB HAMT built. Word it that way. Footnote URL: https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-sources |
| CS2 [2] | **33x** faster report load times | S2 item 2 | From the draft hero stats and hero card. The docx (Tab 1 section) gives the context: "in a recent engagement... a 33x improvement in report load times and interactivity" from optimising pipeline, data model and semantic layers. **A single-client result with no client name or date.** It must carry "in one recent engagement" wording. It needs Content Writer sign-off (OQ4). Footnote: "HLB HAMT client engagement (internal), per HLB HAMT's prepared content." No URL exists. |
| CS3 [6] | **7 days** to a proof of concept | S10 H2 only | From the draft hero stats, engagement model 2 and the methodology subtitle. A service commitment, not a market stat. Footnote: "HLB HAMT service commitment." |
| CS4 | "14+ Yrs Gartner #1" | **Not used as written** | **Inaccurate:** Gartner does not rank vendors "#1", and the count is out of date. Replaced by S-3 below. The source FAQ repeats it ("Ranked #1 by Gartner for 14+ consecutive years"), and that wording must not appear anywhere on the page. |
| (facts) | $4,500 PowerUP! price, terms and deliverables; timelines (2-4 wks / 6-10 wks / 3-6 months / prototype in 2 wks) | S11, FAQ 9 | HLB HAMT commercial facts from the draft. Confirm currency and current validity (OQ4). |

### 6b. Independently sourced by me (credible, recent)

| # | Figure | Context (one line) | Source URL | Age | Where |
|---|---|---|---|---|---|
| S-3 [3] | Microsoft named a **Leader** in the **2026** Gartner Magic Quadrant for Analytics and BI Platforms, **19th consecutive year** | Platform credibility for Power BI/Fabric; Microsoft's recognition, not HLB HAMT's | Microsoft announcement (Power BI Updates Blog): https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Microsoft-named-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for/ba-p/5262403 (returned 403 to my fetch; confirmed through search and the verbatim repost at https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/). For the prior year: 2025 was the 18th consecutive year (https://powerbi.microsoft.com/en-us/blog/microsoft-named-a-leader-in-the-2025-gartner-magic-quadrant-for-analytics-and-bi-platforms/) | MQ published late June 2026, about 3 months old | S2b only |
| S1 [4] | **More than 40,000 paid Fabric customers, up more than 60% year on year** | Momentum behind Fabric, which Power BI now sits inside | Microsoft FY26 Q4 earnings call, 29 July 2026: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4 | 2 months | S5 platform layer only |
| S2 [5] | **73.3%** of the UAE's working-age population used generative AI tools in Q2 2026, vs **18.8%** worldwide | The UAE leads global AI adoption, so AI-assisted analytics lands with teams already using AI | Microsoft On the Issues (Microsoft AI Economy Institute), 21 Sep 2026: https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/ | 1 week (Q2 2026 data) | S6 lede only. Word it as generative AI use in general, **not** BI use. |

**Gartner disclaimer for the sources note (Deliver):** "Gartner does not endorse any vendor, product or service depicted in its research publications. GARTNER and MAGIC QUADRANT are registered trademarks of Gartner, Inc. and/or its affiliates."

### 6c. Verified facts (not stats) to footnote if stated

| # | Fact | Source | Where |
|---|---|---|---|
| F1 | The Power BI service is Microsoft's cloud SaaS for publishing, sharing, collaborating and building apps; Power BI Desktop is the free Windows authoring app | https://learn.microsoft.com/en-us/power-bi/fundamentals/service-service-vs-desktop | S5 card 2, FAQ 1 |
| F2 | Power BI Pro is US$14 and PPU is US$24 per user per month from 1 April 2025 (up from $10/$20) | https://powerbi.microsoft.com/en-us/blog/important-update-to-microsoft-power-bi-pricing/ ; https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing | FAQ 2 |
| F3 | UAE North supports Power BI and all Fabric workloads; UAE Central is a Power BI-only region (Microsoft Learn, updated 22 Sep 2026) | https://learn.microsoft.com/en-us/fabric/admin/region-availability | S1 deployment line, FAQ 6 |
| F4 | Copilot for Power BI: needs paid Fabric F2+ or Premium P1+ (Pro/PPU alone insufficient); non-English prompts not officially supported; off by default outside the US/EU data boundary unless the admin allows cross-geo processing (updated 24 Aug 2026). Power BI Q&A retires February 2027 | https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction ; https://learn.microsoft.com/en-us/power-bi/natural-language/q-and-a-limitations | S6, FAQ 6, FAQ 8 |
| F5 | The Power BI cloud service is in scope for Microsoft's ISO/IEC 27001 certification and SOC 2 reports | https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001 ; https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2 | FAQ 6 |

### 6d. Where I found no strong stat, or chose not to use one
- **S4, S7, S8, S11, S12, S15:** no stat planned. These sections run on HLB HAMT capability and source facts. I found no UAE-specific BI adoption figure from a credible research firm. The market-sizing hits (Mordor Intelligence global BI market, UAE ICT/cloud markets) are too indirect, so none is used.
- **Reserve (not planned):** Forrester TEI of Microsoft Fabric, **379% ROI over three years** (composite organisation, commissioned by Microsoft, published 3 June 2024, about 2 years 4 months old): https://www.microsoft.com/en-us/microsoft-fabric/blog/2024/06/03/forrester-total-economic-impact-study-microsoft-fabric-delivers-379-roi-over-three-years/ . This is only a swap-in if the Content Writer rejects S1.
- **Not used:** "97% of the Fortune 500 use Power BI". It is widely repeated, but I could not find a current official Microsoft source.

---

## 7. Draft meta title and meta description

- **Meta title (59 characters):** `Power BI Service & Consulting Partner in the UAE | HLB HAMT`
- **Alternate, only if OQ1 confirms certification (52 characters):** `Power BI Service | Certified Power BI Partner in UAE`
- **Meta description (159 characters):** `Power BI service from HLB HAMT: consulting, data preparation, Arabic-ready dashboards, training and a 7-day proof of concept for businesses in the UAE and GCC.`

Both lead with the primary keyword, and neither contains an em dash.

---

## 8. Internal linking suggestions

> **R2:** Several links change. L4 moves from the removed S6 to the FAQ. P1 is no longer a placeholder, because the data visualisation page is live at `/services/data-visualization-uae/`. P2 moves to the Chief Analytics Officer card. A new link, L6, points to the live Power BI dashboard development page. See Section 12.9.

**Core links (live URLs taken from the template's own nav, or found through search; Deliver should click through each before publishing):**

| # | Anchor text | Target | Placement |
|---|---|---|---|
| L1 | digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ (the nav's "Digital Transformation & Analytics" parent) | S4 lede |
| L2 | SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ (the uploaded live page; canonical URL per OQ6) | S12 tile 4 ("Dual intelligence") |
| L3 | UAE Corporate Tax advisory | https://hlbhamt.com/services/corporate-tax-advisory-services-in-uae/ | S7 card 2 |
| L4 | Power BI automation with Power Automate | https://hlbhamt.com/insights/unlocking-power-bi-automation-with-power-automate/ (existing HLB HAMT insight) | S6 point 3 ("Alerts") |
| L5 | data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ (nav: "IT Governance & Data Protection Advisory") | FAQ 6 answer |

**Reverse link (SugarAI page → this page):** on the SugarAI homepage's "Dual AI intelligence" tile ("SugarAI prediction plus Power BI analytics, from one partner"), link **"Power BI analytics"** to this page's final URL. Optionally, also link "dashboards" in the SugarAI Packages › Integration tab item "Data & Analytics Integrations". These are edits to a live page, so they go in the Deliver handoff notes.

**Future sibling pages (placeholders; these pages do not exist yet):**

| # | Anchor text | Placeholder target | Placement |
|---|---|---|---|
| P1 | data visualisation services | `/services/data-visualisation-services/` **[PLACEHOLDER LINK, sibling page not yet built]** | S8 item 03 |
| P2 | advanced analytics services | `/services/advanced-analytics-services/` **[PLACEHOLDER LINK, sibling page not yet built]** | S6 lede |

Build writes these as `[data visualisation services](PLACEHOLDER:/services/data-visualisation-services/)` so Test and Deliver can find them. The Content Writer confirms the final slugs when those pages are built.

**Breadcrumb links** (structural, in addition to the above): Technology Consulting Services → https://hlbhamt.com/services/technology-consulting-services-dubai-uae/ ; Digital Transformation & Analytics → L1.

---

## 9. Open questions / missing inputs

1. **Is HLB HAMT's "certified" Power BI partner status real, and what is the exact designation?** The secondary keyword "Certified Power BI Partner in UAE" asserts a certification. The prepared content only says "Power BI implementation partner" and "Microsoft Power BI Partner". Microsoft issues program designations (e.g. "Solutions Partner for Data & AI (Azure)"), not a Power BI-specific certification. An existing HLB HAMT page (`/services/power-bi-partner-in-dubai-uae/`) already uses "certified Microsoft Power BI Partner" according to search snippets, but I could not open hlbhamt.com to check the basis. **Please confirm the designation name, or which consultant certifications (e.g. Microsoft Certified: Power BI Data Analyst Associate) the claim rests on.** **Default if unconfirmed:** S12 tile 1 reads "Microsoft Power BI partner in the UAE", the keyword is recorded as not placed, and the alternate meta title is not used.
2. **"Parent webpage" = Microsoft's Power BI product page?** The requirement lists https://www.microsoft.com/en-in/power-platform/products/power-bi as the parent. That is Microsoft's own product page, not an HLB HAMT page. It reads as vendor background rather than a site-hierarchy parent. The live nav chain is Home › Services › Technology Consulting Services › Digital Transformation & Analytics › Data Analytics & Business Intelligence (Power BI). **Which did you intend?** **Default:** the breadcrumb and parent link use the HLB HAMT nav chain. Microsoft's page is treated as background, and at most it becomes one outbound reference link (not planned by default).
3. **Final URL and overlap with existing HLB HAMT Power BI pages.** The live nav item "Data Analytics & Business Intelligence (Power BI)" already points to `/services/microsoft-power-bi-consulting-in-dubai-uae/` (also the docx's suggested URL). Search shows at least four more live, overlapping pages: `/services/power-bi-partner-in-dubai-uae/`, `/services/data-analytics-business-intelligence/`, `/services/business-intelligence-consulting-service-uae/` and `/services/data-analytics-consulting-uae/`. A new standalone page targeting "Power BI service" will compete with these for the same queries. **Does this page replace the nav target (recommended: publish at `/services/microsoft-power-bi-consulting-in-dubai-uae/` to keep its link equity), and which overlapping pages should be 301-redirected or canonicalised to it?** This does not block Build. It does block Deliver and go-live.
4. **Please confirm the self-published claims:** (a) the **33x** result can be published (client consent, and the "one recent engagement" wording is acceptable); (b) **PowerUP!** is still offered at **$4,500**, in USD (or should it be AED?), and the "Limited offer" badge is still valid; (c) the implementation timelines in FAQ 9 are still accurate. **Default:** publish as planned with the qualifiers above.
5. **Video for S13.** The template has a 60-second overview video. Is there a Power BI demo video? **Default:** a static dashboard screenshot or GIF with the same copy and a "Book a live demo" button.
6. **Which SugarAI URL is canonical?** The uploaded page lives at `/sugarai-crm-2/`. The site's mega-menu links `/sugarai-crm/`, and the dropdown links `/sugar-crm-dubai`. **Default:** link to `/sugarai-crm-2/` (the confirmed live page) until you confirm.
7. **Approve these corrections to the prepared content** (Build applies them unless you object): "14+ Yrs Gartner #1" becomes "Leader, 19th consecutive year (2026)"; no "Q&A in Arabic" or Arabic Copilot claims; mobile is iOS and Android only (the Windows app is retired); Q&A is not featured (it retires February 2027); the Power BI vs Tableau price comparison is dropped, while Tableau and Qlik stay named only as migration sources in S8 item 05; the unverified "Salesforce (60+ modules)" detail is dropped.

---

## 10. Content Writer decisions (2026-09-28) — all 7 open questions approved to their stated defaults

1. **Certification claim:** unconfirmed. Build uses the default: S12 tile 1 reads "Microsoft Power BI partner in the UAE" (not "certified"). The keyword "Certified Power BI Partner in UAE" is recorded as not placed. The alternate meta title (which used "Certified") is not used; only the primary meta title from Section 7 is used.
2. **Parent/breadcrumb:** default confirmed. The breadcrumb and parent link use the live HLB HAMT nav chain (Home › Services › Technology Consulting Services › Digital Transformation & Analytics › Data Analytics & Business Intelligence (Power BI)). Microsoft's Power BI product page is background only, not linked by default.
3. **Final URL / page overlap:** not resolved now (business/IT decision outside this pipeline run, needs the Content Writer to coordinate redirects). Build and Deliver proceed without a final URL; the page is built section-complete and ready to slot into whichever URL is decided later. This remains open before go-live.
4. **Self-published claims (33x, PowerUP! $4,500, FAQ 9 timelines):** default confirmed. Publish as planned, with the "one recent engagement" qualifier on 33x and the offer treated as currently valid in USD.
5. **Video for S13:** no video supplied. Default confirmed: static dashboard screenshot/GIF placeholder with a "Book a live demo" button, copy written so it doesn't depend on a specific asset.
6. **Canonical SugarAI URL:** default confirmed. Link to `/sugarai-crm-2/` (the confirmed live uploaded page).
7. **Corrections to prepared content:** all approved. Build applies every correction listed (Gartner wording, no Arabic Copilot claim, iOS/Android only, Q&A dropped, Tableau/Qlik price comparison dropped but named as migration sources, "Salesforce (60+ modules)" dropped).

---

## 12. Revision 2 (2026-09-29): new sourcing, AI Insights removed, HLB HAMT-led branding

(There is no Section 11. Section 12 is the number the pipeline assigned to this revision.)

**Authoritative spec:** `inputs/revision-2-notes.md`. The Content Writer judged v1 (draft-v4) under-sourced and too Microsoft-led. This is a **content-quality revision, not a structural rebuild**. The SugarAI template mapping, keyword plan, word count range and Section 10 decisions all stand, except where this section explicitly changes them.

### 12.0 Inputs read for this revision

| Input | Lines that matter (the rest is shared nav/footer chrome) | Role |
|---|---|---|
| `inputs/revision-2-notes.md` | all | Spec |
| `inputs/hlbhamt-sibling-pages/power-bi-partner-in-dubai-uae-extracted.txt` (live: `/services/power-bi-partner-in-dubai-uae/`) | 356-796 | Secondary. **This is essentially Bala's Tab 3, already published live**: the same pillars, portfolio, CxO lists, engagement models, PowerUP!, 5 PoC steps and 21-question FAQ. It confirms that the primary source is live, public HLB HAMT copy, and it contains the same outdated claims the brief already corrects. |
| `.../microsoft-power-bi-consulting-in-dubai-uae-extracted.txt` (live: `/services/microsoft-power-bi-consulting-in-dubai-uae/`, the nav target) | 356-503 only | Secondary. Five consulting services (Strategy and Planning; Implementation; Data Integration and Automation; Custom Dashboards and Reporting; Training and Support) and four reasons to choose HLB HAMT (industry expertise, tailored solutions, track record through HLB International, end-to-end service). **Lines 507-585 are WordPress theme demo content** (testimonials credited to "Execor", "Kate Smith, Swirl" and "Carlos Martines, MEX"; stats 90%, 1.6x and 60%). They are not HLB HAMT results. **Never use them.** See 12.12. |
| `.../data-visualization-uae-extracted.txt` (live: `/services/data-visualization-uae/`) | 356-667 | Secondary. This is Bala's Tab 1, now live. Power BI-relevant items: dashboard optimisation "across pipeline, data model, and semantic layers" with **the 33x result stated publicly** ("In a recent engagement, we achieved a 33x improvement in report load times and interactivity"); **Tableau to Power BI migration** as a named service (preserve business logic, redesign visuals, operational continuity); "Proud Microsoft Partner in the Business Intelligence Space"; a 9-item industry list; FAQ timelines identical to Tab 3. |
| `.../power-bi-dashboard-development-extracted.txt` (live: `/services/power-bi-dashboard-development/`) | 356-795 | Secondary. The most technically specific HLB HAMT copy available. It adds six dashboard services (KPI-centric semantic modelling with DAX and reusable layers; drill-through, cross-filtering, slicers and bookmarks; ETL/ELT integration; scheduled and incremental refresh with near-real-time where needed; performance tuning through query reduction, aggregation tables and efficient DAX; security and governance through RLS, workspace governance and access controls). It also adds a 5-step dashboard delivery approach, the positioning line "model-first, not visual-first", a slow-dashboard FAQ ("performance depends more on implementation quality than the tool itself"), cost components and a PoC qualifier ("as little as 7 days for defined use cases"). Eyebrow reads "Microsoft Certified" (see 12.11, R2-2). |
| `inputs/competitor-content/{zenzero,ranosys,dsp,bcn}.txt` | zenzero 843-1207; ranosys 224-422; dsp 305-492; bcn 200-755 | Tertiary. For gaps and positioning only (12.8). Yes Dynamic was not fetched (bot check), so the Section 5 note on it stands as is. |
| `brief.md` Sections 1-10, `draft/draft-v4.md` | all | Baseline and branding audit (12.3c) |

The primary source, `inputs/extracted/hlb-data-viz-v4 (1).html.md` (Bala's Tab 3), **stays the spine**. The sibling pages add detail and HLB HAMT-owned proof. The competitor pages only show gaps.

**How much sibling copy may be reused (duplicate-content guard):** the revision notes allow sibling-page detail, credentials and positioning language to be "drawn from directly". Build may reuse, word for word, **facts, figures, service names, technical terms and short HLB HAMT positioning phrases of 8 words or fewer** (e.g. "model-first, not visual-first", "Finance + Technology under one roof", "self-service BI ecosystems"). Build must **not paste whole sentences or paragraphs** from the sibling pages. They are live on hlbhamt.com, and pasted copy creates same-domain duplicate content that competes with this page for "Power BI service" queries. That competition is already Open Question 3. This limit lifts if the Content Writer confirms the source sibling page will be 301-redirected to this page (R2-1).

### 12.1 What the new sourcing added, corrected or strengthened

| # | Finding | Source | Effect on the brief |
|---|---|---|---|
| N1 | 33x is published on a live HLB HAMT page with the same "in a recent engagement" qualifier and the same pipeline/model/semantic-layer context | data-visualization-uae | CS2 footnote upgraded from "internal" to the live URL (12.7). Wording and single-slot rule unchanged. |
| N2 | The 7-day PoC appears on 3 sibling pages. The dashboard page qualifies it as "for defined use cases" | all 3 Power BI siblings | Add the qualifier to the S9 (was S10) intro. Footnote cites the live partner page. |
| N3 | Implementation timelines (2-4 weeks / 6-10 weeks / 3-6 months / prototype in 2 weeks) are identical on the partner page and the data-viz page | partner, data-viz | Confirmed. FAQ timeline answer unchanged; footnote may cite the live partner page. |
| N4 | Tableau to Power BI migration is a named, live HLB HAMT service, and Qlik migration is also offered | data-viz | Migration moves from a passing mention to a substantive part of S7 item 05. It is still named only as a migration source, with no price comparison. |
| N5 | HLB HAMT has its own technical service detail (semantic modelling, drill-through, bookmarks, incremental refresh, aggregation tables, RLS, workspace governance) | dashboard-development | S7 Services restructured to carry this detail (12.5). A new FAQ on slow dashboards is added. |
| N6 | HLB HAMT's own 5-step **full-implementation** approach (Context and KPI definition → Data modelling → Report architecture and UX → Validation and performance tuning → Deployment and adoption) | dashboard-development | Summarised in S4 card 3 "How we deliver". It is distinct from the 5 PoC steps in S9 and must not duplicate them. |
| N7 | **HLB HAMT established in the UAE in 1999** (as HAMT & Associates) and joined HLB International in 2007 | HLB HAMT press release (12.7, CS5) | New HLB HAMT-owned credential for the S2 strip, replacing the unnumbered "Finance + technology" item. The finance-plus-technology message moves into that item's description. |
| N8 | Security and governance (RLS, workspace governance, access controls) is a named HLB HAMT service | dashboard-development | Becomes part of the new S7 item 04. S10 Support tab gains an access-review item. |
| N9 | Consulting-page positioning: strategy and planning around business goals, data needs and reporting expectations; end-to-end service; track record through HLB International | consulting | Feeds S7 item 01, S4 and S11. |
| N10 | Cost framing: the total cost is licensing **plus** implementation/dashboard development **plus** data integration and modelling, and depends on scope | dashboard-development | FAQ 2 (licensing) now covers the full cost picture, not only Microsoft list prices. |
| N11 | The data visualisation page is **live**, and a dedicated Power BI dashboard development page exists | sibling URLs | P1 is no longer a placeholder, and new link L6 is added (12.9). |
| C1 | Sibling pages still say "14+ Yrs Gartner #1" / "Ranked #1 by Gartner for 14+ consecutive years", "~$15/user/month", "Q&A (ask in English or Arabic)", mobile on "Windows", "Salesforce (60+ modules)" and "ISO 27001/SOC 2 compliant" | partner, data-viz | **No change to the brief.** The Section 10 #7 corrections still apply, and Build must not reintroduce any of these from the sibling pages. The live pages need fixing too (12.12). |

### 12.2 Content change 1: AI Insights removed

**Removed entirely:** original S6 (`#aiinsights`): the eyebrow, H2 "Ask Your Data a Question and Act on the Answer", the lede, the Answers/Explains/Alerts points and the anchor-nav item "AI Insights". **Do not rebuild it as a smaller block elsewhere.** No section may present Key influencers, the Decomposition tree, the narrative visual or anomaly detection as a feature list.

**What happens to its parts:**

| Item that lived in S6 | Revision 2 decision |
|---|---|
| Stat S2 [5]: 73.3% UAE generative-AI use vs 18.8% worldwide | **Retired, with a reason.** Its only slot is gone. It measures general generative-AI use, not BI, so no remaining section can carry it honestly. Moving it into the Copilot FAQ would bring back the AI-promotion angle the Content Writer removed and push that answer past 90 words. The source stays valid, so the stat is **kept on reserve**, not deleted. |
| L4 "Power BI automation with Power Automate" | **Moves to FAQ "Excel reports" (new S14 Q4)**, on the sentence about Power Automate alerts. Anchor and target unchanged. |
| P2 "advanced analytics services" placeholder | **Moves to S6 Use cases card 6 (Chief Analytics Officer), back text**, on forecasting and next-best-action models. |
| F4 Copilot facts | Still used in FAQ 6 (cross-geo default) and FAQ 8 (capacity, admin enablement, English prompts). The Q&A-retirement and no-Arabic-Copilot corrections still apply. |
| Copilot as a topic | Appears **only** in FAQ 6 and FAQ 8. It is not added to the hero, strip, S5 or S7. |

**Renumbering (old → new).** Build and Test use the new numbers from here on:

| Old | New | Section |
|---|---|---|
| S0-S5 | S0-S5 | Breadcrumb, Hero, Strip + S2b, Anchor nav, Why HLB HAMT, The Platform (was "Why Power BI") |
| S6 | removed | AI Insights |
| S7 | **S6** | Use cases by role and sector (`#usecases`) |
| S8 | **S7** | Services (`#services`) |
| S9 | **S8** | Mid-page CTA 1 |
| S10 | **S9** | 5-step proof of concept (`#methodology`) |
| S11 | **S10** | Engagement models + PowerUP! (`#packages`) |
| S12 | **S11** | Why UAE businesses choose HLB HAMT |
| S13 | **S12** | See it in action |
| S14 | **S13** | Mid-page CTA 2 |
| S15 | **S14** | FAQ (`#faq`) |
| S16 | **S15** | Final contact CTA + form (`#contact`) |
| S17 | **S16** | Footer |

**New anchor nav (S3), in DOM order:** Why HLB HAMT · The Platform · Use Cases · Services · Proof of Concept · Engagement Models · FAQ. Anchor IDs are unchanged (`#explorepowerbi` is kept for S5 so no links break).

### 12.3 Content change 2: HLB HAMT-led branding

**Principle:** HLB HAMT is the provider and the actor. Power BI (and Fabric) is the technology HLB HAMT delivers on. The page must read as "HLB HAMT designs, builds, runs and supports Power BI for you". It must not read as a Microsoft product page with HLB HAMT attached. Microsoft facts stay (Gartner recognition, connector library, UAE regions, licence prices, Copilot requirements, ISO/SOC scope), correctly attributed, and they appear as **evidence inside HLB HAMT's story**, not as the lead.

#### 12.3a Rules Build must follow (Test checks B1-B7)

- **B1. H1 names HLB HAMT.** New H1: **"HLB HAMT: Your Power BI Service Partner for Smarter Decisions in the UAE"**. The primary keyword and the compound-noun exception still apply (Section 2b), and "UAE" appears once as before. Build may adjust the words around the keyword, but "HLB HAMT" must open the H1.
- **B2. Openings are HLB HAMT-led.** The **first sentence** of the hero lede and of every section intro or lede in S4, S5, S6, S7, S9, S10 and S11 must have HLB HAMT, "we", "our team" or "our [consultants/engineers/accountants]" as its grammatical subject. Microsoft, Power BI, Fabric, Copilot, "the platform" or "data" must **not** be the subject of those opening sentences.
- **B3. Every FAQ answer includes at least one sentence with HLB HAMT or "we" as the subject.** Factual definitions (FAQ 1 on Desktop vs the service, FAQ 7 on Fabric) may open with the product as subject, but must then say what HLB HAMT does.
- **B4. "HLB HAMT" on-page count: 10-16.** Count it using the Section 2a rules: headings, body, cards and FAQ count; eyebrows, buttons, nav, meta, alt text and schema do not. Below 10 fails. Above 16 is flagged as brand stuffing.
- **B5. "Microsoft" on-page cap: 12 or fewer.** Product names such as "Microsoft Fabric" count. Footnotes, button labels and schema do not. After the first mention in a section, write "Fabric", not "Microsoft Fabric".
- **B6. Retired Microsoft-led framings. None of these may appear:** the eyebrow "Microsoft Power BI"; the H2 "Why Power BI: From Raw Data to Boardroom Decisions"; the sentence opener "Power BI is Microsoft's business intelligence platform"; "Microsoft supplies a capable platform"; the offer title "Microsoft Power BI PowerUP!" (see 12.5 S10 and R2-3); a bare "Microsoft: named a Leader..." recognition line with no HLB HAMT lead-in.
- **B7. Attribution stays honest.** HLB HAMT must never appear to own a Microsoft achievement or feature. The Gartner recognition is Microsoft's. "200+" is Power BI's connector library, not connectors HLB HAMT built. The UAE regions are Microsoft's data centres. "Microsoft Power BI partner in the UAE" stays uncertified (Section 10 #1).

#### 12.3b Voice

- **Verbs belong to HLB HAMT:** we design, model, build, connect, secure, tune, migrate, embed, train, support. Power BI is the object or the instrument: "we build your reports in Power BI Desktop", not "Power BI Desktop lets users...".
- **HLB HAMT-owned proof:** 33x (HLB HAMT's engagement), since 1999 (HLB HAMT's history), finance plus technology under one roof, Arabic/RTL designed from the first mockup, in-region team, fixed-price PowerUP!, the 7-day PoC.
- **Possessives:** "HLB HAMT's Power BI Services", "our Power BI team", "your Power BI service, run by HLB HAMT".
- **What stays the same:** British spelling, zero em dashes, no competitor names, a positive (not pain-led) opening, footnote markers.

#### 12.3c Audit of the delivered v1 (draft-v4): Microsoft-led instances and required fixes

| v4 location | Problem | Required fix (new section numbers) |
|---|---|---|
| S1 eyebrow "Microsoft Power BI" | Microsoft brand leads | Eyebrow becomes **"HLB HAMT POWER BI SERVICES"** (not counted). |
| S1 H1 | HLB HAMT absent | B1 H1. |
| S1 deployment line "Data can stay in-country in Microsoft's..." | Data/Microsoft is the subject | "We set up your environment so data can stay in-country, in Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud region..." Keep the F3 fact that UAE North has full Fabric and UAE Central has Power BI only. |
| S2 item 1 "Data connectors in Power BI..." | Platform stat with no HLB HAMT role | 12.5 S2 item 1 wording. |
| S2b "Microsoft: named a Leader..." | Microsoft recognition standing alone | HLB HAMT lead-in (12.5 S2b). |
| S4 lede "Microsoft supplies a capable platform." | Microsoft is the subject of the first sentence | Open with HLB HAMT (12.5 S4). |
| S5 eyebrow "WHY POWER BI", H2 "Why Power BI...", intro "Power BI is Microsoft's...", every row opener ("Business users build", "It is the cloud side", "Native, certified and custom connectors cover", "Power BI Mobile puts", "Fabric brings Power BI together") | The whole section reads as a product page | Reframe as "The Platform We Deliver" (12.5 S5). Every row description opens with an HLB HAMT action, then names the component and the client benefit. |
| S6 AI Insights | Microsoft AI features as the lead | Removed (12.2). |
| S10 (old S11) featured H3 "Microsoft Power BI PowerUP!" | Microsoft brand on HLB HAMT's own offer | 12.5 S10. |
| S12 (old S13) H2 "Inside a Live Power BI Dashboard" | Product-led | "Inside an HLB HAMT Power BI Dashboard" or similar. |
| FAQ Q3 "Which data sources can Power BI connect to...", Q4 "Can Power BI replace...", A2 opening "At the time of writing, Microsoft lists...", A7 opening | Product as the actor | Reworded questions and HLB HAMT-first answers (12.5 S14). |

### 12.4 Revised skeleton and budgets (replaces the Section 3b table for Build)

The word count stays **3,100-3,500, target about 3,300**. Test fails the page below 2,900 or above 3,750, and the count rule is unchanged. The ~150-190 words freed by removing AI Insights are reallocated to the sibling-sourced detail in S4, S6, S7, S11 and the FAQ. **Do not pad back to 3,300.** If the page lands at 3,150 with all required content, that passes.

| # | Section (anchor) | Heading level | Budget (words) | Change vs original |
|---|---|---|---|---|
| S0 | Breadcrumb | none | excluded | unchanged |
| S1 | Hero + "one version of the numbers" sub-block + deployment line | H1 + H3 cards | 150-190 | H1, eyebrow and deployment line reframed |
| S2 | Dark stats strip (4) + S2b recognition bar | none | 45-70 | item 1 reworded; item 3 becomes "Since 1999"; S2b lead-in |
| S3 | Sticky anchor nav | none | excluded | 7 items |
| S4 | Why HLB HAMT (`#whyhlbhamt`) | H2 + 4 x H3 | 260-310 | HLB HAMT-first lede; card 3 uses N6 |
| S5 | The Platform We Deliver (`#explorepowerbi`) | H2 + 4 x H3 + platform-layer H3 | 380-440 | reframed throughout |
| S6 | Use cases by role and sector (`#usecases`) | H2 + 6 x H3 + pill row | 340-410 | L7 and P2 links; 2 pills added |
| S7 | HLB HAMT's Power BI Services (`#services`) | H2 + 6 x H3 | 380-440 | restructured items with N5/N8/N9/N4 |
| S8 | Mid-page CTA 1 | H2 | 20-30 | unchanged |
| S9 | 5-step proof of concept (`#methodology`) | H2 + 5 x H3 | 150-190 | "defined use case" qualifier |
| S10 | Engagement models + PowerUP! (`#packages`) | H2 + featured H3 + 4 tabs | 360-420 | offer title; Support tab items |
| S11 | Why UAE businesses choose HLB HAMT | H2 + 6 x H3 | 150-190 | tile 5 update |
| S12 | See it in action | H2 | 30-45 | H2 reframed |
| S13 | Mid-page CTA 2 | H2 | 20-30 | unchanged |
| S14 | FAQ (`#faq`) | H2 + **10** x H3 | 780-920 | +1 Q (slow dashboards); reworded Qs; L4 moved here |
| S15 | Final contact CTA + form | H2 | 20-30 | unchanged |
| S16 | Footer | none | no new copy | unchanged |

Minimum total ≈ 3,085; maximum ≈ 3,715. The target of about 3,300 sits comfortably inside that span.

### 12.5 Revised section-by-section changes (apply on top of Section 4; new numbering)

Anything not mentioned for a section stays exactly as Section 4 specifies: sources, keyword slots, stat slots, "do not restate" rules and accuracy corrections.

**S1 Hero.** Eyebrow "HLB HAMT POWER BI SERVICES". H1 per B1. Lede sentence 1 keeps HLB HAMT as subject and primary keyword #2 ("HLB HAMT designs, builds and runs your Power BI service..."). Sentence 2 may draw on the partner page's positioning ("local expertise, industry knowledge") in original wording. The sub-block and 3 cards are unchanged. Deployment line per 12.3c. Buttons unchanged.

**S2 Strip + S2b.**
1. **200+** [1]: the description must attribute the 200+ to Power BI's connector library and give HLB HAMT the action, e.g. "Power BI connectors to draw on; our engineers configure them and build custom ones where none exist." (8-16 words). It must **not** say or imply HLB HAMT built 200+ connectors.
2. **33x** [2]: unchanged wording ("...in one recent HLB HAMT engagement"). The footnote now cites the live data-viz page (12.7).
3. **Since 1999** [12] (new, replaces "Finance + technology"): "A licensed UAE audit, tax and advisory firm that also builds your data platform." This keeps the finance-plus-technology message. Do **not** write "25 years": that figure was 2024's and is now out of date, while "Since 1999" does not age. Do **not** add staff, client or office counts (they date from January 2024).
4. **Arabic and English**: unchanged.
- **S2b** (still Microsoft's recognition, now with an HLB HAMT lead-in, 25-35 words): e.g. "We build on Microsoft Power BI and Fabric. Microsoft has been named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." [3] Button "Read Microsoft's announcement" unchanged. The Gartner disclaimer rule is unchanged. No "#1", "ranked" or "14+".

**S4 Why HLB HAMT.** H2 may stay ("Great Dashboards Start With the Numbers Behind Them"). **The lede opens with HLB HAMT as subject**, e.g. HLB HAMT is a Power BI consulting company (keyword #1) and a licensed audit, tax and advisory firm, a member of HLB International. The platform point comes second and is framed as "Power BI gives us the platform; our accountants and engineers make the numbers reconcile." L1 is unchanged. Cards:
- Card 1 "What we do": unchanged scope, including primary keyword #4. Keep it short because S7 now carries the detail.
- Card 3 "How we deliver" (45-55 words): start with a demo or [proof of concept](#methodology), then run full implementations through HLB HAMT's five stages (define KPIs and metric logic → model the data → design the report architecture and UX → validate accuracy and tune performance → deploy and drive adoption) (N6). **Do not number them or give them H3s** (S9 owns the numbered steps). No durations and no "7 days".
- Card 4 "Support after go-live": unchanged, including "Monday to Friday" (FAQ 21).

**S5 The Platform We Deliver** (was "Why Power BI"). Eyebrow "THE PLATFORM WE DELIVER". **Suggested H2: "What HLB HAMT Builds for You on Power BI"** (Build may refine it, but it must be HLB HAMT-led). Intro (45-60 words), first sentence HLB HAMT-led: HLB HAMT delivers your reporting on Power BI because it works natively with Excel, Teams, SharePoint, Outlook, Azure and Dynamics 365, so teams on Microsoft adopt it with little friction. No singular primary keyword in the intro. The 4 rows keep Bala's 4 pillars and the same bullets. **Each description opens with what HLB HAMT does, then names the component and the benefit:**
1. H3 suggestion **"Self-service reporting your teams run themselves"**: we build models in Power BI Desktop, with DAX measures for YTD, YoY and running totals, so business users explore without joining an IT queue. Dashboard page detail may be added: standardised metric definitions, reusable data layers.
2. H3 **"The Power BI service"** (primary #3, keep exact): we set up, govern and run the cloud service where reports are published as apps, refreshed on schedule and secured [F1]; dashboards serve leadership, reports serve analysts.
3. H3 suggestion **"Connected to the systems you run"**: we connect native, certified and custom connectors to SAP, Oracle, NetSuite and the rest, and install the on-premises data gateway. The Section 4 connector caveat stays. Do not restate 200+.
4. H3 suggestion **"On every device, and inside your own portals"**: we design mobile layouts for iOS and Android with alerts, and embed branded dashboards in portals through Power BI Embedded on capacity-based licensing.
- **Platform layer** H3 suggestion **"Fabric readiness and a medallion lakehouse"**: open with "We assess Fabric readiness and build Bronze, Silver and Gold lakehouses..."; then the Fabric definition; then the attributed stat "Microsoft reports more than 40,000 paid Fabric customers, up more than 60% year on year" [4]. Bullets unchanged.

**S6 Use cases** (was S7). Intro opens with "We" (e.g. we start every engagement from the KPIs a role or sector runs on). Add **L7 "data visualisation services"** in the intro, pointing to the live data-viz page (12.9). Six cards unchanged in scope, with these additions:
- Card 1 (CFO) may add cash flow and **budget variance and forecasting** (dashboard page, "Financial Reporting & Forecasting").
- Card 6 (CAO) carries **P2 "advanced analytics services"** (placeholder, relocated) on forecasting and next-best-action models.
- Pill row: add **Manufacturing** and **Wholesale Distribution** (data-viz industry list; both are also HLB HAMT industries) → 12 pills.
- Drop nothing, and do **not** add cards from the data-viz 9-industry list or the dashboard page's "Top 5". Those pages own that content (hub-and-spoke; see L6/L7).

**S7 HLB HAMT's Power BI Services** (was S8). Eyebrow "WHAT WE DO". **H2 "HLB HAMT's Power BI Services"** (plural keyword #1, now possessive-branded). Intro (30-40 words) opens with HLB HAMT/we. **6 items, 55-65 words each, no more than 2 titles containing "Power BI". No 33x. No sentence copied from a sibling page:**
- **01 Strategy, discovery and licence planning**: goals, data needs and reporting expectations (consulting page); map objectives to KPIs and metric logic, find reporting gaps by role (dashboard page step 01); assess BI readiness and design a scalable architecture (Bala portfolio 1); licence mix (Pro, PPU, capacity).
- **02 Data integration and preparation**: ETL/ELT pipelines in Azure Data Factory; data marts and warehouse layers; certified and custom connectors; gateway configuration; scheduled and **incremental refresh**, near-real-time where required; a lakehouse when scale calls for it (Bala portfolio 2; engagement model 3; dashboard page).
- **03 KPI-centric modelling and dashboard development**: semantic models with standardised metric definitions and tested DAX; "model-first, not visual-first" (an HLB HAMT phrase that may be quoted); drill-through, cross-filtering, slicers and bookmarks; executive dashboards and analyst reports; mobile layouts; Arabic RTL. Link **L6 "Power BI dashboard development"** here.
- **04 Performance tuning, security and governance** (new, N5/N8): tuning across pipeline, data model and semantic layers; query reduction, aggregation tables, efficient DAX patterns; row-level security, workspace governance and access controls. Do not restate 33x (S2 owns it).
- **05 Migration, embedded analytics and Fabric readiness**: Tableau to Power BI and Qlik to Power BI migration, preserving business logic and redesigning visuals for the new platform (N4; **do not** write "zero business logic loss", which is the data-viz page's absolute claim); moving off spreadsheets; Power BI Embedded for portals; Fabric readiness and staged migration.
- **06 Training and continuous support**: unchanged (three tracks, on-site in Dubai, remote or hybrid, Arabic-language delivery, contextual documentation). The training tracks still appear only here.

**S8 Mid-page CTA 1**: unchanged.

**S9 Proof of concept** (was S10). H2 unchanged, and it is still the only place "7 days" appears [6]. The **intro's first sentence is HLB HAMT-led and adds the qualifier "for a defined use case"** (N2), e.g. we prove the value on your own data for a defined use case, against agreed success criteria, before any larger investment. The 5 steps are unchanged (the live partner page confirms them word for word).

**S10 Engagement models + PowerUP!** (was S11). The intro opens with "We". **Featured card H3: "PowerUP!: HLB HAMT's Fixed-Price Power BI Accelerator"** (replaces "Microsoft Power BI PowerUP!"; see R2-3). Price line, 5 terms, 6 deliverables, badge and button are unchanged. Tabs:
- Explore, Implement, Extend: unchanged. Extend keeps "Power BI solutions expert" #2.
- **Support: 4-5 items.** Performance monitoring and troubleshooting now names refresh failures, gateway connectivity and slow pages (an item-level gap competitors cover in detail, 12.8). Quarterly health checks. New dashboards as needs change. Licence advisory and Fabric migration (optional primary #7). Optional 5th item **Security and access reviews** (RLS and workspace permissions checked as teams change; N8). Stay inside the 360-420 budget.

**S11 Why UAE businesses choose HLB HAMT** (was S12). H2 unchanged (plural #2). The intro opens with HLB HAMT/we. Tile changes:
- **Tile 1** stays **"Microsoft Power BI partner in the UAE"**, not certified (Section 10 #1 stands; see R2-2).
- **Tile 5 "Global network"**: "An HLB International member since 2007..." is allowed. It is a different fact from S2's "Since 1999", so no stat repeats. Still no "150+/157 countries".
- The other tiles are unchanged. Tile 2 may now use "finance and technology under one roof" as a phrase, because S2 no longer carries "Finance + technology" as its stat line.

**S12 See it in action** (was S13). **H2 "Inside an HLB HAMT Power BI Dashboard"**. Body: what we build (executive view in Arabic and English, group-to-entity drill). Static-asset default unchanged.

**S13 CTA 2** (was S14): unchanged (keyword "Power BI solutions expert" #1).

**S14 FAQ** (was S15). Keep the H2 ("Questions UAE Teams Ask Before Choosing a Power BI Partner"). **10 Q&As, 65-90 words each, and B3 applies to every answer.** Order:
1. **What is the Power BI service, and how is it different from Power BI Desktop?** Unchanged (primary #5, optional #6). End on what HLB HAMT sets up.
2. **How is Power BI licensed, and what will it cost?** Open with the total cost picture (N10): licences plus implementation plus data integration and modelling, scoped by complexity. Then the list prices "at the time of writing" (US$14 Pro / US$24 PPU) [F2], then capacity for large deployments, embedding and Copilot. Then HLB HAMT's licence advisory, plus a pointer to the fixed-price starter engagement (`#packages`, **no "$4,500"**).
3. **Which of your systems can we connect to Power BI, and do we need a data warehouse first?** (Reworded so the reader and HLB HAMT are the actors.) Content unchanged, and the connector caveat stands. "Custom connectors for legacy systems" (dashboard page) may be added.
4. **Can you replace our manual Excel reports with Power BI?** Content unchanged, and it stays qualitative with no hours figure. **Place L4 "Power BI automation with Power Automate"** on the Power Automate alert sentence.
5. **Do you build Arabic and right-to-left dashboards?** Unchanged. Urdu and Persian as examples. **Do not add Hebrew** from the sibling pages: the approved v1 omitted it, and adding it now would be a new decision the Content Writer has not made.
6. **Is our data secure, and can it stay in the UAE?** Unchanged: F5 "in scope of" wording (**not** the sibling pages' "compliant"), L5 and the Copilot cross-geo sentence. Open with what HLB HAMT configures.
7. **What is Microsoft Fabric, and should we plan for it?** Unchanged. Its second half is HLB HAMT's readiness assessment.
8. **What do we need to use Copilot in Power BI?** Unchanged [F4]. This and FAQ 6 are now the only Copilot mentions on the page.
9. **Why are some Power BI dashboards slow, and can you fix ours?** (**New, from N5**): the usual causes are weak data modelling, inefficient DAX or queries, large unoptimised datasets, and missing aggregations or indexing; performance depends more on how a report is built than on the tool; we tune across pipeline, model and semantic layers. **No 33x** (S2 owns it). Write this answer originally; do not copy the dashboard page's FAQ.
10. **How long does a Power BI implementation take?** Unchanged timelines. Optionally say HLB HAMT confirms timelines after discovery.
- The "Deliberately not carried over" list in Section 4 S15 still applies. "AI features" is now covered by nothing, and that is intentional.

**S15 Contact**: unchanged (optional plural #3). **S16 Footer**: unchanged.

### 12.6 Keyword placement: renumbered (substance unchanged) + branding counts

| Keyword | Count (unchanged) | Placements (new numbering) |
|---|---|---|
| **Power BI service** (singular, `\bPower BI service\b(?!s)`) | **5-7**, hard max 8 | (1) H1 (new B1 wording); (2) hero lede sentence 1; (3) S5 row 2 H3 "The Power BI service"; (4) S4 card 1; (5) S14 FAQ 1 question; (6, optional) FAQ 1 answer once; (7, optional) S10 Support tab. |
| **Power BI Services** (plural) | **2-3** | (1) **S7 H2 "HLB HAMT's Power BI Services"**; (2) S11 H2; (3, optional) S15 body. Never in a section that has a singular instance. |
| **Power BI consulting company** | **1-2** | (1) S4 lede; (2, optional) S11 intro. |
| **Power BI solutions expert** | **1-2** | (1) S13 CTA body; (2, optional) S10 Extend tab. |
| **Certified Power BI Partner in UAE** | **0: not placed** (Section 10 #1) | S11 tile 1 reads "Microsoft Power BI partner in the UAE". See R2-2. |

The stuffing caps are unchanged: "Power BI" 75 or fewer (flag above 85), "UAE" 12 or fewer. At most 2 of the 6 S7 titles and at most 1 of the 5 S9 step titles may contain "Power BI". **New for Test:** B4 "HLB HAMT" 10-16 and B5 "Microsoft" 12 or fewer (12.3a).

**Meta title and description (Section 7): unchanged.** Both already lead with the keyword and name HLB HAMT ("... | HLB HAMT"; "Power BI service from HLB HAMT: ..."). The meta description's "7-day proof of concept" stays, because meta is outside the on-page single-slot rule.

### 12.7 Stats re-verification and revised stat list (2026-09-29)

**Re-verified where the new sources give a different or more specific figure:**

| Stat | New-source variant | Re-verification | Decision |
|---|---|---|---|
| S-3 Gartner [3] | Partner page FAQ: "Ranked #1 by Gartner for 14+ consecutive years"; data-viz hero: "14+ Yrs Gartner #1" | Search results on 29 Sep 2026 again show Microsoft named a Leader in the **2026** MQ for Analytics and BI Platforms for the **19th consecutive year** (Microsoft Fabric Community announcement URL as in Section 6b; also reported by bismart.com and joulyan.com). Gartner does not rank vendors "#1". | **Keep S-3 as is.** The sibling variants are inaccurate and must not be used. |
| F2 Pro/PPU price [8] | Partner page: "~$15/user/month" | Search on 29 Sep 2026: Pro **US$14**, PPU **US$24** per user per month, list prices since 1 April 2025 and still current. | **Keep F2.** "~$15" is not used. |
| CS1 200+ [1] | Partner and data-viz pages: 200+ (consistent). BCN: "150+ data sources" | The Microsoft Learn connector list (updated 18 Sep 2026) was counted at ~210-220 on 28 Sep. BCN's figure is older and lower. | **Keep 200+**, attributed to Power BI's library (S2 item 1 wording, 12.5). |
| CS2 33x [2] | data-viz page: "In a recent engagement, we achieved a 33x improvement in report load times and interactivity" | The same claim is now **published on a live HLB HAMT page**, with the same single-engagement qualifier. Still no client name or date. | **Keep.** Footnote upgrade: "HLB HAMT, Data Visualization Services: https://hlbhamt.com/services/data-visualization-uae/". The "one recent engagement" qualifier stays mandatory. |
| CS3 7 days [6] | dashboard page: "in as little as 7 days for defined use cases" | Consistent across 3 live pages. | **Keep**, adding the "defined use case" qualifier in the S9 intro. Footnote: "HLB HAMT service commitment: https://hlbhamt.com/services/power-bi-partner-in-dubai-uae/". |
| Timelines (FAQ 10) | Identical on the partner and data-viz pages | Consistent | **Keep.** It may footnote the live partner page. |
| F5 ISO/SOC [11] | data-viz: "Power BI is ISO 27001 and SOC 2 compliant" | The Section 6c wording ("in scope of Microsoft's ISO/IEC 27001 certification and SOC 2 reports") is the accurate form. | **Keep the F5 wording.** |
| S2 73.3% [5] | none | Still valid (source unchanged) | **Retired from the page** (12.2 reason); kept on reserve. |

**New stat or fact added:**

| # | Figure | Context | Source | Age | Where |
|---|---|---|---|---|---|
| **CS5 [12]** | **Since 1999** (founded as HAMT & Associates in 1999; joined HLB International in 2007) | HLB HAMT's own track record in the UAE, an HLB HAMT-owned credential for the strip | HLB HAMT press release "HLB HAMT Celebrates 25 Years of Unwavering Excellence": https://hlbhamt.com/press-room/hlb-hamt-celebrates-25-years-of-unwavering-excellence/ (also https://hlbhamt.com/about-us/25-years-of-excellence/). **Self-published by HLB HAMT. WebFetch returned empty pages (client-side rendering), so the 1999 and 2007 dates were confirmed through two independent search-result summaries of these HLB HAMT pages and the HLB HAMT Academy page.** Deliver should click through before publishing. | Historical fact (anniversary event January 2024) | S2 item 3 ("Since 1999"); optionally "since 2007" in S11 tile 5 |

**Revised single-slot map (every stat or fact appears once, in the section named):** 200+ → S2 · 33x → S2 · Since 1999 → S2 · Gartner 2026 / 19th year → S2b · 40,000+ Fabric customers → S5 platform layer · 7 days → S9 H2 · $4,500 → S10 featured card · timelines → S14 FAQ 10 · list prices → S14 FAQ 2 · HLB International since 2007 → S11 tile 5 (optional). **No FAQ restates 200+, 33x, 1999, 19th year, 40,000, 7 days or $4,500.** Facts F1-F5 stay where Section 6c places them, renumbered (F4 is no longer in the removed S6).

**Explicitly not used (new sources):** the consulting page's 90%, 1.6x and 60% results and its testimonials (theme demo placeholders, not HLB HAMT data); BCN's "up to 57%" HR admin time and "up to 80%" reporting-time savings (competitor marketing claims with no source); Ranosys's "2-6 weeks" and "24/7 support" (a competitor's service claims); HLB HAMT's "3,000+ clients / 230+ staff / 9 offices" (dated January 2024 and likely stale; use only if the Content Writer supplies current figures).

**Footnotes:** [5] is retired and [12] is new. Deliver still renumbers in order of appearance (judgment call (h)).

### 12.8 Competitive analysis: updates from the full competitor text

**For direction only. Nothing from these pages may be copied or closely paraphrased.** The Section 5 takeaways stand, with these additions and corrections:

- **The competitors write in a provider-led voice, and that is the model for 12.3.** BCN ("BCN's Power BI services", "our BCN data experts"), DSP ("DSP's multi-disciplinary Power BI services") and Zenzero ("Zenzero's expert Power BI support services") make themselves the actor and Power BI the tool. HLB HAMT v1 did the reverse. The branding shift closes that gap. The UAE, finance-literate and Arabic/RTL angle (Section 5, bullet 1) is still uncontested: none of the four mentions Arabic, UAE hosting, Corporate Tax/VAT or PDPL.
- **BCN's "Power BI Kickstarter" is the closest rival to HLB HAMT's fast start.** It offers 7 days and up to 3 dashboards, with no published price and "subject to an initial review" of the data estate. BCN also runs a free 60-minute data assessment, a separate governance service (risk assessment, disaster recovery, compliance), a demo video and named case studies. **Angle:** HLB HAMT publishes its price and full scope (PowerUP!) *and* names security and governance as a delivered service (S7 item 04), with no gating review.
- **Zenzero's page (as fetched) is a Power BI support page, and its support catalogue is deep:** refresh failures, Power Query errors, gateway/service connectivity, security configuration, support tickets, and dedicated account managers. **Gap in v1:** HLB HAMT's Support tab was four short lines. **Angle:** name concrete support tasks in S10 Support and S4 card 4, including the single point of contact, in HLB HAMT's own words from source FAQ 21.
- **DSP sells outsourcing economics:** no need to hire, train or manage an in-house BI team. HLB HAMT's "Augmented expertise" (S10 Extend) covers this. Keep it capability-led and do not copy DSP's cost framing.
- **Ranosys still says "Gold Partner" (a retired Microsoft label), uses logo walls and lists product components.** It offers no UAE specifics and no price. This confirms the original angle: precise partner wording, no retired terminology.
- **Case studies:** BCN and DSP show named Power BI case studies. HLB HAMT has none it can publish (the consulting page's are placeholders). This is a known gap, not a blocker. See R2-4.
- **Revised positioning line (replaces Section 5's last bullet):** "HLB HAMT delivers Power BI and gets the numbers right: auditor-grade financial logic and in-house engineering, in Arabic and English, hosted in-country."

### 12.9 Internal links (replaces Section 8's tables for Build; new numbering)

| # | Anchor text | Target | Placement | Change |
|---|---|---|---|---|
| L1 | digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ | S4 lede | unchanged |
| L2 | SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ | S11 tile 4 | renumbered |
| L3 | UAE Corporate Tax advisory | https://hlbhamt.com/services/corporate-tax-advisory-services-in-uae/ | S6 card 2 | renumbered |
| L4 | Power BI automation with Power Automate | https://hlbhamt.com/insights/unlocking-power-bi-automation-with-power-automate/ | **S14 FAQ 4** | **moved** from the removed S6 |
| L5 | data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ | S14 FAQ 6 | renumbered |
| **L6** | Power BI dashboard development | https://hlbhamt.com/services/power-bi-dashboard-development/ | **S7 item 03** | **new** (live sibling page) |
| **L7** | data visualisation services | https://hlbhamt.com/services/data-visualization-uae/ | **S6 intro** | **was placeholder P1, now live.** It moves from S8 item 03 to avoid two links in S7 item 03. The anchor keeps British spelling; the URL is the live one. |
| P2 | advanced analytics services | `PLACEHOLDER:/services/advanced-analytics-services/` | **S6 card 6 (CAO)** | **moved** from the removed S6; still a placeholder |

**Do not link** to `/services/power-bi-partner-in-dubai-uae/` or `/services/microsoft-power-bi-consulting-in-dubai-uae/`. Both are candidates in Open Question 3: either could become this page's URL or be redirected to it, so linking now risks a self-link or a redirect chain. The reverse link from the SugarAI page and the breadcrumb links are unchanged (Section 8).

### 12.10 Unchanged from the approved brief (confirmed)

The keyword set, regexes and counts (12.6 only renumbers them). The word count range and count rule. The SugarAI structural mapping (Section 3a) apart from dropping AI Insights. Meta title and description (Section 7). Tone rules (British spelling, zero em dashes, no competitor names, positive opening). Schema (Service, FAQPage with now **10** Q&As, BreadcrumbList). All Section 10 decisions and the Section 10 #7 accuracy corrections.

### 12.11 Open questions for Revision 2 (each has a default; none blocks Build)

- **R2-1. Duplicate content with the live partner page.** `/services/power-bi-partner-in-dubai-uae/` is Bala's Tab 3 almost word for word, so this new page overlaps it heavily (PowerUP!, PoC steps, CxO lists, FAQs). That makes Open Question 3 (final URL and redirects) more pressing before go-live. **Default:** Build applies the reuse limit in 12.0 (facts, names and short phrases only; original sentences). If you confirm the partner page will be 301-redirected to this page, Build may reuse sibling sentences more freely.
- **R2-2. "Certified" claims on the live sibling pages.** The dashboard page's eyebrow reads "Microsoft Certified", the consulting page's breadcrumb reads "Certified Microsoft Power BI Consultant", and the partner page says "a leading Microsoft partner in UAE". A web search on 29 Sep 2026 found only HLB HAMT's own claim, and no Microsoft designation name or partner-directory listing. **Default:** Section 10 #1 stands. Tile 1 reads "Microsoft Power BI partner in the UAE", the keyword is not placed, and "certified" and "leading" are not used. If you supply the designation (e.g. "Solutions Partner for Data & AI (Azure)") or staff certifications, Build switches to the conditional plan in Section 2c.
- **R2-3. Offer name.** The live pages call the offer "Microsoft Power BI PowerUP!", though the site's buttons already say "$4,500 PowerUP! Offer". **Is "Microsoft" part of a required name (e.g. a Microsoft-funded partner offer)?** **Default:** no. The H3 becomes "PowerUP!: HLB HAMT's Fixed-Price Power BI Accelerator".
- **R2-4. Case study.** There is no publishable HLB HAMT Power BI case study (the consulting page's are placeholders). **Default:** no case-study block; 33x stays the only engagement result. If a client-approved story exists, it could replace the S12 "See it in action" copy in a later revision.

### 12.12 Non-blocking notes for the Content Writer (live-site issues found while sourcing)

These are outside this page's scope and go in the Deliver handoff notes.
1. **`/services/microsoft-power-bi-consulting-in-dubai-uae/` shows theme demo content as if it were real:** testimonials from "Execor" / "Kate Smith, Swirl" / "Carlos Martines, MEX" and "success stories" with 90%, 1.6x and 60%. This sits on the nav's live Power BI page and should be removed.
2. **Outdated or inaccurate claims on live sibling pages** that this page corrects: "Ranked #1 by Gartner for 14+ consecutive years" / "14+ Yrs Gartner #1"; "~$15/user/month" and "Tableau ~$75"; "Q&A (ask in English or Arabic)"; mobile on "Windows"; "ISO 27001/SOC 2 compliant"; "zero business logic loss". Once this page is live, the sibling pages will contradict it unless they are updated.
3. **"Celebrating 25 Years" in the site nav** is from 2024 (founded 1999). This page uses "Since 1999" to avoid the dated figure.

---

## 13. Content Writer decisions (2026-09-29) — Revision 2 open questions resolved

1. **R2-1 (duplicate content / redirect):** **Confirmed — the live partner page (`/services/power-bi-partner-in-dubai-uae/`) will be redirected to this new page once it publishes.** The 12.0 reuse limit (facts, names and short HLB HAMT phrases of 8 words or fewer only) is **lifted for this specific source page**: Build may draw on its sentences and paragraphs more freely, since that page is being retired in this page's favour, not left live alongside it as a competing duplicate. The reuse limit **still applies** to the other 3 sibling pages (microsoft-power-bi-consulting, data-visualization-uae, power-bi-dashboard-development), which are not confirmed for redirect and stay live and linked (L6, L7) — copying their sentences would create real duplicate content against pages this one links to.

2. **R2-2 (certification claim) — corrected framing, not simply "yes":** The Content Writer's own words: *"We are partners, but not mentioned by microsoft, but we are reselling partners."* This confirms HLB HAMT is **not** Microsoft-certified or Microsoft-listed — exactly what R2-2's research found — but it **is** a genuine **Power BI reselling partner** (HLB HAMT resells/provisions Power BI licences as part of its service). **Do not use "certified," "Microsoft Certified," or any wording implying a Microsoft-issued designation anywhere on the page** — Section 10 #1's default stands on that point, and B7 (honest attribution) applies. **Instead, state the real, accurate relationship:** S11 tile 1 becomes **"Power BI reselling partner in the UAE"** (replacing "Microsoft Power BI partner in the UAE"), and licence-related copy (S1 sub-block "Deployment," S7 item 01 "licence mix," S14 FAQ 2) may accurately describe HLB HAMT as provisioning/reselling Power BI licences as part of its service. The secondary keyword **"Certified Power BI Partner in UAE" remains not placed** (it asserts certification, which is false) — do not substitute "reselling" into that exact keyword phrase, since that would misrepresent it as the target keyword string. Test should specifically check that "certified" does not appear anywhere near "Microsoft" or "Power BI partner" on the page.

3. **R2-3 (offer name):** **Confirmed — rename.** Featured card H3 is **"PowerUP!: HLB HAMT's Fixed-Price Power BI Accelerator"**, as already specified in 12.5 S10.

4. **R2-4 (case study):** **Confirmed — skip.** No case-study block. 33x remains the only engagement result, as already specified.

**Status: Revision 2 brief APPROVED. Ready for Build**, incorporating Section 12 in full plus the R2-2 correction above (reselling-partner framing, not certified).
