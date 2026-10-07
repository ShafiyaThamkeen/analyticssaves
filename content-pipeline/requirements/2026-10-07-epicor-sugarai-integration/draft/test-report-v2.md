# Test report v2: SugarAI CRM + Epicor ERP Integration subpage (draft-v2.md, loop 2 of 3)

Tested by: Test agent, 2026-10-07
Loop: **2 of 3** (`test-report-v1.md` exists; one more Build→Test loop is available after this one).
Inputs: `brief.md` (Section 10 overrides where noted), `draft/draft-v2.md`, `draft/draft-v1.md` (for the diff), `draft/test-report-v1.md`, `inputs/requirement-notes.md`, `inputs/extracted/tcp-sugarcrm-epicor-kinetic-webinar-slides.pdf.md`, `inputs/structural-sample/hlbhamt-sugarai-insurance.html` and its `.pdf.md` extraction, the saved live hub text (`../2026-09-29-data-visualization-services-homepage/inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`), and the published FSM sibling (`../2026-09-23-sugarai-field-service-management-subpage/output/sugarai-field-service-management.html`, matching its `draft-v5.md`).

Page copy = draft lines 19-327 (Blocks 1-12 and the Sources note). Lines 1-17 are meta and chrome. Lines 328-370 are Build's "Stats used" and "Flags", which are internal and must never ship.

---

## Summary

| # | Item | Result |
|---|---|---|
| L1 | **All 11 loop-1 fixes applied as specified** | **PASS** (11/11 verbatim; no other page line changed) |
| 0a | **Critical: TCP-deck exclusions** | **PASS** (0 hits in page copy, captions, alt text, designer descriptions or meta) |
| 0b | **Critical: positioning ("SugarAI integrates with your existing Epicor")** | **PASS** (unchanged; hero s2 now ties the deployment to the client's own Epicor) |
| 0c | **Layout: prose-led, 2 card blocks** | **PASS** (unchanged) |
| 1 | Keyword placement and density | **PASS** (4 / 2 / 2 / 1 / 2; total 11, cap 12) |
| 2 | Word count | **PASS** (1,655) |
| 3 | Zero em dashes | **PASS** (0 em, 0 en, 0 `--`) |
| 4 | Grammar, spelling (British), punctuation | **PASS** (advisories only) |
| 5 | Originality | **FAIL** (2 lines). The TCP deck, the 5 reference sites, the wider web and the published FSM page are clean. Two of the replacement lines that **test-report-v1 itself prescribed** (O5 step 6 and the O6 callout) still follow the skeleton of the Insurance template and the live hub. |
| 6 | Stat accuracy and footnoting | **PASS** (A1 qualifier fixed and re-verified against Avasant today; the other 4 stats and F1 re-fetched and unchanged) |
| 7 | Human tone / AI-detection heuristics | **PASS** (advisories only) |
| 8 | Section structure | **PASS** |
| 9 | Client requirements (Section 10, requirement notes); no transcript | **PASS** |

**Overall: FAIL (loop 2 of 3).** Build applied every loop-1 fix exactly as written. The two remaining failures come from replacement wording that I specified in test-report-v1, not from a Build error. Applied side by side against their sources, they do not meet the "same skeleton, synonyms swapped" standard that report used to fail O3 and O6. Both fixes below are word-neutral (Block 10 stays at 135, page stays at 1,655).

---

## L1. Verification of the 11 loop-1 fixes: PASS (11/11)

I diffed draft-v1 against draft-v2 line by line over lines 1-327. Exactly 11 copy lines changed, plus the document title on line 7 ("Draft v1" became "Draft v2", which is not page copy). Each changed line matches test-report-v1's replacement text character for character.

| Fix | Location (v2 line) | Specified replacement | In draft-v2 | Words |
|---|---|---|---|---|
| O1 | Hero lede s2 (27) | "Epicor stays the system of record, while we design, build and support a custom connection for UAE and GCC manufacturers and distributors on cloud or on-premise Epicor." | Exact | 27 → 27; lede 55 |
| O2 | Block 3 P1 s3 (79) | "Sales, service and marketing staff handle accounts, opportunities, quotes, cases and campaigns in SugarAI, with each customer created once and shared." | Exact. P1 s1 ("HLB HAMT builds a custom integration into the Epicor ERP you already run...") untouched. | 22 → 21; P1 57 |
| O3 | Block 10 step 1 (260) | "Today's quote, order and invoice steps mapped with your teams." | Exact | 9 → 10 |
| O4a | Block 10 step 4 (269) | "Duplicate accounts resolved; the migration rehearsed at least twice." | Exact | 9 → 9 |
| O4b | Block 8 item 04 (219) | "Customer records from your current CRM and Epicor reconciled, with every load proven in a test environment first." | Exact. No "trial-load", "before cutover" or "removing duplicates". | 15 → 18; Block 8 140 |
| O5 | Block 10 step 6 (275) | "Teams go live in waves, with hypercare before SLA-backed support." | Exact. Not the FSM "Hypercare covers each launch phase..." | 9 → 10 |
| O6 | Block 10 callout (278) | "A SugarAI rollout for sales alone typically takes six to ten weeks. Adding the Epicor connection and data migration usually extends it to 2.5 to 5 months, released in stages so teams start early." | Exact. H4 "Realistic timelines, delivered in phases" kept. | 32 → 34 |
| O7 | Block 9 tile 4 (247) | "One desk takes requests, a named manager owns your account, and escalations follow a set route." | Exact | 15 → 16 |
| O8 | Closing row 1 (324) | "We start by learning how your Epicor, CRM and sales process fit together." | Exact. Not "First, we talk through..." | 12 → 13 |
| O9 | Closing row 3 (326) | "Then a proposal that costs the draft data map and plans each phase." | Exact. No "in writing for your sign-off" or "timeline and cost". | 11 → 13 |
| 6a | Block 2 stat 3 `.d` (69) | "How much likelier mid-sized enterprises that prioritise interoperability and eliminate data silos are to see measurable satisfaction gains, Avasant found." | Exact. `.n` 2.3×, `.l` "Customer satisfaction gains" and marker [2] kept. | 17 → 20 |

- **Supporting edits:** the "Stats used" A1 row (334) now carries the new wording and the full source qualifier. Flag 11 records the qualifier fix, and Flag 14 restates counts. Both are correct.
- **Optional items** G1, G3 and T1-T5 from test-report-v1 were not applied. That is fine, since they were optional.

**About the FSM-avoidance constraints in test-report-v1.** These held against the **published** FSM page (`output/sugarai-field-service-management.html`, lines 528, 543, 553, 578, 658, 660):

| v2 line | FSM published line | Verdict |
|---|---|---|
| Step 1 "Today's quote, order and invoice steps mapped with your teams." | "Workshops follow a typical job end to end: call, visit, invoice and renewal." | No shared frame |
| Step 4 "Duplicate accounts resolved; the migration rehearsed at least twice." | "We trial-load customer, site, asset and contract records, removing duplicates before cutover." | Concept only (duplicates) |
| Step 6 "Teams go live in waves, with hypercare before SLA-backed support." | "Hypercare covers each launch phase; an SLA then governs managed support." | Distinct from FSM. **Fails against Insurance instead** (see 5.4) |
| Tile 4 "One desk takes requests, a named manager owns your account, and escalations follow a set route." | "Your build team stays on after launch under agreed service levels, and one named manager takes escalations." | "named manager" + "escalations" are the shared company facts. The predicates differ. Pass |
| Row 1 "We start by learning how your Epicor, CRM and sales process fit together." | "First, we talk through your job types, contracts, crews and today's systems." | Different verb and list. The "fit together" clause is new. Pass |
| Row 3 "Then a proposal that costs the draft data map and plans each phase." | "Scope, phases, timeline and cost, in writing for your sign-off." | No shared frame |

- **Note (unpublished FSM text, not scored):** Block 8 item 04 sits close to a replacement line that the **FSM test-report-v1 proposed but FSM never adopted**: "Customer, site, asset and contract records deduplicated and proven in a test load first." That sentence was never published (FSM shipped "We trial-load..."), so it creates no duplicate content.

---

## 0a. Critical check: TCP webinar material. PASS (0 hits on the page)

I ran a fresh case-insensitive ripgrep over the whole `draft-v2.md` with: `fluent`, `tcp`, `14.day`, `free trial`, `trial`, `free `, `Southern Alumin`, `Palazzi`, `West Coast`, `Towle`, `200+`, `150+`, `sales day(s)`, `selling day(s)`, `offline`, `any Epicor data`, `Prophet`, `Eclipse`, `BisTrack`, `Northern Depot`, `purpose-built`, `work where you are`, `perfectly integrated`, `excels`, `seamless`, `Kinetic theme`, `dashlet`, `Account 360`, `Navigator`, `O365`, `Microsoft 365`, `Platinum`, `Premier`, `hours, not weeks`, `live in hours`, `Codeless`, `iPaaS`, `middleware`, `sales-i`, `real.?time`, `pre-?built`, `no.code`, `zero code`, `out of the box`, `plug and play`, `certified Epicor`, `Epicor implementation`, `Epicor partner`, `connector`.

| Hits in page copy (19-327) | Status |
|---|---|
| "industrial" ×2 (235) and ×2 (308, Sources [4] title/URL) | Substring of "trial". Not a trial offer. |
| "free zone" (235) | UAE company type |
| "your Epicor partner" (235) | The client's own partner. Correct division of roles. |
| "any existing connector" (298, FAQ A4) | Brief FAQ 4 wording. Names no product. |

- **All other hits are in the Stats-used table (336) or the Flags list (350-369).** The result is identical to v1. None of the 11 edits introduced a banned term.
- **The four designer descriptions** (88, 125, 142, 187) are unchanged and clean.

## 0b. Critical check: positioning. PASS

| Where | Text (line) | Status |
|---|---|---|
| Hero lede s1 | "HLB HAMT connects SugarAI with Epicor ERP as you already run it..." (27) | Unchanged |
| Hero lede s2 | "...a custom connection for UAE and GCC manufacturers and distributors **on cloud or on-premise Epicor**." (27) | Changed by O1. The deployment now refers explicitly to the client's own Epicor, which strengthens the "bring your Epicor" framing. "Custom connection" (Section 10 point 2) is kept. |
| Block 3 P1 s1 | "HLB HAMT builds a custom integration into the Epicor ERP you already run and replaces nothing on the Epicor side." (79) | Unchanged |
| Block 9 | "work alongside your Epicor partner or in-house ERP team" (235) | Unchanged |
| FAQ A4 | "We review your configuration and any existing connector, then extend, repair or replace it." (298) | Unchanged |

- **Banned-claim sweep:** "certified Epicor", "Epicor implementation", partner tiers, real-time, pre-built, no-code, out of the box and plug and play all return **0** in page copy. "Certified" appears only in tile 2 ("Certified SugarAI partner"). Every "implement..." hit is CRM-side.
- **New wording adds no Epicor-expertise inference.** "Customer records from your current CRM and Epicor reconciled" (219) describes a data task, not Epicor implementation.

## 0c. Layout check. PASS (unchanged)

- **Every Format line and block skeleton is identical to v1.** The diff touched copy text only.
- **Blocks:** 12 blocks in brief order.
- **Images:** 4 image slots (IMG-1 to IMG-4) with labels, aspect ratios, designer descriptions, counted captions and alt text. IMG-3 and IMG-4 captions open "Illustrative:".
- **Cards:** **2 card blocks**, Block 5 (6 benefit cards in `.grid-3`) and Block 9 (4 credential tiles in `.grid-4`).
- **Prose-led blocks:** 3, 4, 5 (first half), 7, 9 (paragraph) and the Block 10 callout.
- **List and table formats:** Block 3 table, Block 4 `ol`, Block 8 numbered services and the Block 10 timeline.

---

## 1. Keyword placement and density: PASS

Count rule (brief 2): exact phrase, case-insensitive, on-page copy only (lines 19-327). Meta is placed but not counted.

| Keyword | Count | Placements (line) | Required | Result |
|---|---|---|---|---|
| CRM integration with Epicor ERP | **4** | H1 (25); Block 3 H2 (77); Block 5 prose s1 (137); FAQ A2 s1 (292) | Exactly 4 | Pass |
| SugarAI with Epicor ERP | **2** | Hero lede s1 (27); FAQ Q1 (288) | Exactly 2 | Pass |
| CRM integration services | **2** | Block 8 H2 (201); FAQ A5 (301) | Exactly 2 | Pass |
| CRM integration partner | **1** | Block 9 H2 (233) | Exactly 1 | Pass |
| CRM implementation | **2** | Block 8 item 02 H4 (210); Block 10 lede (257) | Exactly 2 | Pass |

- **Placement:**
  - Meta title (1) and meta description (2) lead with the primary keyword.
  - The H1 covers the first 100 words.
  - Meta keywords (5) are in order.
- **Stuffing:**
  - Total **11** (cap 12), about 0.66% of 1,655 words.
  - Keywords sit only in the H1, the 4 permitted subheadings and FAQ Q1.
  - No sentence holds two keywords.
  - None of the 11 edits added an accidental match. The new "Customer records from your current CRM and Epicor" and "how your Epicor, CRM and sales process" form no tracked phrase.
- **Counts in counted copy:** "Outlook" 1× and "iOS and Android" 1× (191).

## 2. Word count: PASS (1,655)

I re-counted every block word by word under the brief Section 1 rule. Excluded: eyebrows, buttons, nav, breadcrumb, footer, meta, Sources, placeholder labels, alt text, designer descriptions, footnote markers, the `01`-`06` service numerals and the three `.n` figures.

| Block | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v2 words | 134 | 90 | 255 | 125 | 234 | 23 | 123 | 140 | 142 | 135 | 204 | 50 | **1,655** |
| Budget | 120-135 | 85-100 | 240-275 | 120-140 | 225-250 | 20-26 | 117-132 | 140-160 | 130-150 | 115-135 | 204-254 | 46-52 | 1,500-1,700 |

- **Matches Build's 1,655 exactly.** Every block is inside its budget.
- **Block 10 is at its 135 cap**, so the fixes below are word-neutral.
- **Sub-budgets:**
  - Hero lede: 55
  - Stat `.d`: 16 / 16 / 20 (range 16-20)
  - Block 3: P1 57, P2 62, P3 28, table 89
  - Block 8 bodies: 16 / 16 / 15 / 18 / 14 / 15
  - Tiles: 14 / 15 / 16 / 16
  - Process steps: 10 / 9 / 10 / 9 / 8 / 10 (range 8-10)
  - Callout: 34 (range 28-34)
  - Closing rows: 13 / 11 / 13

## 3. Zero em dashes: PASS

- **Whole-file ripgrep:** `—` (U+2014) **0**, `–` (U+2013) **0**, `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- **British spelling sweep:** -ize/-yze/-ization, color, center, program, license, modeled, favor, behavior, catalog, percent.
  - Page copy returns **0**.
  - Off-page hits are "customization", "prioritize" and "percent", all inside source quotes in the Stats-used table (333-334). "sized" is a false positive.
  - The new lines use "prioritise" and "likelier", and my fix text below uses "programmes".
- **No errors** in the 11 new lines.
- **Advisories (not scored):**
  - **G4. Callout (278):** "usually extends it to 2.5 to 5 months" has a double "to ... to". Fix 5-R2 replaces this sentence anyway.
  - **G5. Closing rows (324-326):** row 1 is a full sentence ("We start by..."), row 2 a noun phrase ("A demonstration of..."), and row 3 opens "Then a proposal...". The rows are already numbered, so "Then" is redundant. An optional fix is "A proposal that costs the draft data map and plans each phase." (-1, row 3 becomes 12, which is in range).
  - **G6. Stat 3 `.d` (69):** "satisfaction gains" repeats the `.l` label "Customer satisfaction gains". This is acceptable because the `.d` must restate the cohort, but "measurable improvements in satisfaction" (+1, `.d` becomes 21, over the 20 cap) does not fit. Leave as is.
  - **G1 and G3 from v1** are still open and optional.

## 5. Originality: FAIL (2 lines)

### 5.1 TCP deck (all 20 slides): clean

- **Re-grep of the extraction** for the vocabulary of the new lines (wave, test environment, reconcil, escalat, named, proposal, fit together, rollout, weeks, months, hypercare, duplicate, rehears, system of record, on-premise, we start, discovery, staff, desk): **0 hits.**
- **No slide heading or line** sits near any new sentence.

### 5.2 The five reference sites (re-fetched today for the new wording)

| Site | Access today | Finding for the v2 lines |
|---|---|---|
| tcpamericas.com Sugar-Epicor page | Fetched | The only related line is "Epicor version 10.2.500 or newer, cloud or on-premise". The hero's "on cloud or on-premise Epicor" shares the deployment pair, which is brief-allowed wording ("Epicor Kinetic, in the cloud or on-premise") and generic. No sentence match. |
| fluenterp.com Epicor-SugarCRM | Fetched | No sentence about go-live, hypercare, support desks, escalation, timelines, migration, test environments, proposals or discovery. No match. |
| linkedin.com SugarAI article | Fetched | Closest is "Break down silos" against stat 3's "eliminate data silos". The draft's phrase is Avasant's own qualifier, quoted for accuracy (see 6). No match. |
| codelessplatforms.com | 403 (as before) | Covered by brief-time search text. That text is a generic record list with nothing on process or support. |
| marketplace.sugarai.com TCP listing | Empty (as before) | Same product as the TCP page |

### 5.3 Wider web: exact-phrase searches on the new wording, no matches

| Phrase searched | Result |
|---|---|
| "custom connection for UAE and GCC manufacturers and distributors" | No match (unrelated customs/logistics pages) |
| "Sales, service and marketing staff handle accounts, opportunities, quotes, cases and campaigns" | No match (generic CRM glossaries) |
| "quote, order and invoice steps mapped" | No match |
| "the migration rehearsed at least twice" | No match |
| "with every load proven in a test environment" | No match |
| "go live in waves, with hypercare" | No exact match (generic hypercare blogs) |
| "released in stages so teams start early" | No match |
| "a named manager owns your account" | No match |
| "learning how your Epicor, CRM and sales process fit together" | No match |
| "a proposal that costs the draft data map" | No match |

### 5.4 HLB HAMT's own Insurance template and live hub: FAIL (2 lines)

I applied the same standard test-report-v1 used for O3 and O6: a line fails if it keeps a source sentence's skeleton, element for element, with synonyms swapped in. Shared industry terms and brief-mandated facts alone do not fail a line.

| # | Draft location (line) | Source text | Draft text (v2) | Mapping |
|---|---|---|---|---|
| R1 | Block 10 step 6 (275) | Insurance live HTML process step 6 (line 548): "**Phased go-live with hypercare, then managed support under SLA.**" | "**Teams go live in waves, with hypercare before SLA-backed support.**" | Phased go-live → go live in waves; **"with hypercare"** verbatim; then → before; managed support under SLA → SLA-backed support. Same three-beat frame with 4 shared lexical items ("go live", "with hypercare", "SLA", "support"). This is the class v1 failed as O5. **My v1 replacement only reshuffled it.** |
| R2 | Block 10 callout (278) | Live hub FAQ "How long does implementation take" (lines 1367-1370): "**A sales-focused rollout for one company usually goes live in six to ten weeks.** A larger programme covering sales, service and marketing **with ERP integration and data migration typically runs 2.5 to 5 months, delivered in phases so your first users are working long before the last.**" | "**A SugarAI rollout for sales alone typically takes six to ten weeks. Adding the Epicor connection and data migration usually extends it to 2.5 to 5 months, released in stages so teams start early.**" | **S1:** "A [qualifier] rollout for [scope] [usually/typically] [goes live in/takes] six to ten weeks" is the same frame. **S2:** "[with/adding] [ERP integration/Epicor connection] and data migration [typically runs/usually extends it to] 2.5 to 5 months, [delivered/released] in [phases/stages] so [first users are working long before the last/teams start early]" is clause-for-clause the hub sentence. The adverbs are simply traded between sentences. This is the same finding as v1 O6 ("sentence 2 is lightly reworded"), and my v1 replacement did not clear it. It is also duplicate copy on the same domain. |

**Ruled acceptable (recorded so they are not reopened in loop 3):**

- **O1 hero s2 (27).** Insurance: "HLB HAMT implements SugarAI for insurers, brokers and agencies across the UAE and GCC, cloud or on-premise."
  - The v2 sentence opens on "Epicor stays the system of record, while we design, build and support a custom connection...".
  - It moves "UAE and GCC" in front of the audience as a modifier, and turns "cloud or on-premise" into a modifier of the client's Epicor.
  - The sentence frame and the tail are both gone. What remains are the brief-mandated facts (region, deployment).
- **O2 Block 3 P1 s3 (79).** Insurance FAQ: "SugarAI is where sales, service and claims teams work".
  - Only the generic triad "sales, service and" is shared. The hub's "covering sales, service and marketing" is the same generic list.
  - The frame changed from "SugarAI is where X work" to "X handle Y in SugarAI".
- **O3 step 1 (260).** Insurance: "We map how a quote becomes a policy, claim and renewal today."
  - The content atoms (map, quote, a 3-item list, today) are inherent to a Discovery step on a quote-to-order page.
  - The syntax is entirely different: a noun phrase with a participle, not "We map how a quote becomes...".
  - **Borderline.** Optional tweak O-1 below removes even the atom overlap.
- **O4a step 4 (269).**
  - Against hub "at least two full rehearsal migrations into a test environment": a company fact in new wording.
  - Against Insurance "cleansed, mapped and rehearsed before load": only "rehearsed" is shared.
- **O4b item 04 (219).** Shares only the 2-word technical term "test environment" with the hub.
- **O7 tile 4 (247).**
  - Insurance: "A dedicated team on agreed service levels, with a named manager and a clear escalation path."
  - Hub: "a single service desk with agreed response and resolution times, a named service manager and a defined escalation path"; also "Requests are logged through a single service desk, prioritised and escalated through a defined process".
  - The three facts (one desk, named manager, defined escalation) are the brief's mandated company facts, so they must appear.
  - The v2 line turns the noun list into three clauses, each with a new subject and predicate ("takes requests", "owns your account", "follow a set route").
  - **Borderline but passes.** "a named manager" is a 3-word fact phrase. Optional tweak O-2 below reorders the clauses if the Content Writer wants more distance.
- **O8 row 1 (324).**
  - Against Insurance "A discovery call on your product lines, channels and current systems": shared "your [list]" only.
  - Against Insurance "We start from an insurance blueprint" (HTML 404, 569): only the 2-word opener "We start" is shared. Different verb and object.
- **O9 row 3 (326).** No shared frame with Insurance ("A written proposal covering scope, timeline and investment") or FSM.
- **6a stat 3 `.d` (69).** This reuses Avasant's 9-word qualifier ("mid-sized enterprises that prioritise interoperability and eliminate data silos are"). That is an attributed, footnoted restatement of the cohort a cited statistic applies to, and item 6 requires the precision. It is not an originality violation.

## 6. Stat accuracy and footnoting: PASS

Every source was re-fetched today (2026-10-07).

| ID | Draft (line) | Source check today | Verdict |
|---|---|---|---|
| A1 | `2.3×` / "Customer satisfaction gains" / "How much likelier mid-sized enterprises that prioritise interoperability and eliminate data silos are to see measurable satisfaction gains, Avasant found. [2]" (66-69) | Avasant, fetched. Source: "According to Avasant's Cloud CRM Suites 2024 RadarView™, mid-sized enterprises that prioritize interoperability **and eliminate data silos** are 2.3x more likely to achieve measurable improvements in customer satisfaction and operational responsiveness." Acklin and Frederick, September 2025. | **Pass. The loop-1 defect is fixed.** Both cohort conditions (mid-sized, prioritise interoperability **and** eliminate data silos) are now stated. "Measurable satisfaction gains" with the "Customer" label is faithful to "measurable improvements in customer satisfaction". The fetch also confirms the figure is explicitly attributed to the Cloud CRM Suites 2024 RadarView, so Sources [2]'s parenthetical "(data from Avasant's Cloud CRM Suites 2024 RadarView)" is accurate. |
| N1 | `7%` / "Higher win rates" (57-59), unchanged | Nucleus Z56, fetched: "a seven percent improvement in win rates", 8 April 2025 | Pass |
| N2 | `~50%` / "Shorter customisation timelines" (61-64), unchanged | Same page: "an approximate 50 percent reduction in customization timelines" | Pass |
| A2 | "more than 60% of enterprises still operate with fragmented data environments. [2]" (137), unchanged | Avasant, fetched: "over 60% of enterprises still operate with fragmented data environments", attributed to the same RadarView | Pass |
| U1 | "UAE industrial exports passed AED 262 billion in 2025. [4]" (235), unchanged | Khaleej Times, fetched: "industrial exports surpassing Dh262 billion in 2025", Hassan Al Nowais (MoIAT), 10 June 2026 | Pass |
| F1 | Nucleus SFA Value Matrix 2026 Leader, sixth straight year, "ERP-informed insight" (193), unchanged | 01net reprint, fetched (25 Feb 2026): "named a Leader in the Nucleus Research Sales Force Automation (SFA) Technology Value Matrix 2026"; "sixth consecutive year that Sugar has been recognized as a Leader". The ERP-insight strength is tied in the release to the sales-i add-on, which correctly stays unnamed. | Pass (as v1) |
| F2-F6 | Rebrand, Sugar Connect, mobile app, REST/BAQs, hub facts | Unchanged lines. The hub text was re-read today: 6-10 weeks, 2.5-5 months, "at least two full rehearsal migrations", named service manager and post-release retesting all appear (1367-1418). | Pass |

- **Recency:**
  - Nucleus: about 18 months.
  - Avasant: article 13 months old, data about 2 years old.
  - Khaleej Times: about 4 months.
  - All are inside the 2-3 year window.
- **Footnote markers** [1] [1] [2] (Block 2), [2] (Block 5), [3] (Block 7) and [4] (Block 9) run in order. FAQ answers carry no markers. Sources [1]-[5] are unchanged.
- **No duplication across the project.** No new figure was introduced, and v1's project-wide check stands.
- **No fabricated figures.** The page's only numbers are 7%, ~50%, 2.3×, 60%, AED 262 billion, 26 years, six to ten weeks, 2.5 to 5 months, "at least twice" and "sixth". Each is sourced or is a hub company fact. No pricing appears.
- **Click-checks still pending** (Build Flag 13): the Business Wire original for [3], the support.sugarai.com mobile guide, the knowledgelib.io REST explainer and the hlbhamt.com link targets.

## 7. Human tone / AI-detection heuristics: PASS

- **Stock-phrase sweep:** unlock, seamless, fast-paced, revolution, unleash, in conclusion, game-chang, cutting-edge, leverag, empower, robust, streamline, holistic, elevate, harness, delve, landscape, synerg, transformative, journey, world-class and best-in-class all return **0**.
- **The new lines read as written for this subject.** Examples: "Duplicate accounts resolved", "every load proven in a test environment first", "a proposal that costs the draft data map".
- **Openers stay varied.**
  - Block 10 steps: Today's / Data map / SugarAI / Duplicate / Quote-to-order / Teams.
  - Tiles: Building / Implementation / An / One.
- **Advisories (not scored):**
  - **T6. Hero lede (27).** "Epicor" now appears 4× in two sentences, and sentence 2 ends on "on cloud or on-premise Epicor". This is not a defect, because it carries the positioning. If the Content Writer wants it lighter, "...for UAE and GCC manufacturers and distributors, whether their Epicor runs in the cloud or on-premise." (+4, lede 59) would exceed the 55 cap, so leave it unless the cap is relaxed.
  - **T4 (card 4) from v1** is still open and optional.

## 8. Section structure: PASS

- **Blocks:** 12 blocks in brief order, formats unchanged (0c).
- **Headings:** H1 and H2s are "use as written". Eyebrows and sticky nav labels match brief 3b.
- **Breadcrumb and parent unchanged:**
  - "CRM Solutions (SugarAI)" links to `https://hlbhamt.com/sugarai-crm-2/` (15), per Section 10 point 3.
  - The footer hub link is the same (17).
  - The suggested slug `/sugarai-crm/integrations/epicor-erp/` is unchanged (16).
- **FAQ:** 5 Q&As, first open. Q1 is word for word. Answers are 31 / 30 / 30 / 30 / 31 words with no inline markers. The JSON-LD instruction (5 visible Q&As, word for word) is carried (282). All five are unchanged from v1.
- **Sources note:** one note, after the FAQ and before the closing CTA (303-311).
- **Internal links unchanged:**
  - L1 "SugarAI CRM services" goes to the hub (211).
  - L2 "manufacturers and distributors" goes to /industries/manufacture-and-distribution/ (35).
  - L3 "ERP practice" goes to /services/erp-integration-add-ons/ (244).
  - L4 is omitted (conditional; Flag 8).
- **CTAs unchanged.** There is no trial offer of any kind.

## 9. Client requirements and transcript: PASS

- **No transcript** was supplied (requirement notes). Nothing is attributed to one.
- **Section 10:**
  - Point 1: positioning passes (0b).
  - Point 2: "custom connection" and "custom integration", with no named or resold connector.
  - Point 3: hub parent.
  - Point 4: "Illustrative" captions and mock-up notes. The demo wording still avoids promising the client's own live Epicor data (172, 325).
  - Point 5: Kinetic only, with no Prophet 21, Eclipse or BisTrack.
  - Point 6: N1, N2 and A1 are used, the FSM 8% is not, and sales-i is unnamed.
- **Company facts in the edited lines are accurate to the hub:**
  - six to ten weeks, 2.5 to 5 months and phased delivery (callout);
  - two rehearsals (step 4);
  - test-environment loads (item 04);
  - one service desk, named manager and defined escalation (tile 4).
- **The callout fix below keeps every fact.** It changes only the wording.

---

## Overall: FAIL (loop 2 of 3)

- **All 11 loop-1 fixes were applied exactly.** The A1 stat now carries the full Avasant cohort and was re-verified at source today.
- **The critical checks are still clean.** TCP material is 0 on the page. Positioning is unchanged and slightly stronger in the hero. The layout is unchanged (2 card blocks).
- **Word count is 1,655.** Keywords are 4 / 2 / 2 / 1 / 2 (11). There are 0 dashes.
- **Item 5 fails on 2 lines** (R1 step 6, R2 callout), both in Block 10. Both are replacement texts I prescribed in test-report-v1. Build followed them faithfully. Checked side by side, they keep the Insurance step 6 frame and the live hub timeline FAQ frame with synonyms swapped. That is the same class of finding v1 failed.
- **Everything else passes.** The two fixes below are word-neutral: Block 10 stays 135 and the page stays 1,655. No keyword, stat or structure changes.

## Fix instructions

Apply exactly. Do not change any other line. Keep zero em/en dashes, British spelling and every keyword count. No Stats-used row changes. In Flag 14, Block 10 stays 135 and the total stays 1,655. Flag 6 lists "rehearsed at least twice" among the hub facts, and that wording is unchanged.

**5-R1. Block 10 step 6, Go-live and support (line 275). 10 → 10 words.**
- Replace: "Teams go live in waves, with hypercare before SLA-backed support."
- With: "Each team switches over separately, backed by our service desk."
- **Constraints, if Build must vary it:**
  - do not use "phased", "go live/go-live", "with hypercare", "then ... support" or "SLA ... support" (Insurance step 6);
  - do not use "Hypercare covers each launch phase" or "an SLA then governs" (FSM step 6).
- I checked the replacement: exact-phrase web search finds no match, and it shares no frame with Insurance, the hub or FSM.

**5-R2. Block 10 callout body (line 278). 34 → 34 words (range 28-34).**
- Replace: "A SugarAI rollout for sales alone typically takes six to ten weeks. Adding the Epicor connection and data migration usually extends it to 2.5 to 5 months, released in stages so teams start early."
- With: "Six to ten weeks is typical for a project limited to sales. Connecting Epicor and migrating data puts most programmes at 2.5 to 5 months, with early phases live while later ones are built."
- Keep the H4 "Realistic timelines, delivered in phases" as written.
- **Constraints, if Build must vary it:**
  - do not open with "A [sales-focused/sales-only/SugarAI] rollout/project ... usually/typically ... six to ten weeks";
  - do not use "integration and data migration" or "typically runs";
  - do not use "[delivered/released] in [phases/stages] so [users/teams] ...".
- **The facts must stay exact:** 6-10 weeks for a sales-only scope; 2.5-5 months once Epicor integration and data migration are added; phased so early users are working before the programme ends.
- Exact-phrase web search on "with early phases live while later ones are built" finds no match.

**Word ledger after fixes:** Block 10 = 8 (H2) + 18 (lede) + 14 (step H4s) + 56 (step bodies) + 5 (callout H4) + 34 (callout) = **135**. Total **1,655**.

### Optional (Content Writer or Build discretion; not needed to pass)
- **O-1. Block 10 step 1 (260).** "Today's quote, order and invoice steps mapped with your teams." becomes "Current quote-to-invoice steps reviewed with sales, service and finance." (10 → 9; Block 10 becomes 134). This removes the last atom overlap (map / quote / today) with the Insurance Discovery step.
- **O-2. Block 9 tile 4 (247).** "One desk takes requests, a named manager owns your account, and escalations follow a set route." becomes "Requests reach one desk, escalations follow a set route, and your account has a named manager." (16 → 16, inside the 14-16 range). It breaks the desk, named manager, escalation order shared by Insurance and the hub.
- **G5. Closing row 3 (326).** Drop "Then" (13 → 12).
- **G1, G3, T1, T2, T3, T4, T5 and the tile 3 wording from v1** are still open and optional. T3 cannot be used unless Block 10 frees 2 words (for example via O-1 plus another trim).

---

Sources consulted today:
- [Avasant, Breaking Down Data Silos (Sept 2025)](https://avasant.com/report/breaking-down-data-silos-why-crm-integration-is-now-a-boardroom-priority/): "According to Avasant's Cloud CRM Suites 2024 RadarView™, mid-sized enterprises that prioritize interoperability and eliminate data silos are 2.3x more likely..."; "over 60% of enterprises still operate with fragmented data environments".
- [Nucleus Research Z56](https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/): "a seven percent improvement in win rates"; "an approximate 50 percent reduction in customization timelines"; 8 April 2025.
- [Khaleej Times, 10 June 2026](https://www.khaleejtimes.com/business/uae-industrial-exports-hit-dh262b-as-sectors-gdp-contribution-climbs-by-70): "industrial exports surpassing Dh262 billion in 2025", Hassan Al Nowais, MoIAT.
- [01net reprint of the Nucleus SFA Value Matrix 2026 release](https://www.01net.it/sugarcrm-named-a-leader-in-the-nucleus-research-sales-force-automation-technology-value-matrix-2026/): Leader 2026, sixth consecutive year, 25 Feb 2026.
- Reference sites:
  - [TCP Sugar-Epicor page](https://www.tcpamericas.com/en/pages/sugar-epicor-integration) (fetched)
  - [fluenterp Epicor-SugarCRM](https://www.fluenterp.com/en/integrations/epicor-sugarcrm) (fetched)
  - [SugarAI LinkedIn article](https://www.linkedin.com/pulse/boost-sales-service-epicor-erp-sugarcrm-sugarcrm-42lqf/) (fetched)
  - Codeless Platforms (403 at brief stage and in v1; not re-attempted)
  - SugarAI marketplace listing (empty at brief stage and in v1; not re-attempted)
- Exact-phrase web searches: the 10 new-wording phrases in 5.3, plus the 2 proposed replacements in the fix instructions. None matched.
