# Test report v1: Power BI Services homepage (draft-v1.md)

Tested by: Test agent, 2026-09-28
Loop: **1 of 3** (no earlier test reports in `draft/`)
Inputs checked: `brief.md` (all sections; Section 10 treated as overriding), `draft/draft-v1.md`, `inputs/requirement-notes.md`, `inputs/extracted/hlb-data-viz-v4 (1).html.md`, `inputs/extracted/HLB_HAMT_Data_Viz_Content_Documentation (1).docx.md`, `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`. For exact source wording in the originality check, I also read the **Tab 3 section only** (lines 644-1076) of `inputs/content-source/data-viz-documentation-extracted.md`. I did not open the raw HTML source.
Method note: no shell was available, so all counts are manual, word by word, per section, using the brief Section 1 count rule. Keyword and character checks used ripgrep across the whole file, and I then excluded the non-page lines (meta, chrome, Sources, Stats used, Flags).

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density | **PASS** |
| 2 | Word count | **PASS** |
| 3 | Zero em dashes | **PASS** |
| 4 | Grammar, spelling, punctuation | **FAIL** (minor, 4 fixes) |
| 5 | Originality | **FAIL** (9 sentences to re-frame) |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI heuristics | **FAIL** (repeated sentence structure and internal repetition, no stock AI phrases) |
| 8 | Section structure (and internal links) | **PASS** |
| 9 | Client requirements and the 7 accuracy corrections | **PASS** |
| + | Build's flagged judgment calls | All reasonable (see the end of item 8) |

**Overall: FAIL (loop 1 of 3).** The draft is close. Every structural, keyword, stat and accuracy requirement is met. The failures are all sentence-level rewrites, and each one is specified below with a word-count-safe replacement.

---

## 1. Keyword placement and density: PASS

Counted on-page copy only (H1, headings, body, cards, list items, FAQ Q&A, CTA headings and body). Excluded eyebrows, buttons, breadcrumb, anchor nav, meta, the Sources list, the Stats-used table and the Flags section.

**Primary "Power BI service" (singular), regex `\bPower BI service\b(?!s)`, case-insensitive: 6** (target 5-7, hard max 8). Build's count is confirmed.
1. H1: "Power BI Service Partner for Smarter Decisions Across the UAE" (followed by a space, not "s")
2. Hero lede sentence 1: "HLB HAMT designs, builds and runs your Power BI service, turning..."
3. S4 card 1: "We then set up and govern your Power BI service: workspaces and apps..."
4. S5 row 2 H3: "The Power BI service"
5. FAQ Q1: "What is the Power BI service, and how is it different from Power BI Desktop?"
6. FAQ A1, once only: "The Power BI service is the browser-based cloud platform..."

The optional S11 Support instance was not used ("Help administering the platform"). That is allowed.

**Plural "Power BI Services", regex `\bPower BI services\b`: 3** (target 2-3). Build's count is confirmed.
1. S8 H2 "Our Power BI Services"
2. S12 H2 "Why UAE Businesses Choose HLB HAMT for Power BI Services"
3. S16 body "Our Power BI Services team replies within one business day."

**No section contains both forms.** S8 (lines 211-235), S12 (332-356) and S16 (411-417) have no singular instance. No singular instance sits in a heading/lede pair with a plural one. No "service services" constructions.

**Placement:** the meta title is exactly the brief's Section 7 title (primary at the start). The meta description is exactly the brief's text (primary in the first three words). The primary is in the H1 and twice in the first 100 words (H1 plus lede = 62 words). The S5 intro correctly avoids the singular.

**Secondaries:**
- "Power BI consulting company": **2** (S4 lede; S12 intro). Target 1-2. PASS.
- "Power BI solutions expert": **2** (S11 Extend "Augmented expertise"; S14 body). Target 1-2. PASS.
- "Certified Power BI Partner in UAE": **0, correctly not placed** per brief Section 10 point 1. S12 tile 1 reads "Microsoft Power BI partner in the UAE", and the alternate meta title is not used. PASS.

**Stuffing checks:**
- "Power BI" (any form), on-page: **41** (cap 75, flag above 85). Build's count is confirmed.
- S8 offering titles containing "Power BI": 0 of 6. PoC step titles containing "Power BI": 0 of 5.
- "UAE", on-page: **10** (cap 12): H1; deployment line x2; S4 card 4 ("UAE-based"); S6 lede; S7 card 2 anchor; S12 H2; S12 tile 1; S15 H2; FAQ Q6.
- No awkward repetition of any keyword.

---

## 2. Word count: PASS

Independent manual count, by the brief Section 1 rule:

| Section | My count | Build's count | Budget (3b) | Status |
|---|---|---|---|---|
| S1 | 183 | 183 | 150-190 | OK |
| S2 + S2b | 65 | 65 | 45-65 | OK (at max) |
| S4 | 258 | 259 | 250-300 | OK |
| S5 | 393 (409 with "Capability"/"Key capabilities"/"Platform layer" labels) | 408 | 380-440 | OK either way |
| S6 | 150 | 150 | 150-190 | OK (at floor) |
| S7 | 358 (363 with pill-row label) | 362 | 330-400 | OK |
| S8 | 355 | 355 | 330-390 | OK |
| S9 | 23 | 23 | 20-30 | OK |
| S10 | 156 | 156 | 150-190 | OK |
| S11 | 385 (397 with badge, column labels and tab names) | 394 | 360-420 | OK |
| S12 | 145 | 145 | 140-180 | OK |
| S13 | 34 | 34 | 30-45 | OK |
| S14 | 30 | 30 | 20-30 | OK (at max) |
| S15 | 809 | 805 | 700-850 | OK |
| S16 | 28 | 28 | 20-30 | OK |
| **Total** | **3,372** (3,405 with structural labels) | ~3,370 / ~3,395 | 3,100-3,500 (fail <2,900 or >3,750) | **PASS** |

**Sub-budget notes (not failures; sections are the binding budget):**
- S6 lede: **64** words by my count (Build said 63), against a 45-60 sub-range. Accepted, see judgment call (d).
- S2 item 4 description, "Right-to-left dashboards designed from the first mockup.": **7** words, against the 8-16 sub-range. It is one word short, but S2 is already at its 65 cap. Left as is.
- S11 featured card: 118 words without the badge and column labels, 126 with them (brief: about 120-140). Fine.
- FAQ A6: 90 words (top of the 65-90 range). All other answers are 72-83.
- Card and tile sub-ranges are all met: S4 cards 41/44/49/42; S5 descriptions 39/45/42/44; S5 platform body 60; S7 backs 44/42/38/42/36/38; S8 items 50/51/46/45/47/47; S10 steps 21/17/17/18/20; S12 tiles 14-18.

**Headroom for the fixes below:** S6 (floor), S14 (max) and S2 (max) have no slack. Every replacement text in the Fix instructions has been counted to keep each section inside its budget.

---

## 3. Zero em dashes: PASS

- `—` (em dash): **0** in the whole file.
- `--`: **0** in the whole file.
- `–` (en dash): **0** in the whole file.

---

## 4. Grammar, spelling, punctuation: FAIL (minor)

British spelling is clean. There are no -ize, -yze, "center", "color", "behavior" or "program" hits. "Licence" is a noun and "licensed"/"licensing" are verb forms, both correct. "Programme", "modelling", "visualisation", "optimised", "analyse", "digitise" and "monetisation" are all correct.

Errors found:

| # | Location | Sentence as written | Problem | Fix |
|---|---|---|---|---|
| G1 | S8 item 05 | "Move reporting off spreadsheets or another BI tool, including Tableau and Qlik, without losing..." | A singular "another BI tool" cannot "include" two products. | "...off spreadsheets or another BI tool such as Tableau or Qlik, without losing..." |
| G2 | S8 item 06 | "...with Arabic-language delivery available, and documentation plus ongoing support keep the platform healthy after handover." | "Plus" is a preposition, so formally the verb should be singular. The sentence also runs two ideas together. | Split into two sentences: "...with Arabic-language delivery available. Documentation and ongoing support keep the platform healthy after handover." |
| G3 | S14 body | "A Power BI solutions expert will plan data, phasing and licences with you, free of charge." | "Plan data" is unclear (the brief means data sources). | Resolved by the S14 rewrite in fix 5g. |
| G4 | S6 point 3 | "...while data alerts and Power BI automation with Power Automate email the owner when a KPI crosses its threshold." | The link anchor has been forced in as a grammatical subject, so a process name "emails the owner". | "Anomaly detection flags unusual movements. Data alerts, extended through [Power BI automation with Power Automate](L4), email the owner when a KPI crosses its threshold." (24 words, same as now; keeps L4's exact anchor) |

Optional clarity point, not scored: the S5 row 2 description opens "It is the cloud side of the platform...", where "It" relies on the H3 above it. Consider "This is the cloud side of the platform...".

---

## 5. Originality: FAIL

**Web check: clean.** I searched distinctive draft phrases: "Great Dashboards Start With the Numbers Behind Them", "Ask Your Data a Question and Act on the Answer", "one semantic model, one version of the numbers", "questions they can't yet answer from data they already own" and "Picking a Power BI consulting company is really a decision about whose numbers". None returned an exact or near match. No competitor consultancy is named, and I found no competitor wording. I also searched the source's distinctive strings ("deal pipelines, lead conversion, unit availability...", "Ingest, cleanse, and transform raw data into analytics-ready datasets"). Neither appears to be published on the web.

**SugarAI H2s: no H2 is reused verbatim.** The closest is S12's brief-mandated "Why UAE Businesses Choose HLB HAMT for Power BI Services" (see judgment call (c)). The S4 H3s ("What we do / Who we work with / How we deliver / Support after go-live") and S12 tile titles "In-region team" and "Dual intelligence" match SugarAI labels. These are brief-mandated structural labels, not violations.

**Violations: sentences reused or lightly reworded from the in-scope content source.** The Plan agent's extract says "Nothing here may be reused word for word on the new page", and a lightly reworded sentence counts as a violation under this checklist. The facts are fine to keep. The **sentence frames** must change.

| # | Draft (location) | Source | Assessment |
|---|---|---|---|
| 5a | S7 card 1 back: "Consolidated P&L, balance sheet and cash flow across entities reporting in AED, USD, SAR, EUR and more. Intercompany eliminations, FX conversion and IFRS segment reporting are built into the model..." | docx FAQ (multi-entity): "consolidated P&L, balance sheets, and cash flows across entities in AED, USD, SAR, EUR, and more. Intercompany eliminations, exchange rate conversions, and IFRS segment reporting included." | First sentence is near-verbatim (only "reporting" added). Second sentence is lightly reworded. |
| 5b | S7 card 2 back: "Dashboards follow taxable income, deferred tax under IAS 12, VAT returns, transfer pricing and the split between free zone and mainland entities." | docx FAQ (tax): "We build dashboards tracking taxable income, deferred tax (IAS 12), VAT returns, transfer pricing, and free zone vs mainland segregation." | Lightly reworded ("tracking" became "follow", "segregation" became "split"). |
| 5c | S7 card 3 back: "Track expressions of interest, deal pipeline, lead conversion, unit availability, payment plans, broker performance and DLD compliance." | docx FAQ (real estate): "We track EOIs, deal pipelines, lead conversion, unit availability, payment plans, broker performance, and DLD compliance." | Near-verbatim (EOIs expanded, "We" dropped). |
| 5d | S10 step 2: "We ingest, cleanse and reshape the raw data into analytics-ready datasets, then build optimised models on top." | docx 6.7 step 2: "Ingest, cleanse, and transform raw data into analytics-ready datasets. Build optimized data models for Power BI consumption." | Lightly reworded (one verb swapped, two sentences merged). |
| 5e | S10 step 4: "Interactive reports, dashboards and visuals are built to the approved design, using the models prepared in step two." | docx 6.7 step 4: "Build interactive Power BI reports, dashboards, and visualizations aligned with approved designs..." | Same sentence turned passive, plus a tail clause. |
| 5f | S10 step 5: "We train your users, collect their feedback, complete one round of revisions and publish the finished app to your tenant." | docx 6.7 step 5: "...conduct training, gather feedback, and perform one round of design revision. Publish the final Power BI App." | Same sequence with synonym swaps (gather/collect, perform/complete, final/finished). |
| 5g | S14 body: "A Power BI solutions expert will plan data, phasing and licences with you, free of charge." | SugarAI S14 body: "We scope the packages, phasing and integrations around your team with a free consultation." | Same frame: subject + plan/scope + three-item list with "phasing" second + "with you / around your team" + free. Build changed this section's H2 for echoing SugarAI, but the body still echoes it. |
| 5h | S12 tile 4 body: "Predictive scoring in SugarAI CRM alongside Power BI reporting, planned, built and supported by one partner." | SugarAI tile: "SugarAI prediction plus Power BI analytics, from one partner." | Same four units in the same order with synonym swaps (prediction/predictive scoring, plus/alongside, analytics/reporting, from/by one partner). |
| 5i | FAQ A4: "Clients in the Emirates have removed hours of manual weekly reporting this way..." | docx FAQ: "We've helped UAE businesses eliminate hours of weekly manual reporting." | Lightly reworded claim sentence. |

**Borderline, advisory only (not scored):**
- FAQ A7 "Fabric is Microsoft's unified analytics platform. It puts Power BI alongside data engineering, data warehousing and real-time analytics, under one capacity-based bill." echoes the source's "Fabric is Microsoft's next-gen unified platform: Power BI + data engineering + data warehousing + real-time analytics, all under one roof with simplified billing." Definitional sentences converge, so this is acceptable. A more distinctive opening would help.
- S11 story "aiming for quick wins against clear objectives" reuses a 5-word run from the source ("demonstrate quick wins against clear objectives").
- S8 intro "Take one on its own or combine several, with..." has a skeleton similar to SugarAI's "Choose one or combine them based on your needs, with...". It is a generic clause, and the rest of the sentence is different.
- S10 step 1 keeps the source's list order ("objectives, KPIs, data sources, success criteria") in a new sentence. Acceptable, because the list is the factual scope.

---

## 6. Stat accuracy: PASS

Every stat appears **once** on the page, in the brief's assigned section, with the brief's footnote number. No FAQ restates 200+, 33x, 19th, 40,000, 73.3% or 7 days. None of these figures appears on any other page in `content-pipeline/`. The SugarAI page's stats (26 years, 150+ countries, Nucleus) are not reused.

| Ref | Draft wording | Placement | Verification |
|---|---|---|---|
| [1] 200+ | "200+ / Data connectors in Power BI, from ERP and CRM to cloud databases." | S2 item 1 only | Worded as **Power BI's** library, as required. Source is Microsoft Learn "Data sources in Power BI Desktop" (credible, updated Sept 2026). I did not re-count the list myself. I accept the Plan agent's documented count (~210-220). |
| [2] 33x | "33x / Faster report load times in one recent HLB HAMT engagement." | S2 item 2 only | **Mandatory qualifier present.** Matches the docx context ("in a recent engagement... 33x improvement in report load times"). Publication approved in brief Section 10 point 4. Internal source, no URL (disclosed in the Sources list). |
| [3] Gartner | "Microsoft: named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." | S2b only | Exact brief wording. Clearly Microsoft's recognition, not HLB HAMT's. No "#1", "ranked" or "14+" anywhere on the page. Confirmed by search: the 2026 MQ was published 29 June 2026 and names Microsoft a Leader for the 19th consecutive year (Microsoft Fabric Community post plus the mwpro.co.uk repost). The Gartner disclaimer is included in Sources item 3 for Deliver. |
| [4] Fabric | "Microsoft reports more than 40,000 paid Fabric customers, up more than 60% year on year." | S5 platform layer only | Confirmed via search: Microsoft FY26 Q4 earnings call, 29 July 2026. About 2 months old. Attributed to Microsoft inline. |
| [5] AI diffusion | "in Q2 2026, 73.3% of the UAE's working-age population used generative AI tools, against 18.8% worldwide." | S6 lede only | **Fetched the source directly** (Microsoft On the Issues, 21 Sep 2026): "the UAE (73.3%) and Singapore (64.3%)..." and "In June, AI usage was 18.8% of the working-age population worldwide". The metric is "people aged 15-64 who have used a generative AI product", so the draft's "used generative AI tools" is accurate and is not framed as BI use. Framed positively, as required. |
| [6] 7 days | H2 "A Working Power BI Dashboard on Your Data in 7 Days" | S10 H2 only | HLB HAMT service commitment. "7 days" appears nowhere else on-page (the meta description's "7-day" is brief-prescribed and outside on-page copy). |
| [7] F1 | Desktop vs service (S5 row 2; FAQ A1) | as brief | Consistent with Microsoft Learn. "Free Windows application" is correct for Desktop. |
| [8] F2 | "Power BI Pro at US$14 and Premium Per User at US$24 per user per month, the list prices since 1 April 2025" | FAQ A2 only | Confirmed current in 2026 via multiple sources. "At the time of writing" is present. No competitor prices. |
| [9] F3 | UAE North full Fabric; UAE Central Power BI only | S1; FAQ A6 | **Fetched** Microsoft Learn region availability (updated 22 Sep 2026): "UAE Central ... Power BI only region"; UAE North has all Fabric workloads. |
| [10] F4 | Copilot capacity, English-only prompts, off by default outside the US/EU boundary, capabilities | S6 point 1; FAQ A6; FAQ A8 | **Fetched** Microsoft Learn Copilot overview (ms.date 24 Aug 2026): "Paid Fabric capacity (F2 or higher) or Power BI Premium (P1 or higher)"; "A Power BI Pro or Premium Per User (PPU) license alone isn't sufficient"; "multilingual use isn't officially supported"; "If your tenant or capacity is outside the United States or EU data boundary, Copilot is disabled by default unless..." All match the draft. The Q&A retirement (February 2027) is confirmed via the Fabric Community blog and Message Center MC1218421. The draft correctly does not feature Q&A. |
| [11] F5 | ISO/IEC 27001 and SOC 2 scope | FAQ A6 only | Worded as "within the scope of Microsoft's... certification and SOC 2 reports", not "guarantees compliance". PDPL/DIFC/ADGM uses "in line with", as required. |

Footnote order: [9] (S1) and [7] (S5) render before [1] (S2). This is acceptable because [1]-[6] are fixed by brief Section 6. Deliver should renumber by order of appearance when rendering and keep the Stats-used mapping.

---

## 7. Human tone / AI-detection heuristics: FAIL

**No stock AI phrases.** "Unlock", "seamless", "revolutionise", "leverage", "empower", "harness", "robust", "journey", "in today's..." and "in conclusion" do not appear in on-page copy. The only "unlock" hit is inside the L4 URL. Headings are specific and technical, and the voice is confident and concrete. Most of the page reads as written for this subject.

**Why it fails:** there is one strong structural tic, a verbal filler, and three places where the page repeats its own sentences.

**T1. The ", so [benefit]" consequence clause appears 15 times**, and 5 of the 9 FAQ answers resolve with it. Lines: S1 lede; S1 sub-block; S4 lede; S5 row 1; S5 row 2; S7 card 1; S7 card 3; S8 item 04; S12 tile 6; FAQ A2, A4, A5, A6, A8, A9. The worst cluster is **S5 rows 1 and 2, adjacent cards that both end ", so every..."** ("so every page uses one agreed definition" / "so every part of the business is visible from one place"). The claim-then-", so"-benefit rhythm is a recognisable machine-writing pattern. Rewrite at least these 7 (the other 8 can stay):
- S1 sub-block: "Leadership, analysts and field teams read from the same governed dataset. A revenue figure means the same thing in every meeting."
- S5 row 1, second sentence: "Underneath, DAX measures calculate the KPIs finance reports on, such as year-over-year growth, running totals and year-to-date revenue. Every page then works from one agreed definition." (also drops "actually")
- S5 row 2, second sentence: "Dashboards serve leadership and reports serve analysts. Both draw on the same data, which puts every part of the business in view from one place."
- FAQ A5, last sentence: "Where you need Arabic and English versions of the same report, both sit on one model and the numbers always match."
- FAQ A6, last sentence: "Outside the US and EU data boundaries, Copilot is off by default unless an admin allows cross-region processing. We make that call with you." (keeps [10]; A6 goes to 89 words, within the 90 max)
- FAQ A9, fourth sentence: "Whatever the size, a working prototype arrives within two weeks, early enough for your feedback to shape the build."
- S8 item 04, second sentence: covered by T3 below.

**T2. "Actually" as a filler, 3 times:** S5 row 1 "the KPIs finance actually reports on"; S7 intro "the KPIs a role or sector actually runs on"; S7 card 6 "what the technology can actually deliver". Delete all three instances of "actually". Each sentence stands without it.

**T3. The page repeats itself nearly word for word in three places:**
- On-premises gateway. S5 row 3: "For servers inside your own network, the on-premises data gateway keeps scheduled refresh running..." and S8 item 04: "We also configure the on-premises gateway, so data on servers inside your network refreshes alongside your cloud sources." Rewrite S8 item 04's second sentence: "We also install and configure the on-premises data gateway, then test refresh for every source behind your firewall." (18 words, same as now)
- Source of truth. S5 platform: "giving every report one source of truth" and FAQ A3: "a lakehouse gives every report one reconciled source of truth." Rewrite FAQ A3's last sentence: "Once data is spread across five or more systems, a lakehouse is usually worth it: every report then reconciles to the same cleaned tables."
- KPI threshold alerts. S6: "when a KPI crosses its threshold" and FAQ A4: "when a KPI breaches its threshold". Rewrite FAQ A4's third sentence: "Power Automate can email whoever owns a figure the moment it moves outside its agreed range." (This also removes one ", so" and the source echo "when KPIs breach thresholds".)

---

## 8. Section structure: PASS

**Order and format match brief Section 3b and the real SugarAI sequence** (hero + "one platform" block, dark 4-item strip + recognition bar, anchor nav, Why HLB HAMT, Explore module table + AI layer, AI block, industries grid, numbered offerings, CTA, highlighted methodology, packages matrix, "Why UAE Businesses" tiles, video teaser, CTA, FAQ, contact form, footer):

| Section | Present | Format check |
|---|---|---|
| S0 breadcrumb | Yes | Live HLB chain, correct URLs, final crumb unlinked |
| S1 | Yes | Exactly one H1 on the page; lede of 2 sentences (52 words); sub-block line plus 3 H3 audience cards; deployment line; no stats in the hero |
| S2 / S2b | Yes | 4 strip items with no heading tags; recognition p plus "Read Microsoft's announcement" button |
| S3 anchor nav | Yes | Labels and order match the brief exactly (DOM order) |
| S4 | Yes | H2 plus 4 H3; no durations and no "7 days" in "How we deliver"; "proof of concept" links to #methodology |
| S5 | Yes | H2; intro without the singular keyword; 4 module rows each with label, H3, description and exactly 5 bullets matching the brief word for word; platform-layer H3 with 4 bullets |
| S6 | Yes | H2 plus 3 H3 points |
| S7 | Yes | H2; intro; 6 flip cards (front H3 plus tagline, back plus button); pill row with 10 sectors |
| S8 | Yes | H2 "Our Power BI Services"; intro; 01-06 H3 items; training tracks appear only here |
| S9 | Yes | H2 plus 1 line plus button |
| S10 | Yes | Highlighted band; H2 with "7 Days" [6]; intro; 5 H3 steps |
| S11 | Yes | H2; intro; featured PowerUP! card with badge, H3, price, story, all 5 terms and all 6 deliverables; 4 tabs with the brief's items |
| S12 | Yes | Brief-mandated H2; intro; 6 H3 tiles; no "7 days", "$4,500" or "150+" |
| S13 | Yes | Static asset version (brief Section 10 point 5) |
| S14 | Yes | H2 plus body plus button |
| S15 | Yes | H2 plus 9 H3 questions, in the brief's order |
| S16 | Yes | H2 plus body; "Let's Connect" form component with default "Technology Consulting" |
| S17 | Yes | Global footer |

**Internal links: all 7 present and correctly placed (PASS)**
- L1 "digital transformation and analytics services" goes to /services/digital-transformation-uae/ (S4 lede). Correct.
- L2 "SugarAI CRM" goes to /sugarai-crm-2/ (S12 tile 4). Correct.
- L3 "UAE Corporate Tax advisory" goes to /services/corporate-tax-advisory-services-in-uae/ (S7 card 2). Correct.
- L4 "Power BI automation with Power Automate" goes to /insights/unlocking-power-bi-automation-with-power-automate/ (S6 point 3). Correct. Keep the anchor exact when applying fix G4.
- L5 "data protection advisory" goes to /services/data-privacy-and-security-uae/ (FAQ A6). Correct.
- P1 `[data visualisation services](PLACEHOLDER:/services/data-visualisation-services/)` in S8 item 03. Correct format and placement.
- P2 `[advanced analytics services](PLACEHOLDER:/services/advanced-analytics-services/)` in the S6 lede. Correct format and placement.
- The Microsoft product page is not linked (brief Section 10 point 2).

**Build's flagged judgment calls, evaluated:**
- (a) **S14 H2 changed** to "Talk Through Your Roadmap With a Specialist" (the brief's suggestion echoed SugarAI's "Plan your SugarAI rollout with our consultants"): **Reasonable.** It serves the brief's "do not reuse SugarAI H2s" intent. The body still echoes SugarAI, see fix 5g.
- (b) **S16 H2** "Book Your Free Consultation" instead of the component's "Let's Connect" (a verbatim SugarAI H2): **Reasonable.** Deliver decides whether the form component hard-codes its heading. Carry the flag to Deliver.
- (c) **S12 H2 exception**, "Why UAE Businesses Choose HLB HAMT for Power BI Services": **Accept.** It is brief-prescribed for the plural keyword slot, it is not identical to the SugarAI H2, and it is a "Why [Product]" structural label, which this checklist explicitly treats as non-violating. The intro and all tile bodies under it are original, apart from tile 4 (fix 5h).
- (d) **S6 budget:** Build's arithmetic is correct. H2 (~10) + lede max 60 + 3 x (1-word H3 + 25) = 148, which is below the 150 floor. Letting the lede run to 64 words so the section reaches exactly 150 is a sensible reading of the brief's intent. **Accept, not a failure.** Note that S6 has zero slack, so the G4 rewrite is held at 24 words.
- (e) **S6 point titles** "Answers / Explains / Alerts" instead of "Asks": **Reasonable.** More accurate, and it keeps the three-verb pattern.
- (f) **S7 card 2 H3** "Corporate Tax and VAT" (dropped "UAE"): **Reasonable.** The L3 anchor keeps the locality, and the UAE count stays at 10.
- (g) **"Certified" x3 (connectors only):** brief Section 2c says not to use "certified" anywhere without confirmation, but brief S5 row 3 and S8 item 04 prescribe "certified connectors" word for word. This refers to Microsoft's certified-connector programme, and no instance is adjacent to an HLB HAMT partner claim. **Accept.** Deliver should surface it to the Content Writer with Build's "partner connectors" alternative in case they want zero instances.
- (h) **Footnote numbering out of appearance order:** acceptable. Deliver renumbers when rendering (item 6).
- (i) **Sub-block heading as a styled line rather than an H tag:** acceptable, because Section 3b lists only H1 plus H3 cards for S1.

---

## 9. Transcript and client requirement accuracy: PASS

No transcript was provided (per `requirement-notes.md`). Client requirements and the Content Writer's Section 10 decisions:

- **Scope:** only Tab 3, the shared hero stats and CTA content are used. Advanced analytics and data visualisation are handled as placeholder links, not absorbed into the page. The S8 item 03 "tune across pipeline, data model and semantic layers" line is brief-sanctioned context carried in the in-scope docx extract.
- **Structure:** follows the real SugarAI homepage, not the industry-subpage pattern, as the requirement notes instruct.
- **Section 10 decisions:** 1 no "certified" partner claim (met); 2 HLB breadcrumb chain (met); 3 URL-agnostic (met); 4 33x qualifier, $4,500 USD, "Limited offer" badge, timelines as published (met); 5 static S13 asset (met); 6 /sugarai-crm-2/ (met).

**All 7 accuracy corrections (Section 10 point 7), verified across the whole draft, not just the obvious sections:**

| Correction | Whole-draft search | Result |
|---|---|---|
| "Gartner #1" / "ranked #1" / "14+ years" | "Gartner" appears on-page only in S2b, with correct wording. No "#1", "ranked" or "14+" on-page. | Applied |
| No Arabic Copilot / Arabic Q&A claim | S6 lede has no "in English or Arabic". FAQ A8 says "Microsoft officially supports English prompts only at present, so we design Arabic into the reports themselves". Every "Arabic" mention (S2 item 4, S5 bullet, S8 items 03 and 06, S13, FAQ Q5/A5) is about report design or training. | Applied |
| Mobile is iOS and Android only | S1 card 3 and S5 row 4 say "iOS and Android". The only "Windows" is FAQ A1 "free Windows application" for Desktop, which is correct. | Applied |
| Q&A not featured | No "Q&A" in on-page copy. S6 uses Copilot, Key influencers, decomposition tree and the narrative visual. | Applied |
| No Tableau/Qlik price comparison | Tableau and Qlik are named only in S8 item 05, as migration sources. FAQ A2 quotes Microsoft prices only. | Applied |
| "Salesforce (60+ modules)" dropped | No "60+". Salesforce appears only as a named data source (S5 row 3, FAQ A3). S7 card 3 names no systems. | Applied |
| (Supporting) connector caveat | S5 row 3 "Native, certified and custom connectors cover systems such as..." and FAQ A3 "Microsoft's own connectors, partner-built connectors and custom builds cover sources such as..." | Applied |

---

## Overall: FAIL (loop 1 of 3)

Items 4, 5 and 7 fail. Items 1, 2, 3, 6, 8 and 9 pass. All fixes are sentence-level and budget-safe. Do not change keywords, stats, footnotes, links, section order or any passing content beyond what is listed below.

## Fix instructions (for Build, draft-v2)

**Item 4, grammar**
1. **S8 item 05**, sentence 1: replace "another BI tool, including Tableau and Qlik," with "another BI tool such as Tableau or Qlik,".
2. **S8 item 06**, sentence 2: split it as "Sessions run on-site in Dubai, remotely or in a hybrid format, with Arabic-language delivery available. Documentation and ongoing support keep the platform healthy after handover."
3. **S6 point 3 (Alerts)**: replace the whole body with "Anomaly detection flags unusual movements. Data alerts, extended through [Power BI automation with Power Automate](https://hlbhamt.com/insights/unlocking-power-bi-automation-with-power-automate/), email the owner when a KPI crosses its threshold." (24 words. S6 stays at 150; do not shorten.)
4. **S14 body**: fixed by 5g below ("plan data" becomes "sources").

**Item 5, originality** (keep every fact and link; change the sentence frame. Suggested text is counted to keep budgets. Your own wording is fine if it is equally distinct from the source.)

5a. **S7 card 1 back**, replace both sentences: "Every entity rolls up into one group P&L, balance sheet and cash flow, whatever currency it reports in, from AED and SAR to USD and EUR. Chartered accountants design the intercompany eliminations, currency translation and IFRS segment views, which is why the logic survives audit." (45 words)

5b. **S7 card 2 back**, replace sentence 1 only: "Taxable income, IAS 12 deferred tax, transfer pricing and VAT return figures sit on one page, with free zone results kept apart from mainland ones." Keep sentence 2 with the L3 link unchanged. (45 words)

5c. **S7 card 3 back**, replace both sentences: "Follow each unit from first expression of interest to signed deal, with lead conversion, live availability, payment plans, broker performance and DLD compliance on the same dashboard. CRM and ERP data meet in a lakehouse first, giving sales and finance the same figures." (43 words; also removes one ", so")

5d. **S10 step 2**: "Your raw extracts are loaded, cleaned and reshaped until they can be trusted, then modelled for fast reporting." (18 words)

5e. **S10 step 4**: "Our developers build the interactive pages exactly as signed off, on top of the models from step two." (18 words)

5f. **S10 step 5**: "Users get hands-on training and give feedback, one revision round follows, and the finished app goes live in your tenant." (20 words)

5g. **S14 body**, replace both sentences: "Share your reporting wish list, and a Power BI solutions expert will map it to sources, licences and phases, free of charge." (22 words + 7-word H2 = 29; this keeps "Power BI solutions expert" #1 and fixes G3)

5h. **S12 tile 4 body**: "SugarAI CRM's deal predictions and Power BI's financial reporting side by side, with one team accountable for both." Keep the L2 link on the words "SugarAI CRM". (18 words)

5i. **FAQ A4**, replace sentence 4: "For clients in the Emirates, the result has been hours returned every week that once went on building reports by hand. Excel stays available for anyone who still prefers to analyse there." (Keeps the claim qualitative, with no number. A4 becomes about 77 words.)

Optional (advisory, not required to pass): open FAQ A7 differently from the source's "Fabric is Microsoft's unified platform" definition, and replace "quick wins against clear objectives" in the S11 story with your own phrasing.

**Item 7, tone**

7a. **Break the ", so" pattern** by applying these rewrites (the other ", so" instances may stay):
- S1 sub-block line: "Leadership, analysts and field teams read from the same governed dataset. A revenue figure means the same thing in every meeting."
- S5 row 1, sentence 2: "Underneath, DAX measures calculate the KPIs finance reports on, such as year-over-year growth, running totals and year-to-date revenue. Every page then works from one agreed definition."
- S5 row 2, sentence 2: "Dashboards serve leadership and reports serve analysts. Both draw on the same data, which puts every part of the business in view from one place."
- FAQ A5, last sentence: "Where you need Arabic and English versions of the same report, both sit on one model and the numbers always match."
- FAQ A6, last sentence: "Outside the US and EU data boundaries, Copilot is off by default unless an admin allows cross-region processing. We make that call with you. [10]" (A6 at 89 words; do not exceed 90)
- FAQ A9, sentence 4: "Whatever the size, a working prototype arrives within two weeks, early enough for your feedback to shape the build."

7b. **Delete "actually"** in S5 row 1 ("the KPIs finance actually reports on"), S7 intro ("actually runs on") and S7 card 6 ("can actually deliver"). S5 row 1 is already handled by 7a.

7c. **Remove the internal repetition:**
- S8 item 04, sentence 2: "We also install and configure the on-premises data gateway, then test refresh for every source behind your firewall."
- FAQ A3, last sentence: "Once data is spread across five or more systems, a lakehouse is usually worth it: every report then reconciles to the same cleaned tables."
- FAQ A4, sentence 3: "Power Automate can email whoever owns a figure the moment it moves outside its agreed range."

**After the fixes, re-confirm in the Flags section:** section totals (S6 must stay at 150 or more, S14 and S2 at 30 and 65 or less, FAQ answers at 90 or less); singular keyword count 6, plural 3, "consulting company" 2 and "solutions expert" 2 (the rewrites above preserve all of them); zero em dashes, en dashes and double hyphens; L2 and L4 anchors unchanged.

**Carry to Deliver (no Build action):** judgment calls (b) S16 heading and the form component, (g) "certified connectors" wording for Content Writer awareness, (h) footnote renumbering by appearance, the Gartner disclaimer, and the SugarAI reverse-link edit.

---

Sources consulted for verification:
- [Microsoft named a Leader in the 2026 Gartner Magic Quadrant for Analytics and BI Platforms (Microsoft Fabric Community)](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Microsoft-named-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for/ba-p/5262403)
- [Repost of the Microsoft announcement (mwpro.co.uk)](https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/)
- [Microsoft FY26 Q4 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- [The continued state of global AI diffusion in 2026 (Microsoft On the Issues)](https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/)
- [Copilot for Power BI overview (Microsoft Learn)](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction)
- [Fabric region availability (Microsoft Learn)](https://learn.microsoft.com/en-us/fabric/admin/region-availability)
- [Power BI Q&A retirement reminder: February 2027 (Microsoft Fabric Community)](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/power-bi-qa-retirement-reminder-february-2027-timeline-update/5365841)
- [Power BI pricing 2026 (costbench)](https://costbench.com/software/business-intelligence/power-bi/) and [Power BI licensing 2026 (Zebra BI)](https://zebrabi.com/power-bi-licensing/)
