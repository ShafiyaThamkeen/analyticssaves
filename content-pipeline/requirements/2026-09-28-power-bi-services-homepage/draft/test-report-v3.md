# Test report v3: Power BI Services homepage (draft-v3.md)

Tested by: Test agent, 2026-09-28
Loop: **3 of 3, the final automatic loop.** `test-report-v1.md` and `test-report-v2.md` exist; this is the third report.
Inputs checked: `brief.md` (all sections; Section 10 treated as overriding), `draft/draft-v3.md` (the "Changes from v2" section first, then the whole page), `draft/test-report-v2.md`, `draft/test-report-v1.md` (to check what earlier loops covered), `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt` (all 772 lines), `inputs/extracted/hlb-data-viz-v4 (1).html.md`, `inputs/extracted/HLB_HAMT_Data_Viz_Content_Documentation (1).docx.md`, and, for exact source wording, the Tab 3 section (lines 644-1076) of `inputs/content-source/data-viz-documentation-extracted.md`.
Method: no shell was available. Every changed section was re-counted word by word under the brief Section 1 rule and reconciled against the v2 per-section counts. Characters, keywords, stats and repeated phrases were checked with ripgrep across the whole file. Non-page lines (meta, changelog, chrome, Sources, Stats used, Flags) were then excluded. Every section of the page was compared sentence by sentence against the SugarAI extracted text.

---

## REMAINING ISSUES (for the Content Writer): loop limit reached, do not proceed to Deliver

**Status: Overall FAIL at loop 3 of 3.** Per the loop limit, this draft is **not** sent back to Build and **not** passed to Deliver. The pipeline should report this summary to the user.

**What did pass:** all 14 v2 fixes landed, and so did both of Build's self-reported final-read fixes. Build's independent rewrites (S12 tile 4, S8 items 01-02, S9, S11 story, S7 cards 1 and 3, FAQ A7) are clean against both the in-scope source and SugarAI. The regression checks also pass: keywords (6 singular / 3 plural), all stats and footnotes, the 17-section structure, links L1-L5 and P1-P2, the 7 accuracy corrections, the 3,378 word count and every section budget, zero em dashes, and grammar.

**What still fails:** 5 sentence-level issues in 2 checklist items. **One was introduced in v3** (the fifth "before any..." in S7 card 3). **The other four were already in v1/v2 and I missed or under-rated them in earlier loops.** Build did not cause them, and neither of my earlier reports asked Build to fix them. Two of them come partly from wording the brief prescribed. No issue touches a keyword, stat, link, section or accuracy correction. Each fix below is a drop-in sentence, counted and checked against SugarAI, the source and the rest of the page.

Ranked by severity:

| # | Severity | Location (draft-v3 line) | What fails | Why | Suggested resolution (counted) |
|---|---|---|---|---|---|
| **R1** (5p) | High | S12 tile 1 body (line 378): "Consulting, build and support handled in-country by consultants who work in the platform daily." | Close echo of **two** SugarAI tiles in the same grid | SugarAI tile 1: "Implementation, consulting, migration and support delivered locally." SugarAI "In-region team": "Consultants who scope, build and support from the UAE." The draft keeps the service list (consulting / build / support), swaps "delivered locally" for "handled in-country", and adds "consultants who". In v3, Build avoided "build and support" in tile 4 for exactly this reason, but tile 1 still has it. **Partly brief-driven:** brief S12 tile 1 prescribed "consulting, implementation and support delivered locally", which is itself close to verbatim SugarAI. | "Our own staff handle everything from data engineering to aftercare; nothing is subcontracted." (13 words, -1; S12 = 145, inside 140-180). The claim rests on source FAQ 18 ("End-to-end in-house delivery"). |
| **R2** (5q) | High | S8 intro (line 254): "Six service lines cover the path from a blank whiteboard to a platform your teams use every day. Take one on its own or combine several, with an engagement model sized to the complexity in front of you." | Reworded SugarAI Packages intro | SugarAI: "Every SugarAI engagement **covers six** work categories... **Choose one or combine them** based on your needs, **with** cloud or on-premise deployment available within each category." The same three units appear in the same order: six + cover / choose one or combine / ", with [delivery option]". **I rated only sentence 2 as advisory in v1 and v2 and missed the "six... cover" unit in sentence 1. Together they meet the violation standard, so I am upgrading it and saying so.** | "From the first whiteboard session to the support that follows launch, the work falls into the service lines below. The engagement model you agree with us sets how many you need and when each begins." (35 words, -3; brief 30-40.) This also removes a second repeat: "your teams use every day" (S8) vs "the tools your teams open every day" (S5 intro). |
| **R3** (7d) | Medium | "before any [noun]" appears **5 times**: S4 card 3 "Before any build" (line 117); **S7 card 3 "before any figure goes on screen" (line 224, new in v3)**; S8 item 02 "Before any visual is drawn" (line 260); S8 item 05 "before any migration is planned" (line 269); S10 intro "well before any larger investment" (line 288) | Repetitive construction clustered in S7-S8-S10 | Four of the five sit in three consecutive sections, and two are in one section (S8). By the same cluster standard used in v2 (7c), this fails. The v3 rewrite of S7 card 3 added the fifth. | (a) S7 card 3 sentence 2 becomes "CRM and ERP records are matched unit by unit in a lakehouse." (12 words, -3). (b) S8 item 02 sentence 1 becomes "Dependable data comes first; the charts come later." (8 words, -3; item 02 = 46). (c) S8 item 05 changes "before any migration is planned" to "ahead of planning a migration" (0). This leaves 2 instances, S4 and S10. |
| **R4** (7e) | Medium | S7 flip cards: card 1 tagline "**One** consolidated view across every entity and currency" (211); card 1 back "into **one** group P&L" (212); card 2 back "figures sit **on one page**" (218); card 3 back "DLD compliance **on one dashboard**" (224); card 5 tagline "Every channel and customer cohort **in one picture**" (235) | "One [noun]" cluster and SugarAI tagline formula | Five "one [noun]" phrases in five consecutive cards. Adjacent cards 2 and 3 both end a metric list with "on one [page/dashboard]". Taglines 1 and 5 also follow the SugarAI industry-card formula: "Quotes, shipments and tracking **in one view**", "Territory, margin and live stock **in one view**", "**One view** of the relationship, on your own infrastructure". **Card 2's "sit on one page" was my own v1 suggested text.** | (a) Card 1 tagline becomes "Consolidation across entities and currencies, without the spreadsheets" (8, 0). (b) Card 2 changes "sit on one page" to "sit together" (-2). (c) Card 3 changes "on one dashboard" to "reported alongside" (-1). (d) Card 5 tagline becomes "Campaign spend traced through to customer behaviour" (7, -1). Keep "one group P&L", which is factual. |
| **R5** (5r) | Low-medium | S1 sub-block line (line 67): "Leadership, analysts and field teams read from the same governed dataset." Also FAQ A7 (line 440): "engineering and BI teams working from the same lake" | Reworded SugarAI hero sub-block line, in the identical slot | SugarAI sub-block: "Three teams working from the same information, with your ERP behind it." The draft sentence is [three named teams] + [read/working] from the same [dataset/information], directly under the mirrored "One X, one Y" heading. A7 repeats the same "teams working from the same..." frame, and S5 row 2 ("Both draw on the same data") states the same idea a third time. This is the same kind of echo I failed as 5m in v2 (SugarAI Logistics "sales and operations work from the same picture"). | (a) S1: replace both sub-block sentences with "A revenue figure means the same thing in every meeting, whether a director, an analyst or someone out in the field is reading it." (24 words, +3; S1 = 183, inside 150-190; "meeting" stays at 2 on the page.) (b) A7: change "when you want engineering and BI teams working from the same lake" to "when engineers and analysts should query a single copy of the data" (0; A7 stays 87). |

**If all five resolutions are applied:** S1 183 · S7 356 · S8 348 · S12 145 · S15 811 (A7 87). **Total about 3,367**, inside 3,100-3,500. S2, S6 and S14 (the zero-slack sections) are untouched. No resolution adds or removes a keyword instance, stat, link or "UAE" mention, and none uses "before any", "one [noun]", "side by side", ", giving", "which is what", "specialist", "draw on", "meeting" (beyond the existing 2), "build and support", "one partner/team", "delivered locally" or "in one view".

**Options for the Content Writer:**
1. Apply R1-R5 as written (or with your own wording under the same constraints), then send the page to Deliver after a spot re-check of only those sentences. Nothing else needs to change.
2. Accept any item as a judgment call. R1 and R2 are the clearest template echoes, because both pages will sit on hlbhamt.com. R4 and R5 are the most defensible to keep as they are.
3. Separately, decide whether to keep the **brief-prescribed** wording that echoes SugarAI (see "Brief-level echoes" under item 5). Build followed the brief on these, so they are not scored against Build.

**Carry to Deliver once released (unchanged):** judgment call (b) S16 heading and form component; judgment call (g) "certified connectors" wording; judgment call (h) footnote renumbering; the Gartner disclaimer; the SugarAI reverse-link edit; open item: final URL and handling of the overlapping pages (brief Section 10 point 3).

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density | **PASS** |
| 2 | Word count | **PASS** (3,378) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling, punctuation | **PASS** (4a and 4b fixed; no new errors; 2 style advisories) |
| 5 | Originality | **FAIL** (all v2 items 5h-5o pass; 3 fresh-read SugarAI echoes: R1, R2, R5) |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI heuristics | **FAIL** (7a-7c pass; 2 repetition clusters: R3, R4) |
| 8 | Section structure and internal links | **PASS** |
| 9 | Client requirements and the 7 accuracy corrections | **PASS** |

---

## Verification of the 14 v2 fixes and the 2 advisory edits

Each changed sentence was checked against the in-scope source (docx Tab 3 / HTML Tab 3), the SugarAI page and the rest of this page.

| v2 fix | v3 text (location) | Source check | SugarAI check | Internal check | Verdict |
|---|---|---|---|---|---|
| 4a | A4: "For clients in the Emirates, that Monday routine used to cost hours; now it largely runs itself." | The source's "eliminate hours of weekly manual reporting" frame is gone; the claim stays qualitative | No match | "That Monday routine" correctly refers back to sentence 2. A4 = 73 | **Pass** |
| 4b | S7 intro: "...around the decisions those KPIs support, instead of adapting a generic template." | n/a | See brief-level note (the S7 intro concept) | Antecedent fixed. Intro = 32 | **Pass** |
| 5h | S12 tile 4: "Power BI tracks booked revenue; [SugarAI CRM](...) scores the deals still open. We deliver and maintain both." | n/a | SugarAI tile: "SugarAI prediction plus Power BI analytics, from one partner." The unit order is reversed, the clauses are contrasted, "plus/alongside/side by side/one partner/one team" is gone, and there is no "forecasts which deals close". "Scores" describes SugarAI with its own feature verb, which is acceptable. | 17 words. The L2 anchor is exact | **Pass** (Build's deviation was justified) |
| 5j (01) | S8 01: "We map your source systems, test how ready your people and data are for self-service reporting, and sketch an architecture that fits your plans for growth." | The source's "assess ... to design ..." purpose frame is replaced by a three-verb series. The three brief-mandated facts remain as scope | No match | Item 01 = 51. Minor: "that fits your ... growth" loosely echoes S11 intro "the model that fits your starting point and change it as you grow" (advisory A2) | **Pass** |
| 5j (02) | S8 02: "We consolidate sources into data marts and warehouse layers, then automate loads with Azure Data Factory pipelines." | The "We help prepare, integrate, and manage" frame is gone | No match | Item 02 = 49. It no longer repeats item 04's "bring... together" | **Pass** |
| 5k | S9: "Send a file from your systems or use our demo figures, then tell us what to click next." | The source's "walk you through... sample data or your own custom datasets. No obligation." sequence is gone | No match (SugarAI CTA 1: "See SugarAI configured to the way your teams sell, support and market.") | S9 = 28 (≤30). No overlap with the S11 Live demo line. A person directs the demo, so there is no Q&A implication. "No obligation" is carried by the H2 "...Before You Commit" | **Pass** |
| 5l | S11 story sentence 2: "From workshop to go-live, we wire in your spreadsheets and exports, then sit down with you to choose the KPIs that answer those questions first." | "Quick wins against clear objectives" is removed. The access / visualise / guide three-verb sequence is now two clauses, with guidance folded into a joint decision | No match | Story = 50. No "specialist" | **Pass** |
| 5m | S7 card 3 sentence 2: "CRM and ERP records are matched in a lakehouse before any figure goes on screen." | The source's "Built on Azure Data Lakehouse ingesting..." frame is gone | The SugarAI Logistics "sales and operations work from the same picture" unit is gone | Back = 41. **But it adds a fifth "before any [noun]"** (see R3) | **Pass on originality; causes R3** |
| 5n | A6: "...and our [data protection advisory](...) team helps set each environment up in line with PDPL, DIFC and ADGM requirements." | The source's "We configure environments to meet..." frame is gone | No match | A6 = 89 (≤90). The L5 anchor is exact. "In line with" is kept; there is no compliance guarantee | **Pass** |
| 5o | S5 row 4 sentence 2: "Power BI Embedded goes further: investor portals, client platforms and your web apps can carry branded dashboards on capacity-based licensing, without the expense of building reporting from scratch." | The subject and frame are inverted relative to the source's "lets you put interactive dashboards inside..." | No match | Row 4 = 45 | **Pass** |
| 7a | S1 card 3: "A regional manager reviews yesterday's figures and any alerts on iOS or Android between site visits." | n/a | No match | 16 words. No Windows. No overlap with S5 row 4 or S6 point 3 | **Pass** |
| 7b | A7 sentences 1-2: "Fabric is the larger Microsoft service that Power BI now belongs to. Its other workloads (real-time analytics, data engineering and warehousing) share one pool of capacity." | The source's "next-gen unified platform... all under one roof" frame is gone. No OneLake claim was added | No match | The S5 platform frame ("Fabric brings Power BI together with... on one platform") is no longer mirrored: new subject, relative clause, reordered list. **Correction to Build's changelog:** A7 does still end on a "one [X]" unit ("share one pool of capacity"). The residual overlap is only the brief-mandated list plus that unit, which is acceptable. A7 = 87. Web search: no match. The shared-capacity statement is accurate | **Pass** |
| 7c | S7 card 1 sentence 2: "With audit in mind, chartered accountants design the intercompany eliminations, currency translation and IFRS segment views." | The source's "Our CA background ensures the financial logic is audit-ready" frame is gone; the list is factual scope | No match | Back = 42. The endings of cards 1-3 now differ in shape; card 1 no longer ends on audit | **Pass** |
| Bookkeeping | Flags item 9 quote (line 528) and S12 tile 4 note (line 531) | | | Both match the page | **Pass** |
| Advisory A3 | "...a lakehouse is usually worth it: every report reconciles to the same cleaned tables." | | | "then" is removed, so the S5 row 1 parallel is broken. A3 = 79 | **Pass** |
| Advisory A8 | "...tested measures; that groundwork makes Copilot's answers reliable." | | | "Which is what" now appears once on the page (S11). See advisory A7 on "reliable" | **Pass** |

**Build's self-reported final-read fixes:**
- **"Specialist" count: verified.** There are 3 on-page instances: S11 intro (line 313), S11 Extend tagline (352) and S14 H2 (409). The S11 story has none, so Build correctly avoided adding a fourth. Two instances in S11 is advisory only (A4 below).
- **"Draw on": verified.** The only on-page instance is S5 row 2 (line 144). A7 does not use it.

**Other Build sweep claims, checked:**
- Correct: "side by side" x1, "meeting" x2, "already" x3, "which is what" x1, ", giving" x1 (S5 platform), "behind" not added.
- **Inaccurate, not a failure:** "Bring... together appears once." S5 platform also says "Fabric **brings** Power BI **together** with..." (line 177). The two instances are 90 lines apart and in different senses, so they are acceptable.

---

## 1. Keyword placement and density: PASS

On-page copy only (eyebrows, buttons, anchor nav, breadcrumb, meta, Sources, Stats used and Flags excluded). Ripgrep has no look-ahead, so the singular was matched as `\bPower BI service([^s]|$)`, which is equivalent to the brief's `(?!s)`.

- **"Power BI service" singular: 6** (target 5-7, max 8). Line 59 H1; 61 hero lede; 111 S4 card 1; 143 S5 row 2 H3; 421 FAQ Q1; 422 FAQ A1 (once). A7's "Microsoft service that Power BI" does not match.
- **"Power BI Services" plural: 3** (target 2-3). Line 252 S8 H2; 373 S12 H2; 452 S16 body. No section contains both forms.
- **Meta title and description:** identical to brief Section 7. The primary keyword leads both. It also appears in the H1 and in the first 100 words (H1 plus lede sentence 1).
- **"Power BI consulting company": 2** (S4 lede line 108; S12 intro line 375).
- **"Power BI solutions expert": 2** (S11 Extend line 356; S14 body line 411).
- **"Certified Power BI Partner in UAE": 0**, correctly not placed per Section 10 point 1. "Certified" appears 3 times, all about connectors (lines 155, 157, 266); this is judgment call (g).
- **Stuffing:** "Power BI" on-page is **40** (cap 75, flag at 85). "UAE" on-page is **10** (cap 12): lines 59, 78 x2, 120, 190, 218, 373, 377, 419, 436. S8 offering titles containing "Power BI": 0 of 6. PoC step titles containing "Power BI": 0 of 5.

## 2. Word count: PASS

Changed sections were re-counted word by word and reconciled against the v2 per-section counts:

| Section | v2 | v3 (my count) | Build's figure | Budget (3b) | Status |
|---|---|---|---|---|---|
| S1 | 182 | **180** (card 3: 18 → 16) | 180 | 150-190 | OK |
| S2 + S2b | 65 | 65 (untouched) | 65 | 45-65 | OK (at cap) |
| S4 | 258 | 258 | 258 | 250-300 | OK |
| S5 | 394 | **395** (row 4: 44 → 45) | 395 | 380-440 | OK |
| S6 | 150 | 150 (untouched) | 150 | 150-190 | OK (at floor) |
| S7 | 365 | **363** (intro +3, card 1 -3, card 3 -2) | 363 | 330-400 | OK |
| S8 | 355 | **354** (item 01 +1, item 02 -2) | 354 | 330-390 | OK |
| S9 | 23 | **28** | 28 | 20-30 | OK |
| S10 | 157 | 157 | 157 | 150-190 | OK |
| S11 | 385 | **380** (story sentence 2: 30 → 25) | 380 | 360-420 | OK |
| S12 | 147 | **146** (tile 4: 18 → 17) | 146 | 140-180 | OK |
| S13 | 34 | 34 | 34 | 30-45 | OK |
| S14 | 29 | 29 (untouched) | 29 | 20-30 | OK |
| S15 | 813 | **811** (A3 -1, A4 -4, A7 +4, A8 -1) | 811 | 700-850 | OK |
| S16 | 28 | 28 | 28 | 20-30 | OK |
| **Total** | 3,385 | **3,378** | 3,378 | 3,100-3,500 (fail <2,900 or >3,750) | **PASS** |

- **Zero-slack checks:** S6 = 150, S2 = 65 and S14 = 29, all untouched.
- **FAQ answers:** 79 / 78 / 79 / **73** / 74 / **89** / **87** / 77 / 71. All ≤90.
- **Sub-units:**
  - S1 card 3: 16 (12-18)
  - S5 row 4: 45 (35-45)
  - S7 intro: 32 (25-35)
  - S7 backs: 42 / 45 / 41 / 42 / 36 / 37 (35-45)
  - S8 items: 51 / 49 / 46 / 45 / 48 / 46 (45-55)
  - S12 tiles: 14 / 16 / 18 / 17 / 16 / 18 (10-18)

  All are in range.

## 3. Zero em dashes: PASS

Whole-file ripgrep: `—` **0**, `–` **0**, `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- **G5 (FAQ A4): fixed.** "that Monday routine" has a clear antecedent, and the misplaced relative clause is gone.
- **G6 (S7 intro): fixed.** "the decisions those KPIs support" now has an antecedent.
- **New v3 sentences:** all grammatical: S12 tile 4 (semicolon joins two independent clauses), S8 01-02, S9, S11 story, S7 cards 1 and 3, A6, A7 ("Fabric pays off" fixes the plural-antecedent issue), S5 row 4 and S1 card 3.
- **Spelling:** British spelling is consistent (organisations, optimised, modelling, licence as a noun, programme, analyse, digitise, visualisation, behaviour). There are no -ize forms outside proper names.

**Style advisories (not scored):**
- **Serial comma, used once:** S11 Implement tagline (line 343), "Rollouts scoped to one team, several, or the enterprise." Everywhere else the page drops the serial comma in short lists. Optional: "one team, several or the enterprise".
- **Garden path in S5 row 1** (line 133): "DAX measures calculate the KPIs finance reports on, such as..." It can momentarily read as "KPIs finance reports". Optional: "the KPIs that finance reports on".

## 5. Originality: FAIL

**Standard (unchanged from loops 1-2):**
- Brief-mandated facts, lists and structural labels are not violations.
- A sentence that keeps a source's or SugarAI's unit sequence or verb frame, with synonyms swapped in, is a violation.

### 5a. v2 items 5h-5o

All pass. See the verification table above.

### 5b. Fresh full read against SugarAI: 3 failures

Details and resolutions are in the Remaining issues table above.

- **5p (R1), S12 tile 1:** echoes SugarAI tile 1 ("...consulting, migration and support delivered locally") and the "In-region team" tile ("Consultants who scope, build and support from the UAE").
- **5q (R2), S8 intro:** echoes the SugarAI Packages intro ("covers six work categories... Choose one or combine them..., with..."). This is upgraded from advisory in v1/v2, as disclosed above.
- **5r (R5), S1 sub-block line and A7 phrase:** echo the SugarAI sub-block ("Three teams working from the same information").

### 5c. Fresh full read against the in-scope source: no new failures

Checked sentence by sentence: S4 lede and cards, S5 intro and rows, S6, S7 cards 1-6, S8 items 01-06, S10 intro and steps, S11 story, terms and tabs, S12, and FAQ A1-A9. The remaining overlaps are brief-mandated fact lists in source order: the CDO/CMO/CAO lists, the training tracks, the timelines and the connector names. That matches the standard applied in loops 1-2.

### 5d. Advisories (not scored; for the Content Writer)

- **S4 card 4** (line 120): "A UAE-based team answers... through a single point of contact... that contact owns the request" vs SugarAI "A dedicated support team takes ownership at go-live... logged through a single service desk". "UAE-based team" and "single point of contact" are brief-prescribed facts. Only the ownership idea is shared.
- **S7 card 3** (line 224): "Follow each unit... live availability, payment plans, broker performance" vs SugarAI Real Estate "Track unit availability, bookings and broker commission... payment plan, handover". These are real-estate domain terms from source FAQ 10. The verb frame differs.
- **S8 04 vs S11 "Connector help":**
  - S8 04 (line 266): "We set up certified connectors, write custom connectors for sources without an off-the-shelf option"
  - S11 (line 354): "Existing connectors configured, or custom ones written, for sources your reports depend on"
  - Both keep the source's "implement certified connectors, or build custom connectors tailored to your... data sources" frame. The brief assigns this content to both places, and the idea has few natural phrasings.
- **S13 body** (line 401): "An example of the executive views we build, ..." vs SugarAI "A short walkthrough of the platform as we configure it: ..." They share a two-unit opener only.

### 5e. Brief-level echoes (Build followed the brief; flagged for Content Writer awareness only)

- **S7 intro concept:** brief: "starts from the KPIs a role or sector actually runs on, not from a generic template". SugarAI: "A CRM configured with generic sales stages gets generic adoption. We start from an industry blueprint..."
- **S6 H2** (brief-suggested): "Ask Your Data a Question and Act on the Answer" vs SugarAI "Reads the Data, Your Team Acts on It".
- **S15 H2** (brief-suggested): "Questions UAE Teams Ask Before Choosing a Power BI Partner" vs SugarAI "What buyers ask us before they shortlist".
- **S14 H2:** "Talk Through Your Roadmap With a Specialist" keeps the skeleton of SugarAI's "Plan your SugarAI rollout with our consultants". This was accepted in v1 as an improvement on the brief's even closer suggestion.
- **S12 tile 1:** the brief's prescribed body was near-verbatim SugarAI (see R1).

### 5f. Web check: clean

Searched distinctive v3 phrases:
- "Power BI tracks booked revenue"
- "CRM and ERP records are matched in a lakehouse"
- "that Monday routine used to cost hours"
- "we wire in your spreadsheets and exports"
- "Fabric is the larger Microsoft service that Power BI"

None has an exact or near match online. Results were only generic topic pages.

## 6. Stat accuracy: PASS

On-page placement was verified by whole-file search. Each figure appears exactly once, in its assigned section:

| Ref | On-page wording | Placement | Check (re-confirmed by search today) |
|---|---|---|---|
| [1] 200+ | "Data connectors in Power BI, from ERP and CRM to cloud databases." | S2 item 1 only (line 84) | Worded as Power BI's library. Microsoft Learn source. Unchanged |
| [2] 33x | "Faster report load times in one recent HLB HAMT engagement." | S2 item 2 only (88) | Mandatory qualifier present. Approved (Section 10 point 4) |
| [3] Gartner | "Microsoft: named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." | S2b only (98) | Re-confirmed: Fabric Community announcement and mwpro.co.uk repost, "nineteenth consecutive year". No "#1", "ranked" or "14+" on-page. Disclaimer in Sources item 3 |
| [4] Fabric | "Microsoft reports more than 40,000 paid Fabric customers, up more than 60% year on year." | S5 platform only (177) | Re-confirmed: FY26 Q4 earnings call, 29 July 2026 |
| [5] AI diffusion | "in Q2 2026, 73.3% of the UAE's working-age population used generative AI tools, against 18.8% worldwide." | S6 lede only (190) | Re-confirmed: Microsoft On the Issues, 21 Sep 2026 (ages 15-64). Framed as generative AI use, not BI use |
| [6] 7 days | S10 H2 | S10 only (286) | The meta description's "7-day" is brief-mandated meta, not on-page copy |
| [7]-[11] F1-F5 | Desktop vs service; US$14/US$24 "at the time of writing"; UAE North/Central; Copilot F2/P1, English-only prompts, off by default outside the US/EU boundary; ISO/IEC 27001 and SOC 2 "within the scope of" | as in v1/v2 | Text unchanged. A6's rewritten sentence 3 carries no stat |
| CS facts | $4,500 PowerUP!, 5 terms, 6 deliverables; FAQ 9 timelines | S11; FAQ 9 | Match the source. Approved (Section 10 point 4) |

- No FAQ restates 200+, 33x, 19th, 40,000, 73.3% or 7 days.
- A project-wide search finds these figures only inside this requirement folder. No other page duplicates them.
- No new stat was introduced in v3.

## 7. Human tone / AI-detection heuristics: FAIL

### v2 items

- **7a:** pass. S1 card 3 no longer duplicates S5 row 4 or S6.
- **7b:** pass (see the verification table).
- **7c:** pass. S7 cards 1-3 now end on a factual list, a fronted "Because..." clause and a process fact, respectively.

### Stock AI phrases

None. "Unlock" appears only inside the L4 URL. "Seamless", "revolutionise", "unleash", "in today's..." and "in conclusion" all return 0.

### Phrase tallies from past loops (on-page)

| Phrase | Count | Where |
|---|---|---|
| "meeting" | 2 | S1 |
| "already" | 3 | S5, S6, S11 |
| "side by side" | 1 | |
| ", giving" | 1 | |
| "which is what" | 1 | |
| ", so [benefit]" | 5 | permitted set, unchanged |

### New failures

- **7d (R3):** "before any [noun]" x5, clustered in S7-S10. One instance is new in v3.
- **7e (R4):** "one [noun]" x5 across S7 cards 1-5, plus the SugarAI tagline formula.

### Advisories (not scored; optional polish for the Content Writer)

- **A1. The service definition appears twice in the same shape.**
  - S5 row 2 (line 144): "the cloud side of the platform, where finished reports are published, bundled into apps, refreshed on schedule and secured"
  - FAQ A1 (line 422): "the browser-based cloud platform where those reports go live: they are shared as apps, refreshed automatically and protected by access rules"
  - Both follow the same four-item order. The brief prescribes this fact in both places, and unlike the v2 Fabric case (7b) there is no source echo, so it stays advisory.
  - Optional A1 sentence 2: "The Power BI service runs in the browser: access rules decide who sees each published report, data refreshes on its own, and related reports are grouped into apps for each audience." (31 words; A1 = 84; the singular keyword stays at 6.)
- **A2. "that fits your... grow".**
  - S8 01 (line 257): "an architecture that fits your plans for growth"
  - S11 intro (line 313): "Pick the model that fits your starting point and change it as you grow"
  - Optional S11 change: "Pick the model that suits your starting point and change it as you grow."
- **A3. "Reconcile" x3 and "trust" x4.**
  - "Reconcile": S4 lede, S13 "with every figure reconciling along the way" and A3 "every report reconciles to the same cleaned tables". Two of the three use the "every [noun] reconcil-" frame.
  - "Trust": hero, S7 card 4, S10 step 2 and S12 intro.
  - Both words are on-theme for this page. Optional S13 change: "...drilling from the group total down to each entity without a figure going astray."
- **A4. "Specialist" twice in S11** (intro and Extend tagline), plus the S14 H2. Optional Extend tagline: "Extra hands for the parts your team hasn't covered yet."
- **A5. "Before" as a motif beyond "before any".** S1 card 1 ("before the first meeting"), S9 H2, S11 Explore tagline and A5 ("before the first visual is placed"). Once R3 is applied, these read as varied.
- **A6. "Your teams... every day".** S5 intro (line 128) and S8 intro (line 254). This is resolved automatically by R2.
- **A7. Accuracy hedge in A8** (my own v2 wording): "that groundwork makes Copilot's answers reliable" overstates what Microsoft claims. Microsoft says model preparation *improves* Copilot output. Optional: "that groundwork makes Copilot's answers more reliable" (+1; A8 = 78).

## 8. Section structure and internal links: PASS

**All sections are present in the mandated order:**
- S0 breadcrumb (HLB nav chain)
- S1: one H1, lede, sub-block, 3 H3 cards, deployment line
- S2: 4 strip items, no headings, plus S2b recognition bar and button
- S3 anchor nav: 8 labels in DOM order, matching brief 3b
- S4: H2 + 4 H3
- S5: H2, intro, 4 rows each with label, H3, description and the exact 5 brief bullets; platform layer with 4 bullets
- S6: H2 + 3 H3
- S7: H2, intro, 6 flip cards (front H3 + tagline, back + button), 10-pill row
- S8: H2 "Our Power BI Services", items 01-06
- S9
- S10: highlighted band, H2 with "7 Days" [6], 5 H3 steps
- S11: featured PowerUP! card with badge, price, story, all 5 terms and all 6 deliverables, then 4 tabs
- S12: brief H2, 6 tiles
- S13: static-asset version, per Section 10 point 5
- S14
- S15: H2 + 9 H3 questions in brief order
- S16: form default "Technology Consulting"
- S17

**Links (all correct):**

| Link | Anchor text | Target | Location |
|---|---|---|---|
| L1 | "digital transformation and analytics services" | /services/digital-transformation-uae/ | S4 lede, line 108 |
| L2 | "SugarAI CRM" | /sugarai-crm-2/ | S12 tile 4, line 387. Anchor exact, no possessive |
| L3 | "UAE Corporate Tax advisory" | /services/corporate-tax-advisory-services-in-uae/ | S7 card 2, line 218 |
| L4 | "Power BI automation with Power Automate" | /insights/unlocking-power-bi-automation-with-power-automate/ | S6 point 3, line 199 |
| L5 | "data protection advisory" | /services/data-privacy-and-security-uae/ | FAQ A6, line 437 |
| P1 | `[data visualisation services](PLACEHOLDER:/services/data-visualisation-services/)` | placeholder | S8 item 03, line 263 |
| P2 | `[advanced analytics services](PLACEHOLDER:/services/advanced-analytics-services/)` | placeholder | S6 lede, line 190 |

- In-page links: "proof of concept" → #methodology (S4 card 3); "above" → #methodology (S11 Explore).
- The Microsoft product page is not linked (Section 10 point 2).

## 9. Transcript and client requirement accuracy: PASS

No transcript was supplied. Section 10 decisions 1-6 are all met:
1. No "certified" partner claim; S12 tile 1 title reads "Microsoft Power BI partner in the UAE".
2. HLB breadcrumb chain.
3. URL-agnostic.
4. 33x qualifier, $4,500 USD and the "Limited offer" badge; FAQ 9 timelines as published.
5. Static S13 asset.
6. /sugarai-crm-2/.

**The 7 accuracy corrections, checked by whole-file search:**
- **Gartner wording:** "Gartner" appears on-page only in S2b. "#1", "ranked" and "14+" appear only in Build's Flags.
- **No Arabic Copilot claim:** A8 says "Microsoft officially supports English prompts only at present". Every "Arabic" mention is about report design, training or RTL.
- **Mobile is iOS and Android only:** the only on-page "Windows" is FAQ A1's "free Windows application" for Desktop, which is correct.
- **Q&A is not featured:** there is no "Q&A" on-page. The S9 demo is person-directed.
- **Tableau and Qlik:** named only in S8 item 05, as migration sources. No price comparison.
- **"Salesforce (60+ modules)":** dropped. Salesforce appears only as a data source (S5 row 3, A3).
- **Connector caveat:** kept in S5 row 3 and A3.

None of the R1-R5 resolutions touches a correction. R1's "nothing is subcontracted" rests on source FAQ 18 ("End-to-end in-house delivery").

---

## Overall: FAIL (loop 3 of 3)

Items 5 and 7 fail. Items 1, 2, 3, 4, 6, 8 and 9 pass.

**The loop limit has been reached.** Per the standard loop-3 procedure:
- There is **no Fix-instructions section for Build.**
- The draft does **not** proceed to Deliver.
- The **Remaining issues** summary at the top of this report (R1-R5, with counted resolutions and options) goes to the Content Writer, and the pipeline reports it to the user.

The Content Writer can release the page to Deliver after applying R1-R5 (or accepting any of them as a judgment call), with a spot re-check of those sentences only.

---

Sources consulted for verification:
- [Microsoft FY26 Q4 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) and [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/)
- [Microsoft named a Leader in the 2026 Gartner Magic Quadrant (Microsoft Fabric Community)](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Microsoft-named-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for/ba-p/5262403) and [mwpro.co.uk repost](https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/)
- [The continued state of global AI diffusion in 2026 (Microsoft On the Issues)](https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/)
- [What is Microsoft Fabric (Microsoft Learn)](https://learn.microsoft.com/en-us/fabric/fundamentals/microsoft-fabric-overview), for the A7 shared-capacity statement
