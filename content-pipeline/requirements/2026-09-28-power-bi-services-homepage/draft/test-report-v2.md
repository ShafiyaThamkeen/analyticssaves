# Test report v2: Power BI Services homepage (draft-v2.md)

Tested by: Test agent, 2026-09-28
Loop: **2 of 3** (`test-report-v1.md` exists; this is the second report)
Inputs checked: `brief.md` (all sections; Section 10 treated as overriding), `draft/draft-v2.md` (including "Changes from v1"), `draft/test-report-v1.md`, `inputs/extracted/hlb-data-viz-v4 (1).html.md`, `inputs/extracted/HLB_HAMT_Data_Viz_Content_Documentation (1).docx.md`, `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`. For exact source wording I also re-read the Tab 3 section (lines 644-1076) of `inputs/content-source/data-viz-documentation-extracted.md`.
Method: no shell was available. Every section was re-counted word by word under the brief Section 1 rule. Character, keyword and phrase checks used ripgrep across the whole file. I then excluded the non-page lines (meta, "Changes from v1", chrome, Sources, Stats used, Flags).

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density | **PASS** |
| 2 | Word count | **PASS** |
| 3 | Zero em dashes | **PASS** |
| 4 | Grammar, spelling, punctuation | **FAIL** (G1-G4 fixed; 1 new error introduced in FAQ A4, plus 1 minor clarity point) |
| 5 | Originality | **FAIL** (5a-5g and 5i now pass; 5h still mirrors SugarAI; 6 source echoes found on the fresh full read) |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI heuristics | **FAIL** (the ", so" tic is fixed and "actually" is gone; 2 new internal repeats found; the consequence-clause tail has moved into S7) |
| 8 | Section structure and internal links | **PASS** |
| 9 | Client requirements and the 7 accuracy corrections | **PASS** |

**Overall: FAIL (loop 2 of 3).** The loop-1 fixes landed. Keywords, stats, links, structure, accuracy corrections and every zero-slack budget still hold. The remaining failures are all sentence-level, and each one comes with counted replacement text below. **Several of the new problems come from wording I suggested in test-report-v1** (5h, the FAQ A4 grammar slip, and the S7 card 1 and card 3 endings). I have flagged these plainly and not passed them just because they were my own suggestions.

---

## 1. Keyword placement and density: PASS

On-page copy only (eyebrows, buttons, anchor nav, breadcrumb, meta, Sources, Stats used and Flags excluded).

- **"Power BI service" singular (`\bPower BI service\b(?!s)`): 6** (target 5-7, max 8). Line 50 H1; line 52 hero lede; line 102 S4 card 1; line 134 S5 row 2 H3; line 412 FAQ Q1; line 413 FAQ A1 (once). Unchanged from v1.
- **"Power BI Services" plural (`\bPower BI services\b`): 3** (target 2-3). Line 243 S8 H2; line 364 S12 H2; line 443 S16 body. No section contains both forms.
- **Meta title and description:** identical to brief Section 7. The primary keyword leads both. It also appears in the H1 and in the first 100 words (H1 plus lede sentence 1).
- **"Power BI consulting company": 2** (S4 lede line 99; S12 intro line 366). **"Power BI solutions expert": 2** (S11 Extend line 347; S14 body line 402). **"Certified Power BI Partner in UAE": 0**, correctly not placed per Section 10 point 1. S12 tile 1 reads "Microsoft Power BI partner in the UAE".
- **Stuffing:** "Power BI" on-page is **40** (cap 75). "UAE" on-page is **10** (cap 12): lines 50, 69 x2, 111, 181, 209, 364, 368, 410, 427. S8 offering titles containing "Power BI": 0 of 6. PoC step titles containing "Power BI": 0 of 5.
- "Certified" appears 3 times, all about connectors (lines 146, 148, 257). This is unchanged and already carried to Deliver as judgment call (g).

## 2. Word count: PASS

Independent recount, by section:

| Section | My count | Build's figure | Budget (3b) | Status |
|---|---|---|---|---|
| S1 | 182 | 182 | 150-190 | OK |
| S2 + S2b | 65 | 65 | 45-65 | OK (at cap) |
| S4 | 258 | 258 | 250-300 | OK |
| S5 | 394 | 394 | 380-440 | OK |
| S6 | 150 | 150 | 150-190 | OK (at floor) |
| S7 | 365 (370 with pill label) | 366 | 330-400 | OK |
| S8 | 355 | 355 | 330-390 | OK |
| S9 | 23 | 23 | 20-30 | OK |
| S10 | 157 | 157 | 150-190 | OK |
| S11 | 385 | 385 | 360-420 | OK |
| S12 | 147 | 147 | 140-180 | OK |
| S13 | 34 | 34 | 30-45 | OK |
| S14 | 29 | 29 | 20-30 | OK |
| S15 | 813 | 814 | 700-850 | OK |
| S16 | 28 | 28 | 20-30 | OK |
| **Total** | **3,385** (about 3,418 with structural labels) | 3,387 / ~3,420 | 3,100-3,500 (fail <2,900 or >3,750) | **PASS** |

**Zero-slack checks:** S6 is exactly **150** (point 3 is still 24 words). S2 is **65**. S14 is **29**. FAQ A6 is **89**. All hold.

**Sub-unit checks:** S7 backs are 45 / 45 / 43 / 42 / 36 / 37. S8 items are 50 / 51 / 46 / 45 / 48 / 46. S10 steps are 21 / 18 / 17 / 18 / 20. S12 tiles are 14 / 16 / 18 / 18 / 16 / 18. FAQ answers are 79 / 78 / 80 / 77 / 74 / 89 / 83 / 78 / 71. All are inside their ranges.

**Sub-budget note (not a failure; the section total is the binding budget):** S5 row 2's description is **46** words against a 35-45 sub-range. My own 7a text in v1 caused this, and it can stay.

**Bookkeeping discrepancies in Build's Flags (not failures):** FAQ A9 is 71 words, not "about 80". The S7 card 3 back is 43, not 44.

## 3. Zero em dashes: PASS

Whole-file ripgrep: `—` **0**, `--` **0**, `–` **0**.

## 4. Grammar, spelling, punctuation: FAIL

**The loop-1 errors are all fixed:**
- **G1:** line 260 now reads "another BI tool such as Tableau or Qlik,". Fixed.
- **G2:** line 263 is split into two sentences, and "Documentation and ongoing support keep..." agrees. Fixed.
- **G3:** "plan data" is gone from S14 (line 402). Fixed.
- **G4:** line 190 now reads "Data alerts, extended through [...], email the owner...". The plural subject agrees with its plural verb, and the anchor is no longer the subject. Fixed.

**Spelling:** British spelling is clean. There are no -ize/-yze forms and no "color", "center", "behavior" or "program". "Sized", "right-sizing" and "size" are correct.

**New errors:**

| # | Location | As written | Problem | Fix |
|---|---|---|---|---|
| G5 | FAQ A4, sentence 4 (line 422) | "For clients in the Emirates, the result has been hours returned every week that once went on building reports by hand." | Misplaced relative clause. "that once went on..." attaches to "week", not "hours", so the sentence literally says a week went on building reports. (This was my own 5i wording in v1.) | See fix 4a. |
| G6 | S7 intro, sentence 2 (line 198) | "We shape the model, measures and page layout around those decisions instead of..." | "Those decisions" has no antecedent in the paragraph. The only "decisions" is in the H2, and the sentence before it talks about KPIs. Minor clarity point. | See fix 4b. |

## 5. Originality: FAIL

### 5a. Re-check of the 9 loop-1 violations

| # | v2 text | Verdict |
|---|---|---|
| 5a S7 card 1 | "Every entity rolls up into one group P&L... from AED and SAR to USD and EUR. Chartered accountants design the intercompany eliminations, currency translation and IFRS segment views..." | **Pass.** New subject and verb frame, and the currency order has changed. The three-item consolidation list survives only as factual scope. (The sentence ending is a tone issue; see 7c.) |
| 5b S7 card 2 | "Taxable income, IAS 12 deferred tax, transfer pricing and VAT return figures sit on one page, with free zone results kept apart from mainland ones." | **Pass.** The source's "We build dashboards tracking..." frame is gone, and the list is reordered. |
| 5c S7 card 3 | "Follow each unit from first expression of interest to signed deal, with lead conversion, live availability..." | **Pass against the source.** The list tail keeps the source order, but it is factual scope, the same standard applied to S10 step 1. However, sentence 2 now echoes the **SugarAI** Logistics card (see 5m). |
| 5d S10 step 2 | "Your raw extracts are loaded, cleaned and reshaped until they can be trusted, then modelled for fast reporting." | **Pass.** Load, clean and reshape is the generic ETL sequence. The source's distinctive "analytics-ready datasets" and "optimized data models for Power BI consumption" are gone. |
| 5e S10 step 4 | "Our developers build the interactive pages exactly as signed off, on top of the models from step two." | **Pass.** |
| 5f S10 step 5 | "Users get hands-on training and give feedback, one revision round follows, and the finished app goes live in your tenant." | **Pass.** The step order is brief-mandated. The subject, voice and clause structure are all new. |
| 5g S14 body | "Share your reporting wish list, and a Power BI solutions expert will map it to sources, licences and phases, free of charge." | **Pass.** The three scoping items are brief-prescribed. SugarAI's "We scope the... around your team with a free consultation" frame is gone. |
| **5h S12 tile 4** | "SugarAI CRM's deal predictions and Power BI's financial reporting side by side, with one team accountable for both." | **Still fails.** SugarAI's tile reads "SugarAI prediction plus Power BI analytics, from one partner." The v2 text keeps the same four units in the same order, only swapped for synonyms and padded: SugarAI prediction(s), then plus/side by side, then Power BI analytics/reporting, then one partner/one team. That is the same test v1 failed on. **This was my suggested text, and it did not go far enough.** It also adds "side by side", which already appears in the S7 card 3 tagline (line 214). |
| 5i FAQ A4 | "For clients in the Emirates, the result has been hours returned every week..." | **Pass on originality.** The source's "We've helped UAE businesses eliminate hours..." frame is gone. It fails on grammar instead (G5). |

### 5b. Did the rewrites create new echoes?

- **Of each other:** see item 7 (the S7 cards 1 and 3 endings, and the "Every page then... / every report then..." parallel).
- **Of SugarAI:** yes, one.

| # | Draft | Match | Assessment |
|---|---|---|---|
| **5m** | S7 card 3, sentence 2 (line 215): "CRM and ERP data meet in a lakehouse first, giving sales, finance and operations the same figures." | SugarAI Logistics card: "...so sales and operations work from the same picture." | Same closing unit: sales + operations + "the same [picture/figures]". Both pages will sit on hlbhamt.com. (v1 had an even closer "so sales, finance and operations report from the same figures", which I missed in loop 1.) |

### 5c. New findings from the fresh full read (content source)

The standard is the same as in loop 1. Lists of facts (sector names, systems, schedules, service line items) in the source order are acceptable. A sentence that keeps the source's **verb frame** with synonyms swapped in is a violation.

| # | Draft (location) | Source (docx Tab 3 / HTML Tab 3) | Assessment |
|---|---|---|---|
| **5j** | S8 item 01, sentence 1 (line 248): "We assess your current data systems and how ready the organisation is for business intelligence, then design an architecture that can grow with your strategy." | Portfolio 1: "Our consultants assess your existing data systems and BI readiness to design a scalable architecture that aligns with your strategic objectives." | Clause-for-clause synonym swap: existing/current, BI readiness/how ready for BI, scalable/can grow, strategic objectives/strategy. |
| 5j (cont.) | S8 item 02, sentence 2 (line 251): "We prepare and integrate sources, build data marts and warehouse layers, and..." | Portfolio 2: "We help prepare, integrate, and manage your data, including data mart creation and warehousing..." | The first half keeps the "We [help] prepare, integrate..." frame. Borderline, but it sits in the same list as 01 and costs nothing to fix. |
| **5k** | S9 body (line 269): "A live walkthrough using sample data or your datasets, with no obligation attached." | Engagement model 1: "Let us walk you through Power BI capabilities using sample data or your own custom datasets. No obligation." | Walk through, then "using sample data or your ... datasets", then no obligation. Same sequence, lightly reworded. The same level of closeness failed as 5i in v1. |
| **5l** | S11 PowerUP! story, sentence 2 (line 310): "For one fixed fee, we make that data accessible, put the KPIs that matter on screen and guide your people through the result, aiming for quick wins against clear objectives." | Tagline: "Access your data, visualize your key performance indicators, and receive expert guidance to achieve your objectives, all through a fixed-price engagement." Story: "...demonstrate quick wins against clear objectives..." | The tagline's three clauses map one to one (access data, visualise KPIs, guidance, fixed price), and the sentence ends in a distinctive **5-word verbatim run**. v1 rated only the 5-word run, as advisory. Read as a whole sentence, it meets the violation standard. I am upgrading it and saying so openly. |
| **5n** | FAQ A6, sentence 3 (line 428): "...and we configure environments in line with PDPL, DIFC and ADGM requirements..." | FAQ (data safety): "We configure environments to meet UAE PDPL, DIFC, and ADGM regulations." | Verbatim verb frame "we configure environments", the same list and a synonym for the object. (The brief's wording was the passive "environments configured in line with"; the active form re-matches the source.) |
| **5o** | S5 row 4, sentence 2 (line 157): "Power BI Embedded goes further, placing branded dashboards inside web apps, investor portals or client platforms..." | FAQ (embedding): "Power BI Embedded lets you put interactive dashboards inside your own web apps, investor portals, or client platforms, fully branded." | First 12 words keep the subject, verb frame ("put/placing... dashboards inside"), the same 3-item list in the same order, and "branded". |

**Advisory only (not scored):**
- S6 lede "move a team from asking what happened to deciding what to do next" echoes source FAQ 16 ("move from what happened to what should we do next"). The brief quotes this idea and it is a common descriptive-to-prescriptive framing, so I accept it.
- S8 item 06 and S4 card 4 carry source fact lists (training tracks, delivery modes, "UAE-based team... Monday to Friday"). These are acceptable as factual scope.
- S8 intro "Take one on its own or combine several, with..." is still loosely like SugarAI's "Choose one or combine them based on your needs, with...". This is carried from v1 and remains advisory.

**Web check: clean.** I searched distinctive v2 phrases: "Every entity rolls up into one group P&L", "Chartered accountants design the intercompany eliminations" and "loaded, cleaned and reshaped until they can be trusted". None has an exact or near match online. The source strings behind 5j and 5k ("assess your existing data systems and BI readiness to design a scalable architecture"; "walk you through Power BI capabilities using sample data or your own custom datasets") are not published on the web either. The risk is duplication against HLB HAMT's own prepared content and any future sibling page built from it, not against third parties.

## 6. Stat accuracy: PASS

Stat wording, placement and footnotes are unchanged from v1 and verified again:

| Ref | On-page wording | Placement | Check |
|---|---|---|---|
| [1] 200+ | "Data connectors in Power BI, from ERP and CRM to cloud databases." | S2 item 1 only | Worded as Power BI's library. Microsoft Learn source. Unchanged. |
| [2] 33x | "Faster report load times in one recent HLB HAMT engagement." | S2 item 2 only | Mandatory qualifier present. Approved per Section 10 point 4. |
| [3] Gartner | "Microsoft: named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." | S2b only | **Re-confirmed by search:** MQ published 29 June 2026; Microsoft named a Leader for the 19th consecutive year (Fabric Community post; mwpro.co.uk repost). No "#1", "ranked" or "14+" on-page. The disclaimer is in Sources item 3. |
| [4] Fabric | "Microsoft reports more than 40,000 paid Fabric customers, up more than 60% year on year." | S5 platform only | **Re-confirmed by search:** Microsoft FY26 Q4 earnings call, "over 40,000 paid Fabric customers, up more than 60% year-over-year". |
| [5] AI diffusion | "in Q2 2026, 73.3% of the UAE's working-age population used generative AI tools, against 18.8% worldwide." | S6 lede only | **Re-confirmed by search:** Microsoft On the Issues, 21 Sep 2026 (UAE 73.3%, world 18.8%, ages 15-64). Framed as generative AI use, not BI use. |
| [6] 7 days | S10 H2 | S10 only | "7 days" appears nowhere else on-page. |
| [7]-[11] F1-F5 | Desktop vs service; US$14/US$24 "at the time of writing"; UAE North/Central; Copilot F2/P1, English-only prompts, off by default outside the US/EU boundary; ISO/IEC 27001 and SOC 2 "within the scope of" | as in v1 | Unchanged text. Verified by direct fetch in v1. |
| CS facts | $4,500 PowerUP!, 5 terms, 6 deliverables; FAQ 9 timelines (2-4 wks, 6-10 wks, 3-6 months, prototype within two weeks) | S11; FAQ 9 | Match the source. Approved per Section 10 point 4. |

- No FAQ restates 200+, 33x, 19th, 40,000, 73.3% or 7 days.
- None of these figures appears on any other page under `content-pipeline/`.
- No new stat was introduced in v2.
- Stats used row [7] still quotes the S5 row 2 sentence correctly.

## 7. Human tone / AI-detection heuristics: FAIL

**Loop-1 items confirmed:**
- **", so [benefit]": 15 down to 5.** All six instances listed in v1 7a were rewritten: S1 sub-block (line 58), S5 row 1 (124), S5 row 2 (135), FAQ A5 (425), A6 (428) and A9 (437). The four that v1's other fixes removed are also gone: S7 cards 1 and 3, S8 item 04 and FAQ A4. The 5 left are S1 lede, S4 lede, S12 tile 6, FAQ A2 and FAQ A8, all from the "may stay" set. No two are in adjacent cards.
- **"actually": 0** on-page. The only hit in the file is Build's changelog.
- **Stock AI phrases:** none. "Unlock" appears only inside the L4 URL.
- **v1 internal repeats:**
  - **Gateway:** resolved. S5 row 3 covers refresh without moving the source. S8 item 04 covers install, configure and test.
  - **Source of truth:** resolved at wording level. S5 platform says "one source of truth". FAQ A3 now says "reconciles to the same cleaned tables". The brief assigns the idea to both places.
  - **KPI threshold alerts, S6 vs FAQ A4:** resolved at wording level ("crosses its threshold" vs "moves outside its agreed range"). **However, a third alert sentence, S1 card 3, duplicates S6.** See 7a.

**New failures:**

**7a. S1 card 3 repeats two other sentences almost word for word (pre-existing; missed in loop 1).**
- S1 card 3 (line 67): "The same **reports on iOS and Android, with data alerts when a figure crosses the line you set**."
- S5 row 4 (line 157): "Power BI Mobile puts **reports on iOS and Android, with alerts**, annotation and sharing..."
- S6 point 3 (line 190): "**Data alerts**, extended through [...], email the owner **when a KPI crosses its threshold**."
- One card shares a 7-word run with S5 and a "data alerts when a [figure/KPI] crosses [its threshold/the line you set]" frame with S6.

**7b. Microsoft Fabric is defined twice in the same frame (pre-existing).**
- S5 platform (line 168): "Fabric **brings Power BI together with data engineering, warehousing and real-time analytics on one platform**."
- FAQ A7 (line 431): "Fabric is Microsoft's unified analytics platform. It **puts Power BI alongside data engineering, data warehousing and real-time analytics, under one** capacity-based bill."
- The brief requires the definition in both places, but the frame is identical: Fabric + verb + Power BI + with/alongside + the same list + "on/under one...". A7 also echoes the source ("Fabric is Microsoft's next-gen unified platform... all under one roof with simplified billing"). v1 rated that echo advisory. The internal duplicate makes it a failure.

**7c. The consequence tail moved into S7. My v1 suggestions caused this.** Cards 1, 2 and 3 all end on a benefit consequence, two of them with the same clause-tail shape that the ", so" fix was meant to break:
- card 1: "..., **which is why** the logic survives audit."
- card 2: "Because..., the dashboards are built audit-ready from the start."
- card 3: "..., **giving** sales, finance and operations the same figures."

Cards 1 and 2 also both end on audit. Page-wide, the replacement connectors are ", which is why/what" (x3: S7 card 1, S11 story, A8), ", giving" (x2: S5 platform, S7 card 3) and ", which puts" (x1: S5 row 2). That is acceptable spread across a 3,400-word page. The problem is the S7 cluster.

**Advisory (not scored):**
- "Every page **then** works from one agreed definition." (S5 row 1) and "every report **then** reconciles to the same cleaned tables." (FAQ A3) share a skeleton. Both came from my v1 text. Optional change for A3: "...a lakehouse is usually worth it, because every report reconciles to the same cleaned tables."
- "which is what" appears twice: S11 "Scope is capped, which is what keeps the price fixed." and A8 "...tested measures, which is what makes Copilot's answers reliable." Optional change for A8: "...descriptions and tested measures; that groundwork makes Copilot's answers reliable." (-1 word)
- The sub-block line and card 1 both use "meeting" ("in every meeting" / "the first meeting of the day"). This is acceptable.

## 8. Section structure and internal links: PASS

- All sections are present in the mandated order: S0 breadcrumb, S1 (one H1, lede, sub-block, 3 H3 cards, deployment line), S2 (4 strip items, no headings) plus S2b, S3 anchor nav (8 labels in DOM order, matching the brief), S4 (H2 + 4 H3), S5 (H2, intro, 4 rows each with label, H3, description and exactly 5 brief bullets, platform layer with 4 bullets), S6 (H2 + 3 H3), S7 (H2, intro, 6 flip cards, 10-pill row), S8 (H2 "Our Power BI Services", 01-06), S9, S10 (highlighted band, H2 with "7 Days" [6], 5 H3 steps), S11 (featured PowerUP! card with all 5 terms and 6 deliverables, 4 tabs), S12 (brief H2, 6 tiles), S13 (static-asset version), S14, S15 (H2 + 9 H3 questions in brief order), S16, S17.
- **L1** "digital transformation and analytics services" → /services/digital-transformation-uae/ (S4 lede, line 99). Correct.
- **L2** "SugarAI CRM" → /sugarai-crm-2/ (S12 tile 4, line 378). The anchor is exactly "SugarAI CRM", with the possessive outside the link. Correct.
- **L3** "UAE Corporate Tax advisory" → /services/corporate-tax-advisory-services-in-uae/ (S7 card 2, line 209). Correct.
- **L4** "Power BI automation with Power Automate" → /insights/unlocking-power-bi-automation-with-power-automate/ (S6 point 3, line 190). The anchor is exact. Correct.
- **L5** "data protection advisory" → /services/data-privacy-and-security-uae/ (FAQ A6, line 428). Correct.
- **P1** `[data visualisation services](PLACEHOLDER:/services/data-visualisation-services/)` in S8 item 03 (line 254). **P2** `[advanced analytics services](PLACEHOLDER:/services/advanced-analytics-services/)` in the S6 lede (line 181). Correct format and placement.
- In-page links: "proof of concept" → #methodology (S4 card 3); "above" → #methodology (S11 Explore).
- The Microsoft product page is not linked.

## 9. Transcript and client requirement accuracy: PASS

No transcript was supplied. Section 10 decisions 1-6 are all still met: no "certified" partner claim; HLB breadcrumb chain; URL-agnostic; 33x qualifier, $4,500 USD and the "Limited offer" badge; static S13 asset; /sugarai-crm-2/.

**The 7 accuracy corrections, checked by whole-file search:**
- **Gartner wording:** "Gartner" appears on-page only in S2b (line 89). "#1", "ranked" and "14+" appear only in Build's Flags.
- **No Arabic Copilot claim:** A8 says "Microsoft officially supports English prompts only at present". Every "Arabic" mention is about report design or training.
- **Mobile is iOS and Android only:** the only "Windows" on-page is FAQ A1's "free Windows application" for Desktop, which is correct.
- **Q&A is not featured:** there is no "Q&A" on-page.
- **Tableau and Qlik:** named only in S8 item 05, as migration sources, with no price comparison.
- **"Salesforce (60+ modules)":** dropped. Salesforce appears only as a data source (S5 row 3, FAQ A3).
- **Connector caveat:** kept ("Native, certified and custom connectors cover systems such as..."; "Microsoft's own connectors, partner-built connectors and custom builds cover sources such as...").

None of the fixes below touches a correction. **Constraint for fix 5k:** the replacement must not describe the demo as asking questions of the data in natural language, because that reads like the retired Q&A feature. The suggested text keeps a consultant "driving" the dashboards.

---

## Overall: FAIL (loop 2 of 3)

Items 4, 5 and 7 fail. Items 1, 2, 3, 6, 8 and 9 pass. **One loop remains.** Apply the fixes below exactly, or with your own wording that meets the stated constraint. **Do not change anything else.** Every replacement has been counted, and the projected budgets are at the end.

## Fix instructions (for Build, draft-v3)

**Item 4, grammar**

4a. **FAQ A4, sentence 4** (line 422). Replace "For clients in the Emirates, the result has been hours returned every week that once went on building reports by hand." with:
"For clients in the Emirates, that Monday routine used to cost hours; now it largely runs itself." (17 words; A4 goes from 77 to 73)
Constraint: keep the claim qualitative, with no number, and do not reintroduce the source's "eliminate hours of weekly manual reporting" frame. Then update Flags item 9's quote to match.

4b. **S7 intro, sentence 2** (line 198). Replace "around those decisions instead of adapting a generic template." with "around the decisions those KPIs support, instead of adapting a generic template." (+3; S7 intro is 32 words, inside 25-35)

**Item 5, originality** (keep every fact, keyword and link; change the sentence frame)

5h. **S12 tile 4 body** (line 378). Replace with:
"Power BI shows where revenue landed; [SugarAI CRM](https://hlbhamt.com/sugarai-crm-2/) scores the pipeline still to come. One team supports both." (18 words, unchanged; the L2 anchor is still exactly "SugarAI CRM")
Constraints:
- No "prediction(s) + plus/alongside/side by side + analytics/reporting + one partner/team" sequence.
- No "side by side", which the S7 card 3 tagline already uses.
- Do not use "forecasts which deals close", which echoes SugarAI's "Built-in forecasting predicts which deals are most likely to close".

5j. **S8 item 01, sentence 1** (line 248). Replace with:
"Workshops map the systems you already run, test how ready your people and data are for self-service reporting, and sketch an architecture that fits your plans for growth." (28 words, +3; item 01 body goes to 53)

**S8 item 02, sentence 2** (line 251). Replace "We prepare and integrate sources, build data marts and warehouse layers, and automate loads with Azure Data Factory pipelines." with:
"We bring sources together, stand up data marts and warehouse layers, and automate loads with Azure Data Factory pipelines." (19 words, unchanged)

5k. **S9 body** (line 269). Replace with:
"Pick sample figures or send an extract of your own; a consultant drives the dashboards while you ask questions." (19 words; S9 goes from 23 to 29, max 30)
The H2 "...Before You Commit" already carries the no-obligation point. If you would rather keep "no obligation" in the body, S9 must stay at 30 or less.
Constraints:
- Must not follow the source's "walk you through... using sample data or your own... datasets. No obligation." sequence.
- Must not mirror S11's Live demo line ("A consultant-led session exploring dashboards built on sample data or extracts you share").

5l. **S11 PowerUP! story, sentence 2** (line 310). Replace with:
"For one fixed fee, we get that data into shape, chart the measures your stakeholders keep asking about and coach your team until early results show against the goals you set." (31 words, +1)
Constraints:
- Remove "quick wins against clear objectives".
- Do not keep the access / visualise / guide sequence as three synonym-swapped verbs.
- Keep the brief's content (data access, KPIs, expert guidance, fixed price).

5m. **S7 card 3, sentence 2** (line 215). Replace "CRM and ERP data meet in a lakehouse first, giving sales, finance and operations the same figures." with:
"Behind it, a lakehouse joins CRM and ERP records before any figure reaches a sales or finance meeting." (18 words, +1; the back goes to 44)
This also resolves 7c for card 3.

5n. **FAQ A6, sentence 3** (line 428). Replace "and we configure environments in line with PDPL, DIFC and ADGM requirements, working with our [data protection advisory](...) team." with:
"and our [data protection advisory](https://hlbhamt.com/services/data-privacy-and-security-uae/) team helps set each environment up in line with PDPL, DIFC and ADGM requirements." (19 words, unchanged; **A6 stays at 89, and do not exceed 90**; the L5 anchor stays exact; keep "in line with", never "guarantees compliance")

5o. **S5 row 4, sentence 2** (line 157). Replace with:
"Power BI Embedded goes further: investor portals, client platforms and your web apps can carry branded dashboards on capacity-based licensing, without the expense of building reporting from scratch." (28 words, +1; the row 4 description goes to 45)

**Item 7, tone**

7a. **S1 card 3 body** (line 67). Replace with:
"A regional manager reviews yesterday's figures and any alerts on iOS or Android between site visits." (16 words, -2; card 16 is inside 12-18; S1 goes to 180)
This keeps iOS/Android and alerts as the brief requires, and **no Windows**. Do not reuse "reports on iOS and Android, with alerts" (S5 row 4) or "crosses the line/threshold" (S6).

7b. **FAQ A7, sentences 1-2** (line 431). Replace "Fabric is Microsoft's unified analytics platform. It puts Power BI alongside data engineering, data warehousing and real-time analytics, under one capacity-based bill." with:
"Fabric is Microsoft's single capacity-based service for data engineering, warehousing, real-time analytics and Power BI reporting, built around one shared data lake called OneLake." (24 words, +2; A7 goes to 85)
Leave the S5 platform sentence as it is.

7c. **S7 card 1, sentence 2** (line 203). Replace "Chartered accountants design the intercompany eliminations, currency translation and IFRS segment views, which is why the logic survives audit." with:
"The intercompany eliminations, currency translation and IFRS segment views are designed by chartered accountants and hold up under audit." (19 words, unchanged)
Card 3 is covered by 5m.

**Projected budgets after all fixes** (from my recount):

| Section | Now | After fixes | Budget |
|---|---|---|---|
| S1 | 182 | 180 | 150-190 |
| S5 | 394 | 395 | 380-440 |
| S6 | 150 | 150 (untouched) | ≥150 |
| S7 | 365 | 369 | 330-400 |
| S8 | 355 | 358 | 330-390 |
| S9 | 23 | 29 | ≤30 |
| S11 | 385 | 386 | 360-420 |
| S12 | 147 | 147 | 140-180 |
| S14 | 29 | 29 (untouched) | ≤30 |
| S15 | 813 | 811 (A4 73, A6 89, A7 85) | 700-850; answers ≤90 |
| **Total** | **3,385** | **about 3,395** | 3,100-3,500 |

S2 (65) is untouched.

**Re-confirm after editing:**
- Singular "Power BI service" 6 and plural 3. No fix touches any instance.
- "Power BI" on-page about 40.
- "UAE" 10.
- Em dashes, en dashes and double hyphens all 0.
- L2 anchor exactly "SugarAI CRM" and L5 anchor exactly "data protection advisory".
- Update Stats used / Flags only where a quoted sentence changed (Flags item 9 for A4, and the S12 tile 4 "deal predictions" note in Flags item 9).

**Carry to Deliver (no Build action, unchanged):**
- judgment call (b), the S16 heading and form component
- judgment call (g), "certified connectors"
- judgment call (h), footnote renumbering
- the Gartner disclaimer
- the SugarAI reverse-link edit
- open item: final URL and handling of the overlapping pages

---

Sources consulted for verification:
- [Microsoft FY26 Q4 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) and [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/)
- [Microsoft named a Leader in the 2026 Gartner Magic Quadrant (Microsoft Fabric Community)](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Microsoft-named-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for/ba-p/5262403) and [mwpro.co.uk repost](https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/)
- [The continued state of global AI diffusion in 2026 (Microsoft On the Issues)](https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/)
- Loop-1 direct fetches (unchanged text): [Copilot for Power BI overview](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction), [Fabric region availability](https://learn.microsoft.com/en-us/fabric/admin/region-availability)
