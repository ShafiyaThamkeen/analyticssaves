# Test report v1: SugarAI CRM + Epicor ERP Integration subpage (draft-v1.md, loop 1 of 3)

Tested by: Test agent, 2026-10-07
Loop: **1 of 3** (no earlier test report exists for this requirement).
Inputs: `brief.md` (Section 10 overrides where noted), `draft/draft-v1.md`, `inputs/requirement-notes.md`, `inputs/extracted/tcp-sugarcrm-epicor-kinetic-webinar-slides.pdf.md`, `inputs/structural-sample/hlbhamt-sugarai-insurance.html`, the saved live hub text (`../2026-09-29-data-visualization-services-homepage/inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`), and the FSM sibling page (`../2026-09-23-sugarai-field-service-management-subpage/draft/draft-v5.md`).

Page copy = draft lines 19-327 (Blocks 1-12 and the Sources note). Lines 1-17 are meta and chrome. Lines 328-369 are Build's "Stats used" table and "Flags", which are internal notes and must never ship.

---

## Summary

| # | Item | Result |
|---|---|---|
| 0a | **Critical: TCP-deck exclusions** | **PASS** (0 hits in page copy, captions, alt text, designer descriptions or meta) |
| 0b | **Critical: positioning ("SugarAI integrates with your existing Epicor")** | **PASS** |
| 0c | **Layout: prose-led, not all cards** | **PASS** |
| 1 | Keyword placement and density | **PASS** (4 / 2 / 2 / 1 / 2; total 11, cap 12) |
| 2 | Word count | **PASS** (1,642) |
| 3 | Zero em dashes | **PASS** (0 em, 0 en, 0 `--`) |
| 4 | Grammar, spelling (British), punctuation | **PASS** (advisories only) |
| 5 | Originality | **FAIL**. TCP deck and all 5 reference sites are clean. 9 lines reuse or lightly reword HLB HAMT's own Insurance template or live hub, which brief Sections 4 and 5 forbid. |
| 6 | Stat accuracy and footnoting | **FAIL** (1 item: the A1 qualifier is incomplete; the other 5 figures and facts were re-verified today) |
| 7 | Human tone / AI-detection heuristics | **PASS** (advisories only) |
| 8 | Section structure | **PASS** |
| 9 | Client requirements (Section 10, requirement notes); no transcript | **PASS** |

**Overall: FAIL (loop 1 of 3).** There are two failing items, and both are cheap to fix. The page is clean on the TCP material and on positioning. Fix instructions are at the end.

---

## 0a. Critical check: TCP webinar material. PASS (0 hits on the page)

I ran my own case-insensitive ripgrep over the whole `draft-v1.md`. I did not rely on Build's Flag 1.

| Pattern(s) | Hits in page copy, meta, captions, alt, designer descriptions (lines 1-327) | Hits elsewhere |
|---|---|---|
| `fluent`, `tcp` | **0** | Flags 350, 351, 369 only |
| `14-day`, `14 day`, `free trial` | **0** | Flags 350 only |
| `trial` | **0 as a word**. Substring of "industrial" at 235 (×2, Block 9) and 308 (×2, Sources [4] title and URL) | Stats-used 336 ("industrial"); Flags 350 |
| `free` | **0 as an offer**. Only "free zone" (235, Block 9, a UAE company type) | Flags 350 |
| `Southern Alumin`, `Palazzi`, `West Coast`, `Towle` | **0** | Flags 350 only |
| `200+`, `150+` | **0** | Flags 350 only |
| `sales day(s)`, `2 sales days`, `two sales days`, `selling day(s)` | **0** | Flags 350 only ("sales days") |
| `offline` | **0** | Flags 350 only |
| `any Epicor data` | **0** | Flags 350 only |
| `Prophet`, `Eclipse`, `BisTrack` | **0** | Flags 350, 354 only |
| `Northern Depot` | **0** | Flags 350 only |
| Other deck/TCP-page phrases: `purpose-built`, `work where you are`, `perfectly integrated`, `excels`, `seamless`, `Kinetic theme`, `dashlet`, `Account 360`, `Navigator`, `O365`, `Microsoft 365`, `Platinum`, `Premier`, `hours, not weeks`, `live in hours`, `Codeless`, `iPaaS`, `middleware`, `sales-i` | **0** | `Codeless` in Flag 351 only |

**This matches Build's self-reported search exactly.** The only page-copy substrings are "free zone" and "industrial", and every other hit sits inside the Flags list. The four designer descriptions (88, 125, 142, 187) carry no TCP name, no "Northern Depot" and no TCP stage labels. Build moved the "do not trace TCP slides" instruction to Flag 1a so it never ships in an HTML comment or docx cell. That is the right call, and Deliver must pass Flag 1a to the designer separately.

**The word "connector" appears once on the page** (FAQ A4, 298: "any existing connector"). It is the brief's own FAQ 4 wording and names no product.

**Deliver note:** lines 328-369 (Stats used and Flags) contain every banned term by design. They must not be carried into the HTML or docx.

## 0b. Critical check: positioning. PASS

Content Writer emphasis, Section 10 point 1: "bring your Epicor, we connect SugarAI to it." It must be foregrounded in the hero/lede and Block 3, not merely avoided.

| Where | Text (line) | Verdict |
|---|---|---|
| Hero lede s1 | "HLB HAMT connects SugarAI with Epicor ERP **as you already run it**, so sales and service teams see Epicor orders, prices, stock and invoices on their customer records." (27) | Foregrounded. Keeps the exact secondary keyword. |
| Hero lede s2 | "Epicor stays the system of record, and we design, build and support **a custom connection**..." (27) | Custom build (Section 10 point 2). Epicor is untouched. |
| Block 3 P1 s1 | "HLB HAMT builds **a custom integration into the Epicor ERP you already run** and replaces nothing on the Epicor side." (79) | Foregrounded, as the first sentence of the explanatory section. |
| Block 9 | "work alongside **your Epicor partner or in-house ERP team**" (235) | Correct division of roles. |
| FAQ A4 | "We review your configuration and any existing connector, then extend, repair or replace it." (298) | Consistent. |
| IMG-1 designer label | "Your existing Epicor ERP (Epicor Kinetic, cloud or on-premise)" (88) | Consistent (Flag 6). Designer text, not counted. |

**Banned claims (case-insensitive sweep of page copy):**
- `certified Epicor`, `Epicor partner` (as HLB HAMT's status), `Epicor implementation`, `Platinum`, `Gold`, any partner tier: **0**.
  - "Certified" appears once, in tile 2 "Certified SugarAI partner" (240). That is SugarAI, which is allowed.
  - Every "implement..." hit is CRM-side: item 02 H4 "SugarAI CRM implementation" (210), tile 2 "Implementation, customisation and integration of SugarAI" (241) and the Block 10 lede "new CRM implementation" (257).
- `real-time`, `real time`, `realtime`, `pre-built`, `prebuilt`, `no-code`, `no code`, `zero code`, `out of the box`, `plug and play`, `live in hours`: **0**.
- "automatically" appears once, in Block 4 step 3 (117). It describes workflow behaviour (SugarAI updates the quote), not an integration-method claim, and it is the brief's own step text.

**Advisory (Content Writer, not scored):** Block 9 tile 3 says "An ERP practice and a CRM practice in one firm, answering integration questions from both sides" (244). This is the brief's own wording and it does not say Epicor. Brief OQ1 noted, however, that HLB HAMT's ERP practice appears to be SAP Business One and Sage. If the Content Writer wants zero chance of a reader inferring Epicor expertise, "...answering integration questions on the CRM and ERP sides" keeps the meaning without implying Epicor depth. It is word-neutral.

## 0c. Layout check. PASS

Each block's actual format was checked against brief 3b/4.

| Block | Brief format | Draft format (line) | Match |
|---|---|---|---|
| 1 Hero | Template pattern exactly | Eyebrow, H1, lede, 2 buttons, side panel H3 + sub-line + 3 rows (19-44) | Yes |
| 2 Stats band | 3 stats, dark band | 3 × `.n/.l/.d` with [1] [1] [2] (46-69) | Yes |
| 3 How it works | PROSE (3 paras) + IMG-1 + TABLE | 3 paras (79-83), IMG-1 (85-90), 7-row `table.datamap` (92-102) | Yes. All 7 rows and every Direction cell are exact. Third column tightened, which is allowed. |
| 4 Workflow | PROSE lede + numbered list beside IMG-2 | Lede (112), `ol` of 6 (115-120), IMG-2 right column (122-127) | Yes |
| 5 Benefits | PROSE beside IMG-3, then 6 CARDS | Prose (137), IMG-3 (139-144), 6 × `.card` in `.grid-3` (146-162) | Yes |
| 6 Mid CTA | Template band | H2, body, 1 button (164-174) | Yes |
| 7 Where teams work | IMG-4 left + PROSE (2 paras) | IMG-4 (184-189), 2 paras (191-193) | Yes |
| 8 Services | Numbered list, 6 items, 2 × 3 | `.svc-cols` 01-06 (195-225) | Yes |
| 9 Why HLB HAMT | PROSE paragraph + 4 credential tiles | Paragraph (235), 4 × `.card` in `.grid-4` (237-247) | Yes |
| 10 Process | Timeline (6) + PROSE callout | 6 steps (259-275), `.proc-note` (277-278) | Yes |
| 11 FAQ | 5 Q&As, first open | 5 `details.faq` (288-301) | Yes |
| 12 Closing CTA | Template pattern | H2, button, `.cta-card` H4 + 3 rows (313-326) | Yes |

- **Image slots: all 4 are present in brief order.** Each has a placeholder label, an aspect ratio with its minimum size, a full designer description, a counted caption and alt text. IMG-3 and IMG-4 captions open "Illustrative:" (Section 10 point 4), and their descriptions say "designer mock-up (no demo instance exists yet)". IMG-3 uses the fictional "Gulf Fasteners Trading LLC", and IMG-4 reuses it. The IMG-4 caption avoids "Outlook", as required.
- **A correction to the framing I was given.** Build's Block 5 note calls it "the page's one card grid", which is true for the 6-card `.grid-3`. The brief's own format tally (3b), however, counts **two** card-style blocks: Block 5 (benefits) and Block 9 (4 credential tiles as `.card` in `.grid-4`). The draft has exactly those two, as the brief intends.
- **The page is not an all-card layout.** Prose leads Blocks 3, 4, 5 (first half), 7, 9 (paragraph) and the Block 10 callout. List and table formats carry Blocks 3, 4, 8 and 10.

---

## 1. Keyword placement and density: PASS

Count rule (brief 2): exact phrase, case-insensitive, on-page copy only (lines 19-327, Sources excluded). Meta is placed but not counted.

| Keyword | Count | Placements (line) | Required | Result |
|---|---|---|---|---|
| CRM integration with Epicor ERP | **4** | H1 (25); Block 3 H2 (77); Block 5 prose s1 (137); FAQ A2 s1 (292) | Exactly 4, in those slots | Pass |
| SugarAI with Epicor ERP | **2** | Hero lede s1 (27); FAQ Q1 (288) | Exactly 2 | Pass |
| CRM integration services | **2** | Block 8 H2 (201); FAQ A5 (301) | Exactly 2 | Pass |
| CRM integration partner | **1** | Block 9 H2 (233) | Exactly 1 | Pass |
| CRM implementation | **2** | Block 8 item 02 H4 (210); Block 10 lede (257) | Exactly 2 | Pass |

- **Placement:**
  - Meta title (1) and meta description (2) both lead with the primary and match brief Section 7 exactly.
  - The H1 covers the first 100 words, and the primary is not repeated in the hero lede, as the brief requires.
  - Meta keywords (5) are in the right order.
- **Stuffing:**
  - Total **11** (cap 12), about 0.67% of 1,642 words.
  - Keywords sit in the H1, exactly 4 subheadings (Block 3 H2, Block 8 H2, Block 8 item 02 H4, Block 9 H2) and FAQ Q1. No other heading has one.
  - No sentence holds two different keywords.
  - There are no accidental extra matches. "connect SugarAI with Epicor ERP" occurs only in the hero, and every other passage uses "SugarAI and Epicor".
- **"Outlook"** appears 1× and **"iOS and Android"** 1× in counted copy (191).

## 2. Word count: PASS (1,642)

I counted token by token by the brief Section 1 rule. Excluded: eyebrows, buttons, nav, breadcrumb, footer, meta, Sources, placeholder labels, alt text, designer descriptions, footnote markers and the three `.n` figures.

| Block | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Words | 134 | 87 | 256 | 125 | 234 | 23 | 123 | 137 | 141 | 131 | 204 | 47 | **1,642** |
| Budget | 120-135 | 85-100 | 240-275 | 120-140 | 225-250 | 20-26 | 117-132 | 140-160 | 130-150 | 115-135 | 204-254 | 46-52 | 1,500-1,700 |

- **The total matches Build's 1,642 exactly** (1,645 with the three figures), against 1,500-1,700.
- **Sub-budgets:**
  - The hero lede is 55, at the cap.
  - Stat `.d` lengths are 16 / 16 / 17.
  - Block 3 paragraphs are 58 / 62 / 28, and the table is 89.
  - Workflow steps run 13-16 words.
  - Block 5 prose is 67, and the cards are 19 / 19 / 19 / 19 / 19 / 18.
  - Block 9 paragraph 53; tiles 14 / 15 / 16 / 15.
  - Process steps run 8-10; callout 32.
  - FAQ answers are 31 / 30 / 30 / 30 / 31.
  - Closing rows are 12 / 11 / 11.
- **Observation, not scored:**
  - Block 8 is 137, 3 under its 140 floor. Items 03-06 are 14-15 words against the brief's 16-19. The brief's trim order allows Block 8 bodies "to about 15 words", and the page total is in range.
  - Block 7 paragraph 1 is 52 against 55-60, but the block total is inside its budget.
  - The fixes below happen to bring Block 8 to 140.

## 3. Zero em dashes: PASS

A whole-file ripgrep finds `—` (U+2014) **0**, `–` (U+2013) **0** and `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- **British spelling sweep:** -ize/-yze/-ization, color, center, program, license, modeled, favor, behavior, catalog, percent. Page copy returns **0**.
  - Hits outside the page: "customization" (333) is the Nucleus source quote inside the Stats-used table, and "Mid-sized" is a false positive.
  - The page uses synchronisation, customisation, prioritise, programme, organisations and modelled.
- **No errors found.** Sentence fragments in the side rows, process steps and FAQ A5 follow the template's house style.
- **Advisories (not scored):**
  - **G1. Block 3 P2 s3 (81):** in "Both use Epicor's REST services and saved queries (BAQs)", the antecedent of "Both" is two sentences back. "Both mechanisms use..." is clearer (+1).
  - **G2. Stat 3 `.d` (69):** "are this much likelier" is awkward. Fix 6a below rewrites this line anyway.
  - **G3. Card 6 (162):** "SugarAI's AI" double-taps "AI". "SugarAI's scoring and summaries draw on..." (+1) reads better.

## 5. Originality: FAIL

### 5.1 TCP deck (the extracted file, all 20 slides): clean

Every slide heading and line was compared with the page:
- **"Perfectly Integrated, Out of the Box", "What Separates SugarCRM for Kinetic", "Live views into any Epicor data", "Lead to Order Workflow: CRM & ERP Working Together", "Work where you are", "Why Epicor + SugarCRM Excels", "Purpose-Built for Epicor":** no reuse. The closest is Block 7 H2 "Epicor data wherever your teams work" against "Work where you are". They share a concept, not wording. That H2 is brief-prescribed "use as written" (see advisory T1).
- **Slide 9 stage names** ("Quoting", "Quote Ready", "New Draft Quote", "New Draft Sales Quote", "Opportunity Complete"): absent. Block 4 step 1 dropped the brief's "moves to quoting" for "advancing the opportunity", which is good. "Won" (step 4) is standard CRM vocabulary.
- **Slide 17 value list:** the cards share generic ideas only (one record, segmenting on order history, AI on fuller history), which brief Section 4 permits. No heading or line is reused.

### 5.2 The five reference sites (fetched today where possible)

| Site | Access today | Finding |
|---|---|---|
| tcpamericas.com Sugar-Epicor page | Fetched | No match. Its headings ("Sugar Sells. Kinetic Delivers. Fluently.", "Built for sellers. Trusted by operations.", "Live in hours, not weeks.", "Key records stay in sync, automatically.") and its "two selling days" line are absent. Card 3 "Orders without re-keying" against TCP's "Quote-to-order workflows without re-entry" is a generic concept with different wording. |
| fluenterp.com Epicor-SugarCRM | Fetched | No sentence match. Two near-concepts are noted below. |
| linkedin.com SugarAI article (3 Apr 2025) | Fetched | No match. Its headings ("Automate Admin Work and Focus on Selling", "The Tech Behind the Scenes", "Ready to See It in Action?") and its "pre-built connectors" / "out-of-the-box" claims are absent. "See SugarAI in Action" is the series-standard button label, which is not counted copy. |
| codelessplatforms.com | 403 again | Covered by brief-time search text. The page shares only the standard record list (accounts, contacts, price lists, quotes, orders, invoices), which is generic. |
| marketplace.sugarai.com TCP listing | Empty page again | Same product as the TCP page, which was checked above. |

fluenterp near-concepts, ruled acceptable:
- (a) "synced on a schedule you set" against Block 3 P2 "on a schedule you agree". This is the brief's own allowed wording ("on a schedule agreed with you"). It is a generic 4-word collocation, and the surrounding sentence differs.
- (b) Its FAQ "How quickly are changes reflected across systems?" against our FAQ Q3 "How quickly do changes appear in the other system?". This is the brief-prescribed question, and it is the natural way a buyer asks. The answers are entirely different. See optional T2 if more distance is wanted.

### 5.3 Wider web: exact-phrase searches, no matches

| Phrase searched | Result |
|---|---|
| "two accurate systems into one working view" | No match |
| "replaces nothing on the Epicor side" | No match (epiusers threads on unrelated topics) |
| "live views show current Epicor data" / "synchronised records update on change" | No match (generic iPaaS listing pages) |
| "How quickly do changes appear in the other system" | No match (generic sync-latency blogs) |

### 5.4 HLB HAMT's own Insurance template and live hub: FAIL

Brief Section 5 says the originality check "must cover ... the Insurance template". Brief Section 4 says hub facts are to be used "rewritten, not copied". Block 10 says "Write new descriptions ... specific to integration".

The FSM page in this project set the precedent (FSM test-report-v1, item 5, O1-O9). It failed sentences that keep a template sentence's skeleton with swapped nouns, **even where the brief's outline echoed the template**. Most lines below came straight from this brief's outline, but the rule still applies. One of them is word-for-word.

| # | Draft location (line) | Source | Source text | Draft text |
|---|---|---|---|---|
| O1 | Hero lede s2 (27) | Insurance hero lede s2 | "HLB HAMT implements SugarAI for insurers, brokers and agencies **across the UAE and GCC, cloud or on-premise**." | "...and we design, build and support a custom connection for manufacturers and distributors **across the UAE and GCC, cloud or on-premise**." The same "[we] [verb] ... for [audience] across the UAE and GCC, cloud or on-premise" skeleton and tail. FSM O7 failed this exact pattern. |
| O2 | Block 3 P1 s3 (79) | Insurance FAQ 2 answer | "Policy administration stays the system of record; **SugarAI is where sales, service and** claims **teams** work" | "**SugarAI is where sales, service and** marketing **teams** manage accounts, ..." That is a 7-word run with one noun swapped. |
| O3 | Block 10 step 1 (260) | Insurance process step 1 | "**We map how a quote becomes** a policy, claim and renewal **today**." | "**We trace how quotes become** orders and invoices **today**." Same skeleton, with synonyms swapped in. FSM O6 failed this pattern. |
| O4 | Block 10 step 4 (269) and Block 8 item 04 (219) | Insurance process step 4 | "Policyholder and claims data **cleansed, mapped and rehearsed** before load." | Step 4: "Customer records **matched, cleaned and rehearsed** at least twice." Item 04: "...customer records **matched, cleaned and loaded in full rehearsals before cutover**." Same participle-triple skeleton, matching FSM O5. The page also repeats "matched, cleaned" in two places. |
| O5 | Block 10 step 6 (275) | Insurance process step 6 | "Phased go-live with hypercare, then managed support under SLA." | "**Phased go-live with hypercare, then managed support under SLA.**" **Verbatim.** It is the brief's own step 6 text, but the brief also says "Write new descriptions". FSM O4 failed even a reworded version of it. |
| O6 | Block 10 callout (278) | Live hub FAQ "How long does implementation take" | "A sales-focused rollout for one company usually goes live in six to ten weeks. A larger programme ... with ERP integration and data migration typically runs 2.5 to 5 months, delivered in phases so your first users are working long before the last." | "**A sales-focused** SugarAI **rollout usually goes live in six to ten weeks.** With Epicor **integration and data migration**, expect 2.5 to 5 months, **phased so first users start well before the end**." Sentence 1 is 10 of 12 words in sequence. Sentence 2 is lightly reworded. This puts duplicate copy on the same site and breaks "rewritten, not copied". |
| O7 | Block 9 tile 4 (247) | Insurance "Support that continues" card **and** live hub support FAQ | Insurance: "A dedicated team on **agreed service levels**, with **a named manager and a clear escalation path**." Hub: "a single service desk with agreed response and resolution times, **a named service manager and a defined escalation path**." | "One service desk, **agreed service levels, a named service manager and a clear escalation path**." This blends both sources nearly verbatim. FSM O1 failed the Insurance half. |
| O8 | Closing row 1 (324) | Insurance closing row 1 | "**A discovery call on your** product lines, channels **and current systems**." | "**A discovery call covering your** Epicor setup, sales process **and current CRM**." Same skeleton (FSM O8). |
| O9 | Closing row 3 (326) | Insurance closing row 3 | "**A written proposal covering scope, timeline and investment**." | "**A written proposal with the** data map, phases, **timeline and investment**." Same skeleton (FSM O9). |

**Borderline, not required to fix** (recorded so they are not reopened):
- **Block 10 step 2 (263).** "Data map, sync and conflict rules agreed in writing." The FSM sibling step 2 ends "...assignment rules agreed in writing." They share the 4-word tail, which is a methodology phrase, and the content differs. Optional T3 offers a variant.
- **Block 10 lede (257).** "signed off at each stage" against the Insurance "with sign-off at every stage". This is a methodology concept that the brief prescribes, and the sentence differs.
- **"Epicor stays the system of record" (hero, 27).** Compare Insurance "Policy administration stays the system of record". "System of record" is the industry term, and the subject is this page's subject.
- **Side-panel sub-line (35).** "Set up for ... across the UAE and GCC." against the Insurance "Configured for ... across the UAE and GCC." This is a template structural slot ("mirror the hero exactly") with brief-prescribed wording.
- **FAQ A4 (298) against FSM A7.** The FSM reads "SugarCRM became SugarAI in April 2026, and existing instances keep running." Here the rebrand is the subject ("The April 2026 rebrand ... left existing instances running as they were"). The brief allows this "as a fact only, in new wording". Acceptable.
- **Item 02 (211).** "configure SugarAI around how you sell and serve" against the Insurance "Configuration built around your quote-to-bind process". A common collocation.

## 6. Stat accuracy and footnoting: FAIL (1 item)

Every source was re-checked today (2026-10-07).

| ID | Draft (line) | Source check today | Credible / recent | Verdict |
|---|---|---|---|---|
| N1 | `7%` "Higher win rates" / "The win-rate improvement Nucleus Research found among Sugar customers who brought CRM and ERP data together. [1]" (57-59) | Nucleus Z56, fetched: "seven percent improvement in win rates", 8 April 2025 | Analyst ROI case study, about 18 months old. It is vendor-hosted and the sample size is undisclosed, so "Analyst research" (not "independent") is the right framing (54). | **Pass** |
| N2 | `~50%` "Shorter customisation timelines" (61-64) | Same page: "approximate 50 percent reduction in customization timelines" | Same | **Pass** |
| A1 | `2.3×` "Customer satisfaction gains" / "Mid-sized enterprises that prioritise interoperability are this much likelier to see measurable customer satisfaction improvements, Avasant found. [2]" (66-69) | Avasant, fetched: "**mid-sized enterprises that prioritize interoperability and eliminate data silos** are 2.3x more likely to achieve measurable improvements in customer satisfaction and operational responsiveness". Acklin and Frederick, Sept 2025, Cloud CRM Suites 2024 RadarView data. | Independent advisory firm; data about 2 years old, within the window | **FAIL: the cohort qualifier is incomplete.** The source's group must meet two conditions (prioritise interoperability **and** eliminate data silos). The draft states only the first, which widens the population the 2.3× applies to. Brief 6a says to keep the cohort qualifier. See Fix 6a. |
| A2 | "according to Avasant, more than 60% of enterprises still operate with fragmented data environments. [2]" (137) | Same article: "over 60% of enterprises still operate with fragmented data environments" | Same | **Pass**. The framing is constructive, as the brief requires. |
| U1 | "UAE industrial exports passed AED 262 billion in 2025. [4]" (235) | Khaleej Times, fetched: headline "UAE industrial exports hit Dh262b as sector's GDP contribution climbs by 70%", 10 June 2026. "industrial exports surpassing Dh262 billion in 2025", per Hassan Al Nowais, MoIAT. | Government figure, about 4 months old | **Pass**. The Sources [4] title matches the headline. The lead-in "growing fast" is supported by the same article's 70% GDP-contribution rise. |
| F1 | "Nucleus Research named Sugar a Leader in its 2026 Sales Force Automation Technology Value Matrix, Sugar's sixth straight year as a Nucleus Leader, and listed ERP-informed insight among its strengths. [3]" (193) | 01net reprint, fetched (25 Feb 2026): "named a Leader in the Nucleus Research Sales Force Automation (SFA) Technology Value Matrix 2026"; "sixth consecutive year that Sugar has been recognized as a Leader in Nucleus Research's technology value matrix assessments". The analyst quote positions Sugar Sell for "context-driven selling, **ERP-informed insights**, and AI embedded directly into sales workflows". | Analyst recognition, 7 months old | **Pass**. "ERP-informed insight" is Nucleus's own term. The release ties it to the sales-i add-on, which correctly goes unnamed (Section 10 point 6), and the draft does not claim the integration delivers it. |
| F2 | FAQ A4: "The April 2026 rebrand from SugarCRM to SugarAI..." (298) | Search today: the SugarAI press release URL in Sources [5] is indexed, dated 13 April 2026 (also destinationCRM, itwire and 01net). | Primary source | **Pass** |
| F3 | Sugar Connect: "look up, create and update SugarAI records from their inbox, sync contacts and calendars, and file emails to the right account" (191) | support.sugarai.com Sugar Connect guide (search extract): "sync your Sugar and Outlook contacts and calendars, create new Sugar records ... archive incoming and outgoing email" | Vendor docs | **Pass** |
| F4 / F5 / F6 | Mobile app on iOS and Android; REST + BAQs; hub facts | Search-verified at brief stage. The hub text was re-read today: 6-10 weeks, 2.5-5 months, two rehearsals, named service manager and post-release retesting all appear (lines 1365-1418). | | **Pass** (but see O6/O7 for wording) |

- **Footnotes:** markers [1] [1] [2] in Block 2, [2] in Block 5, [3] in Block 7 and [4] in Block 9 run in order of appearance. FAQ answers carry no markers. Sources lists [1]-[5], with [5] backing FAQ 4.
- **No duplication across the project.** A project-wide ripgrep for "2.3×/2.3x", "262 billion/Dh262", "more than 60%/over 60%", "win-rate improvement", "customisation timelines" and "Value Matrix" finds draft use only here.
  - Power BI's "up more than 60%" is a different Microsoft Fabric figure.
  - "Value Matrix" also appears on the live hub as a badge, which is consistent and is not a recycled stat.
  - The FSM page's Nucleus 8% figure is not used.
- **No invented figures.** No TCP/fluent figures (2,847 runs, 99.2%), no aggregator stats and no pricing appear.
- **Business Wire originals ([3] main URL) were not fetched** (403 for Plan). The reprint confirms the content. A human click-check is still needed (Build Flag 13).

## 7. Human tone / AI-detection heuristics: PASS

- **Stock-phrase sweep:** unlock, seamless, fast-paced, revolution, unleash, in conclusion, game-chang, cutting-edge, leverage, empower, robust, streamline, holistic, elevate, harness, delve, landscape, synerg, transformative, journey, world-class and best-in-class all return **0**.
- **Openers vary.**
  - Block 3: HLB HAMT builds / Epicor remains / SugarAI is / Synchronised records / Live views / Both / Which records / The table.
  - Cards: Sales / Quotes draw / Accepted quotes / Shipments / Sugar Market / Managers.
  - Services bodies: Workshops / Our / Two-way / Existing / End-to-end / Support.
  - Nothing runs more than 2 in a row.
- **The copy is specific to the subject** (BAQs, matching rules, quote-to-order hand-offs, free zone entities). No section reads as templated filler.
- **Advisories (not scored):**
  - **T1. Block 7 H2 (182)** "Epicor data wherever your teams work" sits conceptually close to TCP's "Work where you are" and the slide 17 line "work seamlessly where you already are". It is brief-prescribed "use as written", so Build should not change it unprompted. A more concrete option for the Content Writer is "Epicor data in the inbox and on the road" (+2).
  - **T4. ", so [result]" endings** close 3 of the 6 cards (2, 4, 5), plus the hero, the IMG-2 caption and the callout. Varying one card helps. For card 4 (156), "Shipments, invoices and past cases appear as an agent opens a query, which makes replies quicker and more accurate." (+1).

## 8. Section structure: PASS

- **12 blocks in brief order, each in the correct format** (see 0c).
- **H1 and H2s are "use as written" where specified.** Eyebrows match 3b exactly. The sticky nav labels and anchors match.
- **Breadcrumb and parent:** "CRM Solutions (SugarAI)" links to `https://hlbhamt.com/sugarai-crm-2/` (15), **not** sugarai.com (Section 10 point 3). The footer hub link is the same (17). The suggested slug `/sugarai-crm/integrations/epicor-erp/` is noted for Deliver.
- **FAQ:** 5 Q&As, first open. Q1-Q5 match the brief's questions, and Q1 is word for word. Answers are 30-31 words with the direct answer first and no inline markers. The JSON-LD instruction (5 visible Q&As only, word for word) is carried.
- **Sources note:** one note, after the FAQ and before the closing CTA (303-311).
- **Internal links:**
  - L1 "SugarAI CRM services" goes to the hub (211), on the body opener and not the H4.
  - L2 "manufacturers and distributors" goes to /industries/manufacture-and-distribution/ (35).
  - L3 "ERP practice" goes to /services/erp-integration-add-ons/ (244).
  - L4 is omitted. That is correct: see departure 4.
- **CTAs:**
  - Hero: Request a demo and Talk to our integration team.
  - Mid band: See SugarAI in Action.
  - Closing: Talk to our integration team, linking to /contact/.
  - There is no free-trial or trial-instance offer of any kind.

## 9. Client requirements and transcript: PASS

- **No transcript** was supplied (requirement notes). Nothing is attributed to one.
- **Section 10:**
  - Point 1: positioning passes (0b).
  - Point 2: the connection is described as custom ("custom connection", "custom integration"), and no resold or named connector appears.
  - Point 3: hub parent.
  - Point 4: "Illustrative" captions and mock-up designer notes. The demo wording does not promise a live demo on the client's own Epicor data (172, 325).
  - Point 5: Kinetic is named; Prophet 21, Eclipse and BisTrack are absent.
  - Point 6: N1, N2 and A1 are used, the FSM 8% is not reused, and sales-i is unnamed.
- **Requirement-notes caveat items** (Fluent, trial, testimonials, TCP counts) are all absent (0a). The "two sales days" figure is not used in any form.
- **No fabricated commitments:**
  - No pricing appears. "Investment" (closing row 3) carries no figure.
  - The timelines are the hub's own figures.
  - No customer names or testimonials appear.

### Build's 7 self-reported departures: rulings

| # | Departure | Ruling |
|---|---|---|
| 1 | Stat 2 label "Shorter customisation timelines" instead of the Block 2 "Faster customisation" | **Brief-compliant, not a departure.** Brief 6a (N2) says: "The label must say 'customisation timelines', not 'integration time' or 'implementation time'". Section 10 point 6 says "~50% shorter customisation timelines". "Shorter" is also more faithful to "reduction in customization timelines" than "Faster". Accept. |
| 2 | Stat 1 drops "average" | **Correct.** The Nucleus page today says "seven percent improvement in win rates" with no "average". "Average" is attached only to the 8% recurring-revenue figure. The brief's Block 2 wording was the error. Accept. |
| 3 | No "Epicor ERP 10" on page; FAQ A1 says "older Epicor ERP versions" | **Brief-compliant; the Content Writer may choose to tighten it.** The caller is right that Section 10 point 5 confirms scope and does not ban the words. The brief's own FAQ 1 answer, however, prescribes "Older Epicor ERP versions are assessed during discovery". The guardrail bans "specific Epicor version numbers", and F5 shows its intent: technical versions like "10.2.500+". "Epicor ERP 10" is a product name, so naming it would be permissible but not required. Not a defect. Optional T5: "...and Epicor ERP 10 estates are assessed in discovery" (+1). That is more precise about the confirmed scope and avoids implying Epicor 9/Vantage support. |
| 4 | Internal link 4 omitted | **Correct per brief Section 8.** The link is "conditional ... Include only if Deliver confirms the URL resolves; otherwise omit with no replacement". My WebFetch of hlbhamt.com/sugarai-crm/industries/manufacturing/ returned an empty page, which is inconclusive (the hub fetch also came back empty, so the site may block the fetcher). The template's `/sugarai-crm/...` footer paths do not match the live hub slug `/sugarai-crm-2/`, which is a reason for caution. Deliver to decide; Build's ready-made card 6 variant is in Flag 8. |
| 5 | Demo wording avoids promising the client's own live Epicor data | **Correct** (Section 10 point 4). The mid CTA (172) uses the conditional "would look", and closing row 2 (325) says "modelled on yours". The closing H2 "See your own Epicor quotes and orders working inside SugarAI." is brief "use as written" and reads as the project outcome, not a demo promise. Acceptable. |
| 6 | Nucleus award says "Sugar" | **Correct.** The 25 Feb 2026 release predates the 13 April 2026 rebrand and itself says "Sugar has been recognized". Brief F1 also says "Sugar". |
| 7 | URLs need a human click-check | **Handoff note, not a defect.** I verified Nucleus, Avasant, Khaleej Times and the 01net reprint by fetch today, and the SugarAI rebrand release and Sugar Connect docs by search. Still unverified by fetch: Business Wire [3] main URL, support.sugarai.com mobile guide, the knowledgelib.io REST explainer, and both hlbhamt.com link targets. |

---

## Overall: FAIL (loop 1 of 3)

- **Critical checks are clean.** TCP material in page copy is 0, and Build's self-search is confirmed. Positioning is correct and foregrounded in the hero and Block 3. There are no Epicor certification, tier or implementation claims and no real-time, pre-built, no-code or out-of-the-box claims. The prose-led layout matches the brief block for block.
- **Item 5 fails** on 9 lines (O1-O9) that reuse or lightly reword HLB HAMT's own Insurance template or live hub. One of them, Block 10 step 6, is verbatim. This is the same class of finding FSM loop 1 failed.
- **Item 6 fails** on 1 line: the A1 cohort qualifier is incomplete.
- Everything else passes.
- The fixes below total **+13 words, taking the count to 1,655**. Every affected block stays inside its budget (Block 10 reaches 135, its cap). No keyword counts change.

## Fix instructions

Apply exactly. Do not change any other line. Keep zero em/en dashes, British spelling and every keyword count. Update the "Stats used" A1 row (334) to the new wording.

**5-O1. Block 1 hero lede, sentence 2 (line 27). 27 → 27 words; lede stays 55.**
- Replace: "Epicor stays the system of record, and we design, build and support a custom connection for manufacturers and distributors across the UAE and GCC, cloud or on-premise."
- With: "Epicor stays the system of record, while we design, build and support a custom connection for UAE and GCC manufacturers and distributors on cloud or on-premise Epicor."
- (This drops the Insurance tail and keeps the "your Epicor" framing.)

**5-O2. Block 3 paragraph 1, sentence 3 (line 79). 22 → 21; P1 becomes 57.**
- Replace: "SugarAI is where sales, service and marketing teams manage accounts, opportunities, quotes, cases and campaigns, with each customer created once and shared."
- With: "Sales, service and marketing staff handle accounts, opportunities, quotes, cases and campaigns in SugarAI, with each customer created once and shared."
- Leave sentence 1 ("HLB HAMT builds a custom integration into the Epicor ERP you already run...") untouched.

**5-O3. Block 10 step 1, Discovery (line 260). 9 → 10.**
- Replace: "We trace how quotes become orders and invoices today."
- With: "Today's quote, order and invoice steps mapped with your teams."
- Do not use "Workshops..." as the opener (FSM step 1).

**5-O4a. Block 10 step 4, Data migration (line 269). 9 → 9.**
- Replace: "Customer records matched, cleaned and rehearsed at least twice."
- With: "Duplicate accounts resolved; the migration rehearsed at least twice."

**5-O4b. Block 8 item 04 body (line 219). 15 → 18; Block 8 becomes 140.**
- Replace: "Existing CRM and Epicor customer records matched, cleaned and loaded in full rehearsals before cutover."
- With: "Customer records from your current CRM and Epicor reconciled, with every load proven in a test environment first."
- Do not reintroduce "trial-load", "before cutover" or "removing duplicates" (FSM step 4).

**5-O5. Block 10 step 6, Go-live and support (line 275). 9 → 10.**
- Replace: "Phased go-live with hypercare, then managed support under SLA."
- With: "Teams go live in waves, with hypercare before SLA-backed support."
- Do not use "Hypercare covers each launch phase..." (FSM step 6).

**5-O6. Block 10 callout body (line 278). 32 → 34 (range 28-34).**
- Replace: "A sales-focused SugarAI rollout usually goes live in six to ten weeks. With Epicor integration and data migration, expect 2.5 to 5 months, phased so first users start well before the end."
- With: "A SugarAI rollout for sales alone typically takes six to ten weeks. Adding the Epicor connection and data migration usually extends it to 2.5 to 5 months, released in stages so teams start early."
- Keep the H4 "Realistic timelines, delivered in phases" as written.

**5-O7. Block 9 tile 4 body (line 247). 15 → 16.**
- Replace: "One service desk, agreed service levels, a named service manager and a clear escalation path."
- With: "One desk takes requests, a named manager owns your account, and escalations follow a set route."

**5-O8. Block 12 "What happens next" row 1 (line 324). 12 → 13.**
- Replace: "A discovery call covering your Epicor setup, sales process and current CRM."
- With: "We start by learning how your Epicor, CRM and sales process fit together."
- Do not use "First, we talk through..." (FSM row 1).

**5-O9. Block 12 row 3 (line 326). 11 → 13.**
- Replace: "A written proposal with the data map, phases, timeline and investment."
- With: "Then a proposal that costs the draft data map and plans each phase."
- Do not use "setting out ... timeline and cost" or "in writing for your sign-off" (FSM).

**6a. Block 2 stat 3 `.d` (line 69). 17 → 20 (range 16-20).**
- Replace: "Mid-sized enterprises that prioritise interoperability are this much likelier to see measurable customer satisfaction improvements, Avasant found."
- With: "How much likelier mid-sized enterprises that prioritise interoperability and eliminate data silos are to see measurable satisfaction gains, Avasant found."
- Keep `.n` "2.3×", `.l` "Customer satisfaction gains" and marker [2]. Update the A1 row in "Stats used".

**Word ledger after fixes:** Block 1 134, Block 2 90, Block 3 255, Block 8 140, Block 9 142, Block 10 135, Block 12 50. **Total 1,655** (range 1,500-1,700).

### Optional (Content Writer or Build discretion; not needed to pass)
- **G1.** Block 3 P2 (81): "Both use" becomes "Both mechanisms use" (+1).
- **G3.** Card 6 (162): "SugarAI's AI draws on" becomes "SugarAI's scoring and summaries draw on" (+1).
- **T1.** Block 7 H2 (182): "Epicor data in the inbox and on the road" (+2). This needs Content Writer approval, because the H2 is "use as written".
- **T2.** FAQ Q3 (294): "How current is the Epicor data SugarAI shows?" (-1). This puts more distance from fluenterp's FAQ, and A3 still answers it.
- **T3.** Block 10 step 2 (263): "Data map, sync logic and conflict ownership signed off before build." (+2). This only fits if the budget allows: Block 10 would exceed 135, so trim elsewhere.
- **T4.** Card 4 (156): ", so replies are quicker" becomes ", which makes replies quicker" (+1).
- **T5.** FAQ A1 (289): "older Epicor ERP versions" becomes "Epicor ERP 10 estates" (+1). This is a Content Writer decision.
- **Tile 3 (244):** "answering integration questions from both sides" becomes "answering integration questions on the CRM and ERP sides" (+2). This reduces any inference of Epicor expertise.

---

Sources consulted today:
- [Nucleus Research Z56, How unifying CRM and ERP with Sugar drives sales performance](https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/): 7% win rates (no "average"), ~50% customisation timelines, 8 April 2025.
- [Avasant, Breaking Down Data Silos](https://avasant.com/report/breaking-down-data-silos-why-crm-integration-is-now-a-boardroom-priority/): 2.3x (mid-sized, interoperability **and** eliminate data silos); over 60% fragmented; Sept 2025.
- [Khaleej Times, 10 June 2026](https://www.khaleejtimes.com/business/uae-industrial-exports-hit-dh262b-as-sectors-gdp-contribution-climbs-by-70): Dh262 billion in 2025.
- [01net reprint of the Nucleus SFA Value Matrix 2026 release](https://www.01net.it/sugarcrm-named-a-leader-in-the-nucleus-research-sales-force-automation-technology-value-matrix-2026/): Leader, sixth consecutive year, "ERP-informed insights".
- [SugarAI rebrand press release](https://sugarai.com/press-releases/sugarcrm-unveils-new-brand-identity-as-sugarai-declaring-the-next-generation-of-crm) and [destinationCRM](https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/SugarCRM-Unveils-New-Brand-Identity-as-SugarAI-174328.aspx): 13 April 2026.
- [Sugar Connect user guide](https://support.sugarai.com/documentation/plug-ins/sugar_connect/sugar_connect_user_guide/) (search extract).
- Reference sites:
  - [TCP Sugar-Epicor page](https://www.tcpamericas.com/en/pages/sugar-epicor-integration) (fetched)
  - [fluenterp Epicor-SugarCRM](https://www.fluenterp.com/en/integrations/epicor-sugarcrm) (fetched)
  - [SugarAI LinkedIn article](https://www.linkedin.com/pulse/boost-sales-service-epicor-erp-sugarcrm-sugarcrm-42lqf/) (fetched)
  - [Codeless Platforms](https://www.codelessplatforms.com/solutions/epicor-sugarcrm-integration/) (403)
  - [SugarAI marketplace listing](https://marketplace.sugarai.com/addons/epicorsugar-crm-integration-by-tcp) (empty)
