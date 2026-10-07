# Test report v3: SugarAI CRM + Epicor ERP Integration subpage (draft-v3.md, loop 3 of 3)

Tested by: Test agent, 2026-10-07
Loop: **3 of 3** (`test-report-v1.md` and `test-report-v2.md` exist). This is the final allowed Build→Test loop.
Inputs: `brief.md` (Section 10 overrides where noted), `draft/draft-v3.md`, `draft/draft-v2.md` (for the diff), `draft/test-report-v2.md`, `inputs/requirement-notes.md`, `inputs/extracted/tcp-sugarcrm-epicor-kinetic-webinar-slides.pdf.md`, `inputs/structural-sample/hlbhamt-sugarai-insurance.html` and its `.pdf.md` extraction, the saved live hub text (`../2026-09-29-data-visualization-services-homepage/inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`), and the published FSM sibling (`../2026-09-23-sugarai-field-service-management-subpage/output/sugarai-field-service-management.html`).

Page copy = draft lines 19-327 (Blocks 1-12 and the Sources note). Lines 1-17 are meta and chrome. Lines 328-370 are Build's "Stats used" and "Flags", which are internal and must never ship.

This was a full fresh pass, not only a diff check. I re-counted every block word by word, re-ran every grep, re-fetched all four stat sources and three of the five reference sites, and checked both new lines against every source class.

---

## Summary

| # | Item | Result |
|---|---|---|
| L2 | **Both loop-2 fixes applied exactly; nothing else in page copy changed** | **PASS** |
| 0a | **Critical: TCP-deck exclusions** | **PASS** (0 hits in page copy, captions, alt text, designer descriptions or meta) |
| 0b | **Critical: positioning (SugarAI connects to your existing Epicor; no Epicor certification claim)** | **PASS** |
| 0c | **Layout: prose-led, limited cards, 4 image slots** | **PASS** |
| 1 | Keyword placement and density | **PASS** (4 / 2 / 2 / 1 / 2; total 11, cap 12) |
| 2 | Word count | **PASS** (1,655, independently re-counted) |
| 3 | Zero em dashes | **PASS** (0 em, 0 en, 0 `--`) |
| 4 | Grammar, spelling (British), punctuation | **PASS** |
| 5 | Originality | **PASS** (both new lines are clean against the Insurance template, live hub, FSM, TCP deck, the reference sites and the web) |
| 6 | Stat accuracy and footnoting | **PASS** (all 5 stats plus F1 re-fetched today; no drift) |
| 7 | Human tone / AI-detection heuristics | **PASS** (one optional advisory) |
| 8 | Section structure | **PASS** |
| 9 | Client requirements (Section 10, requirement notes); no transcript | **PASS** |

**Overall: PASS.** Ready for Deliver.

---

## L2. Verification of the 2 loop-2 fixes and full diff: PASS

### Fix application

| Fix | Location (v3 line) | Specified in test-report-v2 | In draft-v3 | Words |
|---|---|---|---|---|
| 5-R1 | Block 10 step 6 (275) | "Each team switches over separately, backed by our service desk." | Exact, character for character | 10 → 10 |
| 5-R2 | Block 10 callout body (278) | "Six to ten weeks is typical for a project limited to sales. Connecting Epicor and migrating data puts most programmes at 2.5 to 5 months, with early phases live while later ones are built." | Exact, character for character. H4 "Realistic timelines, delivered in phases" (277) kept as written. | 34 → 34 |

### Full diff, draft-v2 against draft-v3 (all 370 lines)

| Line | Change | In page copy? |
|---|---|---|
| 7 | "Draft v2" → "Draft v3" | No (document title) |
| 275 | Fix 5-R1 | Yes (intended) |
| 278 | Fix 5-R2 | Yes (intended) |
| 364 | Flag 14 heading "(self-check, v2)" → "(self-check, v3)" | No (internal flag) |
| 365 | Flag 14 explanation adds "the two test-report-v2 fixes are word-neutral: step 6 10 → 10, callout 34 → 34", and "Block totals after fixes" becomes "Block totals" | No (internal flag). Accurate. |

All other lines (1-6, 8-274, 276-277, 279-363, 366-370) are identical to draft-v2. That includes all chrome, every block, every image slot, the Sources note, the Stats-used table and Flags 1-13 and 15. **No unrequested page-copy change.**

### Fresh-eyes originality check on the two new lines

I ran this check with the standard that failed loop 2: a line fails if it keeps a source sentence's skeleton element for element, with synonyms swapped in. Shared company facts and industry terms alone do not fail a line.

| New line | Closest source text | Shared elements | Verdict |
|---|---|---|---|
| **Step 6:** "Each team switches over separately, backed by our service desk." | **Insurance step 6** (HTML 548): "Phased go-live with hypercare, then managed support under SLA." | None. No "phased", "go-live", "hypercare", "then", "managed support" or "SLA". The frame changes from "[noun phrase] with X, then Y" to "[subject] [verb] [adverb], [participle phrase]". | **Clean** |
| | **FSM step 6** (published HTML 553): "Hypercare covers each launch phase; an SLA then governs managed support." | None ("each" only) | **Clean** |
| | **FSM Block 10 lede** (published HTML 521): "The service desk goes live first; mobile job sheets and scheduling follow." | "service desk". In FSM this means the client's service desk team going live. Here it means HLB HAMT's support desk. Different referent and frame. | **Clean** |
| | **Live hub** (lines 412, 457-458): "Requests are logged through a single service desk..." | "service desk", a mandated company fact (brief Section 4 "a single service desk"). | **Clean** (fact, not frame) |
| | **Data Visualization homepage** (published, line 840): "...until the outputs match before anyone switches over." | "switches over", a common 2-word verb in an unrelated sentence and context. | **Clean** |
| **Callout:** "Six to ten weeks is typical for a project limited to sales. Connecting Epicor and migrating data puts most programmes at 2.5 to 5 months, with early phases live while later ones are built." | **Live hub FAQ** (1367-1370): "A sales-focused rollout for one company usually goes live in six to ten weeks. A larger programme covering sales, service and marketing with ERP integration and data migration typically runs 2.5 to 5 months, delivered in phases so your first users are working long before the last." | Only the mandated facts ("six to ten weeks", "2.5 to 5 months", phased) plus the generic noun "programme(s)". **S1** inverts the frame: the duration is now the subject ("Six to ten weeks is typical for..."), not "A [qualifier] rollout ... goes live in". **S2** uses a gerund-pair subject with "puts ... at", not "with ERP integration and data migration typically runs". The tail "with early phases live while later ones are built" replaces "delivered in phases so your first users are working long before the last". None of the three constraints in test-report-v2 5-R2 is breached. | **Clean** |
| | **Insurance FAQ** (HTML 630): "A single-line SugarAI rollout lands in eight to twelve weeks; a wider programme runs five to seven months." | "programme" only. No "rollout lands" or "programme runs" frame. | **Clean** |
| | **Insurance callout** (HTML 553-554) and **FSM callout** (published HTML 558-559) | Both are about Guided Low-Touch onboarding. No timeline frame is shared. | **Clean** |

**TCP deck:** I grepped the extraction for switch, desk, separately, weeks, months, phase, typical, programme, backed, early, later and built. The only hits are line 4 ("built-in PDF renderer", the extraction note) and line 125 ("Purpose-Built for Epicor"). Neither is related. **Clean.**

**Reference sites (re-fetched today):**

| Site | Result |
|---|---|
| tcpamericas.com | The only timeline sentence is "Setup runs through a web portal in hours, not weeks." No match. |
| fluenterp.com | No go-live, timeline, phase or support-desk sentence at all |
| SugarAI LinkedIn article | No go-live, timeline, phase or support-desk sentence at all |
| codelessplatforms.com | 403 at brief stage. Its search text is a record list only. |
| SugarAI marketplace listing | Empty at brief stage. Same TCP product. |

**Exact-phrase web searches (today):**

| Phrase | Result |
|---|---|
| "Each team switches over separately" | No match (sports and gaming pages only) |
| "Six to ten weeks is typical for a project limited to sales" | No match |
| "Connecting Epicor and migrating data" | No match (generic Epicor migration pages) |
| "with early phases live while later ones are built" | No match (construction-phasing pages) |

**Project-wide grep** for "switches over", "early phases live", "later ones are built", "limited to sales" and "backed by our service desk": the only hit outside this requirement is the unrelated Data Visualization FAQ line noted above.

---

## 0a. Critical check: TCP webinar material. PASS

I ran a case-insensitive ripgrep over the whole `draft-v3.md` for: fluent, tcp, 14.day, free trial, trial, Southern Alumin, Palazzi, West Coast, Towle, 200+, 150+, sales day(s), selling day(s), offline, "any Epicor data", Prophet, Eclipse, BisTrack, Northern Depot, purpose-built, "work where you are", "perfectly integrated", excels, seamless, "Kinetic theme", dashlet, real.?time, pre-?built, no.code, zero code, out of the box, plug and play, certified Epicor, Epicor implementation, Epicor partner, connector, "hours, not weeks", sales-i, middleware, iPaaS and Codeless.

| Hits in page copy (19-327) | Status |
|---|---|
| "industrial" ×2 (235) and ×2 (308, Sources [4]) | Substring of "trial". Not a trial offer. |
| "your Epicor partner" (235) | The client's own partner. Correct division of roles. |
| "any existing connector" (298, FAQ A4) | Brief FAQ 4 wording. Names no product. |

- Every other hit is in the Stats-used table (336) or the Flags list (350-369), which are internal.
- **No "Fluent" product name, no 14-day trial or any trial offer, no TCP testimonials, no 200+/150+ counts.** The result is identical to v2.
- The closing CTA (319-326) offers a discovery call, a demonstration and a proposal. There is no trial.

## 0b. Critical check: positioning. PASS (unchanged from v2)

- **Hero lede s1 (27):** "HLB HAMT connects SugarAI with Epicor ERP as you already run it..."
- **Block 3 P1 s1 (79):** "HLB HAMT builds a custom integration into the Epicor ERP you already run and replaces nothing on the Epicor side."
- **Block 9 (235):** "work alongside your Epicor partner or in-house ERP team".
- **FAQ A4 (298):** existing connector extended, repaired or replaced.
- **Banned claims:** "certified Epicor", "Epicor implementation", partner tiers, real-time, pre-built, no-code, out of the box and plug and play all return **0** in page copy. "Certified" appears only in tile 2 ("Certified SugarAI partner").
- **New step 6:** "backed by our service desk" refers to HLB HAMT's own support desk (a hub fact). It implies no Epicor expertise.

## 0c. Layout check. PASS (unchanged)

- **Blocks:** 12 blocks in brief order, each with its Format line.
- **Images:** 4 image slots (IMG-1 to IMG-4), each with a label, aspect ratio, designer description, counted caption and alt text. IMG-3 and IMG-4 captions open "Illustrative:" (Section 10 point 4).
- **Cards:** only **2 card blocks**, the Block 5 benefits grid (6) and the Block 9 credential tiles (4).
- **Prose-led blocks:** 3, 4, 5 (first half), 7, 9 (paragraph) and the Block 10 callout.
- **Lists and tables:** Block 3 table, Block 4 `ol`, Block 8 numbered services and the Block 10 timeline.
- The requirement for real prose rather than everything in cards (requirement notes, point 2) is met.

---

## 1. Keyword placement and density: PASS

Count rule (brief Section 2): exact phrase, case-insensitive, on-page copy only (lines 19-327).

| Keyword | Count | Placements (line) | Required | Result |
|---|---|---|---|---|
| CRM integration with Epicor ERP | **4** | H1 (25); Block 3 H2 (77); Block 5 prose s1 (137); FAQ A2 s1 (292) | Exactly 4 (Content Writer 3-4) | Pass |
| SugarAI with Epicor ERP | **2** | Hero lede s1 (27); FAQ Q1 (288) | Exactly 2 | Pass |
| CRM integration services | **2** | Block 8 H2 (201); FAQ A5 (301) | Exactly 2 | Pass |
| CRM integration partner | **1** | Block 9 H2 (233) | Exactly 1 | Pass |
| CRM implementation | **2** | Block 8 item 02 H4 (210); Block 10 lede (257) | Exactly 2 | Pass |

- **Placement:**
  - The meta title (1) and meta description (2) lead with the primary keyword.
  - The H1 is words 1-6 of the page, which covers the first 100 words.
  - Meta keywords (5) are listed primary first.
- **Stuffing:**
  - Total **11** (cap 12), about 0.66% of 1,655 words.
  - Keywords appear only in the H1, the 4 permitted subheadings and FAQ Q1.
  - No sentence holds two keywords.
  - The two new lines add no match.

## 2. Word count: PASS (1,655)

I counted independently, word by word, under the brief Section 1 rule. Excluded: eyebrows, buttons, nav, breadcrumb, footer, meta, Sources, placeholder labels, alt text, designer descriptions, footnote markers, the `01`-`06` numerals and the three `.n` figures. Hyphenated compounds count as one word.

| Block | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | **Total** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v3 words | 134 | 90 | 255 | 125 | 234 | 23 | 123 | 140 | 142 | 135 | 204 | 50 | **1,655** |
| Budget | 120-135 | 85-100 | 240-275 | 120-140 | 225-250 | 20-26 | 117-132 | 140-160 | 130-150 | 115-135 | 204-254 | 46-52 | 1,500-1,700 |

- **Inside the 1,500-1,700 target**, and inside the brief's 1,580-1,680 writing band. Every block is inside its budget.
- **Block 10:** 8 (H2) + 18 (lede) + 14 (step H4s) + 56 (step bodies 10/9/10/9/8/10) + 5 (callout H4) + 34 (callout) = 135.
- **The new lines are within their sub-ranges:** step 6 is 10 (range 8-10) and the callout is 34 (range 28-34).

## 3. Zero em dashes: PASS

- **Whole-file ripgrep:** `—` (U+2014) **0**, `–` (U+2013) **0**, `--` **0**.

## 4. Grammar, spelling, punctuation: PASS

- **British spelling sweep:** -ize/-ization/-yze, color, center, program, license, modeled, favor, behavior, catalog, percent, organiz, optimiz and analyz.
  - Page copy: **0** US forms.
  - The only hits are "customization", "prioritize", "ize" and "percent" inside verbatim source quotes in the Stats-used table (333-334), which is internal.
  - The new callout uses "programmes", correctly British.
- **New lines:**
  - Step 6 is a complete sentence with a correctly attached participle phrase.
  - In callout S1, "Six to ten weeks is typical" uses a singular verb with a quantity of time, which is standard.
  - Callout S2 is grammatical. The v2 advisory G4 (the double "to ... to") is gone.
- **No errors found.**
- **Carried advisory (optional, not scored):** G5 from test-report-v2. Closing row 3 (326) opens "Then a proposal...". "Then" is redundant in a numbered list, and dropping it leaves 12 words, which is in range.

## 5. Originality: PASS

- **New lines:** see L2. Both are clean against the Insurance template, the live hub FAQ, the FSM published page, the TCP deck, the three fetchable reference sites and the web.
- **Unchanged lines:** they were cleared in test-report-v1 and v2, and none of them changed.
- **No partial-echo fixes were needed.** The items ruled acceptable in test-report-v2 5.4 (O1, O2, O3, O4a, O4b, O7, O8, O9 and 6a) are not reopened, per that report.

## 6. Stat accuracy and footnoting: PASS (no drift)

Every source was re-fetched today (2026-10-07). No stat line changed between v2 and v3.

| ID | Draft (line) | Source today | Verdict |
|---|---|---|---|
| N1 | `7%` / "Higher win rates" / "...win-rate improvement Nucleus Research found among Sugar customers who brought CRM and ERP data together. [1]" (57-59) | Nucleus Research Z56, 8 April 2025: "a seven percent improvement in win rates" | Pass |
| N2 | `~50%` / "Shorter customisation timelines" (62-64) | Same page: "an approximate 50 percent reduction in customization timelines" | Pass |
| A1 | `2.3×` / "Customer satisfaction gains" / "How much likelier mid-sized enterprises that prioritise interoperability and eliminate data silos are to see measurable satisfaction gains, Avasant found. [2]" (67-69) | Avasant (Acklin and Frederick, Sept 2025): "mid-sized enterprises that prioritize interoperability and eliminate data silos are 2.3x more likely to achieve measurable improvements in customer satisfaction and operational responsiveness" | Pass. The full cohort qualifier is kept. |
| A2 | "more than 60% of enterprises still operate with fragmented data environments. [2]" (137) | Same article: "over 60% of enterprises still operate with fragmented data environments" | Pass |
| U1 | "UAE industrial exports passed AED 262 billion in 2025. [4]" (235) | Khaleej Times, 10 June 2026: "industrial exports surpassing Dh262 billion in 2025", Hassan Al Nowais, Undersecretary, MoIAT | Pass |
| F1 | Nucleus SFA Technology Value Matrix 2026 Leader, "sixth straight year", "ERP-informed insight" (193) | 01net reprint, 25 Feb 2026: "named a Leader in the Nucleus Research Sales Force Automation (SFA) Technology Value Matrix 2026"; "sixth consecutive year that Sugar has been recognized as a Leader"; ERP insight is credited to the sales-i add-on ("analyzes ERP order data to uncover account insights"), which correctly stays unnamed (Section 10 point 6) | Pass |
| Hub facts in the new lines | "service desk" (275); "six to ten weeks", "2.5 to 5 months" and phased delivery (278) | Hub 412, 457-458 ("single service desk"); 1367-1370 (six to ten weeks; 2.5 to 5 months; delivered in phases) | Pass. The facts are exact, with no footnote (series convention). |

- **Recency:**
  - Nucleus: about 18 months.
  - Avasant: article 13 months old, data about 2 years old.
  - Khaleej Times: about 4 months.
  - All are inside the 2-3 year window.
- **Footnotes:** markers [1] [1] [2] (Block 2), [2] (Block 5), [3] (Block 7) and [4] (Block 9) run in order. FAQ answers carry no markers. Sources [1]-[5] are unchanged.
- **No fabricated, misattributed or cross-project duplicate figures.** The FSM 8% figure is not used.
- **Click-checks still pending for Deliver or a human** (Build Flag 13): the Business Wire originals for [3] and [5], the support.sugarai.com guides and the knowledgelib.io REST explainer. These are carried, not failures.

## 7. Human tone / AI-detection heuristics: PASS

- **Stock-phrase sweep:** unlock, seamless, fast-paced, revolution, unleash, in conclusion, game-chang, cutting-edge, leverag, empower, robust, streamline, holistic, elevate, harness, delve, landscape, synerg, transformative, journey, world-class and best-in-class all return **0** in page copy. "seamless" in particular was confirmed at 0 by the 0a grep.
- **The new lines read naturally.**
  - "Each team switches over separately" is plain and concrete.
  - The callout's number-first opener ("Six to ten weeks is typical...") also breaks the "A [noun] ..." pattern used by the other Block 10 lines.
- **Block 10 step openers stay varied:** Today's / Data map / SugarAI / Duplicate / Quote-to-order / Each.
- **Advisory T7 (optional, not scored).** "backed by" now appears twice in page copy: tile 1 (238), "backed by the global HLB network", and step 6 (275), "backed by our service desk". They sit in different blocks about 35 lines apart, so this is not a defect. If the Content Writer wants to vary it, step 6 could read "Each team switches over separately, supported by our service desk." (10 → 10). Check it against the hub, which uses "support" only as a noun, so there is no frame risk.

## 8. Section structure: PASS

- **Blocks:** all 12 blocks are present in brief Section 3b order (Hero, Stats band, How it works, Workflow, Business case + benefits, Mid CTA, Where teams work, Services, Why HLB HAMT, Process, FAQ, Closing CTA).
- **Headings:** H1 and all "use as written" H2s, H3s and H4s match, including the Block 10 step names and the callout H4.
- **Eyebrows and nav:** they match brief 3b.
- **FAQ:**
  - 5 Q&As, first open, with answers of 31 / 30 / 30 / 30 / 31 words.
  - No inline markers.
  - The JSON-LD instruction (5 visible Q&As, word for word) is present (282).
- **Sources note:** one note, after the FAQ and before the closing CTA (303-311).
- **Internal links:**
  - L1 "SugarAI CRM services" goes to the hub (211).
  - L2 "manufacturers and distributors" goes to /industries/manufacture-and-distribution/ (35).
  - L3 "ERP practice" goes to /services/erp-integration-add-ons/ (244).
  - L4 is omitted (conditional; Flag 8).
- **Breadcrumb parent:** `https://hlbhamt.com/sugarai-crm-2/` (15), per Section 10 point 3.

## 9. Client requirements and transcript: PASS

- **No transcript** was supplied (requirement notes). Nothing is attributed to one.
- **Section 10:**
  - Point 1: "bring your Epicor" framing in the hero and Block 3; no Epicor certification or implementation claim.
  - Point 2: "custom connection" and "custom integration"; no named or resold connector.
  - Point 3: hub parent.
  - Point 4: "Illustrative" captions and mock-up notes; demo wording avoids promising live client data (172, 325).
  - Point 5: Kinetic and "older Epicor ERP versions" only; no Prophet 21, Eclipse or BisTrack.
  - Point 6: N1, N2 and A1 are used; the FSM 8% is not; sales-i is unnamed.
- **Requirement notes:**
  - Primary keyword 4× (within 3-4).
  - 1,655 words (within 1,500-1,700).
  - British spelling and zero em dashes.
  - Prose mixed with limited cards.
  - Image slots through the flow.
  - No plagiarism from the reference sites or deck.
- **Company facts in the changed lines match the hub exactly:** one service desk; six to ten weeks for a sales-only scope; 2.5 to 5 months once ERP integration and data migration are added; phased so early users work before the programme ends. "Each team switches over separately" describes phased go-live in a way consistent with HLB HAMT's own published phasing language: the Insurance lede "phased so your sales team is working before the claims module lands", and the hub "first users are working long before the last".

---

## Overall: PASS

- **Both loop-2 fixes were applied verbatim.** The diff against v2 shows no other change to page copy.
- **The new wording is original.** Neither line echoes the Insurance template, the live hub FAQ, the FSM page, the TCP deck, the reference sites or the wider web. This loop's check covered exactly the failure mode that sank loop 2.
- **All standard checks pass:** 1,655 words; primary keyword 4× and 11 keyword instances in total; 0 em/en dashes and 0 double hyphens; British spelling; 12 blocks in order; 2 card blocks and 4 image slots.
- **All critical checks pass:** 0 TCP material; correct "existing Epicor" positioning with no Epicor-certification claim; all 5 stats and F1 re-verified at source today, with no drift.

The draft is cleared for Deliver. The optional advisories (G5 closing row 3 "Then"; T7 the second "backed by") and Build Flag 13's pending human click-checks can be passed to the Content Writer and Deliver as notes. None of them blocks delivery.

---

Sources consulted today:
- [Nucleus Research Z56](https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/)
- [Avasant, Breaking Down Data Silos](https://avasant.com/report/breaking-down-data-silos-why-crm-integration-is-now-a-boardroom-priority/)
- [Khaleej Times, 10 June 2026](https://www.khaleejtimes.com/business/uae-industrial-exports-hit-dh262b-as-sectors-gdp-contribution-climbs-by-70)
- [01net reprint of the Nucleus SFA Value Matrix 2026 release](https://www.01net.it/sugarcrm-named-a-leader-in-the-nucleus-research-sales-force-automation-technology-value-matrix-2026/)
- Reference sites (fetched):
  - [TCP Sugar-Epicor page](https://www.tcpamericas.com/en/pages/sugar-epicor-integration)
  - [fluenterp Epicor-SugarCRM](https://www.fluenterp.com/en/integrations/epicor-sugarcrm)
  - [SugarAI LinkedIn article](https://www.linkedin.com/pulse/boost-sales-service-epicor-erp-sugarcrm-sugarcrm-42lqf/)
- Exact-phrase web searches on the 4 new-wording phrases listed in L2. None matched.
