# Test report v2: Data Visualisation Services homepage (draft-v2.md, loop 2 of 3)

Tested by: Test agent, 2026-09-30
Loop: **2 of 3** (`test-report-v1.md` exists; one more loop would be available if needed).

---

## Summary

| # | Item | Result |
|---|---|---|
| 0 | Loop-1 fixes (5a-5f, 7) applied exactly | **PASS** (all 7 verbatim; G1 optional also applied; no other page line changed) |
| 1 | Keyword placement and density; branding B1-B5; T1-T6 | **PASS** |
| 2 | Word count | **PASS** (3,017) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** (advisories only) |
| 5 | Originality (5 competitors + Softcrylic, Tab 1, SugarAI sample, PB v8, AA v5, web) | **PASS** |
| 6 | Stat accuracy and footnoting | **PASS** (all 4 re-verified today) |
| 7 | Human tone / AI-detection heuristics | **PASS** (Flag 17 run ruled acceptable; advisories only) |
| 8 | Section structure, CTAs, FAQ, internal links, flow | **PASS** |
| 9 | Client requirements (Section 10) and no fabricated commitments | **PASS** (L2 go-live condition carried) |

**Overall: PASS.** Details and evidence follow.

---

## Critical re-checks (requested): still clean

Whole-file ripgrep of `draft-v2.md`, notes included, then page lines isolated.

| Check | Pattern | Page count |
|---|---|---|
| 33x | `(?i)33\s?x`, "thirty-three" | **0** |
| PowerUP | `(?i)power\s?up` | **0** |
| $4,500 | `4,500`, `\$4` | **0** |
| Softcrylic | `(?i)softcrylic` | **0** |
| "pipeline, model and semantic layer" and variants | `(?i)semantic layers?`, `pipeline`, plus any line with pipeline + model + semantic | **0 as a phrase.** Remaining single words are brief-prescribed and separate: "modelled into a semantic layer" (S5 foundation, line 134), bullet "Source integration and pipelines" (136), "Automated pipelines pull from each source" (A5, 353). No line carries the triple or any reordering of it. S7 04 (216) contains none of "pipeline", "semantic" or "layer". |
| Other Softcrylic / T5 phrases | "in parallel", "next-gen", "dramatic", "comprehension", "data stor", "key to unlocking", "value reali", "strategic asset", "information silos", "control and clarity", "like never before", "story within", "Identify patterns", "data-to-action", "like capital", "table-stakes", "every data point", "60,000" | **0** |
| T3 tool names | case-sensitive whole-word sweep of the full T3 list plus SQL, Google, AWS, Amazon, Cognos, MicroStrategy, Grafana, Kibana, Alteryx, Power Query, DAX, Dynamics; case-insensitive sweep of microsoft, visio, tableau, qlik, looker, excel, azure, fabric, synapse, oracle, sap, salesforce, snowflake, databricks, bigquery, copilot, sharepoint, d3, zoho, domo, sisense, metabase, superset, spotfire, quicksight, plotly, highcharts | **0.** The only case-insensitive hit is "visio" inside "Revision" (line 7, draft header), a false positive. |
| "Power BI" | | **3** (S11 tile 5 H3, line 308; FAQ A3 x2, line 347, one is the L2 anchor). Cap 4 total, 2 in FAQ 3: met. |
| "SugarAI CRM" | | **1** (S6 card 2, line 159, optional L5). |

Softcrylic was re-searched today. Its indexed copy now also shows a "Dashboard Performance Optimization Checklist" listing about 18 generic items ("data model, efficient queries, data calculations, ... semantic layer, load time ..."). The v2 S7 04 sentence names "the data refresh, the model or the calculations". That is three generic tuning loci, not a sentence or phrase from Softcrylic, and the brief prescribes the remedies ("aggregation tables, query reduction, efficient calculations"). The distinctive Softcrylic sentence ("Optimization at the pipeline, data model, and semantic layers yields dramatic performance increases") has no trace on the page.

---

## 0. Loop-1 fixes: all 7 applied verbatim

I compared every page line of v1 (lines 18-377) with v2. The only changed lines are 30, 85, 154, 159, 169, 179, 189, 216, 341, 344 and 350.

| Fix | Location (v2 line) | Required text (test-report-v1) | v2 | Match |
|---|---|---|---|---|
| 5a | S1 sub-block line (30) | "Each one rests on figures checked before publication." | Identical | Yes |
| 5b | S4 card 3 s3 (85) | "From there, the work runs through our [five-stage method](#methodology), which one core team carries from the opening KPI session to launch and beyond." | Identical; `#methodology` link kept | Yes |
| 5c | S7 04 s2 (216) | "Our engineers time each page, find whether the delay sits in the data refresh, the model or the calculations, and fix it there: aggregation tables, fewer queries per page, leaner formulas." | Identical. s1, s3 and the H3 unchanged. The Softcrylic/PB triple is gone (see critical re-checks). | Yes |
| 5d | FAQ A4 s3-s4 (350) | "Within the first two weeks, you normally have a working prototype on your own data to review. We commit to dates at the end of the dashboard review, when we have seen your reports, sources and KPIs first-hand." | Identical. s1-s2 unchanged. | Yes |
| 5e | FAQ A1 s1 (341) | "Data visualisation is the design of charts, dashboards and interactive reports that make a large body of figures readable in minutes and open to follow-up questions." | Identical. s2-s3 unchanged. | Yes |
| 5f | FAQ A2 s1 (344) | "Analytics is the investigative work of testing and modelling data to explain a result. Visualisation is the presentation layer that turns those findings into pages a manager can act on." | Identical. The remaining three sentences and the L3 link unchanged. | Yes |
| 7 | S6 backs 1, 2, 4, 8, s1 (154, 159, 169, 189) | "Our finance views track..." / "Behaviour, engagement, satisfaction, retention and lifetime value are set side by side in our customer views, with segments that tell account teams where to focus." / "Production reporting from our team tracks..." / "Order, stock and sales data feed our reporting on..." | All four identical. S6 intro and S5 row openers untouched, as instructed. | Yes |
| G1 (optional) | S6 card 6 s2 (179) | "...booking channels, then base pricing..." | Applied, word-neutral | Yes |

Every constraint attached to the fixes holds:
- "draw(s) on the same reconciled" = 0.
- "Every engagement then follows our" = 0.
- "Whatever the size", "In every case", "number and condition of your sources" and "so your feedback steers" = 0.
- "digging through", "hidden in" = 0.
- "visualisation is how" = 0, and "cleaning ... modelling" = 0.
- "decides how people see them" = 0.

---

## 1. Keyword placement and density: PASS

Scope and exclusions are the same as loop 1. Excluded: meta (1-2), the draft header (5, 7), chrome (11-16), structure headers, eyebrows (20, 72, 290), buttons (26, 230, 332), the asset note (324), the grid note (196) and everything from Sources (379) on.

| Keyword | Count | Placements (line) | Target | Result |
|---|---|---|---|---|
| Primary "data visualisation services in UAE" | **3** | H1 (22); hero lede s1 (24); S14 H2 (338) | 3-4 (hard max 5) | Pass |
| Forbidden "...services in the UAE" | **0** | | 0 | Pass |
| Secondary "data visualisation services" (lookahead applied) | **2** | S7 H2 (202); S11 H2 (292) | 2-3 | Pass |
| "data visualisation consulting services" | **2** | S7 intro s1 (204); S10 intro (263) | 2 (max 3) | Pass |
| "data visualisation experts in UAE" | **1** | S13 H2 (328) | 1-2 | Pass |
| "data visualisation technologies" | **1** | S5 intro s2 (96) | 1-2 | Pass |
| "data analytics and visualisation software" | **1** | FAQ Q3 (346) | 1-2, FAQ 3 only | Pass |

- **Meta** (1-2) still matches brief Section 7 exactly. The primary keyword is the first five words of both. The z spelling is correct for meta (Section 10 point 5a).
- **First 100 words:** the primary appears in the H1 and in lede sentence 1.
- **T1 "HLB HAMT": 11** (10-15). Lines 22, 24, 56, 76, 79, 202, 292, 320, 340, 341 and 344.
- **T2 "visualisation" (any form): 18** (cap 28). Lines 22, 24, 96, 202, 204, 263, 282, 292, 308, 328, 338, 340, 341, 343, 344, 346, 358 and 371. Fix 5f swapped one instance for another, so the count is unchanged.
- **T2 "dashboard(s)": 20** (the cap is **35**, and it is flagged only above 42). Lines 24, 28, 44, 52, 79, 212, 213, 215, 226, 267, 270, 275, 320, 341, 349, 350, 352, 355, 361 and 369. The +1 against v1 is A1 (Fix 5e), as predicted.
- **T4 "UAE": 7** (cap 10). Lines 22, 24, 66, 292, 328, 338 and 356.
- **T6:**
  - On-page "visualization" (z) = 0. The z form appears only at 1, 2 (meta), 15 (URL in chrome) and in notes.
  - "certified", "#1", "award-winning", "leading", "compliant", "guarantee", "zero", "always", "instantly" and "100%" = 0 on the page. "always" appears only in the Stats-used note (393).
  - Sibling figures (200+, 7 days / seven days, Since 1999, 25/26 years, 150+, 19th, 14+, 85%, 16%, 6.67, 11 services, 40,000) = 0.
- **2d:** 2 of 6 S7 titles contain "Dashboard" (03 and 04). 0 of 5 S9 titles do. 0 of 9 S6 titles contain "dashboard" or "visualisation".
- **B1-B5:**
  - B1 holds: the H1 opens "HLB HAMT:".
  - B2 openers are unchanged from v1 and all pass.
  - B3 holds in every FAQ answer, including the three edited ones: A1 s2 "HLB HAMT delivers", A2 s4 "HLB HAMT offers both: we design", A4 s4 "We commit to dates".
  - B5 attribution is unchanged (UAE / BARC respondents / Gartner-surveyed organisations).
- **Stuffing:** none. Every instance sits in its brief-assigned slot.

## 2. Word count: PASS (3,017)

Method (no shell):
- (a) A word-by-word audit of every edited sentence, old against new.
- (b) An independent full recount of S1 and S14.
- (c) Sub-budget recounts for every edited card.

**Delta audit (v1 baseline 2,998, from test-report-v1):**

| Fix | Old words | New words | Delta |
|---|---|---|---|
| 5a | 8 | 8 | 0 |
| 5b | 17 | 23 | +6 |
| 5c | 32 | 31 | -1 |
| 5d | 35 (17 + 18) | 38 (17 + 21) | +3 |
| 5e | 22 | 26 | +4 |
| 5f | 23 | 30 (14 + 16) | +7 |
| 7 card 1 | "We build finance views that track" 6 | "Our finance views track" 4 | -2 |
| 7 card 2 | 24 | 25 | +1 |
| 7 card 4 | "We design production reporting around" 5 | "Production reporting from our team tracks" 6 | +1 |
| 7 card 8 | "We connect order, stock and sales data to report" 9 | "Order, stock and sales data feed our reporting on" 9 | 0 |
| G1 | "and" | "then" | 0 |
| **Total** | | | **+19 → 3,017** |

**Independent recounts:**
- **S1 = 197.** H1 11, lede 50 (22 + 28), sub-block heading 8, sub-block line 8, cards 3+21 / 5+19 / 3+19 / 6+20, scope line 24.
- **S14 = 667.** H2 8, questions 90. The answers are:

  | A1 | A2 | A3 | A4 | A5 | A6 | A7 | A8 | A9 |
  |---|---|---|---|---|---|---|---|---|
  | 64 | 64 | 67 | 66 | 58 | 70 | 60 | 59 | 61 |

  That totals 569.
- Both recounts agree with Build's Flag 14 and with the delta audit.

**Sections:**

| Section | S1 | S2+S2b | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 | S14 | S15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Words | 197 | 67 | 254 | 343 | 465 | 404 | 28 | 160 | 202 | 146 | 33 | 29 | 667 | 22 |

Every section is inside its 3b budget. The total is **3,017** against 2,800-3,200 (the page fails only below 2,600 or above 3,400).

**Edited sub-budgets:**

| Item | Words | Budget |
|---|---|---|
| S4 card 3 | 50 | 40-50, at cap |
| S6 card 1 | 37 | 35-42 |
| S6 card 2 | 39 | 35-42 |
| S6 card 4 | 37 | 35-42 |
| S6 card 8 | 41 | 35-42 |
| S7 04 | 59 | 50-60 |
| A1 | 64 | 55-70 |
| A2 | 64 | 55-70 |
| A4 | 66 | 55-70 |

## 3. Zero em dashes: PASS

A whole-file ripgrep for `—` (U+2014), `–` (en dash) and `--` finds **0 / 0 / 0**.

## 4. Grammar, spelling, punctuation: PASS

- **British spelling sweep:** -ize/-ise, -yze, -ization, colo(u)r, center, behavior, modeling/modeled, fulfill(ment), program(s), catalog, toward, judgment, labeled, gray, mockup, license, analyze, optimiz-, organiz-, prioritiz-, utiliz- and standardiz- all return **0** on the page. The only hits were "size"/"sized", which are false positives, and z-spellings in meta and notes. The new sentences use "modelling", "Behaviour" and "first-hand", all British forms.
- **The v2 sentences parse correctly:**
  - The 5c verb series is "time ..., find ..., and fix ...", followed by a colon list.
  - The 5b object relative is "which one core team carries".
  - A4's "Within the first two weeks, you normally have..." is correct.
  - A2's two copular definitions are correct.
- **Advisories (not scored; word-neutral fixes in "Optional"):**
  - **G4 (new). S6 card 8 s1 (189): minor garden path.** In "Order, stock and sales data feed our reporting...", "sales data feed" can be read at first as the noun "data feed". Swapping "data" for "records" removes it.
  - **G3 (carried). S6 card 2 s2 (159): "we connect it directly".** After Fix 7 the nearest singular noun is "SugarAI CRM", so "it" now reads acceptably. Changing it to "the CRM" is still marginally clearer.
  - **G2 (carried). S4 lede s1 (76): the "that" clause attachment.** Unchanged from v1; optional.

## 5. Originality: PASS

### 5.1 Competitor pages (fetched again today) and Softcrylic

I re-fetched all five resolved pages and checked them against the v2 sentences (5a-5f and the Fix 7 openers). I also pulled each page's own sentences on the same topics: dashboard tuning, the definition of visualisation, analytics vs visualisation, timelines and prototypes, sector dashboards, and method and support.

- **instinctools.** No resemblance. Its tuning copy is "query optimization, caching strategies, and load testing"; its timeline is "prototypes in 1-2 weeks and production-ready MVPs in 4-6 weeks". A4 uses Tab 1's own "within the first two weeks" prototype fact, which the Content Writer confirmed (Section 10 point 5b). A4 uses no MVP figure.
- **Damco.** No resemblance. Its definitions are "converting data chaos into clear charts", "a process of storytelling" and "translating complex data into easy-to-understand formats". Its analytics-versus-visualisation line is "data mining finds the secrets, while data visualization shows them".
- **IT IDOL.** No sentence match. Its definition is "Data visualization is the graphical representation of data and information, enabling businesses to make sense of complex datasets through charts, graphs, and other visual tools." A1 s1 shares only the generic "Data visualisation is the ... of ... charts" definitional frame. A1 has a different head noun ("design") and list, and a different outcome ("readable in minutes and open to follow-up questions").
- **Aspire.** No relevant content found.
- **Mindbowser.** No resemblance ("transform their raw data into engaging and informative visuals").
- **Softcrylic.** Clean (see critical re-checks).

### 5.2 Sibling pages (PB draft-v8, AA draft-v5, both read in full today)

**The four loop-1 sibling failures are resolved:**

| Loop-1 finding | Sibling line | v2 text | Ruling |
|---|---|---|---|
| (a) S1 sub-block | AA 30 "Every model and every report we deliver draws on the same reconciled data." | "Each one rests on figures checked before publication." | No shared phrase. PB's sub-block (30) is also unrelated. Pass. |
| (b) S4 card 3 s3 | AA 80 "Every engagement then follows our [five-stage method]..., and each stage ends with something you can review." / PB 76 "Full implementations then move through five stages" | "From there, the work runs through our [five-stage method]..., which one core team carries from the opening KPI session to launch and beyond." | Only the brief-prescribed "five-stage method" link is shared. "runs through" / "move through five stages" is a common collocation, and the clauses around it differ. Pass. |
| (c) FAQ A4 s3-s4 | PB 373 "In every case you get a working prototype inside the first two weeks, so your feedback steers the rest of the build. HLB HAMT confirms the timeline after discovery, once we know the condition of your data and how many sources are involved." | "Within the first two weeks, you normally have a working prototype on your own data to review. We commit to dates at the end of the dashboard review, when we have seen your reports, sources and KPIs first-hand." | The facts (a two-week prototype; dates confirmed after the review) are brief-prescribed. The PB framings are gone: the absolute, "feedback steers", and "condition of your data / how many sources". Pass. |
| (d) S7 04 s2 | PB 208 "we tune across the pipeline, data model and semantic layers, cutting query load, adding aggregation tables ... replacing heavy measures"; PB A9 370 "We work through the pipeline, the model and the semantic layer" | "Our engineers time each page, find whether the delay sits in the data refresh, the model or the calculations, and fix it there: aggregation tables, fewer queries per page, leaner formulas." | The locus triple is gone. What remains shared is the brief-prescribed remedy set (brief S7 04: "aggregation tables, query reduction, efficient calculations"), written in different words and a different structure. Pass. |

**The other new v2 wording was checked against both siblings:**
- **5e A1 s1:** no sibling counterpart. AA A1 defines advanced analytics, not visualisation.
- **5f A2 s1-s2.**
  - Against **AA A1 (329)**: "Advanced analytics uses statistical modelling, machine learning and predictive techniques to explain the cause behind a result...". The shared idea is analytics explaining a result, which is the standard diagnostic-analytics definition. The frames differ ("uses [list] to explain the cause behind" against "is the investigative work of testing and modelling data to explain"), and so do the lists.
  - Against **AA A9 (353)**: "data visualisation decides how people see them". No shared wording.
  - Pass.
- **Fix 7 openers.** The comparison was PB card 5 (178), "CRM, e-commerce and campaign data meet in a 360-degree customer view, from which we report...", against DV card 8, "Order, stock and sales data feed our reporting on...", and DV card 2, "...set side by side in our customer views".
  - The shared part is a generic "[three data types] data [verb]" syntax and the common noun "customer view(s)".
  - The content, sector and clause structure all differ.
  - Pass.
- **Newly checked (missed in loop 1, recorded so it is not reopened):**
  - **S5 foundation s1 "We build this layer first." (134)** against **AA foundation s1 (128)**, "We build the layer every model depends on, and we build it first."
  - They sit in the same slot, and both briefs mandate the "We build..." opener (DV brief line 224: 'Open "We build..."').
  - The shared material beyond the mandated words is only the ordering idea "first". AA's distinctive part ("the layer every model depends on") is absent. DV's is a 5-word sentence, not a reworded one.
  - **Acceptable.** An optional word-neutral rewrite that also drops "first" is at Optional K.

### 5.3 Content source (Tab 1): the two loop-1 failures are resolved

| Loop-1 finding | Tab 1 | v2 | Ruling |
|---|---|---|---|
| (e) A1 s1 | "Data visualization transforms raw data into graphical formats (charts, dashboards, heatmaps, and interactive reports) making complex information instantly understandable. ... enabling teams to spot trends, anomalies, and opportunities that would remain hidden in spreadsheets or databases." | "Data visualisation is the design of charts, dashboards and interactive reports that make a large body of figures readable in minutes and open to follow-up questions." | The failing tail ("trends/anomalies ... hidden in spreadsheets") is gone. The core ("charts, dashboards, interactive reports that make complex data readable") is **brief-prescribed** (brief S14 FAQ 1). The remaining echo is "readable in minutes" against "instantly understandable". That is a two-word qualifier on the prescribed "readable", and it is the non-absolute form the brief asks for. Pass. |
| (f) A2 s1 | "Data analytics is the process of examining, cleaning, modelling, and interpreting data to extract insights. Data visualization is how those insights are communicated visually." | "Analytics is the investigative work of testing and modelling data to explain a result. Visualisation is the presentation layer that turns those findings into pages a manager can act on." | Both loop-1 discriminators are gone: the "cleaning ... modelling" sequence and the "visualisation is how" copula. The frame that remains ("X is the [noun] of [gerund(s)] data to [purpose]") is the textbook definition shape. Tab 1's own sentence is itself a paraphrase of the standard definition ("data analysis is the process of inspecting, cleansing, transforming, and modeling data...", found across the web in today's search). The content slots are not synonyms of Tab 1's. The two-sentence analytics-then-visualisation pairing is **brief-prescribed** ("Analytics examines and models data to produce insight; visualisation presents it so people act"). Pass. Optional M offers a variant that uses the brief's verb frame instead, if the Content Writer wants no copular definition at all. |

The other Tab 1 checks from loop 1 still stand, because those lines are unchanged. The Fix 7 openers use only the permitted metric lists and new framing. None uses Tab 1's "Transform financial data into...", "Derive meaningful customer insights...", "Drive operational excellence..." or "Streamline distribution operations..." openers.

### 5.4 SugarAI structural sample: clean

- I grepped the sample for every distinctive v2 fragment: "rests on", "checked before", "runs through", "core team", "and beyond", "side by side", "feed our", "from our team", "presentation layer", "investigative", "follow-up questions", "commit to", "first-hand", "time each page", "delay", "leaner" and "fewer queries".
- The one hit is "Your existing system stays readable for an agreed period after go-live", which is unrelated.
- The loop-1 rulings on structural labels stand.

### 5.5 Web: exact-phrase searches today, no matches

| Phrase searched | Result |
|---|---|
| "find whether the delay sits in" | No match (generic refresh-latency articles only) |
| "readable in minutes and open to follow-up questions" | No match |
| "Visualisation is the presentation layer that turns" | No match (generic layered-architecture articles) |
| "Analytics is the investigative work of testing and modelling data" | No match (generic analytics definitions) |
| "rests on figures checked before publication" | No match |
| "We commit to dates at the end of the dashboard review" | No match |
| "one core team carries from the opening" / "the work runs through our five-stage method" | No match |
| "Order, stock and sales data feed" | No match |
| "set side by side in our customer views" / "Production reporting from our team tracks" | No match |
| "Our engineers time each page" + "fewer queries per page" | No match (generic aggregation-table guides) |
| "We build this layer first" | No match (generic semantic-layer articles) |

## 6. Stat accuracy and footnoting: PASS

All four sources were re-checked today. The stat sentences are unchanged from v1.

| Ref | Figure | Location | Check today | Result |
|---|---|---|---|---|
| [1] | UAE 9th of 69, IMD WDCR 2025; 1st for talent | S2b only (66) | u.ae fetched: "ranked 9th amongst 69 countries reviewed globally", "1st in talent", updated 25 Nov 2025. The latest edition (2026 is due in Nov). Attributed to the UAE (B5). | Pass |
| [2] | 1,579 professionals; data quality management first, level with data security and privacy | S5 foundation only (134) | BARC fetched: 1,579; data quality management 7.9/10, tied with data security and privacy; 12 Nov 2025 (about 10 months old). | Pass |
| [3] | Only 22% defined, tracked and communicated business impact metrics for most D&A use cases | S9 intro only (238) | Search extract of the Gartner release (20 Feb 2025; 504 leaders, Sep-Nov 2024) plus BigDATAwire: "for the bulk of their D&A use cases". About 19 months old, inside the window. | Pass |
| [4] | UAE PDPL, Federal Decree-Law No. 45 of 2021 | FAQ 6 only (356) | u.ae fetched: "Federal Decree Law No. 45 of 2021 Regarding the Protection of Personal Data", in force 2 Jan 2022. "in line with", not "compliant". | Pass |
| CS1 | 9 sectors | S2 item 1 only (51) | Tab 1 cards 01-09; HLB HAMT's own content, no footnote | Pass |
| FAQ 4 | 2-4 wk / 6-10 wk / 3-6 mo / prototype in the first 2 wk | FAQ 4 only (350) | Tab 1 FAQ 4, confirmed in Section 10 point 5b. "normally" rather than any absolute; no "7 days". | Pass |

- The markers run in order of appearance ([1] S2b, [2] S5, [3] S9, [4] FAQ 6), and the Sources list matches.
- **Each stat appears once.** No FAQ restates 9 sectors, 9th of 69, BARC or 22%.
- **No cross-project duplication.** Ripgrep of every requirement folder for "1,579", "9th of 69", "Only 22%" and "Trend Monitor 2026" finds page use only here. The AA hits are test-report lines about a different PwC "22%" figure that is not used on the AA page.
- **No invented figures.** Competitor outcome numbers = 0.

## 7. Human tone / AI-detection heuristics: PASS

**Stock-phrase sweep (the same 50-term list as loop 1): 0 hits on the page.** There are two false or near positives:
- "whether you" matched "whether your people trust" (S11 intro, 294), which is not the stock construction.
- "**and beyond**" (S4 card 3, 85) is new in v2. It came from Test's own Fix 5b wording and is a mild stock idiom. It is not scored, because one idiom does not make a templated section. A word-neutral replacement is at Optional N.

**Loop-1 failure resolved.**
- **Inside S6:** the longest literal "We + verb" run is now 1. The back openers are Our finance views / Behaviour... / We map / Production reporting... / From HR..., we / For hotels..., we / We build / Order, stock... / We measure.
- **Across S6 → S7:** the longest run is 3 (card 9 → S7 intro → S7 01).
- **S9 steps 3-5** ("We sketch / We develop / We publish") are also 3. That is within the tolerance loop 1 accepted.

### Ruling on Build's Flag 17: the 6-paragraph "We + verb" run (S5 intro → S6 intro) is acceptable. No fix.

| # | Paragraph (line) | Opener | Brief requirement |
|---|---|---|---|
| 1 | S5 intro (96) | "We turn" | B2: section intro must have HLB HAMT/we as subject; F1 bridge |
| 2 | S5 row 1 (101) | "We design" | Brief S5: "35-45-word description opening with an HLB HAMT action" |
| 3 | S5 row 2 (112) | "We build" | same |
| 4 | S5 row 3 (123) | "We produce" | same |
| 5 | S5 foundation body (134) | "We build this layer first." | **Brief S5 foundation: 'Open "We build..."' (brief line 224)** |
| 6 | S6 intro (149) | "We apply" | B2 + F1 (brief's own example: "We apply those three views...") |

Reasons:
1. **All six openers are brief-mandated, not five.** Build's Flag 17 says the foundation body is "not mandated". That is incorrect: brief Section 4, S5, tells Build to open the foundation block with "We build...". **Build's suggested "This layer comes first." should therefore not be applied.** It would trade a tone preference for a departure from an explicit brief instruction.
2. **The reader does not meet these as consecutive prose.** Each opener starts a separate visual component: an H2 intro, three "View" module rows each with its own H3 and a 5-bullet "Key features" list, a labelled foundation block with its own H3 and 4 bullets, and then a new section with a new H2.
3. **The run is not monotonous.** The verbs vary (turn, design, build, produce, build, apply), and each sentence continues differently: an audience-specific object, a "So..." result clause, a data-flow description or a bridge. "We build" occurs twice, 2 components apart.
4. **This differs from the loop-1 failure and the PB/AA precedents.** Those were runs through flip-card backs that the brief did not require to open with "We". Loop 1 excluded the S5 rows from the finding for this same reason. Loop 1's Fix 7 then brought the unmandated part of the run down to 1.

Using the remaining loop on this would mean rewriting brief-mandated openers, which the brief does not allow. If the Content Writer wants a lighter feel later, the only change that keeps every mandated opener is to vary the verb *after* "We" in row 2 (for example "We create interactive reports..."). That removes the repeated "We build". It is optional and not needed.

**Tone advisories (not scored; suggestions in "Optional"):**
- **O (new). The triplet "reports, sources and KPIs" now appears 3 times.** It is in S8 body (228), S10 "Dashboard review" (268) and, since Fix 5d, A4 s4 (350). S13 (330) adds "audiences, KPIs and sources". The S8/S10 pair is brief-prescribed (loop-1 advisory E). The A4 instance came from Test's own fix wording and is the easiest to vary. Optional P gives a replacement.
- **C, D, F and I (carried from loop 1, unchanged):** C is S11 tile 5's double "firm"; D is the S4 card 4 H3/opener echo; F is the RLS phrasing appearing three times; I is S12's closeness to PB/AA teaser wording. All four are still optional.
- **S6 second sentences (carried):** 6 of 9 still use "[role] managers/leaders/teams see/compare/spot..." (cards 4-9). Each back is revealed singly on a flip card, not read as running prose, and loop 1 scoped its required fix to openers. It is not scored.

## 8. Section structure, CTAs, FAQ, internal links, flow: PASS

- **Order and format are unchanged from v1** and match brief 3b:
  - S0 breadcrumb (brief chain).
  - S1: H1 + lede + buttons + sub-block + 4 H3 cards + scope line; no stats.
  - S2 (4 items) + S2b + reference link.
  - S3: 7 anchor labels in brief order.
  - S4: H2 + lede + 4 H3 cards.
  - S5: H2 + intro + 3 rows + foundation block.
  - S6: H2 + intro + 9 flip cards; no buttons, no pill row.
  - S7: H2 + intro + 01-06.
  - S8 CTA.
  - S9: highlighted band with 5 steps; no durations, no button.
  - S10: 3 tabs; no featured card, no button.
  - S11: 6 tiles.
  - S12: static placeholder.
  - S13 CTA.
  - S14: 9 H3 Q&As, single accordion.
  - S15: form.
  - S16: footer.

  There is exactly one H1, no "Why AI Changes CRM" equivalent, no case study, and no reused SugarAI, PB or AA H2.
- **CTAs: exactly 4, in the specified places.**

  | CTA | Section | Button(s) | Line |
  |---|---|---|---|
  | 1 | Hero | "Book a free consultation" (#contact) + "Explore our services" (#services) | 26 |
  | 2 | S8 | "Request a dashboard review" (not called free) | 230 |
  | 3 | S13 | "Talk to our visualisation team" (body says "free consultation") | 332 |
  | 4 | S15 | Form "Schedule a Consultation" (H2 says "Free") | 373 |

  There are no other buttons. "Read the ranking" (68) is the S2b reference link (brief 3d). The in-text links "five-stage method" (85) and "agree the measures" (359) → #methodology are allowed.
- **FAQ:** 9 Q&As, answers 58-70 words, in the brief's F3 order (definition → vs analytics → software → time → sources → accuracy/security → return → existing dashboards → migration).
- **Internal links (all real, anchors exact, unchanged):**
  - L1 → /services/digital-transformation-uae/ (76).
  - L2 → /services/power-bi-partner-in-dubai-uae/ (347).
  - L3 → /services/advanced-data-analytics-uae/ (344).
  - L4 → /services/data-privacy-and-security-uae/ (356).
  - L5 → /sugarai-crm-2/ (159).
  - There is no self-link and no link to a "do not link" URL.
- **Flow F1-F3 holds.** No bridge sentence was edited. Fix 5b keeps the S4 card 3 → #methodology hand-off, and "to launch and beyond" leads straight into card 4, "Support after launch".
- **Build's departures 1-5** (Flags 3-7) were accepted in loop 1. Nothing about them changed.

## 9. Client requirements (Section 10) and fabricated commitments: PASS

- **Point 1 (replace in place):** the canonical note is at line 15, and the Deliver handoffs are in Flag 8 (including the outstanding AA L3 edit).
- **Point 2:** 33x and PowerUP! are absent (critical re-checks).
- **Point 3:** there is no AI/CRM section.
- **Point 4:** 4 CTAs; S8 is not "free"; S13 and S15 are "free".
- **Point 5a:** meta uses the z spelling, and the page uses the s spelling.
- **Point 5b:** FAQ 4 uses Tab 1's ranges. "7 days" / "seven days" = 0. The "Whatever the size" absolute is gone, and "normally" is used instead.
- **Point 6:** there is no case study and no "delivered for X clients" claim. S6 is framed as blueprints (149, 196).
- **Point 7 (post-launch support):** it is described as a real offering in S4 card 4 (88), S7 06 (222), S9 step 5 (253) and S10 Managed support (284): monitoring, fixes, tuning, new views, training and health checks.
  - Ripgrep for "SLA", "24/7", "hours", "response time", "Monday" and "Friday" on the page returns **0**. The only hits are in Build's Flag 9 note.
  - Fix 5b's "to launch and beyond" makes no commitment about scope or hours.
- **Point 8:** S12 is a static placeholder.
- **Point 9:** there is no Arabic, RTL or bilingual content, and no "CRM Training & Adoption" or "customer intelligence" leftovers.
- **Requirement notes:** the page is a service page, not an explainer. Definitions appear only in FAQ 1-2, each pivoting to HLB HAMT. Real links go to both siblings. Visio and Microsoft = 0.
- **No transcript was supplied.**
- **No fabricated commitments.** "Reply within one business day" (371) is the site-standard promise prescribed by brief S15. There are no prices, client counts or durations outside FAQ 4.
- **Go-live condition (carried, Deliver, not Build):** the L2 target `/services/power-bi-partner-in-dubai-uae/` still shows the "$4,500 PowerUP! Offer" in the uploaded snapshot. Do not publish with L2 live until the Power BI page has replaced or 301-redirected that URL. Swap L2 to the PB final URL once it is set (Build Flag 7).

---

## Overall: PASS

- All 7 loop-1 fixes are applied word for word, with no collateral changes; G1 was also applied.
- Critical exclusions stay at 0: 33x, PowerUP, $4,500, Softcrylic, the "pipeline, model and semantic layer" triple and every third-party tool name. "Power BI" = 3 and "SugarAI CRM" = 1, both within their permitted slots.
- Keywords are 3 / 2 / 2 / 1 / 1 / 1. "HLB HAMT" = 11, "UAE" = 7, "visualisation" = 18 and "dashboard(s)" = 20 (cap 35).
- The word count is 3,017. There are zero em dashes, and the page uses British spelling.
- The new wording is original against all five competitors, Softcrylic, Tab 1, the SugarAI sample, PB v8, AA v5 and the web.
- All four stats were re-verified today.
- There are exactly 4 CTAs and 5 real internal links.
- **Flag 17 ruling:** the 6-paragraph run is entirely brief-mandated, including the foundation's "We build..." opener (brief line 224). It is acceptable. Do not apply "This layer comes first."

Ready for Deliver, subject to the L2 go-live condition and the Deliver handoffs in Build's Flag 8.

### Optional (not needed to pass; for the Content Writer's or Deliver's discretion; each stays within budget)

- **N. S4 card 3 s3 (85).** Change "to launch and beyond" to "through launch and support". This is word-neutral and removes the mild stock idiom.
- **P. FAQ A4 s4 (350).** Change "when we have seen your reports, sources and KPIs first-hand" to "once we have seen your current reporting and the systems behind it". That is +2, so A4 becomes 68. It stops the third verbatim "reports, sources and KPIs". Do not use "condition of your data" (PB A10).
- **K. S5 foundation s1-s2 (134).**
  - Replace: "We build this layer first. Data from your ERP, CRM, finance and operational systems is integrated, cleaned and modelled into a semantic layer with one definition per KPI, then validated against source before design begins."
  - With: "We build the foundation from your ERP, CRM, finance and operational systems, integrating, cleaning and modelling their data into a semantic layer with one definition per KPI, then validating it against source before design begins."
  - The change is word-neutral (35 → 35). It keeps the brief's "We build..." opener and removes the "build ... first" echo of AA's foundation sentence.
- **M. FAQ A2 s1 (344).** Replace with "Analytics tests and models data to explain why a result happened." That is -3, so A2 becomes 61. It uses the brief's own verb frame, so no copular definition remains.
- **G4. S6 card 8 s1 (189).** Change "sales data feed" to "sales records feed". Word-neutral; it removes the "data feed" misreading.
- **G2, G3, A, B, C, D, E, F, I, J and L** from test-report-v1 remain available unchanged. None was applied, and none is required.

---

Sources consulted for verification (today):
- [UAE Government portal, Global digital competitiveness](https://u.ae/en/about-the-uae/uae-competitiveness/global-digital-competitiveness): 9th of 69; 1st in talent; updated 25 Nov 2025.
- [BARC, Data, BI and Analytics Trend Monitor 2026](https://barc.com/news/barc-publishes-the-data-bi-and-analytics-trend-monitor-2026/): 1,579; data quality management 7.9, tied with data security and privacy; 12 Nov 2025.
- [Gartner press release, 20 Feb 2025](https://www.gartner.com/en/newsroom/press-releases/2025-02-20-gartner-survey-finds-one-third-of-cdaos-cite-measuring-data-analytics-and-ai-impact-as-top-challenge) (search extract) and [BigDATAwire](https://bigdatawire.com/2025/02/24/cdoas-are-struggling-to-measure-data-analytics-and-ai-impact-gartner-report): 22%, "the bulk of their D&A use cases"; 504 leaders.
- [UAE Government portal, Data protection laws](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws): Federal Decree Law No. 45 of 2021.
- Competitor pages re-fetched today:
  - [instinctools](https://www.instinctools.com/data-visualization/)
  - [Damco](https://www.damcogroup.com/data-visualization-services)
  - [IT IDOL Technologies](https://itidoltechnologies.com/technologies/data-visualization-services/)
  - [Aspire Systems](https://www.aspiresys.com/data-and-ai-solutions/data-management/data-visualization-services)
  - [Mindbowser](https://www.mindbowser.com/data-visualization-services/)
- Softcrylic: search extracts only (client-rendered), including the [Dashboard Performance page](https://www.softcrylic.com/dashboard-performance-optimization-tableau-power-bi-data-studio/attachment/tableau-logo-2/) checklist extract.
- The exact-phrase searches in 5.5 returned no matches.
