# Test report v2: Advanced Analytics Services homepage (draft-v2.md, loop 1 of 3)

Tested by: Test agent, 2026-09-29
Loop: **1 of 3.** This is the first Test pass for this requirement. draft-v1 was a Build-only pass, superseded by v2 before any Test ran. The report is numbered v2 to match the draft it tests.

Inputs checked:
- `brief.md`, all of it. Section 10 (Content Writer decisions) overrides Sections 1-9 where it says so, in particular point 4 (OQ5: S9, S10 and the support angle may draw substance from competitor pages, but no wording).
- `draft/draft-v2.md`, all of it: page, Sources, Stats used and all 10 Flags. I compared it line by line with `draft/draft-v1.md`.
- `inputs/competitor-content/research-summary.md` and the four fetched competitor texts: `drcsystems.txt`, `ometis.txt`, `protiviti.txt` and `insightconsulting.txt`. The page copy was read in full, not just the grepped sections.
- `inputs/extracted/` (Tab 2 HTML extract and docx extract), including the two [DO NOT REUSE] intro paragraphs and the 7 source FAQ answers.
- `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`, all of it.
- The delivered Power BI homepage: `2026-09-28-power-bi-services-homepage/draft/draft-v7.md` (the page that passed) and `test-report-v7.md` (for project conventions).
- Web: PwC UAE and Middle East CEO Survey extracts, the HLB press release, and exact-phrase searches for distinctive draft sentences (listed at the end).

Method:
- There was no shell. Names, keywords, characters, links and footnotes were checked with ripgrep across the whole file. I then excluded lines that are not page copy: meta, draft header, chrome, structure headers, eyebrows, buttons, URLs, Sources, Stats used and Flags.
- **Word count:** I copied the counted copy of every section into a scratch file, one section per line, and machine-counted whitespace-delimited tokens with ripgrep (offset probing). I checked the section boundaries by line number and hand-counted each section to confirm.

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density, branding B1-B5, T1-T6 | **PASS** |
| 2 | Word count | **PASS** (2,736) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** (2 advisories) |
| 5 | Originality (competitors, content source, SugarAI template, Power BI sibling, web) | **FAIL** (3 close paraphrases of the content source; one also echoes the Power BI sibling. All 6 competitor pages are clean) |
| 6 | Stat accuracy and footnoting | **PASS** |
| 7 | Human tone / AI-detection heuristics | **FAIL** (a run of 10 consecutive "We + verb" paragraph openers across S6 and S7) |
| 8 | Section structure, CTAs, FAQ, internal links | **PASS** |
| 9 | Client requirements (Section 10 decisions, OQ5 competitor sourcing, no fabricated commitments) | **PASS** (2 go-live confirmations carried) |

### Answers to the five specific questions

1. **Copying from the 6 competitor pages: none found.** I read the whole page against all four fetched texts and the Apexon and Softcrylic summaries. No sentence, heading or distinctive phrase is copied or closely paraphrased. Build's S9 intro fix holds: v1's "so you always know what happens next" (DRC: "so you always know exactly what happens next") is gone. The only failures under item 5 are against **HLB HAMT's own content source** and the **Power BI sibling**, not against competitors.
2. **Fabricated commitments: none.** No duration, price, uptime figure, response time or SLA term appears in S4 card 4, S9, S10 or anywhere else. The only time-bound promise on the page is S15's "we reply within one business day". That is the site's standing contact-form promise (the SugarAI template says "within one business day"), and brief S15 prescribes it. It is not an analytics support SLA.
3. **S9 methodology: credible and grounded, without copied wording.** Stage mapping:

   | S9 stage | DRC Systems | Insight Consulting |
   |---|---|---|
   | Discover and assess | 01 Data Discovery & Strategy | "thorough business requirements meeting" |
   | Engineer the foundation | 02 Data Preparation | (blueprint) |
   | Build and validate models | 03 Analytics Development | "iterative development process" |
   | Deploy into daily reporting | 04 Deployment | "deliver the final solution" |
   | Track performance and retrain | 05 Maintenance and Support | "training, maintenance, and ongoing support" |

   The stages also keep Tab 2's own sequence (organise sources, model data, apply statistics, visualise) and its readiness-assessment line. The only shared words with DRC are the single generic verbs "discover" and "deploy". Every step body is concrete and HLB-specific: stakeholders and success criteria, star schemas fixing KPI logic, testing on unseen periods, forecasts against actuals, and data-load gap checks. None of it echoes DRC's step text, for example "closely monitor, refine, and optimize ... keeps adding value" or "integrate it with your processes without data loss and hurdles". The section reads as more substantive than the brief's original self-derived version.
4. **PwC attribution: confirmed footnote-only.** "PwC" appears only in Sources 1 and 3 (lines 369, 371) and in the Flags. S2 item 2 now reads "85% [1] / of UAE CEOs surveyed say their organisation's culture enables AI adoption." The S5 foundation block reads "...only 16% of GCC CEOs surveyed agree ... documents and data. [3]". This matches the delivered Power BI page (draft-v7), where every stat carries only an `[n]` marker and no inline source. "CEOs surveyed" keeps B5 attribution to survey respondents clear. Markers run [1] S2, [2] S2b, [3] S5, [4] FAQ 8, in order of appearance.
5. **S5 row 2 H3 "What happens next": generic, fine. Not an echo.**
   - DRC uses the phrase in a different sense: project predictability in a methodology intro ("so you always know exactly what happens next"). Here it means forecasting future outcomes.
   - The closer semantic match is Ometis's predictive blurb ("anticipates what might happen next"). But the why / what next / what to do framing is the standard analytics-maturity model, and it is HLB HAMT's own Tab 2 FAQ 1 wording ("why it happened, what will happen next, and what you should do about it"). The brief prescribes the heading.
   - For completeness, row 3's "What to do about it" also matches a clause in Ometis's prescriptive blurb ("It guides you on what to do about it"). The same ruling applies: it is a generic idiom, it derives from HLB's own source, it is brief-prescribed, and it is not Ometis's heading. Ometis's headings are "Descriptive / Predictive / Prescriptive", which the draft correctly avoids.
   - "What happens next" now appears only once on the page (line 105).

---

## 1. Keyword placement and density: PASS

On-page copy only, using the brief Section 2a rules and the lookahead logic applied by hand.

| Keyword | Count | Placements (line) | Target | Result |
|---|---|---|---|---|
| Primary "advanced analytics services in UAE" | **4** | H1 (22); hero lede s1 (24); S14 H2 (326); S15 body (359) | 3-4 (max 5) | Pass |
| Secondary "advanced analytics services" (not followed by "in (the) UAE") | **3** | S7 H2 (183); S10 intro (250); S11 H2 (281) | 2-3 | Pass |
| "advanced analytics company in UAE" | **1** | S4 lede s1 (71) | 1 (max 2) | Pass |
| "data analytics and automation" | **2** | S7 intro (185); S11 tile 2 H3 (288) | 2-3 | Pass |
| Forbidden "advanced analytics services in the UAE" | **0** on page | (only Flags line 403) | 0 | Pass |

- **Meta title** (line 1) and **meta description** (line 2) match brief Section 7 exactly. Both lead with the primary keyword.
- **H1 and first 100 words:** the primary keyword appears in the H1 and in hero lede sentence 1. Pass.
- **T1 "HLB HAMT": 11** (range 9-14), at lines 22, 61, 71, 161, 176, 183, 281, 283, 308, 329 and 353. Excluded: eyebrows (20, 279) and structure headers (65, 179, 277).
- **T2 "advanced analytics" (any form): 12** (cap 18), at lines 22, 24, 71, 183, 250, 281, 326, 328, 329, 352, 353 and 359.
- **T3 third-party names:** the case-sensitive whole-word sweep of the full brief list plus SQL, AWS, Google, Looker, Power Automate, Teams and SharePoint found **0**. "Power BI" = **4** (S11 tile 5 H3 297, tile 5 body 298, Q9 352, A9 353). That meets the max of 4, in the two permitted slots only. Line 299 is a Deliver note. "Microsoft" = 0 on the page. "SugarAI CRM" appears only as L5 (161).
- **T4 "UAE": 8** (cap 10), at lines 22, 24, 51, 71, 281, 326, 350 and 359.
- **T5 and T6:** 0 hits on the page for every banned string, the sibling-page stats, "certified", "leading", "#1", "award-winning", "guarantee" and "zero manual intervention".
- **2d:** 2 of the 6 S7 titles contain "analytics" (items 03 and 04); 0 of the 5 S9 titles do. Titles do not all start with "Data".
- **Branding:**
  - B1: the H1 opens "HLB HAMT:".
  - B2: every opening sentence has HLB HAMT or "we" as its subject: hero "We deliver"; S4 "HLB HAMT is"; S5 "We treat"; S6 "We start"; S7 "We run"; S9 "We run"; S10 "We package"; S11 "HLB HAMT pairs".
  - B3: every FAQ answer has an HLB or "we" subject: A1 "HLB HAMT builds"; A2 "We build"; A3 "We design"; A4 "We test"; A5 "We connect"; A6 "We use"; A7 "we recommend"; A8 "We limit"; A9 "HLB HAMT delivers".
  - B5: the revenue is "network-wide" and belongs to HLB. The PwC figures are "CEOs surveyed".
- **Stuffing:** none. Each secondary keyword sits in its assigned slot, and no sentence repeats a keyword awkwardly.

## 2. Word count: PASS (2,736)

This was a fresh machine count under the brief Section 1 rule.
- **Included:** H1, H2s, H3s, ledes, sub-block line, card, tile and strip text, S2b, bullets, tab names, taglines, pill label and pills, FAQ questions and answers, and CTA headings and bodies.
- **Excluded:** eyebrows, buttons, nav, breadcrumb, form, S5 "Capability" / "Key capabilities" / "Foundation layer" labels, S7 pillar labels, footnote markers, Sources and Flags.

| Section | Count | Budget (3b) | Status |
|---|---|---|---|
| S1 | 154 | 130-160 | OK |
| S2 + S2b | 70 (S2b 24) | 50-70 | OK |
| S4 | 259 (lede 61; cards 42/41/46/45) | 220-260 | OK (1 under cap) |
| S5 | 322 (intro 49; row descriptions 40/41/44; foundation body 64) | 320-380 | OK |
| S6 | 320 (backs 32/32/32/34/30/30; taglines 7-9) | 260-320 | OK (at cap; the 26 pill tokens include 4 "&" and "/" symbols) |
| S7 | 350 | 330-380 | OK |
| S8 | 28 | 20-30 | OK |
| S9 | 157 | 130-160 | OK |
| S10 | 210 (with tab names) | 170-220 | OK |
| S11 | 150 | 120-150 | OK (at cap) |
| S12 | 30 | 25-40 | OK |
| S13 | 27 | 20-30 | OK |
| S14 | 630 (answers 57/65/59/60/56/56/59/65/55) | 550-660 | OK |
| S15 | 29 | 20-30 | OK |
| **Total** | **2,736** | 2,400-2,800 (fail below 2,250 or above 3,000) | **PASS** |

- Build's self-count (about 2,739) agrees within 3 words. The small per-section differences are S2 (Build 69, Test 70) and S5 (Build about 325, Test 322).
- Sub-unit note, not scored: S7 item bodies run 44-52 words, and items 02 and 03 are one word under the 45-word guide if the H3 is excluded. Every item is inside 45-55 if the H3 is included, except item 05 (56). This is within rounding either way.

## 3. Zero em dashes: PASS

Whole-file ripgrep: `—` **0**, `–` (en dash) **0**, `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- I re-read every page line (22-359) and found no grammatical errors. Constructions checked and confirmed correct:
  - A2's colon followed by a three-part series with semicolons.
  - A8's "That matters because ..." clause chain.
  - S5 row 3's colon list.
  - S9 intro's compound sentence.
- **British spelling:** the sweep for -ize/-yze, color, center, program, behavior, modeling, license, toward and catalog found **0** on the page. Hits appear only in Flags (388, 392: "optimize", "Catalog" inside competitor quotes). British forms confirmed: organisation, modelling, standardise, prioritisation, prioritised, personalised, behaviour, visualisation, programme, centre.
- **Advisory A (not scored): S2 strip punctuation.** Item 1's description ("across data transformation, statistical modelling and enterprise reporting", line 47) has no full stop. Items 2-4 end with one. Add a full stop for consistency.
- **Advisory B (not scored): S4 card 4, sentence 1** (line 83). "Models drift as markets move, so we can stay involved after launch." Here "so" presents the offer as a consequence of drift, which reads slightly off. Suggested wording (13 words, S4 = 260, still at cap): "Models drift as markets move, so we offer to stay on after launch."

## 5. Originality: FAIL

### 5.1 Competitor pages (all 6): clean

- **DRC Systems.**
  - Approach intro ("so you always know exactly what happens next"): gone from S9. The v2 intro "Each stage has an agreed owner and deliverable, and nothing moves on until your team approves the one before" shares no phrasing with it.
  - Stage 05 ("closely monitor, refine, and optimize ... keeps adding value") vs S9 step 5 and S4 card 4: no shared run over 2 words ("monitor" and "retrain" are generic verbs).
  - "Flexible engagement models tailored to you": not used.
  - "Platform-Agnostic": not used.
- **Ometis.**
  - "ongoing consultancy and training to build internal capability" / "grow in capability and confidence" vs S4 card 4 "we coach your analysts to take on more": different wording.
  - "instructor-led training and hands-on support" vs S10 "Hands-on training and self-service data preparation": the only overlap is the 2-word generic "hands-on".
  - Support-channel list (email, portal, phone): not used.
  - Descriptive / Predictive / Prescriptive headings: not used (see question 5 above).
- **Protiviti.** "ongoing monitoring", "Preventive not responsive", "Operational resilience", "trigger systems": 0 on the page.
- **Insight Consulting.** "thorough business requirements meeting", "comprehensive blueprint", "training, maintenance, and ongoing support for your investment", "we partner with our clients": 0 on the page.
- **Apexon and Softcrylic (summaries only).** "The 4 C's", "Curate, Catalog, Context, Consume", "frame the problem worth solving", "Managed Services", "tool-agnostic", "consistent monitoring and fixing": 0 on the page. S10's "Post-launch model care" differs from "Managed Services".
- A ripgrep of the four raw texts for 30 draft terms (retrain, drift, periodic, named, go-live, success criteria, deliverable, owner, proof of value, roadmap, readiness, starting point, pay back, monitor, coach and others) found no shared phrase beyond single generic words.

### 5.2 SugarAI structural sample: clean

- The template labels "What we do", "Who we work with", "How we deliver" and "In-region" are structural labels, which the Section 5 rule allows.
- S4 card 4's H3 "Support once models are live" is adapted from the template's "Support after go-live", not copied, and its body shares no wording with the template's.
- No SugarAI H2 is reused.
- **Advisory C (not scored):** S2 item 4, "Scoped and built by our Dubai consultants, in your time zone," sits close to SugarAI tile "In-region team: Consultants who scope, build and support from the UAE." The brief prescribes the line and it is same-site, so it is not scored. Optional variant: "Our Dubai team plans and builds your models, in your time zone." (11 words, count unchanged.)

### 5.3 Power BI sibling (delivered draft-v7): one required fix, one advisory

- **Fails, see 5.4(c):** FAQ A7 sentence 3.
- **Advisory D (not scored):** S4 lede sentence 1 (line 71), "HLB HAMT is an advanced analytics company in UAE that is also a licensed audit, tax and advisory firm and a member of the HLB network." This is the same frame as the Power BI S4 lede: "HLB HAMT is a Power BI consulting company that is also a licensed audit, tax and advisory firm, and a member of the HLB International network." About 16 of the 20 non-keyword words match in order. Brief Section 2b prescribes this sentence as its example, and it is a same-site factual self-description, so it is not scored. Build should still vary it, because the two pages link to each other. Optional wording (27 words, S4 = 260): "HLB HAMT is an advanced analytics company in UAE and, as a licensed audit, tax and advisory firm in the HLB network, checks numbers for a living."
- **Other close checks, all passed:**
  - S7 06 "access set by role so people see only what they should" vs Power BI "so each person sees only the data their role allows".
  - S7 02 "When volume and variety grow, we extend the design into a layered lakehouse" vs Power BI "move to a lakehouse once volume and system count call for it".
  - S15 "we reply within one business day" (site standard).
  - All three share an idea but not a sentence.

### 5.4 Content source (Tab 2): three close paraphrases (the failures)

The brief's reuse rule (Section 4) says "Build must write new copy for every sentence" and "Build must never use the two Tab 2 intro paragraphs, or close paraphrases of them". In each case below the brief's own outline modelled the wording closely, so Build followed the brief. The resulting sentences still fail the rule.

**(a) S5 row 1 description, sentence 1 (line 96): a close paraphrase of a [DO NOT REUSE] intro clause**, which itself tracks Softcrylic (brief 5b).

| draft-v2 | Tab 2 intro paragraph 1 [DO NOT REUSE] | Softcrylic (brief 5b extract) |
|---|---|---|
| "We apply statistical techniques, including regression and correlation analysis, to find the relationships and trends behind a KPI movement." | "applying advanced statistical techniques to identify relationships and trends" | "apply statistical modeling to identify key relationships in the data" |

The same verb, object and purpose clause appear in the same order, with one synonym swapped (identify → find). This is the Softcrylic-derived chain the brief bans from the page.

**(b) S6 flip card 5 back (line 166): a light rewording of Tab 2 FAQ 6, both sentences.**

| draft-v2 | Tab 2 FAQ 6 (source, live on the page being replaced) |
|---|---|
| "We group customers by behaviour, value, preferences or demographics for personalised campaigns, upselling, retention and resource allocation." | "Customer segmentation uses data analytics to group customers by behavior, value, preferences, or demographics. This enables personalized marketing campaigns, targeted upselling, improved retention strategies, and better resource allocation." |
| "Machine learning surfaces high-value cohorts a manual cut of the data would miss." | "Our segmentation models use machine learning to identify high-value cohorts that manual analysis would miss." |

- Sentence 1 keeps the source's four attributes in the same order and its four uses in the same order, with only adjectives removed.
- Sentence 2 keeps the structure "machine learning → high-value cohorts → manual ... would miss".
- By contrast, FAQ A6 on the same topic is properly rewritten ("Segmentation divides your customer base into groups that behave alike...").

**(c) FAQ A7, sentence 3 (line 347): tracks both the source FAQ 7 and the Power BI sibling's A3.**

| draft-v2 | Tab 2 FAQ 7 (source) | Power BI draft-v7 A3 (sibling) |
|---|---|---|
| "For enterprise-scale work across many systems, we recommend a data lakehouse, which combines a lake's flexibility with a warehouse's structure and uses the layered design described above." | "For enterprise-scale analytics, we recommend an Azure Data Lakehouse, combining the best of data lakes and data warehouses with a Bronze → Silver → Gold medallion architecture." | "Once data spreads across five or more systems, we recommend a lakehouse so every report works from the same cleaned tables." |

- Against the source, the sentence is clause-for-clause: the same opener ("For enterprise-scale"), the same main clause ("we recommend a ... lakehouse"), the same lake-plus-warehouse appositive and the same trailing layered-architecture reference.
- It also shares the sibling's "across ... systems, we recommend a lakehouse" frame.
- **This answers Build's Flag 9 judgement call.** A7's topic overlap with Power BI FAQ 3 is fine, but this one sentence is not. The rest of A7 is sufficiently rewritten.

**Checked and passed (not failures):**
- A1, A2 and A3 follow the source's fact order, as the definitional answers the brief prescribes.
- Their wording is substantially new.
- The longest shared runs are fixed terms: "ETL stands for extract, transform, load", "that run on (a) schedule", "fact table", "dimension tables".
- S1 card lines use the permitted 3-word pillar descriptors.
- Tile 6's "rip-and-replace" is a shared industry term.

### 5.5 Web (exact-phrase searches, today): no matches

| Phrase searched | Result |
|---|---|
| "Models drift as markets move" | No match. Only generic model-drift articles. |
| "nothing moves on until your team approves" | No match. |
| "compare forecasts with actuals" + "retrain when patterns shift" | No match. |
| "named consultant watches pipelines, data quality and model drift" | No match. |
| "Where Our Models Earn Their Keep" | No match. Fashion-modelling results only. |
| "From First Workshop to Live Forecast" | No match. |
| "no longer depend on someone re-keying numbers by hand" | No match. |
| "a spreadsheet filter would not reveal" | No match. |
| "Our accountants know how a revenue line or cash position is produced" | No match. |
| "combines a lake's flexibility with a warehouse's structure" | No exact match. The lakehouse definition is a ubiquitous generic concept (for example Databricks and DataCamp describe it in similar terms). The problem with A7 is the source and sibling frame, not the web. |
| "group customers by behavior, value, preferences, or demographics" (the source's own wording) | No third-party page reproduces it. Generic segmentation guides only. So 5.4(b) is a source-reuse problem, not web plagiarism. |

## 6. Stat accuracy and footnoting: PASS

| Ref | Figure | Location | Check | Result |
|---|---|---|---|---|
| [1] S-1 | 85% of UAE CEOs say their organisation's culture enables AI adoption | S2 item 2 only | Search extract of PwC's *29th Global CEO Survey: UAE findings* (Jan 2026) confirms "85% of UAE CEOs say that their organisation's culture enables AI adoption". Credible, and about 8 months old. | Pass |
| [2] S-3 | HLB network revenue US$6.67bn for 2025, up 12% | S2b only | The HLB press-room title "HLB reports 12% global growth, reaching US$6.67 billion in FY2025" plus Consultancy.com.au. Attributed to the network ("network-wide revenue"), not HLB HAMT (B5). | Pass |
| [3] S-2 | 16% of GCC CEOs agree their most-used AI tools have access to all relevant documents and data | S5 foundation block only | Search extract of PwC's *Middle East findings*: "Only 29 percent of Middle East CEOs and 16 percent in the GCC agree that their most-used AI tools have access to all relevant documents and data." The draft uses only the GCC figure both sources agree on. Framed as the reason to build the foundation first, not as a scare line. | Pass |
| [4] F1 | UAE PDPL, Federal Decree-Law No. 45 of 2021 | FAQ 8 only | Matches the u.ae data-protection-laws page cited in brief 6c. The draft says "governed by" and "in line with", never "guarantees compliance". | Pass |
| (none) CS1 | 11 services | S2 item 1 only | Tab 2 badges: 5 + 3 + 3. HLB HAMT's own catalogue, so no footnote. | Pass |

- Each stat appears in one section only. No FAQ restates 11, 85%, 16% or US$6.67bn.
- No figure is invented.
- **No duplication across the project:** ripgrep of every other requirement's `draft/` and `output/` files for `6\.67`, `85%` and `16% of` finds no use on the Power BI or SugarAI FSM pages. The only `85%` hits are CSS heights in the Power BI HTML.
- The sibling-page stats (200+, 33x, 7 days, Since 1999, 25/26 years, 150+, 19th, 14+) appear 0 times on the page.

## 7. Human tone / AI-detection heuristics: FAIL

**Stock-phrase sweep: 0 hits on the page.** The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just", "in conclusion", cutting-edge, game-changing, revolutionise, unleash, delve, landscape, ever-evolving, state-of-the-art, world-class, best-in-class, synergy, supercharge, transformative, navigate, pivotal, crucial, furthermore, moreover, additionally, ensure, comprehensive, innovative, dynamic, effortless, stunning and insight(s). The only hits are in Flags (386 "Insight", 392 "tailored"). The copy is specific and concrete throughout. Examples: "Planners see a shortfall or overstock building early", "so forecasts reconcile to the ledger you close each month", "Ramadan, Eid and the summer slowdown".

**Failure: repetitive "We + verb" openers across S6 and S7, a templated rhythm.**
- S6 flip-card backs: **5 of 6** open "We + verb" (card 1 "We forecast", 3 "We score", 4 "We rank", 5 "We group", 6 "We build"; only card 2 opens "Our models estimate").
- S7 items: **5 of 6** open "We + verb" (01 "We extract", 02 "We design", 03 "We design", 04 "We train", 05 "We forecast"; 06 "Our team designs"). Items 02 and 03 open with the **same two words**, back to back.
- Read in page order, card 3 through S7 item 05 gives **10 consecutive paragraphs** that open "We + verb": card 3, card 4, card 5, card 6, S7 intro, and items 01, 02, 03, 04 and 05. Only the pill row sits in between.
- **Project precedent:** Power BI `test-report-v5.md` item 7 failed the same pattern (all 6 S6 backs opening "We + verb") and fixed it by varying three openers while keeping HLB HAMT as the actor (Fix 7). B2 requires an HLB-led first sentence for **section intros only**, not for every card.
- S5's rows are excluded because the brief mandates "opens with an HLB HAMT action". S9 (3 of 5) is acceptable.

Suggested rewrites (in Fix instructions 7a-7c): vary S6 cards 3 and 5 and S7 item 03. Afterwards, S6 opens We / Our models / Signals / We / Our clustering models / We, and S7 opens We / We / Star schemas / We / We / Our team.

## 8. Section structure, CTAs, FAQ, internal links: PASS

- **Order:** S0 breadcrumb, S1 hero, S2 strip + S2b, S3 anchor nav, S4 Why HLB HAMT, S5 Explore (3 rows + foundation block), S6 Use cases (6 flip cards + pill row), S7 Services (01-06), S8 CTA, S9 method (5 steps, highlighted band), S10 Engagement models (3 tabs, no featured card), S11 (6 tiles), S12 teaser, S13 CTA, S14 FAQ, S15 contact, S16 footer. All present, in the Section 3b order. The excluded "Why AI Changes CRM" has no equivalent. Pass.
- **Headings:** exactly one H1 (22). Every section H2 is present. No SugarAI or Power BI H2 is reused verbatim. S10 avoids the Power BI H2, as instructed.
- **S3 anchor nav:** 7 labels in brief order: Why HLB HAMT · Capabilities · Use Cases · Services · Our Method · Engagement Models · FAQ.
- **CTAs: exactly 4.**
  - CTA 1: hero "Book a free consultation" (#contact) + "Explore our services" (#services).
  - CTA 2: S8 "Request a readiness assessment" (#contact). The S8 body does not call the assessment free, which is correct.
  - CTA 3: S13 "Talk to our analytics team" (#contact).
  - CTA 4: S15 form "Schedule a Consultation".
  - No buttons on S6, S9, S10 or S12.
  - The S2b "Read HLB's announcement" link-button is the brief-prescribed recognition-bar element (Section 4, S2b), not a conversion CTA.
  - In-text links ("five-stage method" → #methodology, "use cases above" → #usecases, "readiness assessment" → #contact) are allowed by 3c.
- **FAQ:** **9** Q&As, with H3 questions in a single accordion. Q1-Q7 keep Tab 2's questions, lightly reworded in British spelling. Q8 and Q9 are new, as planned. Every answer is 55-65 words and opens with a direct answer. B3 holds (item 1). "Power BI" appears 2 times in the Q9 Q&A (cap 2), and Q9 carries no links. Pass.
- **Internal links:**

| Link | Anchor | Target | Location | Result |
|---|---|---|---|---|
| L1 | digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ | S4 lede (71) | Exact |
| L2 | Power BI services | `PLACEHOLDER:power-bi-services-homepage-final-url` + Deliver note (299) | S11 tile 5 (298) | Exact, per Section 8 and Section 10 point 3(a) |
| L3 | data visualisation services | `PLACEHOLDER:/services/data-visualisation-services/` + Deliver note (172) | S6 card 6 (171) | Exact, per Section 10 point 3(b) |
| L4 | data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ | FAQ 8 (350) | Exact |
| L5 | SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ | S6 card 4 (161) | Exact (optional link, used) |

  - Nothing links to the live AA URL, which would be a self-link, or to any "do not link" page. The only external URL in the page body besides L1 and L4 is the S2b button target, the HLB press release.
- **Schema (for Deliver):** Service, FAQPage (9 Q&As, identical text, `[n]` stripped) and BreadcrumbList, as Flag 10 says.

## 9. Client requirements (Section 10 decisions): PASS

- **Point 1 (OQ1):** replace in place at `/services/advanced-data-analytics-uae/` (chrome note, line 15). Pass.
- **Point 2 (OQ3):** no platform names. "Microsoft" = 0. "Power BI" appears only as the sibling-service name (4). Pass.
- **Point 3 (OQ4):** both placeholders are in place (L2, L3). Pass.
- **Point 4 (OQ5):**
  - The substance for S9, S10 and support is now drawn from the competitor research. It covers stages in the discovery → preparation → build → deploy → monitor pattern, and pipeline and data-quality monitoring, predictions measured against actuals, retraining, periodic reviews, capability building and a named contact.
  - The wording is original (item 5.1).
  - It is qualitative only: no durations, prices or SLA terms (see question 2).
  - DRC's "24 hours" and Ometis's "2-4 weeks" and "90 days" are not borrowed.
  - Section 10 point 4 explicitly overrides brief S4 card 4's original "do not promise ... model monitoring or retraining" default. Pass.
- **Point 5 (OQ6):** "PowerUP!" appears 0 times anywhere in the file. Pass.
- **Point 6 (OQ7):** S12 uses a static screenshot/GIF placeholder, and its copy does not depend on a specific asset. Pass.
- **No transcript** was supplied for this requirement.
- **For the Content Writer, before go-live (non-blocking; Build Flag 2):**
  - (a) Confirm that HLB HAMT analytics engagements can include post-go-live monitoring, retraining and periodic reviews (S4 card 4, S9 step 5, S10 Extend).
  - (b) Confirm that a named consultant is assigned for post-launch model care (S10 Extend).
  - Both are qualitative and allowed under Section 10 point 4, but neither is confirmed by an HLB HAMT source. Fallback for (b): "We watch pipelines, data quality and model drift..." (word count stays in range).

---

## Overall: FAIL (loop 1 of 3)

Two items fail, and the fixes are small.
- **Item 5, originality:** 3 sentences are close paraphrases of HLB HAMT's Tab 2 source, and one of them also echoes the Power BI sibling.
- **Item 7, tone:** a 10-paragraph run of "We + verb" openers across S6 and S7.

Everything else passes:
- Keywords 4 / 3 / 1 / 2, "HLB HAMT" 11, "UAE" 8, "Power BI" 4.
- Word count 2,736.
- Zero em dashes.
- All stats verified.
- Structure, CTAs, FAQ and links are correct.
- The competitor-sourcing work in S9, S10 and S4 card 4 is clean and credible.

## Fix instructions

Word-count effect of all required fixes together: S5 322 → 321, S6 320 → 320, S7 350 → 349, S14 630 → 633. The total stays about 2,737, and every section stays inside its budget. Change nothing else.

**Fix 5a (required). S5 row 1 description, sentence 1 (line 96).**
- Replace "We apply statistical techniques, including regression and correlation analysis, to find the relationships and trends behind a KPI movement."
- With: "We run regression and correlation analysis on the transactions and ledger lines that sit behind a KPI movement." (18 words, previously 19; description = 39).
- Keep sentence 2 ("Instead of a flat month-on-month variance...") and the bullets unchanged. The bullet "Relationship and trend analysis" is a brief-prescribed generic label and may stay.
- Do not reintroduce "apply ... statistical techniques/modelling to identify/find ... relationships (and trends)" anywhere on the page.

**Fix 5b + 7b (required, one edit). S6 flip card 5 back (line 166).**
- Replace both sentences with: "Our clustering models group customers by what they buy, how often and how much they spend, so marketing and sales can target, retain or upsell each segment on its own terms." (31 words, previously 30; the card back range is 30-40).
- This drops the source's four-attribute list and four-use list, and varies the opener.
- The machine-learning / high-value cohort point is already carried by S5 row 3 ("High-value cohort identification") and FAQ A6, so do not re-add it here.
- The front H3 and tagline are unchanged.

**Fix 5c (required). FAQ A7, sentence 3 (line 347).**
- Replace "For enterprise-scale work across many systems, we recommend a data lakehouse, which combines a lake's flexibility with a warehouse's structure and uses the layered design described above."
- With: "Where the numbers come from many systems at enterprise scale, we build a data lakehouse instead, pairing a lake's flexibility with a warehouse's structure through the layered design described above." (30 words, previously 27; A7 = 62, within 50-65).
- Keep "we" as the subject: this is A7's only B3 sentence.
- Sentences 1, 2 and 4 are unchanged. Keep the "readiness assessment" link to #contact.

**Fix 7a (required). S6 flip card 3 back (line 156).**
- Replace "We score each customer's likelihood of leaving from signals such as falling order frequency, shrinking spend or rising complaints. Account teams get a ranked list and step in before the relationship lapses."
- With: "Signals such as falling order frequency, shrinking spend or rising complaints drive our churn score for each customer. Account teams get a ranked list and step in before the relationship lapses." (31 words, previously 32).
- HLB HAMT stays the actor ("our churn score").

**Fix 7c (required). S7 item 03 body, sentence 1 (line 197).**
- Replace "We design star schemas around the KPIs you report on, so queries return quickly and every measure has one agreed definition."
- With: "Star schemas built around the KPIs you already report on keep queries fast and give every measure one agreed definition." (20 words, previously 21).
- This breaks the back-to-back "We design" openers of items 02 and 03.
- Keep sentence 2 ("Alongside them, we set up self-service data preparation...") unchanged, so HLB HAMT stays the actor.
- Star schemas are still named, not defined (FAQ 3 defines them).

**Optional, same pass (advisories, not required to pass):**
- A (S2 item 1, line 47): add a full stop at the end of the description.
- B (S4 card 4, line 83): "Models drift as markets move, so we offer to stay on after launch." (+1 word; S4 = 260, at cap).
- D (S4 lede, line 71): vary the sentence shared with the Power BI lede, for example "HLB HAMT is an advanced analytics company in UAE and, as a licensed audit, tax and advisory firm in the HLB network, checks numbers for a living." (+1 word). **Apply B or D, not both, or S4 exceeds its 260 cap.** If both are wanted, trim one word elsewhere in S4.
- C (S2 item 4, line 59): "Our Dubai team plans and builds your models, in your time zone." (11 words, no change).

After the fixes, Build should update:
- Flag 5 (word counts).
- Flag 9: record Test's ruling on the FAQ 7 judgement call, meaning the topic is fine and the sentence 3 frame is fixed.

---

Sources consulted for verification:
- [PwC, 29th Global CEO Survey: UAE findings](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026/29th-ceo-survey-uae-findings-2026.html): 85% of UAE CEOs say culture enables AI adoption (search extract)
- [PwC, 29th Global CEO Survey: Middle East findings](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026.html): 16% in the GCC, 29% Middle East (search extract)
- [Middle East AI News, "Middle East CEOs lead globally in AI adoption"](https://www.middleeastainews.com/p/middle-east-ceos-lead-globally-in): corroboration
- [HLB press release, FY2025 results](https://www.hlb.global/press-room/hlb-reports-12-global-growth-reaching-us6-67-billion-in-fy2025/) and [Consultancy.com.au](https://www.consultancy.com.au/news/12048/hlb-joins-the-6-billion-global-revenue-club-in-return-to-double-digit-growth): US$6.67bn, up 12%
- Web exact-phrase searches with no match are listed in 5.5.
