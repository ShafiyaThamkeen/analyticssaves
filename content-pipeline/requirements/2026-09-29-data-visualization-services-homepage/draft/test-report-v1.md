# Test report v1: Data Visualisation Services homepage (draft-v1.md, loop 1 of 3)

Tested by: Test agent, 2026-09-30
Loop: **1 of 3** (fresh cycle; no earlier test reports in `draft/`).

---

## Priority checks (requested first): 33x, PowerUP!, competitor wording, tool names

**Result: CLEAN on the page.** Details:

| Check | Method | Page count | Notes |
|---|---|---|---|
| "33x" / "33 x" / "thirty-three" | case-insensitive grep, whole file | **0** | |
| "PowerUP" / "Power UP" | case-insensitive grep, whole file | **0** | |
| "$4,500" / "4,500" | grep, whole file | **0** | |
| "Softcrylic" | case-insensitive grep, whole file | **0** | |
| "Proud" / "Microsoft Partner" / "Partner in the Business" | case-insensitive grep | **0** | The only partner wording is "As a reselling partner" (FAQ A3, line 347), which brief 6a allows. |
| PowerUP! offer furniture: "fixed-price", "accelerator", "data dictionary", "model diagram", "transformation scripts", "published app", "report tabs", "personas", "round of revision", "file-based", "5 days", "proof of concept", "MVP" | case-insensitive grep | **0** | "fixed-price" appears only in Build's own notes (lines 395, 400), not on the page. S10 "Prototype on a defined use case" (line 269) carries no price, no deliverable list and no duration. It is the brief's own Start item, not the offer. |
| T5 competitor-matched phrases (all 19, including "comprehension", "data story", "key to unlocking", "value realisation", "in parallel with", "next-gen/next generation", "strategic asset", "information silos", "control and clarity", "like never before", "story within", "Identify patterns", "data-to-action", "like capital", "table-stakes", "every data point", "60,000") | case-insensitive grep | **0** | |
| Tab 1 [COMPETITOR-MATCHED] sentences (brief 5b; extraction 4.2 and 4.3) | read side by side (item 5.3) | **0 reused sentences** | **One residual fragment:** S7 04 (line 216) keeps the noun sequence "across the pipeline, model and semantic layer". That is the distinctive triple from the Softcrylic-matched "Optimization across pipeline, data model, and semantic layers" sentence, and Revision 4 of the Power BI page cited it as evidence of copying. The brief does permit the *concept*. Because the same sentence also rewords the Power BI page's S7 04, it is a required fix under item 5 (Fix 5c). |

**Third-party tool names (T3, plus the extra names requested).**
- I ran a case-sensitive whole-word grep for the full T3 list plus SQL, Google, AWS, Amazon, Cognos, MicroStrategy, Grafana, Kibana, Alteryx, Power Query, DAX and Dynamics.
- I also ran a case-insensitive grep for microsoft, visio, tableau, qlik, looker, d3, excel, azure, fabric, synapse, oracle, sap and salesforce.
- **Result: 0 on the page.**
  - "Microsoft" = 0 and "Visio" = 0, anywhere in the file.
  - "Teams" (capitalised) = 0. Only lowercase "teams" appears.
- **"Power BI" = 3 on the page**, all in permitted slots:
  - S11 tile 5 H3 (line 308).
  - FAQ A3 × 2 (line 347), one of them the L2 anchor.
  - The cap is 4 in total and 2 in FAQ 3. Both are respected.
- **"SugarAI CRM" = 1** (S6 card 2, line 159), as optional link L5.
- **Not tool names:**
  - "PDF" (S5 row 3, line 123) is a file format.
  - "IMD", "BARC" and "Gartner" are research bodies named for stat attribution (B5).

**Go-live condition carried from this check (Deliver, not Build).** The L2 target `/services/power-bi-partner-in-dubai-uae/` is the live partner page. The uploaded snapshot of that page (`2026-09-28-power-bi-services-homepage/inputs/hlbhamt-sibling-pages/power-bi-partner-in-dubai-uae-extracted.txt`, lines 370, 535-537 and 800) still shows the **"$4,500 PowerUP! Offer"**.
- The Content Writer has confirmed that this URL will be 301-redirected to the new Power BI page (PB brief Section 13, item 1).
- Until that happens, this page would send readers to a page that still advertises the competitor-traced offer.
- **So this page must not go live before the Power BI page has replaced or redirected that URL.** The alternative is to publish with L2 temporarily unlinked.
- The draft itself is not at fault here (see item 8, departure 5).

---

Inputs checked:
- `brief.md`, all 558 lines. Section 10 overrides Sections 1-9 where it says so.
- `draft/draft-v1.md`, all of it: page, Sources, Stats used and Flags 1-16.
- `inputs/extracted/hlb-data-viz-v4 (1).html.md`: Tab 1, the shared hero and the closing CTA, including every [DO NOT REUSE] and [COMPETITOR-MATCHED] item.
- `inputs/requirement-notes.md`.
- The structural sample, `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt` (credential grid and S4 area).
- Sibling pages, for originality and for Build's heading departures:
  - Power BI `draft/draft-v8.md` (Revision 4, the delivered state), read in full.
  - Power BI `output/power-bi-services-homepage.html`, grepped for H1-H3.
  - Advanced Analytics `draft/draft-v5.md` (delivered), read in full.
  - PB `inputs/revision-4-notes.md` and PB brief Section 13.
- The five resolved competitor pages, fetched today: instinctools, Damco, IT IDOL Technologies, Aspire Systems and Mindbowser. Softcrylic was covered through search extracts only; it renders client-side.
- Web checks: the u.ae IMD page, the BARC release and the u.ae PDPL page (all fetched), a Gartner search extract, and 8 exact-phrase originality searches.

Method:
- This session has no shell.
  - Strings, keywords, names and banned terms were checked with ripgrep on `draft-v1.md`.
  - I then excluded non-page lines: meta, draft header, chrome, structure headers, eyebrows, buttons, notes, Sources, Stats used and Flags.
- **Word count:** a manual word-by-word token count of every counted line, section by section, under the brief Section 1 rule.
  - Included: H1, H2s, H3s, ledes, the sub-block heading and line, card, tile and strip text (including the strip stat lines), S2b, bullets, tab names, taglines, FAQ questions and answers, and CTA headings and bodies.
  - Excluded: eyebrows, buttons, nav, breadcrumb, the form, the S5 "View" / "Foundation" / "Key features" labels, footnote markers, Sources and Flags. The label exclusion matches the AA precedent.

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density; branding B1-B5; T1-T6 | **PASS** |
| 2 | Word count | **PASS** (2,998) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** (3 clarity advisories) |
| 5 | Originality (competitors, Tab 1, siblings, template, web) | **FAIL** (6 sentences: 4 sibling-page echoes, one of which carries the Softcrylic noun triple; 2 Tab 1 FAQ paraphrases) |
| 6 | Stat accuracy and footnoting | **PASS** |
| 7 | Human tone / AI-detection heuristics | **FAIL** ("We + verb" opener run across S5-S7; 7 of 9 S6 backs open "We") |
| 8 | Section structure, CTAs, FAQ, internal links, systematic flow (F1-F3), Build's 5 departures | **PASS** |
| 9 | Client requirements (Section 10) and no fabricated commitments | **PASS** (1 go-live condition on L2) |

---

## 1. Keyword placement and density: PASS

On-page copy only, under the brief 2a rules. I applied the secondary lookahead by hand: I listed every hit and excluded those followed by "in (the) UAE".

| Keyword | Count | Placements (line) | Target | Result |
|---|---|---|---|---|
| Primary "data visualisation services in UAE" | **3** | H1 (22); hero lede s1 (24); S14 H2 (338) | 3-4 (hard max 5) | Pass |
| Forbidden "...services in the UAE" | **0** | | 0 | Pass |
| Secondary "data visualisation services" (lookahead) | **2** | S7 H2 (202); S11 H2 (292) | 2-3 | Pass |
| "data visualisation consulting services" | **2** | S7 intro s1 (204); S10 intro (263) | 2 (max 3) | Pass |
| "data visualisation experts in UAE" | **1** | S13 H2 (328) | 1-2 | Pass |
| "data visualisation technologies" | **1** | S5 intro s2 (96) | 1-2 | Pass |
| "data analytics and visualisation software" | **1** | FAQ Q3 (346) | 1-2, FAQ 3 only | Pass |

- **Meta title and description** (lines 1-2) match brief Section 7 character for character. Both open with "Data Visualization Services in UAE" / "Data visualization services in UAE". The z spelling is correct for meta (2a, Section 10 point 5a).
- **First 100 words:** the primary appears in the H1 and in lede sentence 1 (word 3).
- **Keyword-bearing headings are exact:** H1, S7 H2, S11 H2, S13 H2 and S14 H2 each carry the keyword string as the brief specifies.
- **T1 "HLB HAMT": 11** (range 10-15). The instances are at lines 22, 24, 56, 76, 79, 202, 292, 320, 340, 341 and 344. Excluded: nav (16), eyebrows (20, 72, 290), structure headers (70, 198, 288) and the note at 196.
- **T2 density:**
  - "visualisation" (any form, keywords included): **18** (cap 28). Lines 22, 24, 96, 202, 204, 263, 282, 292, 308, 328, 338, 340, 341, 343, 344, 346, 358 and 371.
  - "dashboard(s)": **19** (cap 35). Lines 24, 28, 44, 52, 79, 212, 213, 215, 226, 267, 270, 275, 320, 349, 350, 352, 355, 361 and 369. Build's "about 18" is one low, which does not matter.
- **T4 "UAE": 7** (cap 10). Lines 22, 24, 66, 292, 328, 338 and 356.
- **T6:**
  - On-page "visualization" with a z: **0**. The z form appears only in meta (1-2), the URL in chrome (15) and notes.
  - "certified", "#1", "award-winning", "leading", "compliant", "guarantee", "zero", "always", "instantly" and "100%": all **0**.
  - Sibling figures (200+, 7 days / seven days, Since 1999, 25/26 years, 150+, 19th, 14+, 85%, 16%, 6.67, 11 services, 40,000): all **0**.
- **2d:** 2 of the 6 S7 titles contain "Dashboard" (03 and 04). 0 of the 5 S9 titles do, and 0 of the 9 S6 titles contain "dashboard" or "visualisation".
- **Branding:**
  - **B1:** the H1 opens "HLB HAMT:".
  - **B2** holds for every required opener: hero "We deliver", S4 "HLB HAMT stands", S5 "We turn", S6 "We apply", S7 "We answer", S9 "...we deliver" (main clause), S10 "We offer" and S11 "Our team judges".
  - **B3** holds for all 9 answers: A1 "HLB HAMT delivers", A2 "HLB HAMT offers both: we design", A3 "we deliver", A4 "we put", A5 "We regularly combine", A6 "We build", A7 "We do not quote", A8 "We review" and A9 "We start".
  - **B5:** the IMD ranking is attributed to the UAE ("We build from the UAE, which ranked..."), BARC to "the 1,579 professionals surveyed" and Gartner to "organisations Gartner surveyed". "Microsoft partner" = 0.
- **Stuffing:** none. Every instance sits in its brief-assigned slot. The optional placements that were skipped (S15 primary, S4 lede "experts in UAE", S7 05 "technologies", FAQ 1 "consulting services") keep density low. Departure 4 is assessed in item 8.

## 2. Word count: PASS (2,998)

This is an independent manual count (see Method).

| Section | Count | Budget (3b) | Status |
|---|---|---|---|
| S1 | 197 | 170-200 | OK |
| S2 + S2b | 67 (strip 45 + S2b 22) | 50-70 | OK |
| S4 | 248 | 230-270 | OK |
| S5 | 343 (351 if the four "Key features" labels are counted) | 340-390 | OK (near floor) |
| S6 | 465 | 430-490 | OK |
| S7 | 405 | 360-410 | OK |
| S8 | 28 | 20-30 | OK |
| S9 | 160 | 140-170 | OK |
| S10 | 202 | 190-230 | OK |
| S11 | 146 | 120-150 | OK |
| S12 | 33 | 25-40 | OK |
| S13 | 29 | 20-30 | OK |
| S14 | 653 (H2 8 + questions 90 + answers 555) | 620-700 | OK |
| S15 | 22 | 20-30 | OK |
| **Total** | **2,998** | 2,800-3,200 (fail below 2,600 or above 3,400) | **PASS** |

- **Agreement with Build.** My count matches Build's "about 3,005" to within one or two words per section. The 7-word difference is Build counting the S5 "Key features" labels. Every section is inside its 3b budget.
- **Sub-budgets checked:**
  - Hero lede: 50 words (40-55).
  - S1 cards: 21 / 19 / 19 / 20 (15-22).
  - S4 lede: 64 (50-65).
  - S4 cards: 41 / 40 / 44 / 39 (40-50). Card 4 is one word under, which is immaterial.
  - S5 row descriptions: 44 / 45 / 45 (35-45).
  - S5 foundation body: 63 (50-65).
  - S6 intro: 30 (20-30).
  - S6 backs: 35-41 (35-42).
  - S6 taglines: 6-10 (6-10).
  - S7 bodies: 54-60 (50-60).
  - S9 intro: 40 (at cap).
  - S9 step bodies: 17-22 (15-22).
  - S10 intro: 33 (25-35).
  - S10 taglines: 10 each (8-12).
  - S10 items: 15-20 (12-20).
  - FAQ answers: 57-70 (55-70). A6 is exactly 70.
- **Word count after all required fixes** (see Fix instructions): about **3,017**. Every section stays inside its budget: S4 254, S7 404 and S14 667.

## 3. Zero em dashes: PASS

A whole-file ripgrep finds `—` (U+2014) **0**, `–` (en dash) **0** and `--` **0**. Ranges are written in words ("two to four weeks").

## 4. Grammar, spelling, punctuation: PASS

- **British spelling.** I swept for -ize/-ise, -yze, -ization, color, center, program(s), behavior, modeling/modeled, license (noun), fulfill, favor, catalog, toward, analyze, judgment, labeled, gray and mockup.
  - **0** on the page. The only regex hits were "size" and "sized", which are false positives.
  - British forms confirmed: visualisation, organisation, behaviour, utilisation, fulfilment, modelled/modelling, programme, licences, modernisation, rigour.
- **No outright grammatical errors.** Fragments appear only in UI slots (strip descriptions, taglines, tiles, S12), which is normal for UI copy.
- **Clarity advisories (not scored; word-neutral fixes offered in "Optional"):**
  - **G1. S6 card 6, sentence 2 (line 179): garden path.** "General managers and revenue teams compare properties, room types and booking channels and base pricing and staffing decisions on current figures." Three "and"s in a row make "booking channels and base pricing" read as one list.
  - **G2. S4 lede, sentence 1 (line 76): relative-clause attachment.** In "...advisory firm, and a member of the HLB International network, that also designs and builds reporting", the "that" clause lands after the network. On first read it seems to say the network designs reporting.
  - **G3. S6 card 2, sentence 2 (line 159): pronoun.** "Where your records sit in SugarAI CRM, we connect it directly as a source." "it" follows the plural "records". "connect the CRM directly" is clearer.

## 5. Originality: FAIL (6 sentences)

### 5.1 Competitor pages (5 resolved + Softcrylic extracts): clean

The five competitor pages were fetched today, and headings, taglines, section openers, process stages and FAQ answers were compared with every page line.

- **instinctools.** No match.
  - "Solve data visualization problems once...", "Treat your data like capital", "table-stakes", "data-to-action", "Knowledge transfer", "Testing and feedback-based adjustments" and "prototypes in 1-2 weeks, MVPs in 4-6 weeks" are all absent.
  - S9 step 1 ("agree the KPIs, their calculation rules, targets and the criteria that will show success") shares only the generic "success criteria" idea with instinctools stage 1 ("Aligning stakeholders on definitions, expectations, and success criteria").
- **Damco.** No sentence match.
  - "Make Every Data Point Count" = 0. "Turning Dashboards into Growth Engines", "Agreement on Service Models", "Onboarding and Documentation" and "data mining finds the secrets" are absent.
  - **Advisory L:** the S7 02 H3 "Data Preparation and Integration" equals Damco's H3 "Data Preparation & Integration". The brief prescribes this title (Section 4, S7 02), and it is a standard industry service label; PB uses "Data integration and preparation". Not scored. An optional rename is offered.
- **IT IDOL.** No match. "Next-Gen Data Platform Development", "Interactive and Efficient Dashboard Optimization", "Hands-On Workshops & Corporate Training" and the FAQ answers are absent. The tagline overlap with A1 s1 is covered in 5.3.
- **Aspire.** No match. "Decode Complicated Data to Compelling Stories" and "Revolutionize your data storytelling" are absent. "Mobile-friendly layouts" (S5 bullet, brief-prescribed) is a generic feature term.
- **Mindbowser.** No match. "Transform your boring numbers into eye-catching stories" and "pixel-perfect reports" are absent. Its Collect / Clean / Choose / Prepare / Visualize process is not the S9 shape.
- **Softcrylic** (search extracts in brief 5b, re-searched today): no sentence reused. The one residual noun sequence is handled in 5.2(d).

### 5.2 Sibling pages (delivered PB draft-v8 and AA draft-v5): 4 failures

Build rightly treated sibling echoes as a problem for headings (departure 3). The same test applies to body sentences: the pages link to each other and sit in the same cluster. Failed items are lightly reworded sentences that the brief did **not** prescribe.

**(a) S1 sub-block line (line 30), against AA's sub-block line (AA v5 line 30).**

| DV draft-v1 | AA (delivered) |
|---|---|
| "All four **draw on the same reconciled** figures." | "Every model and every report we deliver **draws on the same reconciled** data." |

- It sits in the same slot on the page.
- 5 of its 8 words mirror AA, and "figures" simply swaps in for "data".
- The brief specifies only "+ 1 sentence".

**(b) S4 card 3, sentence 3 (line 85), against AA S4 card 3, sentence 3 (AA v5 line 80).**

| DV draft-v1 | AA (delivered) |
|---|---|
| "**Every engagement then follows our [five-stage method](#methodology)**, with a review point at the end of each stage." | "**Every engagement then follows our [five-stage method](#methodology)**, and each stage ends with something you can review." |

- It is the same card in the same position.
- The first 7 words and the link are identical, and the tail rewords AA's tail.
- The brief prescribes only "then follow a [five-stage method](#methodology)".

**(c) FAQ A4, sentences 3-4 (line 350), against PB FAQ A10, sentences 3-4 (PB v8 line 373).**

| DV draft-v1 | PB (delivered) |
|---|---|
| "**Whatever the size**, we put **a working prototype** in front of you **within the first two weeks**." | "**In every case** you get **a working prototype inside the first two weeks**, so your feedback steers the rest of the build." |
| "We **firm up dates after the dashboard review**, when **the number and condition of your sources** are clear." | "HLB HAMT **confirms the timeline after discovery**, once we know **the condition of your data and how many sources** are involved." |

- The brief prescribes the facts (the ranges, the two-week prototype and "confirmed after the dashboard review"). It does not prescribe the "number and condition of your sources" rationale or the "Whatever the size / In every case" frame.
- Sentence 4 swaps synonyms slot for slot: confirm becomes firm up, timeline becomes dates, discovery becomes review, and "condition + how many sources" becomes "number and condition of sources".
- **Also an absolute-claim issue.** "Whatever the size" restores the absolute that the brief removed from the source's "We always deliver a working prototype within 2 weeks" ("No 'always'").

**(d) S7 04, sentence 2 (line 216), against PB S7 04, sentence 1 (PB v8 line 208) and the Softcrylic-matched Tab 1 sentence.**

| DV draft-v1 | PB (delivered) | Tab 1 [COMPETITOR-MATCHED] / Softcrylic extract |
|---|---|---|
| "Our engineers profile where the time goes **across the pipeline, model and semantic layer**, then fix it at that point: **aggregation tables** for large histories, **fewer queries** per page and **leaner formulas**." | "When reports drag, we tune **across the pipeline, data model and semantic layers**, **cutting query load, adding aggregation tables** over large fact tables and **replacing heavy measures** with efficient DAX patterns." | "Optimization **across pipeline, data model, and semantic layers** delivers significant performance gains." / Softcrylic: "Optimization at the **pipeline, data model, and semantic layers** yields dramatic performance increases..." |

- The brief lists these ingredients (S7 04). Even so, the result is a light rewording of PB's sentence: the same locus triple, then the same three remedies.
- It also keeps the exact noun sequence that Revision 4 identified as Softcrylic's framing. My exact-phrase search today returned only generic semantic-layer articles, not this sequence, so it is not demonstrably generic.
- Brief 5b requires the concept to be "re-expressed from scratch". Given the Content Writer's zero-tolerance instruction, the triple should go.

**Checked and acceptable (recorded so they are not reopened; advisories in "Optional"):**
- **Brief-prescribed wording** (the same treatment as AA advisory D; the brief's sibling rule covers H2s only). None of these is scored:
  - S1 lede s2, "as a firm that audits and advises on the numbers as well as engineering them", vs AA lede s2, "a firm that also audits and advises on the numbers" (advisory A).
  - The hero lede s1 frame "We deliver ... services in UAE that ..." vs AA.
  - The scope line vs AA's scope line.
  - S12 H2 vs PB's (one word different).
  - S15 H2.
  - S11 tile 3.
  - A3 "As a reselling partner, we ... supply".
  - FAQ A7's benefit list.
- **Shared technical vocabulary, not shared sentences:**
  - S9 step 3 vs PB step 3 (wireframe approval).
  - S7 05 vs PB S7 05 (migration preserving logic).
  - S7 06 vs PB S7 06 (role-based training).
  - S6 card 1 "tie back to your books" vs AA card 1 "ties back to your financial statements".
  - S10 Prototype vs AA Proof of value.
  - S10 Specialists "or on a retainer" vs PB "or retainer".
  - A6 PDPL citation vs AA A8.
- **Advisory F (not scored):** S7 03 "sees only the records their role allows" is close to PB S7 04's "sees only the data their role allows". Standard RLS phrasing, but it also repeats inside this page (A6, S11 tile 4).

### 5.3 Content source (Tab 1): 2 failures

The brief's reuse rule (Section 4) says: "Build must write new copy for every sentence, card title, tagline and FAQ answer." AA test-report-v4 set the project standard: a sentence that keeps the source's structure and swaps in synonyms fails, even when the source is HLB HAMT's own copy.

**(e) FAQ A1, sentence 1 (line 341), against Tab 1 FAQ 1, sentences 1-2.**

| DV draft-v1 | Tab 1 FAQ 1 |
|---|---|
| "Data visualisation **turns** figures **into charts**, scorecards **and interactive reports**, so patterns, **exceptions and trends** stand out **without anyone digging through tables**." | "Data visualization **transforms** raw data **into** graphical formats (**charts**, dashboards, heatmaps, **and interactive reports**) ... enabling teams to spot **trends, anomalies**, and opportunities **that would remain hidden in spreadsheets or databases**." |

- The brief prescribes the definition list ("charts, dashboards, interactive reports that make complex data readable").
- The **tail** is not prescribed. It is the source's sentence 2 with synonyms swapped: anomalies becomes exceptions, "hidden in spreadsheets or databases" becomes "without anyone digging through tables", and spot becomes stand out.
- The tail is also close to IT IDOL's tagline: "we turn complex data into clear, interactive visuals that reveal trends, patterns, and opportunities".

**(f) FAQ A2, sentence 1 (line 344), against Tab 1 FAQ 2, sentences 1-2.**

| DV draft-v1 | Tab 1 FAQ 2 |
|---|---|
| "Analytics works out what the data means, through **cleaning**, statistical testing **and modelling**; **visualisation is how** that meaning reaches the people who decide." | "Data analytics is the process of examining, **cleaning, modelling**, and interpreting data to extract insights. **Data visualization is how** those insights are communicated visually." |

- The brief's prescription is "Analytics examines and models data to produce insight; visualisation presents it so people act".
- The draft goes back to the source's own frame instead: "cleaning ... modelling" in the source's order, and the "visualisation is how [insights/meaning] [are communicated/reaches]" copula.
- Risk is low: the source leaves the live site when this page replaces it. But this is the same pattern AA's loop 3 failed, so it is caught now rather than in loop 3.

**Checked and acceptable against Tab 1:**
- **S1 cards 1-4.** Only the permitted ideas survive. Card 1 shares "complex datasets" and "KPIs" but not "visibility", "time-to-insight" or "Comprehension". Card 4 has no "data story".
- **S6 backs.** The metric lists are permitted substance ("the metric lists in each industry card"). Every framing sentence is new.
- **S7 05.** It carries the permitted "reporting while the platform is modernised" idea in new words ("at the same time", "being rebuilt", "advise your engineers", "working prototype"). The banned "in parallel with platform modernisation" and "Next-generation platforms" = 0.
- **A3-A9.** The facts are prescribed, and the wording is new. A4's ranges are prescribed. A7's list is prescribed by brief S14 FAQ 7.

### 5.4 SugarAI structural sample: clean

- These are template structural labels, which the checklist allows:
  - The S4 card H3s "What we do / Who we work with / How we deliver".
  - The S11 H2 frame.
  - The "See it in action" eyebrow.
- **Advisory B (not scored):** S11 tile 6 "Our consultants scope, build and support your reporting from Dubai..." follows SugarAI tile 6 "Consultants who scope, build and support from the UAE". The brief prescribes this wording. "from Dubai" also repeats the H3 "Delivered from Dubai".

### 5.5 Web (exact-phrase searches today): no matches

| Phrase searched | Result |
|---|---|
| "meetings open on decisions rather than disputed numbers" | No match (only generic meeting-effectiveness articles) |
| "Measures First, Visuals Second" | No match |
| "so reports get opened, not archived" | No match |
| "Who stays, who drifts" (customer lifetime value) | No match |
| "An Audit Firm's Rigour Behind Every Chart" / "Sector Blueprints Built Around the Metrics You Report" | No match |
| "Structure comes before styling" (dashboard/KPI) | No match |
| "answer a tracking query without calling the depot" | No match |
| "shift budget towards what their audiences actually respond to" / "where discounting is eating into profit" | No match |
| "pipeline, data model, and semantic layers" | Only generic semantic-layer articles, with no clear exact-sequence hit outside the Softcrylic context (see 5.2(d)) |

## 6. Stat accuracy and footnoting: PASS

| Ref | Figure | Location | Check (today) | Result |
|---|---|---|---|---|
| [1] S-1 | UAE 9th of 69 in IMD World Digital Competitiveness Ranking 2025; 1st for talent | S2b only (66) | u.ae page fetched: "ranked 9th amongst 69 countries reviewed globally"; sub-factor "1st in talent"; updated 25 Nov 2025. The 2026 edition is not due until November, so this is the latest. Attributed to the UAE, not HLB HAMT (B5). | Pass |
| [2] S-2 | 1,579 professionals; data quality management ranked first, level with data security and privacy | S5 foundation only (134) | BARC release fetched: 1,579 respondents; data quality management first, 7.9/10, tied with data security and privacy; 12 Nov 2025. The 7.9 score is not quoted, which is correct. Framed as the reason HLB HAMT validates first, not as a scare line. | Pass |
| [3] S-3 | Only 22% had defined, tracked and communicated business impact metrics for most D&A use cases | S9 intro only (238) | Gartner release (HTTP 403 to fetch). Search extract plus BigDATAwire: "Only 22% ... for the bulk of their D&A use cases"; 504 leaders, Sep-Nov 2024; released 20 Feb 2025. "most of" is a fair rendering of "the bulk of". About 19 months old, inside the 2-3-year window. | Pass |
| [4] F1 | UAE PDPL, Federal Decree-Law No. 45 of 2021 | FAQ 6 only (356) | u.ae page fetched: "Federal Decree Law No. 45 of 2021 Regarding the Protection of Personal Data", in force 2 Jan 2022. The draft says "in line with", never "compliant" or "guarantees". | Pass |
| CS1 | 9 sectors | S2 item 1 only (51) | Tab 1 industry cards 01-09. HLB HAMT's own content, so no footnote. | Pass |
| FAQ 4 timelines | 2-4 wk / 6-10 wk / 3-6 mo / prototype within 2 wk | FAQ 4 only (350) | Tab 1 FAQ 4, confirmed by Section 10 point 5b. No "7 days". | Pass (wording issue in 5.2(c)) |

- **Markers run in order of appearance:** [1] S2b, [2] S5, [3] S9, [4] FAQ 6. The Sources list matches.
- **Each stat appears once.** No FAQ restates 9 sectors, 9th of 69, BARC or 22%.
- **No cross-project duplication.** A ripgrep of every other requirement for "1,579", "9th of 69", "Only 22%" and "Trend Monitor 2026" finds no page use; the only hits are unrelated lines in AA test reports.
- **No invented figures.** No competitor outcome numbers appear (30%, 2x, 80%, 40% and 1,850+ = 0).

## 7. Human tone / AI-detection heuristics: FAIL

**Stock-phrase sweep: 0 hits on the page.** The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just", "in conclusion", cutting-edge, game-changing, revolution-, unleash, delve, landscape, ever-evolving, state-of-the-art, synergy, supercharge, transformative, navigate, pivotal, crucial, furthermore, moreover, additionally, ensure, comprehensive, innovative, dynamic, effortless, stunning, insight(s), data-driven, end-to-end, powerful, foster, realm, embark, paramount, "at the heart of", "next level", "whether you're", world-class and best-in-class.

The copy is specific and well observed in places. Examples: "customer service can answer a tracking query without calling the depot", "which lines move, which sit, and where discounting is eating into profit", "rather than drifting back to spreadsheets".

**Failure: a long run of "We + verb" paragraph openers, and templated S6 backs.**
- **S6 backs.** 7 of 9 open "We + verb": card 1 "We build", 2 "We bring", 3 "We map", 4 "We design", 7 "We build", 8 "We connect" and 9 "We measure". Cards 5 and 6 front a phrase and then use "we" ("From HR and payroll records, we produce"; "For hotels and resorts, we track"). So all 9 use the same "[we] [verb] [metric list]" sentence 1.
- **Second sentences.** 6 of 9 second sentences follow one frame, "[role] managers/leaders/teams see/compare/spot..." (cards 4-9).
- **Run length in page order.**
  - S5 row 1 through S6 card 4 is **9 consecutive "We + verb" paragraphs**: "We design", "We build", "We produce", "We build this layer", "We apply", "We build", "We bring", "We map", "We design".
  - After two fronted-"we" cards, card 7 through S7 01 is **5 more**: "We build", "We connect", "We measure", "We answer", "We start".
  - "We build" opens 4 of those paragraphs.
- **Project precedent.** PB test-report-v5 item 7 failed all 6 S6 backs opening "We + verb". AA test-report-v2 item 7 failed 5 of 6 S6 backs plus a 10-paragraph run. B2 requires an HLB-led first sentence for **section intros only**, not for every card. The S5 rows are excluded from the finding because the brief mandates "opening with an HLB HAMT action" there, but they lengthen the run a reader actually experiences.
- **Fix 7** varies 4 S6 openers (cards 1, 2, 4 and 8) and keeps HLB HAMT as the actor through "our". It is word-neutral in total.

**Tone advisories (not scored; suggestions in "Optional"):**
- **C.** S11 tile 5 says "firm" twice ("One firm for Power BI..." / "from the same firm"), and "One firm for" echoes AA tile 3 "One firm for the follow-through".
- **D.** S4 card 4: the H3 "Support after launch" is followed at once by "After launch, our team...".
- **E.** S8 body (228) and S10 "Dashboard review" (268) say nearly the same thing ("current reports, sources and KPIs ... first build"). Both are brief-prescribed, so vary one.
- **F.** RLS phrasing appears three times ("sees only the records their role allows", "the records their role permits", "sees only the data it should").
- **I.** S12 body opener "A sample executive view" is near PB's "A sample of the executive views we build", and "Shown on illustrative data" is near AA's "Illustrative view on sample data".

## 8. Section structure, CTAs, FAQ, internal links, flow, Build's departures: PASS

**Order and format.** The page follows the 3b skeleton exactly:
- S0 breadcrumb (brief chain).
- S1: H1 + lede + buttons + sub-block heading and line + 4 H3 cards + scope line. No stats.
- S2: 4 strip items with no heading tags, plus S2b and the reference link.
- S3: 7 anchor labels in brief order.
- S4: H2 + lede + 4 H3 cards.
- S5: H2 + intro + 3 "View" rows (H3, description, 5 bullets) + H3 foundation block with 4 bullets.
- S6: H2 + intro + 9 flip cards (H3, tagline, back). No buttons and no pill row.
- S7: H2 + intro + 01-06 H3.
- S8: H2 + body + button.
- S9: H2 + intro + 5 H3 steps, highlighted band. No durations and no button.
- S10: H2 + intro + 3 tabs with 2 H3 items each. No featured card and no button.
- S11: H2 + intro + 6 H3 tiles.
- S12: H2 + body, static placeholder.
- S13: H2 + body + button.
- S14: H2 + 9 H3 Q&As, single accordion.
- S15: H2 + body + form.
- S16: footer.

Other structure checks:
- There is exactly one H1.
- "Why AI Changes CRM" has no equivalent (Section 10 point 3).
- There is no case study block (point 6).
- No SugarAI, PB or AA H2 is reused verbatim.

**CTAs: exactly 4, in the specified places.**
- CTA 1: hero "Book a free consultation" (#contact) + "Explore our services" (#services) (26).
- CTA 2: S8, after S7, "Request a dashboard review" (230). The review is not called "free".
- CTA 3: S13, after S12, "Talk to our visualisation team" (332). The body says "free consultation".
- CTA 4: S15 form "Schedule a Consultation" (373). The H2 says "Free".
- Nothing else is a button: S5, S6, S9, S10, S11 and S12 have none. The S2b "Read the ranking" link (68) is the recognition-bar reference link, not a conversion CTA (brief 3d). The in-text links "five-stage method" (85) and "agree the measures" (359) → #methodology are allowed.

**FAQ.** 9 Q&As with H3 questions. Answers run 57-70 words. The order matches brief S14 and 3c step 9 exactly. See F3 below.

**Internal links (anchors exact; all real, no placeholders):**
- L1 "digital transformation and analytics services" → https://hlbhamt.com/services/digital-transformation-uae/ (S4 lede, 76).
- L2 "Power BI services" → https://hlbhamt.com/services/power-bi-partner-in-dubai-uae/ (FAQ 3, 347).
- L3 "advanced analytics services" → https://hlbhamt.com/services/advanced-data-analytics-uae/ (FAQ 2, 344).
- L4 "data protection advisory" → https://hlbhamt.com/services/data-privacy-and-security-uae/ (FAQ 6, 356).
- L5 "SugarAI CRM" → https://hlbhamt.com/sugarai-crm-2/ (S6 card 2, 159).
- There is no self-link and no link to any page on the "do not link" list.

**Systematic flow (Content Writer instruction 4; F1-F3).**
- **F1 bridges (spot-checked every one Build claims, plus S8, S11 and S13): pass.**
  - S4 "HLB HAMT stands behind those four outcomes..." picks up S1's four cards.
  - S5 "We turn the four outcomes above into three kinds of reporting, each resting on the measures and model agreed at the start" picks up S1 and S4 card 3.
  - S6 "We apply those three kinds of reporting to the metrics each sector actually runs on" picks up S5's three rows.
  - S7 "We answer those sector needs with six offerings" picks up S6.
  - S8 "Show us your current reports..." follows the services naturally.
  - S9 "Whichever services you choose, we deliver them in five stages" picks up S7 and S8.
  - S10 "...in three shapes built around the five stages above" picks up S9.
  - S11 "Our team judges its work by whether your people trust the figures and open the reports" is a reassurance opener. F1 does not require a bridge here.
  - S13 follows the S12 teaser.
  - None of these reads as a cold restart.
- **F2 no forward-leaking: pass.**
  - **Services:** only S4 card 1's one-sentence summary appears before S7. The S5 rows describe capabilities, not buyable services.
  - **Stages:** only S4 card 3's "five-stage method" link appears before S9. S7 03's "once you have approved the wireframes" sits after S7 begins and is brief-prescribed.
  - **Engagement options:** none before S10, apart from the brief-mandated S8 dashboard review CTA.
  - **Sector examples:** none before S6, apart from the S1 lede's "from finance to operations". S4 card 2 names functions and roles (finance directors, operations and commercial heads), not sectors. The S1 card 2 "sales, cost and operational data" is data types.
- **F3 FAQ order: pass.** The order runs definition + what we deliver → vs analytics → software → time → disconnected sources → accuracy and security → return → existing dashboards → migration. That is definition to decision, exactly as brief S14 lists it.

**Build's five self-reported departures.**

| # | Departure | Ruling | Reason |
|---|---|---|---|
| 1 | S2 item 1 drops "from financial reporting to events and media" | **Accept** | The brief's own S2 wording conflicts with its F2 rule, which allows only one sector example before S6. Build resolved the conflict in favour of the Content Writer's explicit flow instruction. The replacement "with dashboard blueprints ready to adapt to your data" is accurate (the S6 intro says exactly that) and adds no claim. |
| 2 | S2 + S2b at about 67 words | **Accept; fits (67, cap 70)** | Correction to Build's note: the budgets do **not** conflict. The minimum possible is 7 label words + 4 × 8 + 25 = 64, which fits within 70. As drafted, S2b is **22 words, 3 under its 25-35 outline range**, while the combined 3b budget (the binding one) is met. Not scored. Optional fix J brings S2b to 25 and the total to 70. |
| 3 | Five H2s and three S11 tile titles reworded | **Accept; all necessary** | Checked against PB v8 / output HTML and AA v5 headings. S6's suggestion ("Dashboards Shaped Around How Your Sector Runs") matched 4 words of PB's "Dashboards Shaped Around the Decisions You Make". S9's ("From First Workshop to...") repeated AA's "Five Stages From First Workshop to Live Forecast". Tile 5's suggestion was almost AA's tile 5 "Analytics and Power BI from one partner". "In-region team" is PB's and SugarAI's tile verbatim. S4 (PB "Great Dashboards Start With the Numbers Behind Them"), S5 (PB "One semantic model, one version of the numbers" and AA "One data foundation. Three ways...") and S10 (AA "Start Where Your Data Is, Then Scale", the same "Start..., Then [verb]" shape) were close enough to justify a change. Tile 2's suggestion duplicated S2 item 2's "Source to screen". Every replacement heading is original (5.5, no web hits), and no keyword-bearing heading was touched: H1, S7, S11, S13 and S14 are exact. Minor echo: advisory C. |
| 4 | Primary keyword 3, not 4 | **Accept** | The brief's target is "3-4 (hard max 5)" and the S15 instance is marked "(4, optional)", so 3 is fully compliant, with all 3 mandatory slots filled (H1, lede s1, S14 H2). Build's rationale is only half right: AA's S15 does use "Our advanced analytics services in UAE start with a free consultation", but PB's S15 does not. AA alone is still a reasonable reason to avoid the echo. |
| 5 | L2 → `/services/power-bi-partner-in-dubai-uae/` | **Accept as the interim choice** | This is the brief's own Section 8 default. The Content Writer confirmed the URL will be 301-redirected to the new PB page (PB brief Section 13, item 1). The PB final URL is still open (PB sources log lines 3 and 101). Either way the link reaches Power BI content, and it is a real link, not a placeholder. **Go-live condition:** the live page at that URL still shows "$4,500 PowerUP! Offer" (snapshot lines 370, 535-537 and 800). Do not publish this page with L2 live until the PB page has replaced or redirected that URL. Swap L2 to the PB final URL once it is set. |

## 9. Client requirements (Section 10) and fabricated commitments: PASS

- **Point 1 (replace in place):** the canonical and URL note are at line 15, and the Deliver handoffs are in Flag 8. The AA L3 edit is still outstanding for Deliver.
- **Point 2 (33x / PowerUP!):** absent (see the priority checks).
- **Point 3:** there is no AI/CRM section.
- **Point 4 (4 CTAs; S8 not free; S13 and S15 free):** confirmed (item 8).
- **Point 5a:** meta uses the z spelling and the page uses the s spelling (item 1).
- **Point 5b:** FAQ 4 uses Tab 1's ranges (two to four weeks / six to ten weeks / three to six months / prototype within the first two weeks). "7 days" and "seven days" = 0. The "Whatever the size" absolute is addressed by Fix 5d.
- **Point 6:** there is no case study. No "delivered for X clients" claim is made; S6 blueprints are framed as starting points (149).
- **Point 7 (post-launch support as a real offering):** present in S4 card 4 (88), S7 06 (222), S9 step 5 (253) and S10 Managed support (284), covering monitoring, fixes, tuning, new views and training. **0** SLAs, hours, "24/7", response times or frequencies. "Monthly pack" (82) describes a client's report, not support. "Each night" (210) describes a refresh pattern.
- **Point 8:** S12 is a static placeholder, and its copy does not depend on a specific asset.
- **Point 9:** there is no Arabic, RTL or bilingual content (0 hits), and no "CRM Training & Adoption" or "customer intelligence" leftovers.
- **Requirement notes:**
  - The page talks about HLB HAMT's service. Definitions appear only in FAQ 1-2, and each pivots to HLB HAMT.
  - Real links go to both siblings as separate pages.
  - Visio and Microsoft = 0.
- **No transcript** was supplied.
- **No fabricated commitments.** "Reply within one business day" (371) is the site-standard promise prescribed by brief S15. There are no prices or durations outside FAQ 4, and no client counts.
- **Housekeeping (not scored):**
  - Build's Flag 1 says the six-item deliverable package is "named in the brief's Section 10 instruction". It is in Section 5b, not Section 10.
  - Brief lines 553-557 are stray template lines, which Build correctly ignored (Flag 16).

---

## Overall: FAIL (loop 1 of 3)

- **Item 5, originality (6 sentences):**
  - Three body sentences lightly reword the delivered AA and PB sibling pages: the S1 sub-block line, S4 card 3 s3 and FAQ A4 s3-s4.
  - A fourth, S7 04, rewords PB S7 04 and keeps the Softcrylic "pipeline, (data) model and semantic layer(s)" noun triple.
  - Two FAQ definition sentences (A1 s1, A2 s1) swap synonyms into Tab 1's FAQ 1 and FAQ 2 wording.
- **Item 7, tone:** a 9-paragraph "We + verb" opener run from S5 into S6, with 7 of 9 S6 backs opening "We". PB test-report-v5 and AA test-report-v2 both failed this same pattern.
- **Everything else passes**:
  - The critical exclusions are clean: 33x, PowerUP!, $4,500, Softcrylic and "Proud Microsoft Partner" are all 0, and no third-party tool name appears beyond 3 permitted "Power BI" and 1 "SugarAI CRM".
  - Keywords: 3 / 2 / 2 / 1 / 1 / 1. "HLB HAMT" 11, "visualisation" 18, "dashboard(s)" 19, "UAE" 7.
  - Word count 2,998.
  - Zero em dashes.
  - British spelling.
  - All four stats verified and footnoted in order.
  - Exactly 4 CTAs.
  - F1-F3 flow holds.
  - All 5 departures accepted.
  - Real L1-L5 links.
- **All fixes are sentence-level and keep every section inside budget.** The projected total afterwards is about 3,017.

## Fix instructions (for Build)

Apply these exactly, or write an equivalent that meets the stated constraint. Update the FAQPage schema text for A1, A2 and A4 to match.

**Fix 5a (required). S1 sub-block line (line 30).**
- **Replace:** "All four draw on the same reconciled figures."
- **With:** "Each one rests on figures checked before publication."
- Word-neutral (8 words), so S1 stays at 197.
- Constraint: do not use "draw(s) on the same reconciled" or "one version of the numbers" (PB).

**Fix 5b (required). S4 card 3, sentence 3 (line 85).**
- **Replace:** "Every engagement then follows our [five-stage method](#methodology), with a review point at the end of each stage."
- **With:** "From there, the work runs through our [five-stage method](#methodology), which one core team carries from the opening KPI session to launch and beyond."
- Effect: +6, so card 3's body is 50, S4 is 254 and the #methodology link is kept.
- Constraint: do not open with "Every engagement then follows our", and do not end on a "review at the end of each stage" idea (AA). Avoid "From First Workshop" (AA S9 H2).

**Fix 5c (required). S7 04, sentence 2 (line 216).**
- **Replace:** "Our engineers profile where the time goes across the pipeline, model and semantic layer, then fix it at that point: aggregation tables for large histories, fewer queries per page and leaner formulas."
- **With:** "Our engineers time each page, find whether the delay sits in the data refresh, the model or the calculations, and fix it there: aggregation tables, fewer queries per page, leaner formulas."
- Effect: -1, so S7 04's body is 59 and S7 is 404.
- Constraint: the noun sequence "pipeline, (data) model and semantic layer(s)" must not appear anywhere on the page. It is the Softcrylic / Tab 1 [COMPETITOR-MATCHED] framing, and PB S7 04 also uses it. Leave sentences 1 and 3 and the H3 unchanged.

**Fix 5d (required). FAQ A4, sentences 3-4 (line 350).**
- **Replace:** "Whatever the size, we put a working prototype in front of you within the first two weeks. We firm up dates after the dashboard review, when the number and condition of your sources are clear."
- **With:** "Within the first two weeks, you normally have a working prototype on your own data to review. We commit to dates at the end of the dashboard review, when we have seen your reports, sources and KPIs first-hand."
- Effect: +3, so A4 is 66. B3 holds through "We commit". The Tab 1 facts are unchanged, with no "7 days" and no absolute.
- Constraint: do not use "Whatever the size", "In every case", "number and condition of your sources" or "so your feedback steers" (PB A10). Leave sentences 1-2 unchanged.

**Fix 5e (required). FAQ A1, sentence 1 (line 341).**
- **Replace:** "Data visualisation turns figures into charts, scorecards and interactive reports, so patterns, exceptions and trends stand out without anyone digging through tables."
- **With:** "Data visualisation is the design of charts, dashboards and interactive reports that make a large body of figures readable in minutes and open to follow-up questions."
- Effect: +4, so A1 is 64. "dashboard(s)" rises to 20 (cap 35).
- Constraint: no "trends/anomalies/exceptions ... hidden in / digging through spreadsheets/tables" tail (Tab 1 FAQ 1, IT IDOL tagline). Leave sentences 2-3 unchanged.

**Fix 5f (required). FAQ A2, sentence 1 (line 344).**
- **Replace:** "Analytics works out what the data means, through cleaning, statistical testing and modelling; visualisation is how that meaning reaches the people who decide."
- **With:** "Analytics is the investigative work of testing and modelling data to explain a result. Visualisation is the presentation layer that turns those findings into pages a manager can act on."
- Effect: +7, so A2 is 64.
- Constraint: no "visualisation is how ..." frame, and no "cleaning ... modelling" source sequence. Do not use "decides how people see them" (AA A9). Leave "One without the other tends to stall.", the HLB HAMT / L3 sentence and "Both run on the same governed data." unchanged.

**Fix 7 (required). Vary four S6 back openers; word-neutral in total.**
- **Card 1 s1 (line 154).**
  - Replace: "We build finance views that track revenue streams, cost structure, profitability trend and risk exposure, giving leadership a clear basis for deciding where to invest next."
  - With: "Our finance views track revenue streams, cost structure, profitability trend and risk exposure, giving leadership a clear basis for deciding where to invest next."
  - Effect: -2, back 37.
- **Card 2 s1 (line 159).**
  - Replace: "We bring customer data together to show behaviour, engagement, satisfaction, retention and lifetime value, grouped into segments that tell account teams where to focus."
  - With: "Behaviour, engagement, satisfaction, retention and lifetime value are set side by side in our customer views, with segments that tell account teams where to focus."
  - Effect: +1, back 39. Keep sentence 2 and the L5 link. Optional G3 can be applied at the same time.
- **Card 4 s1 (line 169).**
  - Replace: "We design production reporting around efficiency, quality, downtime and resource utilisation, broken down by line, shift and product."
  - With: "Production reporting from our team tracks efficiency, quality, downtime and resource utilisation, broken down by line, shift and product."
  - Effect: +1, back 37.
- **Card 8 s1 (line 189).**
  - Replace: "We connect order, stock and sales data to report fulfilment, warehouse efficiency, demand by product and channel performance, with margin shown at each level."
  - With: "Order, stock and sales data feed our reporting on fulfilment, warehouse efficiency, demand by product and channel performance, with margin shown at each level."
  - Effect: 0, back 41.
- **Result:**
  - S6 backs open: Our finance views / Behaviour... / We map / Production reporting... / From HR..., we / For hotels..., we / We build / Order, stock... / We measure.
  - The longest literal "We + verb" run outside the brief-mandated S5 rows is 3 (card 9 → S7 intro → S7 01). S6 stays at 465.
- **Do not change** the S6 intro, which is a B2 slot, or any S5 row opener, which the brief mandates.

**Totals after all required fixes:** S1 197, S4 254, S6 465, S7 404, S14 667. Page total about **3,017**. Every section stays inside its 3b budget. Keyword, "HLB HAMT", "UAE" and "visualisation" counts are unchanged; "dashboard(s)" becomes 20.

**Do not change anything else.** In particular, leave the keyword headings, all stat sentences, the S2 strip, CTAs, links and F1 bridge sentences as they are.

### Optional (recommended; not needed to pass; each within budget)

- **A.** S1 lede s2 (24). This is brief-prescribed wording, but it echoes AA's lede ("a firm that also audits and advises on the numbers"). Option: "HLB HAMT designs and builds each dashboard and report on integrated, governed data, and our accountants check the numbers as closely as our engineers build them." (+1, S1 198)
- **B.** S11 tile 6 body (312). Change "from Dubai" to "locally". This removes the echo of the H3 and of SugarAI's "scope, build and support from the UAE". (-1)
- **C.** S11 tile 5 body (309). Replace with: "Reporting today, with forecasting and prediction added when your data is ready, without changing partners." (-1) This removes the second "firm".
- **D.** S4 card 4 s1 (88). Change "After launch, our team monitors..." to "With reporting in use, our team monitors...". (+1; do not use PB's "Once reports are live")
- **E.** S10 Dashboard review body (268). Replace with: "A short look at how your current reporting is built and used, ending with a recommended first build." (0) This stops it restating the S8 body.
- **F.** S11 tile 4 (306). Change to "Each audience sees its own slice of the data, with access revisited whenever your organisation changes shape." (0) This reduces the three near-identical RLS phrasings.
- **G1.** S6 card 6 s2 (179). Change "...booking channels and base pricing..." to "...booking channels, then base pricing...". (0)
- **G2.** S4 lede s1 (76). Replace with: "HLB HAMT stands behind those four outcomes as a licensed audit, tax and advisory firm that also designs and builds reporting, and as a member of the HLB International network." (+1)
- **G3.** S6 card 2 s2 (159). Change "we connect it directly" to "we connect the CRM directly". (+1)
- **I.** S12 body (322). Change "A sample executive view:" to "What you would see:". (+1) Also change "Shown on illustrative data." to "Built on illustrative figures." (0)
- **J.** S2b (66). Change "and 1st for talent" to "and 1st of all 69 for talent". (+3) S2b becomes 25 and the strip total 70.
- **L.** S7 02 H3 (209). Optionally rename to "Source Integration and Data Modelling" to move off Damco's H3. Brief-prescribed, so Build's discretion.

---

Sources consulted for verification:
- [UAE Government portal, Global digital competitiveness](https://u.ae/en/about-the-uae/uae-competitiveness/global-digital-competitiveness): 9th of 69; 1st in talent; updated 25 Nov 2025.
- [BARC, Data, BI and Analytics Trend Monitor 2026](https://barc.com/news/barc-publishes-the-data-bi-and-analytics-trend-monitor-2026/): 1,579; data quality management first, 7.9, tied with security and privacy; 12 Nov 2025.
- [Gartner press release, 20 Feb 2025](https://www.gartner.com/en/newsroom/press-releases/2025-02-20-gartner-survey-finds-one-third-of-cdaos-cite-measuring-data-analytics-and-ai-impact-as-top-challenge) (search extract) and [BigDATAwire](https://bigdatawire.com/2025/02/24/cdoas-are-struggling-to-measure-data-analytics-and-ai-impact-gartner-report): 22%, "the bulk of their D&A use cases".
- [UAE Government portal, Data protection laws](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws): Federal Decree-Law No. 45 of 2021.
- Competitor pages fetched today:
  - [instinctools](https://www.instinctools.com/data-visualization/)
  - [Damco](https://www.damcogroup.com/data-visualization-services)
  - [IT IDOL Technologies](https://itidoltechnologies.com/technologies/data-visualization-services/)
  - [Aspire Systems](https://www.aspiresys.com/data-and-ai-solutions/data-management/data-visualization-services)
  - [Mindbowser](https://www.mindbowser.com/data-visualization-services/)
- Softcrylic: search extracts only (client-rendered). Also consulted: [GoodData, What is a semantic layer](https://gooddata.com/blog/what-is-a-semantic-layer) and [IBM, What is a semantic layer](https://ibm.com/think/topics/semantic-layer), generic results for the "pipeline, data model, and semantic layers" search.
- The exact-phrase searches in 5.5 returned no matches.
