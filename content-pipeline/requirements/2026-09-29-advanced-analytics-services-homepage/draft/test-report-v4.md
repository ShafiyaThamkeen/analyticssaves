# Test report v4: Advanced Analytics Services homepage (draft-v4.md, loop 3 of 3, FINAL)

Tested by: Test agent, 2026-09-29
Loop: **3 of 3.** This is the final loop. Per the project convention, this report does not go back to Build. The remaining issue below goes to the Content Writer.

---

## Remaining issues (for the Content Writer)

**Overall verdict: FAIL, on one sentence.** Everything else passes. That includes all three loop-2 fixes, which are applied word for word.

**The one failing item (item 5, originality): FAQ A6, sentence 3 (draft-v4 line 344).** It is a light rewording of the last sentence of HLB HAMT's own Tab 2 FAQ 6 answer. That sentence is also live on the page this one replaces.

| draft-v4 A6, sentence 3 | Tab 2 FAQ 6, sentence 3 (source, HTML version and live page) |
|---|---|
| "We **use machine learning to** find valuable **cohorts**, often small ones, **that** a spreadsheet filter **would** not reveal." | "Our segmentation models **use machine learning to** identify high-value **cohorts that** manual analysis **would** miss." |

- Every slot of the source sentence is kept, in the same order, with synonyms swapped:
  - "use machine learning to" is verbatim.
  - identify becomes find.
  - high-value becomes valuable.
  - "cohorts that" is verbatim.
  - manual analysis becomes a spreadsheet filter.
  - would miss becomes would not reveal.
- The only addition is "often small ones".
- **Why this is a failure and not a judgement call.** Loop 1 (test-report-v2, 5.4(b)) failed S6 card 5 sentence 2 against this same source sentence. That draft read "Machine learning surfaces high-value cohorts a manual cut of the data would miss", and the stated reason was that it kept the "machine learning → high-value cohorts → manual ... would miss" structure. A6 sentence 3 keeps that same structure, and even more of the source's exact wording. Loop 2 (Fix 5d) also removed an 8-of-9-word splice from this FAQ 6 answer.
- **This is a Test miss, not a Build error.** Loop 1 described A6 as "properly rewritten", quoting only its first sentence. Neither earlier loop compared sentence 3 with the source.
- **Risk is low.** The source is HLB HAMT's own copy, and it leaves the live site when this page replaces it (brief Section 10, point 1). No third-party page carries the sentence (web search, 5.5). The breach is of the brief's Section 4 reuse rule ("Build must write new copy for every sentence, including all FAQ answers"), not third-party plagiarism.

**Fix (one sentence, exact text):**
- **Replace:** "We use machine learning to find valuable cohorts, often small ones, that a spreadsheet filter would not reveal." (18 words)
- **With:** "We run machine learning clustering across many customer attributes, then profile each cluster so your team knows who is in it and what it is worth." (26 words)
- **Effect of the change:**
  - A6 goes from 56 to 64 words (range 50-65).
  - S14 goes from 634 to 642 (budget 550-660).
  - The page total goes from 2,733 to **2,741** (range 2,400-2,800).
  - B3 still holds, because "We" stays the subject.
  - Nothing else changes: A6 sentences 1 and 2, the Q6 heading and every other line stay as they are.
- **Deliver must update the FAQPage schema** `acceptedAnswer.text` for A6 to match.
- **Once this one sentence is swapped, the draft is ready for Deliver.** No other item needs work. If the Content Writer decides the echo is acceptable, since it is HLB HAMT's own retired copy, the draft can go to Deliver as it stands.

**Recommended but not required (Content Writer's call; none affects the verdict).** Details are under "Optional" at the end.
- **D.** The S4 lede, sentence 1, still repeats the Power BI homepage's S4 lede almost word for word. The brief prescribes this boilerplate, so it has not been scored in any loop. The two pages link to each other, though, so changing it is worthwhile.
- **H (new).** A4, sentence 2 reads as a garden path. A comma fixes it at no word-count cost.
- **Go-live confirmations carried from loops 1-2:**
  - (a) Confirm that analytics engagements include post-go-live monitoring, retraining and reviews (S4 card 4, S9 step 5, S10 Extend).
  - (b) Confirm the "named consultant" in S10 Extend. Fallback: "We watch pipelines, data quality and model drift...", which keeps the word count in range.
  - (c) The final URLs for placeholders L2 and L3 (OQ4).

---

Inputs checked:
- `brief.md`, all 481 lines. Section 10 overrides Sections 1-9 where it says so.
- `draft/draft-v4.md`, all of it: page, Sources, Stats used and Flags 1-11. I compared every v4 page line with `draft/draft-v3.md`.
- `draft/test-report-v2.md` and `draft/test-report-v3.md`, for the specified fix wording and the earlier rulings.
- `inputs/extracted/hlb-data-viz-v4 (1).html.md`, meaning Tab 2: the [DO NOT REUSE] intro paragraphs, the 11 services and all 7 FAQ answers.
- The competitor pages:
  - `inputs/competitor-content/drcsystems.txt`, `ometis.txt`, `protiviti.txt` and `insightconsulting.txt`, read in full.
  - `research-summary.md`.
  - Apexon and Softcrylic through WebSearch. WebFetch today returned HTTP 503 for Apexon and an empty client-rendered page for Softcrylic, the same as in loops 1-2.
- The structural sample, `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`, read in full.
- The delivered Power BI homepage:
  - `2026-09-28-power-bi-services-homepage/draft/draft-v7.md`, read in full.
  - A grep of `output/power-bi-services-homepage.html`, which confirms the output matches v7 (for example "Great Dashboards Start With the Numbers Behind Them" and "Once data spreads across five or more systems, we recommend a lakehouse").
- Web checks: PwC, HLB and u.ae stat checks, and exact-phrase searches (5.5).

Method:
- This session has no shell. I checked characters, names, keywords, links and banned strings with ripgrep on `draft-v4.md`, then removed lines that are not page copy: meta, draft header, chrome, structure headers, eyebrows, buttons, Deliver notes, Sources, Stats used and Flags.
- **Word count.**
  - I wrote the counted copy of each section to its own scratch file, following the brief Section 1 rule and the same inclusions and exclusions as loops 1-2.
  - I then machine-counted whitespace-delimited tokens per file with ripgrep offset probing. For each file, the token at the expected count is the section's last word, and no token follows it.

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density, branding B1-B5, T1-T6 | **PASS** |
| 2 | Word count | **PASS** (2,733, exact machine count) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** (1 new clarity advisory, H) |
| 5 | Originality (6 competitors, content source, SugarAI template, Power BI sibling, web) | **FAIL** (1 sentence: FAQ A6, sentence 3, against the content source) |
| 6 | Stat accuracy and footnoting | **PASS** |
| 7 | Human tone / AI-detection heuristics | **PASS** (advisories only) |
| 8 | Section structure, CTAs, FAQ, internal links | **PASS** |
| 9 | Client requirements (Section 10) and no fabricated commitments | **PASS** (go-live confirmations carried) |

### Loop-2 fixes: all 3 applied verbatim

| Fix | Location (v4 line) | Specified in test-report-v3 | In draft-v4 | Match |
|---|---|---|---|---|
| 5d | S7 item 05, sentence 2 (205) | "Customer segments, grouped by behaviour and value, are refreshed as new transactions arrive, so targeting does not run on stale groups." | Identical. Sentence 1 and the H3 are unchanged. | Yes |
| 5e | FAQ A2, sentence 3 (332) | "We turn those three steps into pipelines that start at set times, replacing manual file copying." | Identical. Sentences 1 and 2 are unchanged. | Yes |
| 5f | FAQ A7, sentence 3 (347) | "Larger programmes that draw on many systems are better served by a data lakehouse, which blends a lake's flexibility with a warehouse's structure; we lay it out in the layers described above." | Identical. Sentences 1, 2 and 4 and the `#contact` link are unchanged. Optional E was not applied. | Yes |

- **No other page line changed between v3 and v4.** I compared lines 18-365 of both files. The only differences are lines 205, 332 and 347.
- **The fix conditions hold:**
  - "Our segmentation models" appears **0** times. "segmentation models" appears only as a list item in S4 card 1 (line 74) and S9 step 3 (line 234), which is not the source frame.
  - "group customers by" appears only in S6 card 5 (line 166), which loop 2 accepted.
  - "we build/recommend a (data) lakehouse" appears **0** times on the page. The only hits are in Flags (406, 424).
  - "nobody" appears **0** times on the page.
- **Build's word-count arithmetic is confirmed:** S7 = 344, S14 = 634 (A2 64, A7 64), total 2,733.
- **Build Flag 10's FAQPage text for A2 and A7** matches the page copy exactly.

---

## 1. Keyword placement and density: PASS

On-page copy only, under the brief Section 2a rules. The secondary keyword was counted with the lookahead logic, by hand, because ripgrep has no look-around; I listed every "advanced analytics services" hit and excluded those followed by "in UAE".

| Keyword | Count | Placements (v4 line) | Target | Result |
|---|---|---|---|---|
| Primary "advanced analytics services in UAE" | **4** | H1 (22); hero lede s1 (24); S14 H2 (326); S15 body (359) | 3-4 (max 5) | Pass |
| Secondary "advanced analytics services" (not followed by "in (the) UAE") | **3** | S7 H2 (183); S10 intro (250); S11 H2 (281) | 2-3 | Pass |
| "advanced analytics company in UAE" | **1** | S4 lede s1 (71) | 1 (max 2) | Pass |
| "data analytics and automation" | **2** | S7 intro (185); S11 tile 2 H3 (288) | 2-3 | Pass |
| Forbidden "advanced analytics services in the UAE" | **0** on page | Flags line 403 only | 0 | Pass |

- **Meta title and description** (lines 1-2) match brief Section 7 exactly. Both open with the primary keyword.
- **First 100 words:** the primary keyword appears in the H1 and in lede sentence 1 (word 3 of the lede).
- **T1 "HLB HAMT": 11** (range 9-14), at lines 22, 61, 71, 161, 176, 183, 281, 283, 308, 329 and 353. Excluded: nav (16), eyebrows (20, 67, 279) and structure headers (65, 179, 277).
- **T2 "advanced analytics", any form: 12** (cap 18), at lines 22, 24, 71, 183, 250, 281, 326, 328, 329, 352, 353 and 359. Line 85 is a structure header.
- **T4 "UAE": 8** (cap 10), at lines 22, 24, 51, 71, 281, 326, 350 and 359.
- **T3 third-party names.**
  - I ran a case-sensitive whole-word sweep for the full brief list (SQL Server, Oracle, SAP, NetSuite, Salesforce, Dynamics 365, Tally, QuickBooks, BigQuery, Snowflake, Azure, Fabric, Synapse, Databricks, Excel, Python, Tableau, Qlik, Copilot, Kimball). I added SQL, Microsoft, AWS, Google, Looker, SharePoint, Teams, Power Automate, PowerUP, and the competitor-page tools Jedox, Sigma, Inphinity and Cognos.
  - The page has **0** hits. The only hit in the file is in the Flags (line 404).
  - **"Power BI" = 4 on the page:** S11 tile 5 H3 (297), tile 5 body (298), Q9 (352) and A9 (353). That is the maximum of 4, in the two permitted slots only. Line 299 is a Deliver note.
  - "Microsoft" = 0. "SugarAI CRM" appears only as L5 (161).
- **T5 and T6: 0 hits on the page.** The sweep covered all ten competitor-derived phrases, "zero manual", "certified", "#1", "award-winning", "leading", "guarantee", "best-in-class", "world-class" and the sibling stats (200+, 33x, 7 days, Since 1999, 25/26 years, 150+, 19th, 14+). The only hit in the file is the Stats-used note (line 382).
- **2d:** 2 of the 6 S7 titles contain "analytics" (03, 04). 0 of the 5 S9 titles do. No set of titles all start with "Data".
- **Branding:**
  - **B1:** the H1 opens "HLB HAMT:".
  - **B2** holds for every section opener: hero "We deliver", S4 "HLB HAMT is", S5 "We treat", S6 "We start", S7 "We run", S9 "We run", S10 "We package", S11 "HLB HAMT pairs".
  - **B3** holds for all 9 answers: A1 "HLB HAMT builds", A2 "We turn", A3 "We design", A4 "We test", A5 "We connect", A6 "We use", A7 "we lay it out", A8 "We limit", A9 "HLB HAMT delivers". The A6 fix keeps "We".
  - **B5:** the S2b figure is "network-wide revenue" of HLB, and both PwC figures belong to "CEOs surveyed".
- **Stuffing:** none. Each keyword sits in its brief-assigned slot, and no sentence repeats a keyword.

## 2. Word count: PASS (2,733)

This is a fresh, independent machine count, one scratch file per section. Each count was confirmed by offset probing: the token at the stated count is the section's last word, and no further token exists.

| Section | Count | Last token | Budget (3b) | Status |
|---|---|---|---|---|
| S1 | 154 | "platform." | 130-160 | OK |
| S2 + S2b | 70 | "12%." | 50-70 | OK (at cap) |
| S4 | 259 | "more." | 220-260 | OK |
| S5 | 321 | "models" | 320-380 | OK |
| S6 | 320 | "Telecommunications" | 260-320 | OK (at cap) |
| S7 | 344 | "report." | 330-380 | OK |
| S8 | 28 | "answer." | 20-30 | OK |
| S9 | 157 | "owner." | 130-160 | OK |
| S10 | 210 | "themselves." | 170-220 | OK |
| S11 | 150 | "rip-and-replace." | 120-150 | OK (at cap) |
| S12 | 30 | "data." | 25-40 | OK |
| S13 | 27 | "you." | 20-30 | OK |
| S14 | 634 | "place." | 550-660 | OK |
| S15 | 29 | "day." | 20-30 | OK |
| **Total** | **2,733** | | 2,400-2,800 (fail below 2,250 or above 3,000) | **PASS** |

- **Inclusions and exclusions** are the same as loops 1-2.
  - Included: H1, H2s, H3s, ledes, sub-block heading and line, card, tile and strip text (including the strip stat lines), S2b, bullets, tab names, taglines, pill label and pills, FAQ questions and answers, and CTA headings and bodies.
  - Excluded: eyebrows, buttons, nav, breadcrumb, the form, the S5 "Capability" / "Key capabilities" / "Foundation layer" labels, the S7 pillar labels, footnote markers, Sources and Flags.
- The count matches Build's figure of about 2,733 and the post-fix total projected in test-report-v3.
- **After the required A6 fix:** S14 = 642 and the total = **2,741**. Both stay in range.

## 3. Zero em dashes: PASS

A whole-file ripgrep finds `—` **0**, `–` (en dash) **0** and `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- **Grammar.** I re-read every page line (22-361), including the three changed sentences.
  - No grammatical errors.
  - Fragments appear only in taglines, tab items, card lines and S12, which is normal for UI copy.
  - Constructions checked and confirmed correct:
    - The colon plus semicolon series in A2.
    - The semicolon-joined independent clause in A7 ("...structure; we lay it out...").
    - The participial close in A2 ("..., replacing manual file copying").
    - The "custom data views plus self-service analytics let..." subject in S7 06.
- **British spelling.** The sweep covered -ize/-yze/-ization forms, color, center, program(s), behavior, modeling/modeled, license, toward, catalog, analyze, favor, fulfill, optimiz-, judgment, labeled, defense and gray.
  - **0** on the page. The only regex hit was "size" (line 41), a false positive.
  - British forms confirmed: organisation(s), modelling, standardise, prioritisation, prioritised, behaviour, visualisation, programme(s), centre. "Licensed" is the correct UK participle.
- **Advisory H, new (not scored; clarity). A4, sentence 2 (line 338).**
  - "We test every model against periods it has not seen before anyone relies on it" reads first as "has not seen before", and the reader stumbles at "anyone".
  - Word-neutral fix: add a comma, making it "...against periods it has not seen, before anyone relies on it, then place the predictions...".
  - The FAQPage text must match.
- **Advisory B, carried (not scored).** S4 card 4 s1 (line 83): the "so" in "Models drift as markets move, so we can stay involved after launch" still reads slightly off. See Optional.

## 5. Originality: FAIL (1 sentence)

### 5.1 Competitor pages (all 6): clean

- **DRC Systems** (full read).
  - The approach intro ("so you always know exactly what happens next"), stage 05 ("closely monitor, refine, and optimize ... keeps adding value"), "Flexible engagement models tailored to you" and "Platform-Agnostic" are all absent.
  - The capability H3s "Data Transformation" and "Predictive Analytics" overlap only with Tab 2's own pillar name (S1 card 1, permitted) and with generic terms.
  - DRC's "Book a free consultation" is a button label here (not counted, brief-prescribed).
- **Ometis** (full read).
  - The Descriptive / Predictive / Prescriptive H3s are not used.
  - S5 row 3's "What to do about it" was ruled in loop 1 as a generic, brief-prescribed idiom. The ruling stands.
  - "We map, cleanse, and transform it" vs S7 01 "clean, standardise and reshape it" is a generic verb set, not a sentence.
  - "build internal capability", "grow in capability and confidence", "instructor-led training" and the support-channel list are absent.
- **Protiviti** (full read). "ongoing monitoring", "Preventive not responsive", "Operational resilience" and "trigger systems" are absent. "Time series forecasting" is an industry term.
- **Insight Consulting** (full read). "thorough business requirements meeting", "comprehensive blueprint", "training, maintenance, and ongoing support for your investment" and "we partner with our clients" are absent.
- **Softcrylic** (search extracts today). Its core sentence ("building a strong data foundation by organizing disparate data and developing efficient data models...") is the banned Tab 2 intro source. None of its clauses appears on the page. "Data foundation" (S1, S5, A1) is a generic term, and T5's "disparate data" and "efficient data models" = 0. Its "Supervised and unsupervised learning to detect latent relationships", "predicting future trajectory based on historical trends", "Managed Services Model ... Level-1 through Level-3" and "consistent monitoring and fixing" are absent.
- **Apexon** (search extracts today). "The 4 C's" / "Curate, Catalog, Context, Consume", "frame the problem worth solving", "MLOps and model governance", "embedding insights into enterprise workflows", "closed-loop data pipelines" and "Lab-as-a-Service" are absent. S9's discover → engineer → build → deploy → retrain sequence is the common industry pattern that Section 10 point 4 permits, written in original words.
- **The new v4 sentences** have no competitor overlap beyond single generic words.

### 5.2 SugarAI structural sample: clean

- These are template structural labels, which the checklist allows:
  - The S4 card H3s "What we do" / "Who we work with" / "How we deliver".
  - The S11 H2 frame "Why UAE Businesses Choose HLB HAMT for ...".
  - The "See it in action" eyebrow.
  - The S1 sub-block pattern ("One data foundation. Three ways to put it to work." vs "One platform. One customer record.").
- **S11 tile 5** "Analytics and Power BI from one partner" mirrors the template's "Dual AI intelligence: SugarAI prediction plus Power BI analytics, from one partner", as brief S11 prescribes. The only shared phrase is the generic "from one partner".
- **S13** "Plan Your First Forecast With Our Analytics Team" / "In a free consultation, we agree the use case, the data sources and the right starting point with you." follows the template CTA pattern ("Plan your SugarAI rollout with our consultants" / "We scope the packages, phasing and integrations ... with a free consultation"). Every content slot is different, and the brief prescribes it. Acceptable.
- **S4 card 1** "One team owns the whole path" vs the template's "We take responsibility for the whole CRM ... delivered by one team" is a shared idea (brief-prescribed), not a shared sentence.
- **Advisory C (S2 item 4)** stands, not scored.
- No SugarAI H2 is reused verbatim.

### 5.3 Power BI sibling (delivered draft-v7 / output HTML): no failure; advisory D carried

- **The three v4 fixes against the sibling:**
  - **5f (A7 s3).** The "[N systems], we build/recommend a lakehouse" frame of Power BI S5 (line 140) and A3 (line 376) is gone. The subject is now "Larger programmes" and the verb is the passive "are better served by". Only the idea (many systems, therefore a lakehouse) remains. Pass.
  - **5e (A2 s3)** vs Power BI A4 "Rather than a team member copying figures between workbooks every week, data refreshes on a schedule". The only shared word is "copying", in a different structure. Pass.
  - **5d:** no Power BI counterpart.
- **Other pairs checked and passed** (a shared idea or technical vocabulary, not a shared sentence):
  - The S5 foundation block ("Automated pipelines feed a central warehouse or layered lakehouse, where data is refined from Bronze (raw) to Silver (cleaned) to Gold (business-ready)...") vs the Power BI S5 platform block ("a lakehouse fed by automated data pipelines, refining records through Bronze, Silver and Gold layers..."). "Pipelines feed a lakehouse; data is refined through Bronze/Silver/Gold" is the standard description of the medallion architecture, and brief S5 prescribes it. The AA block adds its own glosses and "then modelled into star schemas", and it has no systems-count condition.
  - S10 "Enterprise data platform ... delivered in phases across departments" vs the Power BI Tab 2 "Enterprise platform with a data lakehouse ... delivered in phases under central governance". They share "delivered in phases", a generic 3-word phrase; the item contents differ.
  - S6 intro vs the Power BI S6 intro: both start from the decision or the KPI, in different words.
  - S7 02 lakehouse extension, S7 06 role-based access, S9 step 1 success criteria, S15's "reply within one business day" (the site standard) and S15 H2 "Book Your Free Analytics Consultation" vs "Book Your Free Consultation" (a brief-prescribed CTA label, not verbatim).
- **Advisory D, carried (not scored; recommended). S4 lede, sentence 1 (line 71).**
  - "HLB HAMT is an advanced analytics company in UAE that is also a licensed audit, tax and advisory firm and a member of the HLB network." vs Power BI: "HLB HAMT is a Power BI consulting company that is also a licensed audit, tax and advisory firm, and a member of the HLB International network."
  - It has been left unscored in all three loops for the same reasons: brief Section 2b prescribes the sentence as the keyword carrier; it is factual company boilerplate; and the brief's sibling rule covers H2s only.
  - Because the two pages link to each other, the Content Writer may still want it varied. Wording is under Optional D.

### 5.4 Content source (Tab 2): one failure

**FAQ A6, sentence 3 (line 344): the failure.** The side-by-side comparison, the reasoning and the fix are in "Remaining issues" at the top.

**Checked and acceptable (recorded so they are not reopened).** Each restates a permitted Tab 2 fact in close to its minimal form, or uses a fixed industry term. None carries over the source's surrounding framing:
- **S5 intro, s2** ("A standard report tells you what happened; our analytics team takes the same data further, to explain why it happened, estimate what comes next and show where to act") vs source FAQ 1. "Tells you what happened / why it happened / what will happen / what to do" is the standard wording of the four-stage analytics maturity model and appears across the web. Brief S5 prescribes the frame, and the sentence is restructured around "our analytics team takes the same data further".
- **A1**, the same model. Sentence 1's examples (sales last quarter, stock on hand, staff costs) are different metrics from the source's. Brief S14 FAQ 1 prescribes the technique list.
- **A2 s1** (the ETL definition), **A3** (the star-schema definition and the textbook fact/dimension examples; "We design star schemas around your KPIs using dimensional modelling") and **A5** ("we build on what you have already paid for rather than asking you to replace it"). Loops 1-2 ruled all three acceptable; brief-prescribed facts.
- **A6 s1-s2.** A6 s1 is a definition of segmentation with a different attribute list; only "demographics" is shared. s2 uses a different structure, and its only shared concepts are retention and upselling/cross-selling.
- **A7 s2 and S4 card 3 s2** ("A focused/smaller initiative can ... the sources you already run"). This is the permitted FAQ 7 fact in its minimal form. There is no other natural way to say it, and each sentence adds its own clause ("which keeps the first project light"; "; an enterprise-scale programme justifies a dedicated data platform"). Loop 1 passed the rest of A7 explicitly.
- **A7 s3 (Fix 5f)** vs source FAQ 7 s3. The source's opener and main clause ("For enterprise-scale analytics, we recommend...") are gone. What remains is the generic lakehouse definition and the brief-prescribed back-reference to the layers ("name the approach, do not re-explain the layers"). Test prescribed this wording in loop 2.
- **A2 s3 (Fix 5e)** no longer shares the source's "builds automated ETL pipelines ... that run on schedule" frame or the absolute "zero manual intervention".
- **S7 05 s2 (Fix 5d)** no longer shares any FAQ 6 wording beyond "behaviour and value". Those are two attribute nouns, recast as a participle phrase.
- **S7 01** "then clean, standardise and reshape it" vs source FAQ 2 "cleaning and reshaping it". The verb pair is generic and brief-prescribed ("clean and reshape it"), and it sits in a different sentence frame.

### 5.5 Web (exact-phrase searches, today): no matches

| Phrase searched | Result |
|---|---|
| "We turn those three steps into pipelines that start at set times" (Fix 5e) | No match. Only generic pipeline-scheduling documentation. |
| "Customer segments, grouped by behaviour and value, are refreshed as new transactions arrive" (Fix 5d) | No match. Only generic segmentation guides. |
| "better served by a data lakehouse" + "lake's flexibility with a warehouse's structure" (Fix 5f) | No match. The lakehouse definition itself is generic (Databricks, Onehouse, Monte Carlo). |
| "machine learning to identify high-value cohorts that manual analysis would miss" (the Tab 2 source of A6 s3) | No third-party page reproduces it. Only generic cohort-analysis articles. So the A6 issue is source reuse, not web plagiarism. |
| "forecasts reconcile to the ledger" / "hand forecasts to the people who decide" / "keeps the first project light" | No match |
| "Every model and every report we deliver draws on the same reconciled data" | No match |
| Softcrylic and Apexon page extracts (4 queries) | No overlap with the draft (5.1) |

Loops 1-2 already recorded no-match results for the other distinctive lines, and those lines are unchanged in v4.

## 6. Stat accuracy and footnoting: PASS

| Ref | Figure | Location | Check (today) | Result |
|---|---|---|---|---|
| [1] S-1 | 85% of UAE CEOs say their organisation's culture enables AI adoption | S2 item 2 only (51) | Search extract of PwC's *29th Global CEO Survey: UAE findings* (released 28 Jan 2026): "85% of CEOs in the UAE say their organisational culture supports AI adoption". The Middle East figure is 82%. PwC is credible, and the survey is about 8 months old. | Pass |
| [2] S-3 | HLB network revenue US$6.67bn for 2025, up 12% | S2b only (61) | The HLB press-room page title plus Consultancy.com.au: "revenue reached US$6.67 billion in 2025, representing growth of 12%". Credited as "network-wide revenue" of HLB, not HLB HAMT (B5). About 5-6 months old. | Pass |
| [3] S-2 | 16% of GCC CEOs agree their most-used AI tools have access to all relevant documents and data | S5 foundation block only (128) | PwC *Middle East findings* extract: "Only 22% of Middle East CEOs and 16% in the GCC agree...". Only the GCC figure is used, and the sources agree on it; the Middle East figure still varies between sources, as brief 6b notes. It is framed as the reason to build the foundation first, not as a scare line. | Pass |
| [4] F1 | UAE PDPL, Federal Decree-Law No. 45 of 2021 | FAQ 8 only (350) | The u.ae "Data protection laws" page; in force since 2 Jan 2022. The draft says "governed by" and "in line with", never "guarantees compliance". | Pass |
| CS1 | 11 services | S2 item 1 only (47) | Tab 2 badges: 5 + 3 + 3. HLB HAMT's own catalogue, so no footnote. | Pass |

- **PwC attribution is footnote-only.** "PwC" appears only in Sources 1 and 3 (369, 371) and in Flag 4 (393). There is no inline "(PwC, 2026)" on the page. Lines 51 and 128 carry only the [1] and [3] markers, plus "CEOs surveyed".
- **Markers run in order of appearance:** [1] S2, [2] S2b, [3] S5, [4] FAQ 8.
- **Each stat appears in one section only.** No FAQ restates 11, 85%, 16% or US$6.67bn. The A6 fix adds no figure.
- **No duplication across the project.** A ripgrep of every other requirement for `6\.67`, `85% of`, `16% of` and "culture enables AI" finds no page use. The only hit is "28.16% of" in an FSM source line.
- No figure is invented.

## 7. Human tone / AI-detection heuristics: PASS

- **Stock-phrase sweep: 0 hits on the page.** The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just", "in conclusion", cutting-edge, game-changing, revolution-, unleash, delve, landscape, ever-evolving, state-of-the-art, synergy, supercharge, transformative, navigate, pivotal, crucial, furthermore, moreover, additionally, ensure, comprehensive, innovative, dynamic, effortless, stunning, insight(s), data-driven, end-to-end, powerful, foster, realm, embark, paramount, "at the heart of", "next level" and "whether you're". The only hits are in Flags (386, 392).
- **The copy stays specific throughout.** Examples: "Ramadan, Eid and the summer slowdown", "forecasts reconcile to the ledger you close each month", "falling order frequency, shrinking spend or rising complaints".
- **The v4 fixes read naturally.**
- **The loop-1 "We + verb" run is still resolved.** S6 backs open We / Our models / Signals / We / Our clustering models / We. S7 opens We / We / We / Star schemas / We / Customer segments (item 05 s2) / Our team.
- **Advisories (not scored):**
  - **E, carried. The "already [verb]" tic.** It appears 10 times on the page (lines 24, 80, 117, 197, 201, 271, 302, 338, 341, 347). "the sources you already run" is repeated exactly at 80 and 347. Word-neutral option: in A7 s2 (347), change "the sources you already run" to "the systems you have today".
  - **F, carried.** 4 of the 6 S6 backs hinge on ", so ...". Word-neutral option for card 4 s2 (161): "Scores can flow into HLB HAMT's own SugarAI CRM and sit beside each lead in the pipeline." Keep the L5 link.
  - **G, new. Three "We run" openers:** S5 row 1 (96), S7 intro (185) and S9 intro (225). Word-neutral option for S9 intro s1: "We put every engagement through the same five stages." B2 still holds.

## 8. Section structure, CTAs, FAQ, internal links: PASS

- **Order.** S0, S1 (H1 + 3 H3 cards + scope line), S2 + S2b, S3, S4 (4 cards), S5 (3 rows + foundation block), S6 (6 flip cards + pill row), S7 (01-06), S8, S9 (5 steps, highlighted band), S10 (3 tabs, no featured card), S11 (6 tiles), S12, S13, S14, S15, S16. This matches the Section 3b order. "Why AI Changes CRM" has no equivalent.
- **Headings.** There is exactly one H1 (22). No SugarAI or Power BI H2 is reused verbatim.
- **S3 anchor nav.** 7 labels in brief order (16).
- **CTAs: exactly 4, in the planned places.**
  - CTA 1: hero "Book a free consultation" (#contact) + "Explore our services" (#services) (26).
  - CTA 2: S8, after S7 Services, "Request a readiness assessment" (217). The assessment is not called "free".
  - CTA 3: S13, after the S12 teaser, "Talk to our analytics team" (320).
  - CTA 4: S15 form "Schedule a Consultation" (361).
  - No buttons on S6 (174), S9 (242), S10 (275) or S12 (312).
  - The only other button is the S2b "Read HLB's announcement" link (63). It is the recognition-bar element that brief Section 4 (S2b) prescribes, not a conversion CTA, and all three loops have ruled it the same way.
  - The in-text links "five-stage method" (#methodology, 80), "use cases above" (#usecases, 338) and "readiness assessment" (#contact, 347) are allowed by 3c.
- **FAQ.** 9 Q&As, with H3 questions in a single accordion. Every answer is 55-65 words, and A6 will be 64 after the fix. Q1-Q7 keep Tab 2's questions. Q9 has 2 "Power BI" mentions and no links.
- **Internal links (all anchors exact):**
  - L1: S4 lede (71) → https://hlbhamt.com/services/digital-transformation-uae/
  - L2: S11 tile 5 (298) → `PLACEHOLDER:power-bi-services-homepage-final-url`, plus the Deliver note (299)
  - L3: S6 card 6 (171) → `PLACEHOLDER:/services/data-visualisation-services/`, plus the Deliver note (172)
  - L4: FAQ 8 (350) → https://hlbhamt.com/services/data-privacy-and-security-uae/
  - L5: S6 card 4 (161) → https://hlbhamt.com/sugarai-crm-2/
  - There is no link to the live AA URL (which would be a self-link) or to any "do not link" page.

## 9. Client requirements (Section 10) and fabricated commitments: PASS

- **Point 1:** replace in place at `/services/advanced-data-analytics-uae/` (line 15).
- **Point 2:** "Microsoft" = 0, and "Power BI" = 4, as the sibling-service name only.
- **Point 3:** the L2 and L3 placeholders are in place.
- **Point 4 (OQ5).** S9, S10 Extend and S4 card 4 draw their substance from the competitor pattern: discovery → preparation → build → deploy → monitor/retrain, periodic reviews, capability building and a named contact. The wording is original (5.1). It reads more substantive than the brief's self-derived default, and it stays qualitative.
- **Point 5:** "PowerUP!" appears 0 times.
- **Point 6:** S12 is a static placeholder, and its copy does not depend on a specific asset.
- **No transcript** was supplied.
- **No fabricated commitments.** There are no durations, prices, uptime or response-time figures, or SLA terms.
  - "We reply within one business day" (S15) is the site-standard form promise that the brief prescribes.
  - "Week by week or quarter by quarter" (S7 05) describes forecast granularity, not a delivery time.
  - No competitor number (DRC "24 hours", Ometis "2-4 weeks" / "90 days") is borrowed.
- **Go-live confirmations (non-blocking), carried from Build Flag 2:**
  - (a) Post-go-live monitoring, retraining and reviews (S4 card 4, S9 step 5, S10 Extend).
  - (b) The "named consultant" (S10 Extend, line 269). Fallback: "We watch...".
- **Deliver handoffs** (unchanged from Build Flags 8 and 10):
  - Set the final URLs for L2 and L3 (OQ4).
  - Update the Power BI homepage's P2 placeholder to `/services/advanced-data-analytics-uae/`.
  - Build the FAQPage schema from the final on-page text. That means v4's A2 and A7, and A6 as fixed.

---

## Overall: FAIL (loop 3 of 3)

- **Only item 5 fails, on one sentence:** FAQ A6 sentence 3 slot-for-slot rewords Tab 2 FAQ 6 sentence 3. Loop 1 failed the same source-sentence echo in S6 card 5, and both earlier loops missed this instance.
- **Everything else passes:**
  - All 3 loop-2 fixes are applied verbatim.
  - Keywords are 4 / 3 / 1 / 2. "HLB HAMT" = 11, "advanced analytics" = 12, "UAE" = 8, "Power BI" = 4 in its permitted slots, and there are no other third-party names.
  - The word count is 2,733 (2,741 after the fix).
  - There are zero em dashes.
  - The spelling is British.
  - All stats are verified, and PwC is cited in footnotes only.
  - There are exactly 4 CTAs.
  - There are 9 FAQs.
  - The links are correct.
  - No commitments are fabricated.
- **This is loop 3 of 3, so there is no Build loop.** The pipeline should report the remaining issue to the Content Writer, not proceed to Deliver.
- **Once the Content Writer approves the one-sentence replacement** (or accepts the sentence as is), the draft is ready for Deliver with no further Test pass needed. The replacement is word-count safe and changes nothing else.

## Fix instructions (for the Content Writer; exact text)

**Required: FAQ A6, sentence 3 (line 344).**
- **Replace:** "We use machine learning to find valuable cohorts, often small ones, that a spreadsheet filter would not reveal."
- **With:** "We run machine learning clustering across many customer attributes, then profile each cluster so your team knows who is in it and what it is worth."
- A6 goes to 64 words, S14 to 642 and the total to 2,741. B3 is kept ("We").
- Leave sentences 1 and 2 unchanged.
- Do not reintroduce "use machine learning to ... cohorts that ... would miss/not reveal" anywhere on the page. The high-value cohort idea stays on the page through S5 row 3's bullet "High-value cohort identification".
- Update the FAQPage `acceptedAnswer.text` for A6 to match.

**Optional (Content Writer's discretion; none needed to pass; all within budget):**
- **D (recommended). S4 lede, sentence 1 (line 71).**
  - Change to: "HLB HAMT is an advanced analytics company in UAE and, as a licensed audit, tax and advisory firm in the HLB network, checks numbers for a living."
  - Effect: +1 word, so S4 = 260, at its cap.
  - Why: it removes the near-verbatim match with the Power BI S4 lede.
  - If D is applied, do not also apply B.
- **H (recommended, word-neutral). A4, sentence 2 (line 338).**
  - Add a comma after "seen": "We test every model against periods it has not seen, before anyone relies on it, then place the predictions inside the reports your teams already open."
  - Update the FAQPage text to match.
- **B. S4 card 4, sentence 1 (line 83).**
  - Change to: "Models drift as markets move, so we offer to stay on after launch."
  - Effect: +1 word. Apply only if D is not applied.
- **C. S2 item 4 (line 59).**
  - Change to: "Our Dubai team plans and builds your models, in your time zone."
  - Word count unchanged.
- **E. A7, sentence 2 (line 347).**
  - Change "the sources you already run" to "the systems you have today".
  - Word-neutral. Update the FAQPage text to match.
- **F. S6 card 4, sentence 2 (line 161).**
  - Change to: "Scores can flow into HLB HAMT's own SugarAI CRM and sit beside each lead in the pipeline."
  - Word-neutral. Keep the L5 link.
- **G. S9 intro, sentence 1 (line 225).**
  - Change to: "We put every engagement through the same five stages."
  - Word-neutral. B2 still holds.

**If every optional item is applied (D rather than B):** the total is 2,742 and every section stays within its Section 3b budget.

---

Sources consulted for verification:
- [PwC, 29th Global CEO Survey: UAE findings](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026/29th-ceo-survey-uae-findings-2026.html): search extract, UAE 85%.
- [PwC, UAE CEO agenda media release](https://www.pwc.com/m1/en/media-centre/2026/uae-ceo-agenda-investment-acquisitions-ambition.html): corroborates the UAE 85% and the 28 Jan 2026 release.
- [PwC, 29th Global CEO Survey: Middle East findings](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026.html): search extract, GCC 16%.
- [Middle East AI News](https://www.middleeastainews.com/p/middle-east-ceos-lead-globally-in): corroboration.
- [HLB press release, FY2025](https://www.hlb.global/press-room/hlb-reports-12-global-growth-reaching-us6-67-billion-in-fy2025/) and [Consultancy.com.au](https://www.consultancy.com.au/news/12048/hlb-joins-the-6-billion-global-revenue-club-in-return-to-double-digit-growth): US$6.67bn, up 12%.
- [UAE Government portal, Data protection laws](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws): PDPL, Federal Decree-Law No. 45 of 2021.
- [Softcrylic, Advanced Analytics Services](https://www.softcrylic.com/advanced-analytics-services/) and [Softcrylic, Advanced Analytics](https://softcrylic.com/data-and-analytics-services/advanced-analytics/): search extracts only; the page renders empty to WebFetch.
- [Apexon, Advanced Analytics and AI/ML Services](https://www.apexon.com/our-services/data-analytics/advanced-analytics-and-ai-ml-services/) and [Apexon, Data Training as a Service](https://www.apexon.com/our-services/data-analytics/data-training-as-a-service/): search extracts only; WebFetch returned HTTP 503.
- [Onehouse, Data Lake vs. Warehouse vs. Lakehouse](https://www.onehouse.ai/blog/data-lake-vs-warehouse-vs-lakehouse) and [Databricks, Data Lakes vs Data Warehouses](https://www.databricks.com/blog/data-lakes-vs-data-warehouses-what-your-organization-needs-know): the generic lakehouse definition.
- [Statsig, What is cohort analysis?](https://www.statsig.com/perspectives/what-is-cohort-analysis) and [Conviva, Cohort Analysis](https://www.conviva.ai/glossary/cohort-analysis/): generic cohort material; no copy of the Tab 2 sentence.
- The other exact-phrase searches returned no match (5.5).
