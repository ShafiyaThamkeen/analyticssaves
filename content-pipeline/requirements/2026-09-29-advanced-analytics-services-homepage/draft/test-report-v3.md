# Test report v3: Advanced Analytics Services homepage (draft-v3.md, loop 2 of 3)

Tested by: Test agent, 2026-09-29
Loop: **2 of 3.** One more Build→Test loop is available after this one.

Inputs checked:
- `brief.md`, all of it. Section 10 (Content Writer decisions) overrides Sections 1-9 where it says so.
- `draft/draft-v3.md`, all of it: page, Sources, Stats used and all 11 Flags.
- `draft/draft-v2.md` and `draft/test-report-v2.md`. I diffed v2 and v3 line by line.
- `inputs/extracted/hlb-data-viz-v4 (1).html.md` (Tab 2 source, including the [DO NOT REUSE] intro paragraphs and all 7 FAQ answers).
- `inputs/competitor-content/` (all four raw texts plus `research-summary.md` for Apexon and Softcrylic).
- `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`.
- The delivered Power BI homepage, `2026-09-28-power-bi-services-homepage/draft/draft-v7.md`, all of it.
- Web: PwC and HLB stat checks, plus exact-phrase searches for the new v3 sentences and other distinctive lines (listed in 5.5).

Method:
- There was no shell. Names, keywords, characters and links were checked with ripgrep on `draft-v3.md`.
- **Word count:** I wrote the counted copy of every section to a scratch file, one section per line. I then machine-counted whitespace-delimited tokens with ripgrep offset probing and confirmed every section boundary by line number. Exclusions follow the brief Section 1 rule, the same as loop 1.

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density, branding B1-B5, T1-T6 | **PASS** |
| 2 | Word count | **PASS** (2,737, exact machine count) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** |
| 5 | Originality (competitors, content source, SugarAI template, Power BI sibling, web) | **FAIL** (3 sentences; see 5.4) |
| 6 | Stat accuracy and footnoting | **PASS** |
| 7 | Human tone / AI-detection heuristics | **PASS** (loop-1 opener run fixed; advisories only) |
| 8 | Section structure, CTAs, FAQ, internal links | **PASS** |
| 9 | Client requirements (Section 10) and no fabricated commitments | **PASS** |

### Loop-1 fixes: all 5 applied verbatim

Each v3 line matches, word for word, the replacement text specified in test-report-v2.md. No other page line changed between v2 and v3, apart from advisory A.

| Fix | Location (v3 line) | Specified in test-report-v2 | In draft-v3 | Match |
|---|---|---|---|---|
| 5a | S5 row 1, s1 (96) | "We run regression and correlation analysis on the transactions and ledger lines that sit behind a KPI movement." | Identical | Yes |
| 5b + 7b | S6 card 5 back (166) | "Our clustering models group customers by what they buy, how often and how much they spend, so marketing and sales can target, retain or upsell each segment on its own terms." | Identical | Yes |
| 5c | FAQ A7, s3 (347) | "Where the numbers come from many systems at enterprise scale, we build a data lakehouse instead, pairing a lake's flexibility with a warehouse's structure through the layered design described above." | Identical | Yes (but see 5.4(c): this wording, which was mine, recreates a sibling-page frame) |
| 7a | S6 card 3 back, s1 (156) | "Signals such as falling order frequency, shrinking spend or rising complaints drive our churn score for each customer." | Identical | Yes |
| 7c | S7 item 03, s1 (197) | "Star schemas built around the KPIs you already report on keep queries fast and give every measure one agreed definition." | Identical | Yes |
| Adv. A | S2 item 1 (47) | Full stop added | Present | Yes |

- Build's word-count arithmetic is also right. S5 goes 322 → 321, S6 stays at 320, S7 goes 350 → 349 and S14 goes 630 → 633. The total is **2,737**, which my machine count confirms exactly.
- The "We + verb" run is broken.
  - S6 backs now open We / Our models / Signals / We / Our clustering models / We.
  - S7 now opens We / We / We / Star schemas / We / We / Our team (intro plus items 01-06).
  - The longest run is 3 within a section (S7 intro, 01, 02; Build's Flag 11 says 2 because it counts items only). Across the S6/S7 break it is 4 (card 6, S7 intro, 01, 02), split by the pill row and the S7 H2. The loop-1 run was 10.
- **Loop-1 item 7 is resolved.**

### Ruling on Build's Flag 11: the repeated "Our [X] models group customers by ..." frame

**Fix it now, using Build's suggested rewrite.** The repeated shape is a minor tone issue: two sentences about 40 lines apart, in different sections. On tone alone I would only make it advisory. The real problem is where the S7 wording comes from.

- S7 item 05, sentence 2 (line 205), opens "Our segmentation models group customers by behaviour and value". That clause is spliced from the same Tab 2 FAQ 6 answer that loop 1 failed on S6 card 5:
  - Source sentence 3 opens "**Our segmentation models** use machine learning...".
  - Source sentence 1 reads "...uses data analytics to **group customers by behavior, value**, preferences, or demographics."
- 8 of the clause's 9 words come from those two source sentences, in the source's order. The only other word is "and". I missed this in loop 1. After loop 1's card 5 fix, it is the last echo of FAQ 6 left on the page. Leaving it would be inconsistent with the loop-1 ruling.
- Build's alternative removes both the source splice and the repeated frame. It keeps S7 at 344 words, inside its 330-380 budget. It is **Fix 5d** below.
- The new S6 card 5 wording is fine as it stands. "Group customers by what they buy, how often and how much they spend" is the generic RFM (recency, frequency, monetary) description of behavioural segmentation. It shares only the 3-word verb phrase "group customers by" with the source, and the web has no exact match (5.5).

---

## 1. Keyword placement and density: PASS

On-page copy only, using the brief Section 2a rules and the lookahead logic.

| Keyword | Count | Placements (v3 line) | Target | Result |
|---|---|---|---|---|
| Primary "advanced analytics services in UAE" | **4** | H1 (22); hero lede s1 (24); S14 H2 (326); S15 body (359) | 3-4 (max 5) | Pass |
| Secondary "advanced analytics services" (not followed by "in (the) UAE") | **3** | S7 H2 (183); S10 intro (250); S11 H2 (281) | 2-3 | Pass |
| "advanced analytics company in UAE" | **1** | S4 lede s1 (71) | 1 (max 2) | Pass |
| "data analytics and automation" | **2** | S7 intro (185); S11 tile 2 H3 (288) | 2-3 | Pass |
| Forbidden "advanced analytics services in the UAE" | **0** on page | Flags line 403 only | 0 | Pass |

- **Meta title and description** (lines 1-2) match brief Section 7 exactly, and both lead with the primary keyword.
- **H1 and the first 100 words** carry the primary keyword: H1 plus lede sentence 1.
- **T1 "HLB HAMT": 11** (range 9-14), at lines 22, 61, 71, 161, 176, 183, 281, 283, 308, 329 and 353. Excluded: nav (16), eyebrows (20, 67, 279) and structure headers (65, 179, 277).
- **T2 "advanced analytics", any form: 12** (cap 18).
- **T4 "UAE": 8** (cap 10). Both counts were machine-counted on the scratch copy.
- **T3 third-party names.** I ran a case-sensitive whole-word sweep for SQL Server, SQL, Oracle, SAP, NetSuite, Salesforce, Dynamics (365), Tally, QuickBooks, BigQuery, Snowflake, Azure, Fabric, Synapse, Databricks, Excel, Python, Tableau, Qlik, Copilot, Kimball, Microsoft, AWS, Google, Looker, SharePoint, Teams and Power Automate. The page has **0** hits.
  - "Power BI" = **4**: S11 tile 5 H3 (297), tile 5 body (298), Q9 (352) and A9 (353). That is the maximum, and only in the two permitted slots. Line 299 is a Deliver note, not copy.
  - Competitor names appear only in Flags (386, 392).
- **T5 and T6: 0 hits on the page.** This covers the competitor-derived phrases, "zero manual intervention", "certified", "#1", "award-winning", "leading", "guarantee" and the sibling-page stats.
- **2d.** 2 of the 6 S7 titles contain "analytics" (03, 04). 0 of the 5 S9 titles do.
- **Branding:**
  - **B1:** the H1 opens "HLB HAMT:".
  - **B2** holds for every section opener: hero "We deliver", S4 "HLB HAMT is", S5 "We treat", S6 "We start", S7 "We run", S9 "We run", S10 "We package", S11 "HLB HAMT pairs".
  - **B3** holds for all 9 answers.
  - **B5:** "network-wide revenue", and the PwC figures are credited to "CEOs surveyed".
- **Stuffing:** none. Every keyword sits in its assigned slot.

## 2. Word count: PASS (2,737)

Fresh machine count on the scratch copy. I confirmed each section's end token by probing the token offsets either side of it.

| Section | Count | Budget (3b) | Status |
|---|---|---|---|
| S1 | 154 | 130-160 | OK |
| S2 + S2b | 70 | 50-70 | OK |
| S4 | 259 | 220-260 | OK |
| S5 | 321 | 320-380 | OK |
| S6 | 320 | 260-320 | OK (at cap) |
| S7 | 349 | 330-380 | OK |
| S8 | 28 | 20-30 | OK |
| S9 | 157 | 130-160 | OK |
| S10 | 210 | 170-220 | OK |
| S11 | 150 | 120-150 | OK (at cap) |
| S12 | 30 | 25-40 | OK |
| S13 | 27 | 20-30 | OK |
| S14 | 633 (A7 = 62) | 550-660 | OK |
| S15 | 29 | 20-30 | OK |
| **Total** | **2,737** | 2,400-2,800 (fail <2,250 or >3,000) | **PASS** |

After the required fixes below, S7 = 344, S14 = 634 (A2 64, A7 64) and the total = **2,733**. All sections stay in budget.

## 3. Zero em dashes: PASS

A whole-file ripgrep finds `—` **0**, `–` **0** and `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- I re-read every page line, 22-359. The five changed sentences are grammatical, and so is the rest of the page. Fragments are used only in tab items, taglines and S12, which is normal UI copy.
- **British spelling.** The sweep for -ize/-yze forms, color, center, program, behavior, modeling, license, toward, catalog, analyze, favor and fulfill found **0** on the page.
- S2 strip punctuation is now consistent: all four descriptions end with a full stop.

## 5. Originality: FAIL

### 5.1 Competitor pages (all 6): clean

- I grepped the four raw competitor texts for every distinctive term in the v3 changes and the wider page. That covered cluster, how often, churn, ledger, regression, correlation, lakehouse, star schema, order frequency, segment, re-key, by hand, readiness, starting point, proof of value, self-service, scorecard, time zone, rip-and-replace, drift, retrain, data marts, reconcile, ETL and pipelines. The only hits were generic single words ("flexibility", "historical data", "data readiness", "data pipelines").
- The Apexon and Softcrylic markers ("4 C's", "tool-agnostic", "Managed Services", "consistent monitoring and fixing") are absent.
- Loop 1's full read of the competitor set still holds, because only the five fixed sentences changed.

### 5.2 SugarAI structural sample: clean

- The only overlap with any v3 wording is "by hand". SugarAI line 629 has "reps stop assembling context by hand" and A2 has "copies files by hand". It is a generic phrase, and Fix 5e removes it from A2 anyway.
- No SugarAI H2 is reused. Advisory C from loop 1 (S2 item 4) stands, not scored.

### 5.3 Power BI sibling (draft-v7): one failure, one advisory carried forward

- **Fails, see 5.4(c):** FAQ A7 sentence 3.
- **Advisory D, carried from loop 1 (not scored, recommended):** S4 lede sentence 1 (line 71). It still shares about 16 of 20 non-keyword words, in order, with the Power BI S4 lede. It is brief-prescribed company boilerplate, so it is not scored, but the two pages link to each other. See Optional D below.
- **Checked and passed:**
  - S7 03 "one agreed definition" vs Power BI "consistent KPI definitions" / "We define each measure once".
  - S9 step 1 "agree measurable success criteria" vs Power BI S9 "success criteria agreed at the outset" (short generic phrase).
  - S9 intro "nothing moves on until your team approves" vs Power BI "development starts only when they have approved the design".
  - S7 06 role-based access vs Power BI S7 04.
  - None of these shares a sentence frame.

### 5.4 The failures

**(a) S7 item 05, sentence 2 (line 205): a splice of the Tab 2 FAQ 6 source.** Same finding as the Flag 11 ruling above.

| draft-v3 | Tab 2 FAQ 6 (source; live on the page being replaced) |
|---|---|
| "**Our segmentation models group customers by behaviour** and **value**, and we refresh those segments as new transactions arrive, so targeting does not run on stale groups." | s3: "**Our segmentation models** use machine learning to identify high-value cohorts..."; s1: "...uses data analytics to **group customers by behavior, value**, preferences, or demographics." |

- 8 of the first 9 words are the source's own words, in source order.
- The same shape also appears in S6 card 5 ("Our clustering models group customers by..."), which is Build's Flag 11.

**(b) FAQ A2, sentence 3 (line 332): the source sentence with the tool name removed, and the banned absolute reworded.**

| draft-v3 | Tab 2 FAQ 2 (source) |
|---|---|
| "We **build** ETL as **automated pipelines that run on a schedule**, so nobody copies files by hand." | "HLB HAMT **builds automated ETL pipelines** using Azure Data Factory **that run on schedule** with zero manual intervention." |

- The subject, verb, object and relative clause are the same, in the same order. 8 of the 17 words are verbatim (build, ETL, automated, pipelines, that, run, on, schedule).
- The trailing clause "so nobody copies files by hand" restates the source's "zero manual intervention". That is still an absolute claim, and brief Section 1 (tone) and Section 4 (FAQ 2) ban that claim.
- Loop 1 treated "that run on (a) schedule" as a fixed term and passed this sentence. On a closer read, the whole sentence tracks the source. This is a loop-1 miss, not a new regression.

**(c) FAQ A7, sentence 3 (line 347): my loop-1 replacement recreated the Power BI sibling's frame.**

| draft-v3 A7 s3 | Power BI draft-v7, S5 platform block (line 140) | Power BI draft-v7, A3 (line 376) |
|---|---|---|
| "**Where** the numbers **come from many systems** at enterprise scale, **we build a data lakehouse** instead, pairing a lake's flexibility with a warehouse's structure **through the layered design** described above." | "**When** your data **sits in five or more systems**, **we build a lakehouse** fed by automated data pipelines, refining records **through Bronze, Silver and Gold layers**..." | "Once data spreads across five or more systems, we recommend a lakehouse..." |

- Loop 1 failed v2's "across many systems, we recommend a lakehouse" for tracking Power BI A3.
- The wording I prescribed changed "recommend" to "build". That lined the sentence up with the Power BI **S5 platform block** instead: a condition about the number of systems, then "we build a (data) lakehouse", then a participle phrase ending "through ... layer(s)".
- The sibling-echo problem is therefore not solved. Fix 5f gives a restructured sentence that drops the "[many systems], we build/recommend a lakehouse" frame altogether.

**Checked and acceptable (no change needed; recorded so loop 3 does not reopen them).** Each of these restates a permitted Tab 2 fact in close to its minimal form, or uses a fixed term. None carries over the source's surrounding phrasing:
- **A1 s2:** the technique list "statistical modelling, machine learning and predictive techniques". These are industry terms, prescribed by brief S14 FAQ 1.
- **A2 s1:** "ETL stands for extract, transform, load:". Expanding the acronym is definitional, and the verbs and middle clause are new.
- **A3:** fact and dimension table examples (standard textbook examples). s3 "We design star schemas around your KPIs using dimensional modelling" is the bare fact, with the source's qualifiers ("Kimball-standard", "tailored to your business KPIs") replaced.
- **A5:** "we build on what you have already paid for rather than asking you to replace it". Both content slots are rewritten.
- **S4 card 3 s1:** "We begin by assessing data readiness and recommending where to start" is the bare fact from FAQ 7, prescribed by the brief.
- **S6 card 5:** see the Flag 11 ruling.

### 5.5 Web (exact-phrase searches, today): no matches

| Phrase searched | Result |
|---|---|
| "group customers by what they buy, how often and how much they spend" | No exact match. Only generic RFM and behavioural-segmentation guides, e.g. a grocery-retail blog listing "how often someone shops, what they buy, how much they spend". This is a generic concept, not a copied sentence. |
| "regression and correlation analysis on the transactions and ledger lines" | No match |
| "falling order frequency, shrinking spend or rising complaints" | No match |
| "Star schemas built around the KPIs you already report on" | No match |
| "pairing a lake's flexibility with a warehouse's structure" | No exact match. The lakehouse definition is ubiquitous and generic. |
| "so targeting does not run on stale groups" | No match |
| "Spot likely leavers while you can still act" | No match (HR-attrition articles only) |
| "One data foundation. Three ways to put it to work" | No match |
| "Forward-Looking Analytics, Grounded in How the Numbers Are Made" | No match |
| Fix wording: "draw on many systems are better served by a data lakehouse" | No match |
| Fix wording: "Customer segments, grouped by behaviour and value, are refreshed as new transactions arrive" | No match |

## 6. Stat accuracy and footnoting: PASS

| Ref | Figure | Location | Check | Result |
|---|---|---|---|---|
| [1] S-1 | 85% of UAE CEOs say their organisation's culture enables AI adoption | S2 item 2 only | Today's search extract of PwC's 29th CEO Survey gives "82 percent [Middle East] ... with UAE CEOs at 85%". About 8 months old. | Pass |
| [2] S-3 | HLB network revenue US$6.67bn for 2025, up 12% | S2b only | The HLB press-room title plus Consultancy.com.au. Attributed as "network-wide revenue" of HLB (B5). | Pass |
| [3] S-2 | 16% of GCC CEOs agree their most-used AI tools have access to all relevant documents and data | S5 foundation block only | Today's extract: "Only 22% of Middle East CEOs and 16% in the GCC agree...". The Middle East figure still varies between sources (22% vs 29%), as brief 6b notes. The GCC 16% is consistent, and it is the only figure used. | Pass |
| [4] F1 | UAE PDPL, Federal Decree-Law No. 45 of 2021 | FAQ 8 only | u.ae data-protection page (brief 6c). Uses "governed by" and "in line with", with no guarantee. | Pass |
| CS1 | 11 services | S2 item 1 only | Tab 2 badges 5 + 3 + 3. HLB HAMT's own catalogue, so no footnote. | Pass |

- **PwC attribution is footnote-only.** "PwC" appears only in Sources 1 and 3 (lines 369, 371) and in Flags. There is no inline "(PwC, 2026)" on the page. Lines 51 and 128 carry only the [1] and [3] markers, plus "CEOs surveyed".
- Markers appear in order of appearance: [1] S2, [2] S2b, [3] S5, [4] FAQ 8.
- Each stat appears in one section only. No FAQ restates 11, 85%, 16% or US$6.67bn.
- **No duplication across the project.** Ripgrep of every other requirement for `6\.67`, `85%` and `16% of` finds no page use. The only hits are a Power BI HTML CSS height and "28.16% of" in an FSM source line.
- The sibling stats (200+, 33x, 7 days, Since 1999, 25/26 years, 150+, 19th, 14+) appear 0 times.

## 7. Human tone / AI-detection heuristics: PASS

- **Stock-phrase sweep, 0 hits on the page.** The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just", "in conclusion", cutting-edge, game-changing, revolutionise, unleash, delve, landscape, ever-evolving, state-of-the-art, world-class, best-in-class, synergy, supercharge, transformative, navigate, pivotal, crucial, furthermore, moreover, additionally, ensure, comprehensive, innovative, dynamic, effortless, stunning, insight(s), data-driven, end-to-end and powerful.
- **Loop-1 opener failure: resolved** (see the table at the top).
- **Build's Flag 11 frame:** handled under item 5 (Fix 5d). On tone alone it would be advisory only.
- **Advisories (not scored; apply only if word-neutral as specified):**
  - **E. The "already [verb]" tic.** "you/your ... already [hold/run/use/open/report on/paid for]" appears **10 times**: hero; S4 card 3; S5 row 3; S7 03; S7 04; S10 Extend; S11 tile 6; A4; A5; A7.
    - "the sources you already run" is an exact repeat at S4 card 3 (line 80) and A7 s2 (line 347).
    - Optional, word-neutral: in A7 s2, change "the sources you already run" to "the systems you have today".
  - **F. The ", so" result clause in S6.** 4 of the 6 flip-card backs hinge on ", so ..." (cards 1, 2, 4, 5).
    - Optional, word-neutral (S6 is at its 320 cap): card 4 sentence 2, "Scores can flow into HLB HAMT's own SugarAI CRM, so sales teams see them in the pipeline." becomes "Scores can flow into HLB HAMT's own SugarAI CRM and sit beside each lead in the pipeline." (17 words, unchanged; keep the L5 link on "SugarAI CRM").

## 8. Section structure, CTAs, FAQ, internal links: PASS

- **Order.** S0, S1, S2 + S2b, S3, S4, S5 (3 rows + foundation block), S6 (6 flip cards + pill row), S7 (01-06), S8, S9 (5 steps, highlighted band), S10 (3 tabs, no featured card), S11 (6 tiles), S12, S13, S14, S15, S16. This matches the Section 3b order. "Why AI Changes CRM" has no equivalent.
- **Headings.** There is exactly one H1 (22). No SugarAI or Power BI H2 is reused.
- **S3 anchor nav.** 7 labels in the brief's order.
- **CTAs: exactly 4.**
  - CTA 1: hero "Book a free consultation" + "Explore our services" (26).
  - CTA 2: S8 "Request a readiness assessment" (217). The assessment is not called "free".
  - CTA 3: S13 "Talk to our analytics team" (320).
  - CTA 4: S15 form "Schedule a Consultation" (361).
  - Every other "button" hit is a "No button" note (174, 242, 275, 312) or the brief-prescribed S2b recognition-bar link (63).
  - The in-text links (#methodology, #usecases, #contact) are allowed by 3c.
- **FAQ.** 9 Q&As, H3 questions, single accordion. Answers run 55-65 words. Q9 has 2 "Power BI" mentions and no links.
- **Internal links:**
  - L1: S4 lede (71), https://hlbhamt.com/services/digital-transformation-uae/
  - L2: S11 tile 5 (298), Power BI placeholder plus Deliver note
  - L3: S6 card 6 (171), data visualisation placeholder plus Deliver note
  - L4: FAQ 8 (350), https://hlbhamt.com/services/data-privacy-and-security-uae/
  - L5: S6 card 4 (161), https://hlbhamt.com/sugarai-crm-2/
  - All anchors are exact. There is no self-link and no link to any "do not link" page.

## 9. Client requirements (Section 10) and fabricated commitments: PASS

- **Point 1:** replace in place (line 15).
- **Point 2:** "Microsoft" 0 and "Power BI" 4.
- **Point 3:** L2 and L3 placeholders are present.
- **Point 4:** S9, S10 and support substance come from the competitor pattern, in original wording (5.1).
- **Point 5:** "PowerUP!" appears 0 times.
- **Point 6:** S12 uses a static placeholder.
- **No transcript** was supplied.
- **No fabricated commitments.** The page has no durations, prices, uptime or response-time figures, or SLA terms.
  - "We reply within one business day" (S15) is the site-standard form promise that the brief prescribes.
  - "Week by week or quarter by quarter" (S7 05) describes forecast granularity, not a delivery time.
- **Still open for the Content Writer before go-live (non-blocking, carried from Build Flag 2):**
  - (a) Post-go-live monitoring, retraining and reviews (S4 card 4, S9 step 5, S10 Extend).
  - (b) The "named consultant" (S10 Extend). Fallback: "We watch...".

---

## Overall: FAIL (loop 2 of 3)

Only item 5 fails, on three single sentences:
- **(a)** S7 item 05 s2 splices the Tab 2 FAQ 6 source. It is also Build's Flag 11 frame repeat.
- **(b)** FAQ A2 s3 is the source sentence minus the tool name, with a still-absolute "nobody copies files by hand".
- **(c)** FAQ A7 s3: my own loop-1 wording recreated the Power BI S5 "[many systems], we build a lakehouse ... through ... layers" frame.

(a) and (b) were missed by Test in loop 1, and (c) was introduced by Test's own loop-1 wording. None is a Build error. All three fixes are single-sentence swaps, with exact text below. Everything else passes, and all 5 loop-1 fixes are verified verbatim.

## Fix instructions

Word-count effect of all three required fixes: S7 349 → 344 and S14 633 → 634 (A2 65 → 64, A7 62 → 64). The total goes 2,737 → **2,733**, and every section stays inside its budget. Change nothing else in the page copy, except any optional items you choose to apply.

**Fix 5d (required). S7 item 05, sentence 2 (line 205). This is Build's own Flag 11 suggestion.**
- Replace "Our segmentation models group customers by behaviour and value, and we refresh those segments as new transactions arrive, so targeting does not run on stale groups." (26 words)
- With: "Customer segments, grouped by behaviour and value, are refreshed as new transactions arrive, so targeting does not run on stale groups." (21 words)
- Item 05's body becomes 47 words, or 51 with the H3. Sentence 1 ("We forecast revenue, cash and demand...") and the H3 stay unchanged.
- Do not reintroduce "Our segmentation models" or "group customers by" anywhere else on the page. S6 card 5 keeps its "group customers by what they buy..." wording.

**Fix 5e (required). FAQ A2, sentence 3 (line 332).**
- Replace "We build ETL as automated pipelines that run on a schedule, so nobody copies files by hand." (17 words)
- With: "We turn those three steps into pipelines that start at set times, replacing manual file copying." (16 words; A2 = 64)
- This keeps "We" as the subject for B3. It keeps the automated, scheduled-pipeline fact without the source's "build automated ETL pipelines that run on schedule" frame, and it drops the absolute "nobody".
- Sentences 1 and 2 stay unchanged. Update the FAQPage schema text to match.

**Fix 5f (required). FAQ A7, sentence 3 (line 347). This supersedes loop-1 Fix 5c.**
- Replace "Where the numbers come from many systems at enterprise scale, we build a data lakehouse instead, pairing a lake's flexibility with a warehouse's structure through the layered design described above." (30 words)
- With: "Larger programmes that draw on many systems are better served by a data lakehouse, which blends a lake's flexibility with a warehouse's structure; we lay it out in the layers described above." (32 words; A7 = 64)
- B3 is carried by the "we lay it out" clause.
- Sentences 1, 2 and 4 stay unchanged, and so does the "readiness assessment" → #contact link. The only exception is sentence 2 if you apply Optional E, which is word-neutral.
- Do not use "we build/recommend a (data) lakehouse" after a condition about the number of systems anywhere on the page. Update the FAQPage schema text to match.

**Optional, same pass (advisories, not required to pass):**
- **D (recommended), S4 lede s1 (line 71).** "HLB HAMT is an advanced analytics company in UAE and, as a licensed audit, tax and advisory firm in the HLB network, checks numbers for a living." (+1 word; S4 = 260, at cap.) This removes the near-verbatim match with the Power BI S4 lede. If you apply D, do **not** also apply B.
- **B, S4 card 4 s1 (line 83).** "Models drift as markets move, so we offer to stay on after launch." (+1 word.) Apply only if D is not applied.
- **C, S2 item 4 (line 59).** "Our Dubai team plans and builds your models, in your time zone." (no count change)
- **E, A7 s2 (line 347).** "the sources you already run" becomes "the systems you have today". This is word-neutral and removes the exact repeat with S4 card 3.
- **F, S6 card 4 s2 (line 161).** "Scores can flow into HLB HAMT's own SugarAI CRM and sit beside each lead in the pipeline." This is word-neutral; keep the L5 link.

After the fixes, Build should update:
- Flag 5 (word counts).
- Flag 10 (FAQPage text for A2 and A7).
- Flag 11, recording that Test accepted the Flag 11 suggestion and that Fix 5f supersedes loop-1 Fix 5c.

---

Sources consulted for verification:
- [PwC, 29th Global CEO Survey: UAE findings](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026/29th-ceo-survey-uae-findings-2026.html) (search extract: UAE 85%)
- [PwC, 29th Global CEO Survey: Middle East findings](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026.html) (search extract: GCC 16%)
- [HLB press release, FY2025](https://www.hlb.global/press-room/hlb-reports-12-global-growth-reaching-us6-67-billion-in-fy2025/) and [Consultancy.com.au](https://www.consultancy.com.au/news/12048/hlb-joins-the-6-billion-global-revenue-club-in-return-to-double-digit-growth) (US$6.67bn, up 12%)
- [IT Retail, customer segmentation for grocery](https://www.itretail.com/blog/customer-segmentation-grocery) and [Braze, RFM segmentation](https://www.braze.com/resources/articles/rfm-segmentation) (the generic RFM concept behind S6 card 5; no copied sentence)
- [Starburst, data lakehouse](https://www.starburst.io/blog/data-lakehouse/) (the generic lakehouse definition)
- The other exact-phrase searches returned no match (5.5).
