# Test report v6: Power BI Services homepage (draft-v6.md, Revision 2 loop 2 + Revision 3)

Tested by: Test agent, 2026-09-29
Loop: **Revision 2, loop 2 of 3** (loop 1 = `test-report-v5.md`). Revision 3 (`inputs/revision-3-notes.md`) is applied on top of brief Sections 1-13 and overrides any brief wording that names a non-Power-BI product.

Inputs checked:
- `brief.md` in full (Sections 12 and 13 override 1-10; Revision 3 overrides named-product wording in all of them).
- `inputs/revision-3-notes.md` in full.
- `draft/draft-v6.md` (page, Sources, Stats used, all 15 Flags) diffed sentence by sentence against `draft/draft-v5.md`.
- `draft/test-report-v5.md` (the 5 required fixes and the accepted deviations).
- Sibling pages and competitor files in `inputs/` (ripgrep for new phrases).
- `output/power-bi-services-homepage.html` (the previous delivery), to check how Deliver renders the Sources list.
- Live Microsoft Learn pages, fetched today: Copilot-for-Power-BI overview (updated 24 Aug 2026) and region availability (updated 25 Sep 2026).

Method:
- No shell was available.
- Every changed sentence was counted by hand. Unchanged sentences keep the v5 counts from test-report-v5.
- Names, keywords, characters, links and footnotes were checked with ripgrep across the whole file. Non-page lines were then excluded (meta, draft header, chrome, structure headers, eyebrows, buttons, URLs, Sources, Stats used, Flags).

---

## Summary

| # | Item | Result |
|---|---|---|
| R3 | Revision 3 name sweep, Fabric stat, reworked FAQs, footnotes | **PASS** (with a Deliver carry-forward, see R3-D) |
| F | The 5 test-report-v5 fixes | **PASS** (all 5 applied verbatim) |
| 1 | Keyword placement and density (incl. B4/B5) | **PASS** |
| 2 | Word count | **PASS** (3,473) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling, punctuation | **FAIL** (1 unclear referent, introduced by the Revision 3 rewording) |
| 5 | Originality | **PASS** |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI-detection heuristics | **FAIL** (FAQ 3 now near-duplicates S5 row 3) |
| 8 | Section structure, links, schema | **PASS** |
| 9 | Client requirements (Revision 2, Section 13, Section 10 corrections, B1-B7, Revision 3) | **PASS**, subject to the Content Writer's calls in the "Content Writer decisions" section |

Headline: Revision 3 is carried out cleanly.
- No banned product name appears in the page copy.
- The 40,000+ Fabric stat is gone, with no substitute.
- The two FAQs that named products read naturally.
- Footnotes are consistent.
- All five v5 fixes are in.

Two sentence-level fixes are needed. Both are side effects of swapping generic wording in for product names. Separately, two of Build's extra removals, plus the region-name call, need the Content Writer's explicit sign-off. Those are decisions, not Build fixes.

---

## R3. Revision 3 checks

### R3-A. Name sweep: PASS

I ran a case-insensitive ripgrep across the whole file for:
- the Revision 3 list: `SAP|Oracle|NetSuite|Salesforce|SugarCRM|Snowflake|BigQuery|Tableau|Qlik|Data Factory|Excel|SharePoint|Outlook|Dynamics|Fabric|Copilot|Azure`
- Build's extras: `Tally|QuickBooks|SQL Server|iOS|Android|Windows|Power Query|Power Automate`
- other product names that could slip in: `Microsoft 365|Office|Google|AWS|Databricks|Looker|Synapse|OneLake|Purview|Entra|Power Apps|Power Platform|OneDrive|PowerPoint|Apple|Mac|Zoho|Odoo|HubSpot|Shopify|Domo|Cognos|MicroStrategy|Xero|OpenAI|ChatGPT|Gemini`

**Page copy: 0 hits.** Every hit is outside the page copy:
- **URLs only:** line 63 (S2b button href, `community.fabric.microsoft.com`), 417 (Source 3 URL), 423 (Source 9 URL `/fabric/admin/`), 424 (Source 10 URL `/copilot-introduction`), 436/442/443 (Stats used URLs), and 379 (the L4 href slug `...-with-power-automate/`).
- **Flags item 4** (lines 481-485), which names the removed products so Test can check them.

**Specific checks:**
- **"Teams":** 5 on-page hits, all the plain noun, not the product: S1 card H3 "Teams on the move" (38, brief-prescribed), "across your teams" (80), "your teams run themselves" (95), "Media teams" (182) and the FAQ H2 "Questions UAE Teams Ask..." (367). A4 "their teams" and A7 "analyst teams" are the same noun.
- **"SugarAI CRM":** 1 on-page hit, the L2 cross-link in S11 tile 4 (335), which is permitted. There is no "SugarCRM".
- **"UAE North (Dubai) / UAE Central (Abu Dhabi)":** S1 deployment line (41), permitted as a judgment call (see Content Writer decision D).
- **Terms kept, correctly:** Power BI Desktop, Power BI Embedded, Pro, Premium Per User, DAX and "on-premises data gateway". These are Power BI's own names or technical terms that brief Section 1 (Tone) requires ("DAX... data gateway"). Gartner is exempt (analyst firm). HLB International is a network.
- **"DSPs, SSPs"** (S6 card 5, line 182) are ad-tech categories. "DSP" is also the name of a competitor consultancy (`inputs/competitor-content/dsp.txt`), but the plural ad-tech use cannot be read as that firm. No action needed; noted for awareness.

### R3-B. Fabric-customers stat removed: PASS

- There is no "40,000", "60%" or adoption figure anywhere on the page (ripgrep `40,000|60%` returns hits only in Stats used and Flags, lines 446 and 499).
- The S5 platform block (140) now has no number at all. "Five or more systems" is the pre-existing source FAQ 14 threshold, also in A3 since v4, not a substitute stat.
- Source 4 is marked retired (418) with the reason. The Stats used note (446) says no substitute was introduced. That is true.

### R3-C. The two reworked FAQs: PASS

- **Q7 "Do we need a data platform beyond Power BI, and when?"** (387) takes the Content Writer's example question word for word.
  - A7 (388) opens "Not always. Power BI handles most departmental reporting on its own." It then gives the same three triggers as v5 and ends HLB-led ("we plan it in stages").
  - "Microsoft's wider data platform, which adds data engineering, warehousing and real-time analytics on a common pool of capacity" describes the product without naming it, and is attributed honestly (B7).
  - It reads as a genuine answer, not a dodge. The "Not always" opener does real work.
- **Q8 "Does Power BI include AI features, and what do we need to use them?"** (390) takes the Content Writer's example word for word.
  - A8 (391) covers what the assistant does, paid capacity, admin enablement, model preparation and English-only prompts.
  - "Q&A" and "narrative" are avoided, per the Section 10 and 12.2 checks.
  - It reads naturally.
  - **Accuracy re-checked today against Microsoft Learn:**
    - "Paid Fabric capacity (F2 or higher) or Power BI Premium (P1 or higher)".
    - "A Power BI Pro or Premium Per User (PPU) license alone isn't sufficient; Copilot requires organizational capacity".
    - "multilingual use isn't officially supported at this time".
  - "It runs only on paid capacity, a higher-tier licence bought for the whole organisation; Pro and Premium Per User on their own are not enough" is a fair generic rendering of "organizational capacity".
  - **Admin step:** Learn says Copilot is "enabled by default", **but** "if your tenant or capacity is outside the United States or EU data boundary, Copilot is disabled by default unless your Fabric tenant admin enables" cross-geo processing. UAE tenants fall in that group, so A8's "A tenant administrator must also switch it on" is accurate for this page's audience.
  - **Flag required by revision-3-notes.md:** the precise capacity tiers (F2+ / P1+) had to be dropped under the no-tool-names rule. A8 is still accurate, but less precise than v5.
- **FAQ 6 (385):** "Outside the US and EU data boundaries, Power BI's AI assistant stays off unless an admin allows cross-region processing" matches the Learn wording above.

### R3-D. Footnote and source consistency: PASS (one Deliver carry-forward)

- **On-page markers, in order** (ripgrep `\[\d+\]`): [9] 41 · [1] 47 · [2] 51 · [12] 55 · [3] 61 · [7] 107 · [6] 232 · [12] 338 · [7] 370 · [8] 373 · [11] [9] [10] 385 · [10] 391.
  - Every marker has a Sources entry.
  - Every live entry (1-3, 6-12) is used.
  - [4] and [5] appear nowhere on the page.
  - This matches Build's list (448).
- **Build's URL claim is accurate:**
  - Product names survive only inside four URLs: S2b href and Source 3 (`community.fabric...`), Source 9 (`/fabric/admin/region-availability`) and Source 10 (`/copilot-introduction`).
  - These are Microsoft's canonical URLs and cannot be changed.
  - Source 9 was re-fetched today (updated 25 Sep 2026) and still shows "UAE Central ... Power BI only region" and "UAE North ... All Fabric workloads ✅".
  - The source **descriptions** were rewritten generically and contain no banned name: "cloud region availability for Power BI and Microsoft's data platform"; "overview of the generative AI assistant in Power BI". They are paraphrases, not quoted titles, which is honest.
- **Carry-forward for Deliver (mandatory, not a Build fix): the risk of leaking names at render time is real.** The previous delivery rendered raw URLs as visible link text and quoted the Microsoft page titles:
  - `output/power-bi-services-homepage.html` line 883: `Microsoft Learn, "Fabric region availability" ... >https://learn.microsoft.com/en-us/fabric/admin/region-availability</a>`
  - line 890: `"Copilot for Power BI" overview ... >https://learn.microsoft.com/.../copilot-introduction</a>`

  If Deliver repeats that pattern, "Fabric" and "Copilot" will be visible on the page. Deliver must:
  1. use the v6 descriptions as the link text, with URLs in `href` only;
  2. not restore the quoted Microsoft page titles.

  The same output file also still contains "Excel and SharePoint sources" (590) and "Azure Data Factory pipelines" (685), confirming Build's Flag 15: every output file must be regenerated from v6 or later, not patched.

---

## F. Verification of the 5 test-report-v5 fixes: PASS

| Fix | Required | v6 (line) | Result |
|---|---|---|---|
| 4a | S4 lede opens "That combination anchors our digital transformation and analytics services..." | "That combination anchors our [digital transformation and analytics services](https://hlbhamt.com/services/digital-transformation-uae/), where we build self-service BI ecosystems on figures your finance team has already approved." (71) | Pass. L1 anchor and target unchanged. |
| 4b | S11 tile 3 "Begin with the fixed-price PowerUP! or a working dashboard on your data, then scale once it proves itself." | Identical (332) | Pass (18 words) |
| 4c | S6 card 3 tagline "onwards" | "Units, brokers and collections tracked from EOI onwards" (169) | Pass. Ripgrep `onward\b` finds nothing on the page (only line 461, in Flags). |
| 5 | S11 tile 1 "We supply your licences, and our own staff handle everything from data engineering to aftercare." | Identical (326) | Pass. No [service list] + deliver + in-house/locally frame remains. |
| 7 | S6 backs 1, 3 and 5 no longer open "We + verb" | 1: "Group P&L, balance sheet and cash flow roll up..." (158); 3: "Dashboards cover expressions of interest..." (170); 5: "CRM, e-commerce and campaign data meet in a 360-degree customer view..." (182). Backs 2/4/6 still open "We track / We help / We align". | Pass. 3 of 6 now open with "We". HLB HAMT is still the actor in each card ("Our chartered accountants design", "We land", "from which we report"). Lengths are 45 / 44 / 42, the same as v5. |

---

## 1. Keyword placement and density: PASS

On-page copy only (brief Section 2a).

| Keyword | Count | Placements (line) | Target | Result |
|---|---|---|---|---|
| "Power BI service" singular | **6** | H1 (22); hero lede (24); S4 card 1 (74); S5 row 2 H3 (106); Q1 (369); A1 once (370) | 5-7 (max 8) | Pass |
| "Power BI Services" plural | **3** | S7 H2 (198); S11 H2 (321); S15 body (403). The S1 eyebrow (20) is excluded, as accepted in v5. | 2-3 | Pass. No section has both forms. |
| "Power BI consulting company" | **2** | S4 lede (71); S11 intro (323) | 1-2 | Pass |
| "Power BI solutions expert" | **2** | S10 Extend (302); S13 body (359) | 1-2 | Pass |
| "Certified Power BI Partner in UAE" | **0** | not placed | 0 (Section 13) | Pass |

**Branding:**
- **B4 "HLB HAMT": 12** (range 10-16). Lines 22, 24, 51, 61, 71, 89, 91, 198, 263, 321, 347, 397. Eyebrows (20, 67, 319) and structure headers (65, 194, 317) are excluded.
- **B5 "Microsoft": 6** (cap 12). This confirms Build's figure. Lines 41 (regions), 61 (Gartner), 91 (app ecosystem), 373 (list prices), 385 (audit scope), 388 (vendor's data platform). The line 63 button is excluded. Every use is vendor attribution, as Revision 3 allows.

**Other checks:**
- **Meta title and description:** identical to brief Section 7 and free of banned names.
- **First 100 words:** the primary keyword is in the H1 and lede sentence 1.
- **Stuffing caps:**
  - "Power BI" (any form) on the page = **50** (cap 75). Buttons (26, 361) and the eyebrow are excluded.
  - "UAE" = **10** (cap 12): 22, 41 x2, 55, 83, 164, 321, 325, 367, 384.
- **Titles containing "Power BI":** S7 0 of 6, S9 0 of 5.

## 2. Word count: PASS (3,473)

Counted under the brief Section 1 rule. The S5 labels "Capability", "Key capabilities" and "Platform layer" are excluded, as in v5.

| Section | v5 (Test) | Change in v6 | v6 (Test) | Build | Budget (12.4) | Status |
|---|---|---|---|---|---|---|
| S1 | 189 | card 3 -1 ("on their phones"); deployment line +1 | 189 | 189 | 150-190 | OK |
| S2 + S2b | 80 | S2b -3 ("and Fabric", "Microsoft" dropped) | 77 | 77 | 45-70 | Over; accepted in v5 (content floor 73). S2b alone = 27, inside 12.5's 25-35. |
| S4 | 271 | lede +1 (fix 4a) | 272 | 272 | 260-310 | OK |
| S5 | 393 | intro +2; row 3 -3; platform H3 +1; body +3 | 396 | 396 | 380-440 | OK |
| S6 | 385 | 0 | 385 | 385 | 340-410 | OK |
| S7 | 410 | item 02 -2; item 05 H3 +1, body +5 | 414 | 414 | 380-440 | OK |
| S8 | 26 | 0 | 26 | 26 | 20-30 | OK |
| S9 | 153 | 0 | 153 | 153 | 150-190 | OK |
| S10 | 402 | Support item 4 H3 +1, body +3 | 406 | 406 | 360-420 | OK |
| S11 | 151 | tile 3 +1 | 152 | 152 | 150-190 | OK |
| S12 | 36 | 0 | 36 | 36 | 30-45 | OK |
| S13 | 29 | 0 | 29 | 29 | 20-30 | OK |
| S14 | 915 | A3 -5; A4 -3; A6 -1; Q7 +1; A7 -1; Q8 +4; A8 +1 | 911 | 914 | 780-920 | OK |
| S15 | 27 | 0 | 27 | 27 | 20-30 | OK |
| **Total** | **3,467** | **+6** | **3,473** | ~3,476 | 3,100-3,500 (fail <2,900 or >3,750) | **PASS** |

**Changed sub-units, all in range:**
- S5 intro 57 (45-60); row 3 description 40 (35-45); row 4 description 43; platform body 59 (45-60).
- S7 item 02 55, item 05 62 (55-65).
- S11 tiles 15 / 17 / 18 / 17 / 16 / 17 (10-18).
- FAQ answers 75 / 82 / 72 / 76 / 71 / 88 / 84 / 84 / 77 / 77 (65-90).

**Quality of the reworked sections, judged on content rather than budget:**
- **The platform block (140) still does its job.** It shows the readiness assessment, the lakehouse trigger, the Bronze/Silver/Gold refinement and the "one trusted set of tables" outcome, and it opens HLB-led. It is no thinner for losing the stat.
- **S7 item 05 (215) keeps all four brief units:** migration (logic kept, visuals redesigned), off-spreadsheet moves, Embedded, and staged platform readiness.

**The fixes below net +3** (page ≈ 3,476; S1 188; S14 915). Both stay inside every ceiling.

## 3. Zero em dashes: PASS

Whole-file ripgrep: `—` **0**, `–` **0**, `--` **0**.

## 4. Grammar, spelling, punctuation: FAIL

| # | Location | Text | Problem | Fix |
|---|---|---|---|---|
| **4a** | S1 deployment line, sentence 2 (line 41) | "Dubai hosts **the full data platform**; Abu Dhabi supports Power BI only." | **Unclear referent, created by the Revision 3 swap.** "The full data platform" is the page's first use of "data platform". The definite article points back to nothing. Thirty words later, S2 item 3 (55) uses the same noun for something else: HLB HAMT "also builds **your data platform**". A reader can take S1 to mean that HLB HAMT's platform, or theirs, is hosted only in Dubai. v5's "every Fabric workload" was precise; the generic substitute is not. This is the same class of error as v5 fix 4a (an "It" with no clear antecedent). | See Fix 4a. |

**Checked and clean:**
- Every new or changed sentence was read: S1 card 3, S2b, S5 intro, rows 1/3/4, platform H3/body/bullets, S7 02 and 05, S10 Support item 4, S11 tiles 1 and 3, A1-A4, A6-A8.
- "A free, installable application" (A1) uses coordinate adjectives correctly.
- "It runs only on paid capacity, a higher-tier licence bought for the whole organisation; Pro and..." has a correct appositive and semicolon.
- A7's three "once..." clauses are parallel.
- **British spelling:** "organisation", "licence" as a noun (A8, S10), "analyse", "optimised", "cleansing". The only `-ization` hits are inside the L7 and Source URLs (153, 416, 433, 509). "Right-sizing" is not a US spelling.

**Style advisories (not scored):**
- A1 "a free, installable application" is slightly stiff. Optional: "a free application you install on your computer" (+4; A1 79). This only applies if the Content Writer accepts decision B below.
- S2b (61) "HLB HAMT builds on Power BI. Microsoft was named a Leader..." leaves the reader to infer that Microsoft is Power BI's vendor. Optional: "HLB HAMT builds on Microsoft Power BI." (+1; "Microsoft" 7, cap 12; "Microsoft Power BI" is Power BI itself, so Revision 3 allows it).

## 5. Originality: PASS

- **New sentences vs sibling pages, competitors and SugarAI:** ripgrep across `inputs/` for "departmental reporting", "single environment", "productivity and business apps", "other BI tools", "unified data platform", "beyond Power BI", "higher-tier", "plain-language questions", "file shares" and "trusted set of tables" finds hits **only in `revision-3-notes.md`**. They are the Content Writer's own suggested wording, which is prescribed and not a violation.
  - The S5 intro echoes the partner page's "connects natively to Excel, Azure, Teams..." (partner 624). That page is confirmed for redirect (Section 13 point 1), so freer reuse is allowed, and the product list is gone anyway.
- **S7 item 05, sentence 1** ("We migrate reports from other BI tools to Power BI, carrying your business logic across and redesigning each visual...") keeps the unit order that brief 12.5 and revision-3-notes.md both prescribe ("migration from other reporting tools to Power BI, preserving business logic and redesigning visuals"). It is a brief-level echo, as in v5 5d-2, and not scored.
- **Web search** (distinctive phrases, today): no exact or near match for any of these:
  - "Power BI handles most departmental reporting on its own"
  - "brings data preparation, storage and reporting into a single environment"
  - "answers plain-language questions and drafts written summaries of report pages"
  - "We migrate reports from other BI tools to Power BI"

  Only generic migration guides and Microsoft Learn pages came back.
- **Q7 and Q8** take the revision-3-notes.md example questions verbatim, which is prescribed.

## 6. Stat accuracy: PASS

- **No stat was added, changed or moved.** 200+ [1], 33x [2], Since 1999 [12], Gartner 19th year [3], 7 days [6], $4,500, the FAQ 10 timelines, Pro US$14 / PPU US$24 [8], and HLB International since 2007 [12] all sit exactly as passed in v5. Each appears once, in its assigned slot.
- **[4] is retired with no substitute** (R3-B).
- **The facts touched by the rewording were re-verified today on Microsoft Learn:**
  - **F3, region availability (updated 25 Sep 2026):** "UAE Central: Power BI only region"; "UAE North: All Fabric workloads". S1 (41) and A6 (385) are accurate, but see 4a on the S1 wording.
  - **F4, Copilot overview (updated 24 Aug 2026):** F2+/P1+ capacity; Pro/PPU alone not enough; non-English prompts not officially supported; off by default outside the US/EU boundary. A6 and A8 are accurate (R3-C).
- **Nothing invented or misattributed.** "Microsoft's wider data platform" (A7) is attributed to the vendor. S5 row 4's "capacity-based licensing" and A2's "run on capacity-based licensing, priced separately" are accurate generic descriptions of capacity SKUs.
- **Duplicate-stat check:** no new figures, so the v5 cross-project sweep result stands.
- **Bookkeeping:** the Stats used row for "HLB International member since 2007" now reads [12], as v5 advised.

## 7. Human tone / AI-detection heuristics: FAIL

**Stock AI phrases:** none on the page. The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just", "in conclusion", cutting-edge, game-changing, revolutionise, unleash, delve, landscape and ever-evolving. The only hit is "unlock" inside the L4 URL (379).

### Failure

**7a. FAQ 3 now repeats S5 row 3 almost word for word.** Removing the product names left the two sentences with the same frame, the same list order and the same close:

| S5 row 3 description (line 118) | FAQ A3 sentence 2 (line 376) |
|---|---|
| "Our engineers **reach your ERP, CRM, accounting and finance** systems, **cloud** warehouses, spreadsheets, file shares **and REST APIs through** native, **partner-built** and custom **connectors**." | "We **reach your ERP, CRM, accounting and finance** platforms, on-premises databases, **cloud** data warehouses **and REST APIs through** standard and **partner-built connectors**, and write custom connectors for legacy systems nothing else covers." |

- They share a 7-word run ("reach your ERP, CRM, accounting and finance"), plus "and REST APIs through", "partner-built" and "connectors".
- In v5 the two named-system lists differed (A3 had Tally, QuickBooks and SQL Server), which hid the shared frame. With the names gone, a reader who opens FAQ 3 after S5 meets a recycled sentence. That is the templated self-repetition this check exists to catch.
- It is also the same class of issue as v5's 7f (repeated openers across a grid). See Fix 7a.

### Advisories (not scored)

- **"data platform" x11 on the page, and "unified data platform" x3** (S5 platform body 140, S7 item 05 215, S10 Support 313).
  - Each is the one-for-one stand-in for "Fabric", so the phrase recurs wherever the brand did.
  - "Data platform readiness" also appears in two H3s (S5 139, S7 214) and one bullet (142).
  - After Fix 4a the count drops to 10. That is acceptable, because the uses are sections apart.
  - Optional S10 Support body: "Right-sizing licences, administering your tenant and phasing any move to a larger data platform." (15, 0).
- **"Teams on the move" (38)** is brief-prescribed and reads as the common noun. No change needed.

## 8. Section structure, links and schema: PASS

- **Order:** S0-S16 in the 12.2 order, with one H1.
- **S5:** the platform block keeps its H3 plus 4 bullets.
- **S14:** 10 H3 questions in the 12.5 order. Q7 and Q8 are reworded in place, not dropped.
- **S10 Support:** 5 items.
- **Anchor nav (16):** unchanged.
- **Links:**

| Link | Anchor | Target | Location | Result |
|---|---|---|---|---|
| L1 | digital transformation and analytics services | /services/digital-transformation-uae/ | S4 lede (71) | Exact |
| L2 | SugarAI CRM | /sugarai-crm-2/ | S11 tile 4 (335) | Exact |
| L3 | UAE Corporate Tax advisory | /services/corporate-tax-advisory-services-in-uae/ | S6 card 2 (164) | Exact |
| L4 | **Power BI automation** (brief: "...with Power Automate") | /insights/unlocking-power-bi-automation-with-power-automate/ | FAQ 4 (379) | Target unchanged; anchor shortened under Revision 3 (see Build extension 5) |
| L5 | data protection advisory | /services/data-privacy-and-security-uae/ | FAQ 6 (385) | Exact |
| L6 | Power BI dashboard development | /services/power-bi-dashboard-development/ | S7 item 03 (209) | Exact |
| L7 | data visualisation services | /services/data-visualization-uae/ | S6 intro (153) | Exact |
| P2 | advanced analytics services | PLACEHOLDER:/services/advanced-analytics-services/ | S6 card 6 (188) | Exact |

- **In-page links:** "proof of concept" (80) and "above" (286) → #methodology; "PowerUP!" (373) → #packages.
- **Excluded pages:** the partner and consulting URLs appear only in Flags (512), not on the page.
- **Schema:** Service, FAQPage with **10** Q&As (Q4, Q7 and Q8 text changed; Deliver must regenerate from on-page text) and BreadcrumbList. This is still true.

## 9. Client requirements: PASS (subject to the Content Writer decisions below)

- **Revision 3:** all 11 affected locations in revision-3-notes.md were handled as specified:
  - S5 intro, row 3 and platform block
  - FAQ 7 and FAQ 8
  - S7 item 05 and item 02
  - the S10 Support tab
  - S2b
  - S1 regions (kept)
  - the SugarAI link (kept)

  The S2b wording follows the notes' example ("We build on Power BI...").
- **Revision 2 / Section 13:**
  - There is still no "certified" or "leading" wording on the page (ripgrep `(?i)certif|leading` hits only Flags, 492 and 498).
  - S11 tile 1 is still "Power BI reselling partner in the UAE".
  - AI Insights stays removed. AI-assistant content appears only in FAQ 6 and FAQ 8.
  - B1-B7 all hold:
    - B2: every intro opens HLB-led, including S5 "HLB HAMT delivers...".
    - B3: every answer has an HLB/"we" sentence. A3 "We reach"; A7 "we plan it in stages"; A8 "which we prepare", "we put Arabic into report design".
- **Section 10 #7 corrections still hold:**
  - There is no "Gartner #1", "ranked" or "14+".
  - There is no Arabic AI-prompt claim.
  - There is no "Q&A" feature.
  - There is no Windows mobile claim.
  - There is no "Salesforce (60+ modules)".
  - There is no competitor price comparison.
  - Tableau and Qlik are no longer named at all. Revision 3 supersedes 10 #7 on that point.
- **Section 4 connector caveat:** met trivially now that no system is named. Fix 7a makes it explicit ("Where a standard or partner-built connector exists...").

---

## Evaluation of Build's 5 extensions beyond the literal Revision 3 list

Revision 3's rule is "any other tool names", clarified as "all named software/products" plus "Microsoft's own related product names". Its precedence clause says that where the brief gave exact wording with a now-banned name, it should be rewritten "to the same intent using generic language".

| # | Build's change | Verdict | Reasoning |
|---|---|---|---|
| 1 | **iOS and Android removed:** S1 card 3 "on their phones" (39); S5 row 4 "on phones and tablets" (129); bullet "Power BI mobile apps" (131) | **Needs Content Writer sign-off.** Test leans towards accepting it. | iOS and Android are operating systems from Apple and Google. They are not BI competitors, not source systems and not Microsoft products, so they fall outside both clarified categories. This change also goes a step past a correction the Content Writer explicitly approved (Section 10 #7: "mobile is iOS and Android only"). Nothing becomes inaccurate: the Windows error is not reintroduced, and "phones and tablets" is true. But a buyer loses the platform fact. Restore cost: S1 card 3 "on iOS or Android" (+1; S1 = 189 after Fix 4a); S5 row 4 "on iOS and Android" (0); bullet "iOS and Android apps" (0). |
| 2 | **"Windows" removed from A1:** Desktop is now "a free, installable application" (370) | **Needs Content Writer sign-off.** Test leans towards accepting it. | Windows is a Microsoft product, so by analogy it falls under Revision 3 point 2 (Microsoft's own product names). But it carried a buyer-relevant fact recorded in F1: Desktop is Windows-only, which matters to teams on Macs. FAQ 1 is exactly where that question arises. The answer is not wrong now, only less informative. Restore cost: "a free Windows application" (0). A generic middle ground that keeps some of the fact: "a free application installed on a PC" (+3; A1 78). |
| 3 | **"Power Query data shaping" bullet → "Data shaping and cleansing"** (100) | **Accept. Within the rule; no sign-off needed.** | Power Query is a separately branded Microsoft engine (also in Excel and dataflows), not a "Power BI"-named component. That puts it in category 2. The bullet keeps its meaning and its 4-word length, so no content is lost. DAX and "data gateway" are correctly kept: they are technical terms the brief's tone rule names, not products. |
| 4 | **Tally, QuickBooks and SQL Server removed from A3** | **Accept. Squarely within the rule; this was required, not an extension.** | These are the same class as the listed SAP/Oracle/NetSuite: named source systems used as connector examples. SQL Server is also a Microsoft product (category 2). The generic replacements ("accounting and finance platforms", "on-premises databases") keep the coverage. |
| 5 | **L4 anchor "Power BI automation with Power Automate" → "Power BI automation"** (379) | **Accept. Within the rule; no sign-off needed** (FYI to the Content Writer). | Power Automate is a Microsoft product (category 2). revision-3-notes.md says banned names in brief-prescribed wording (here 12.9 L4) must be rewritten generically. The target URL is unchanged. The anchor still describes the linked article accurately and stays descriptive for SEO. The `power-automate` slug sits in the href only. |

**Also needing the Content Writer's decision (flagged by revision-3-notes.md itself):**
- **D. UAE North (Dubai) / UAE Central (Abu Dhabi) region names in S1 (41).**
  - Test agrees with keeping them. They are data-centre region names, not products, and they carry the page's in-country residency claim, which was verified today.
  - Fallback if overruled: "in Microsoft's Dubai or Abu Dhabi cloud region" (-4; S1 184 after Fix 4a).
- **E. Precise Copilot capacity tiers dropped from A8.** The notes asked for this to be flagged. The page no longer tells readers which capacity tier (F2+/P1+) they need, only "paid capacity, a higher-tier licence". This is accurate, but less actionable. No action is needed unless the Content Writer wants it back, and it cannot come back without the banned name.

---

## Overall: FAIL (loop 2 of 3, Revision 2)

Items 4 and 7 fail, with one fix each. Everything else passes, including all Revision 3 requirements and all five v5 fixes. Both failures are side effects of the generic wording Build substituted, and both fixes are drop-in sentence edits. **Change nothing else.**

### Needs a Build fix (required for PASS)

**Fix 4a: S1 deployment line, sentence 2 (line 41).**
- Replace "Dubai hosts the full data platform; Abu Dhabi supports Power BI only." with:
  > "Dubai runs every data workload; Abu Dhabi supports Power BI only."
- Word count: 11 (-1). S1 becomes 188.
- This restores v5's precision without the brand name, and it removes the clash with S2 item 3's "your data platform".
- If you write your own wording:
  - do not use "data platform";
  - do not name any product;
  - do not add a "Microsoft" that pushes S1 past 190 words.

**Fix 7a: FAQ A3, sentence 2 (line 376).**
- Replace "We reach your ERP, CRM, accounting and finance platforms, on-premises databases, cloud data warehouses and REST APIs through standard and partner-built connectors, and write custom connectors for legacy systems nothing else covers." with:
  > "Where a standard or partner-built connector exists, we use it, and we write custom connectors for legacy systems that have none. That covers accounting packages, ERP and CRM platforms, on-premises databases, cloud warehouses and REST APIs."
- Word count: 36 (+4). A3 becomes 76 (65-90) and S14 becomes 915 (cap 920).
- Keep "Most of them." before it. Keep the rest of A3 unchanged ("A warehouse is not always step one..." onward).
- B3 still holds ("we use it", "we write", "we recommend").
- The Section 4 connector caveat is now explicit.
- If you write your own wording, it must not share S5 row 3's frame: "[We/Our engineers] reach your ERP, CRM, accounting and finance ... through ... connectors".
- Alternatively, rewrite S5 row 3 instead, under the same constraint and within 35-45 words.

**After both fixes:**
- **Totals:** page ≈ **3,476**, S1 188, S14 915.
- **Unchanged counts:** keywords (6 / 3 / 2 / 2 / 0), "HLB HAMT" 12, "Microsoft" 6, "UAE" 10, "Power BI" 50. Links, stats and footnotes are also unchanged.
- **Banned names:** neither fix text contains a banned product name.
- **Optional:** the advisories in items 4 and 7 are optional.

### Needs the Content Writer's decision (not Build fixes; do not block on Build)

1. **Extension 1 (iOS/Android removal):** sign-off needed. Test leans towards accepting it. Restore wording is given above.
2. **Extension 2 (Windows removal in A1):** sign-off needed. Test leans towards accepting it, or using the "installed on a PC" middle ground.
3. **D (UAE North/UAE Central region names kept):** confirm or overrule, as revision-3-notes.md asks.
4. **E (Copilot capacity tiers dropped from A8):** awareness only.
5. **Extensions 3, 4 and 5 (Power Query, Tally/QuickBooks/SQL Server, L4 anchor):** accepted as within the rule. FYI only.

If the Content Writer overrules extension 1, extension 2 or D, Build applies the one-line restores listed above in the same v7 pass as Fixes 4a and 7a. Every restore keeps each section inside its budget.

### Carry to Deliver (from this report)
- Render Source link text from the v6 descriptions, with raw URLs in `href` only. Do not restore the quoted Microsoft page titles ("Fabric region availability", "Copilot for Power BI"). Otherwise "Fabric" and "Copilot" become visible (R3-D; evidence: `output/power-bi-services-homepage.html` lines 883 and 890).
- Regenerate every output file (HTML, DOCX, PDF, insurance-format DOCX, sources log) and the FAQPage schema from the passing draft. The current outputs still show "Excel and SharePoint sources" (HTML 590) and "Azure Data Factory pipelines" (HTML 685).

---

Sources consulted for verification:
- [Copilot for Power BI overview, Microsoft Learn (updated 24 Aug 2026)](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction): capacity F2+/P1+, Pro/PPU insufficient, English-only prompts, off by default outside the US/EU boundary
- [Fabric region availability, Microsoft Learn (updated 25 Sep 2026)](https://learn.microsoft.com/en-us/fabric/admin/region-availability): UAE Central Power BI-only; UAE North all workloads
- Web originality searches (no matches): "Power BI handles most departmental reporting on its own"; "brings data preparation, storage and reporting into a single environment"; "answers plain-language questions and drafts written summaries of report pages"; "We migrate reports from other BI tools to Power BI"
