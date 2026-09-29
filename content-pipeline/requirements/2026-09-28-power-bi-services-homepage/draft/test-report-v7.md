# Test report v7: Power BI Services homepage (draft-v7.md, Revision 2 loop 3 of 3 + Revision 3)

Tested by: Test agent, 2026-09-29
Loop: **Revision 2, loop 3 of 3 (final).** Loop 1 = `test-report-v5.md` (FAIL, 5 fixes), loop 2 = `test-report-v6.md` (FAIL, 2 fixes). Revision 3 (`inputs/revision-3-notes.md`) applies on top of brief Sections 1-13.

Inputs checked:
- `brief.md` in full (Sections 12 and 13 override 1-10; Revision 3 overrides any named-product wording).
- `inputs/revision-3-notes.md` in full.
- `draft/draft-v7.md` in full (page, Sources, Stats used, all 16 Flags), diffed line by line against `draft/draft-v6.md` lines 1-410.
- `draft/test-report-v6.md` and `draft/test-report-v5.md` (fixes, accepted deviations, count conventions).
- Sibling pages and competitor files in `inputs/` (ripgrep for new phrases).
- `output/power-bi-services-homepage.html` (previous delivery; rendering check only).
- Live pages fetched today: Microsoft Learn region availability (ms.date 25 Sep 2026), Microsoft Learn Copilot-for-Power-BI overview (ms.date 24 Aug 2026), Microsoft Power BI pricing page, and the mwpro.co.uk verbatim repost of Microsoft's Gartner announcement.

Method:
- No shell was available. Names, keywords, characters, links and footnotes were checked with ripgrep across the whole file, then non-page lines were excluded (meta, draft header, chrome, structure headers, eyebrows, buttons, URLs, Sources, Stats used, Flags).
- **Word count was recounted from scratch this loop, not carried over.** I transcribed the counted copy of every section into separate scratch files and counted whitespace-delimited tokens with ripgrep (offset probing), so every section total below is a fresh machine count.

Standing Content Writer decisions respected (not flagged): the iOS/Android removal (S1 card 3, S5 row 4 and bullet) and the Windows removal from FAQ A1 are **approved and intentional**, per the Content Writer.

---

## Summary

| # | Item | Result |
|---|---|---|
| V | Loop-2 fixes (4a S1 deployment line, 7a FAQ A3) applied correctly, nothing else changed | **PASS** |
| R3 | Revision 3 full name sweep, URLs not rendered as visible text in the draft | **PASS** (Deliver carry-forward, see R3-B) |
| 1 | Keyword placement and density, branding B1-B7, stuffing caps | **PASS** |
| 2 | Word count | **PASS** (3,477; 3,471 without the two PowerUP! column labels) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** |
| 5 | Originality | **PASS** |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI-detection heuristics | **PASS** |
| 8 | Section structure, AI Insights removal and renumbering, internal links, schema | **PASS** |
| 9 | Client requirements (Revision 2, Section 13, Section 10 corrections, Revision 3) | **PASS** |

---

## V. Verification of the two test-report-v6 fixes: PASS

**Diff result:** comparing v7 against v6 line by line (lines 1-410), the page copy differs in **exactly two lines**: 41 and 376. Lines 5 and 7 (draft title and header note) also changed, but they are not page copy. Nothing else in the page copy changed.

| Fix | Required (test-report-v6) | v7 text | Result |
|---|---|---|---|
| 4a | S1 deployment line, sentence 2: "Dubai runs every data workload; Abu Dhabi supports Power BI only." | Line 41: "We set up your environment so data can stay in-country, in Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud region. Dubai runs every data workload; Abu Dhabi supports Power BI only. [9]" | **Pass.** Verbatim. The line is 33 words (22 + 11; 12.5 budget is 25-35) and S1 is 188 (cap 190). "Data platform" now first appears in S2 item 3 ("also builds your data platform"), so the unclear referent is gone. The fact is re-verified today (see item 6). No product name added. |
| 7a | FAQ A3, sentence 2 replaced with "Where a standard or partner-built connector exists, we use it, and we write custom connectors for legacy systems that have none. That covers accounting packages, ERP and CRM platforms, on-premises databases, cloud warehouses and REST APIs." | Line 376: "Most of them. Where a standard or partner-built connector exists, we use it, and we write custom connectors for legacy systems that have none. That covers accounting packages, ERP and CRM platforms, on-premises databases, cloud warehouses and REST APIs. A warehouse is not always step one. ..." | **Pass.** Verbatim. "Most of them." kept, and the rest of A3 is unchanged. A3 = 76 words (3 + 21 + 15 + 7 + 9 + 21; range 65-90). B3 holds ("we use it", "we write", "we recommend"). The 7-word shared frame with S5 row 3 ("reach your ERP, CRM, accounting and finance ... through ... connectors") is gone. The longest remaining shared run is "and REST APIs" (3 words), which is a generic list item. |

**Did the fixes break anything else?** No:
- "data platform" on the page is now 10 (55, 139, 140, 142, 214, 215, 312, 313, 387, 388), none in S1.
- The keyword, branding, "UAE", "Power BI" and footnote counts are unchanged from v6 (see item 1).
- A3's "custom connectors for legacy systems" also appears in S7 item 02 (206: "writing custom connectors for legacy systems"). That run already existed in v6's A3. Brief 12.5 FAQ 3 explicitly allows the dashboard-page phrase ("'Custom connectors for legacy systems' (dashboard page) may be added"), and it is under the 8-word reuse limit. Not a finding.

---

## R3. Revision 3 name sweep: PASS

### R3-A. Page copy: 0 banned names

I ran case-insensitive ripgrep across the whole file for:
- **The full Revision 3 list:** `SAP|Oracle|NetSuite|Salesforce|Sugar|Snowflake|BigQuery|Tableau|Qlik|Data Factory|Excel|Teams|SharePoint|Outlook|Dynamics|Fabric|Copilot|Azure`
- **Wider sweep:** `Tally|QuickBooks|SQL|iOS|Android|Windows|Power Query|Power Automate|Microsoft 365|Office|Google|AWS|Databricks|Looker|Synapse|OneLake|Purview|Entra|Power Apps|Power Platform|OneDrive|PowerPoint|Apple|Mac|Zoho|Odoo|HubSpot|Shopify|Domo|Cognos|MicroStrategy|Xero|OpenAI|ChatGPT|Gemini|Slack|Zapier|Jira|Workday|Sage|Dropbox|Adobe`

**Every hit, classified:**
- **"Sugar" on the page:** only line 335, S11 tile 4, the permitted "[SugarAI CRM](https://hlbhamt.com/sugarai-crm-2/)" cross-link (L2). "SugarCRM" appears nowhere. Line 137, "mirrors the SugarAI 'AI Layer'", is a structure note for Deliver, not page copy.
- **"Teams":** 38 "Teams on the move" (brief-prescribed card title), 80 "across your teams", 95 "your teams run themselves", 182 "Media teams", 367 FAQ H2 "Questions UAE Teams Ask...", 379 "their teams" and 388 "analyst teams". All seven are the plain noun, not the product.
- **"Excel":** only lines 426 and 434, inside "Unwavering **Excel**lence" (Source 12 title and URL). That is the word "excellence", not the product. `\bExcel\b` has 0 hits.
- **False substrings, not names:** "Office" (174/180/186, Chief ... Officer); "entra" (41/295/385, Central/central); "sage" (107/113, usage).
- **URL strings only:** 63 (S2b button href, `community.fabric.microsoft.com`), 379 (L4 href slug `...-with-power-automate/`), 417 (Source 3), 422 (Source 8, `/power-platform/`), 423 (Source 9, `/fabric/`), 424 (Source 10, `/copilot-introduction`), and the Stats used rows 436/442/443.
- **Flags only (not page copy):** lines 465, 481-486, 505 and 516.

**Terms confirmed as allowed:**
- **Power BI's own names:** Power BI Desktop, Power BI Embedded, Pro, Premium Per User.
- **Technical terms the tone rule requires:** DAX, "on-premises data gateway".
- **Region names:** "UAE North (Dubai) / UAE Central (Abu Dhabi)". revision-3-notes.md says these may stay.
- **Other exempt names:** Gartner (analyst firm), HLB International (network), and the regulation names IFRS, IAS 12, PDPL, DIFC, ADGM, ISO/IEC 27001 and SOC 2.
- **"DSPs, SSPs":** generic ad-tech categories.

### R3-B. URLs are not rendered as visible link text in the draft: PASS (Deliver carry-forward)

**In the page copy, no URL is visible text:**
- All 8 inline links use descriptive anchors: 71, 153, 164, 188, 209, 335, 379 and 385.
- The S2b button label is "Read Microsoft's announcement", with the forum URL as its target only (63).
- The in-page links are "proof of concept" (80), "above" (286) and "PowerUP!" (373).

**The Sources list is where the risk sits.** The draft lists each source as "description: raw URL". The descriptions themselves are clean:
- Source 3: "Microsoft, 'Microsoft named a Leader in the 2026 Gartner Magic Quadrant for Analytics and BI Platforms' (Power BI Updates Blog)"
- Source 8: "Microsoft Power BI pricing update and pricing page"
- Source 9: "Microsoft Learn, cloud region availability for Power BI and Microsoft's data platform"
- Source 10: "Microsoft Learn, overview of the generative AI assistant in Power BI"

**Evidence that the carry-forward is necessary:** the previous delivery rendered raw URLs as visible anchor text. `output/power-bi-services-homepage.html` shows the following as visible text:
- line 883: `>https://learn.microsoft.com/en-us/fabric/admin/region-availability</a>`
- line 886: `>https://community.fabric.microsoft.com/...</a>`
- line 890: `>https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction</a>`
- line 892: `>https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing</a>`

**Bookkeeping gap in Build's Flags item 6:** it lists the S2b, Source 3, Source 9, Source 10 and L4 URLs, but **omits Source 8** (`/power-platform/`, a Microsoft product-family name). This does not fail the draft, because the URL is a citation string and the Deliver rule already covers every source. Deliver should apply the rule to Source 8 as well (see Carry to Deliver).

---

## 1. Keyword placement and density: PASS

On-page copy only (brief Section 2a). Ripgrep has no look-ahead, so "Power BI service" hits were classified by hand for a following "s".

| Keyword | Count | Placements (line) | Target (12.6) | Result |
|---|---|---|---|---|
| "Power BI service" singular | **6** | H1 (22, "Power BI Service Partner", the compound-noun exception); hero lede sentence 1 (24); S4 card 1 (74); S5 row 2 H3 (106); FAQ Q1 (369); FAQ A1, once (370) | 5-7 (max 8) | Pass |
| "Power BI Services" plural | **3** | S7 H2 (198); S11 H2 (321); S15 body (403). The S1 eyebrow (20) is excluded, as accepted since v5. | 2-3 | Pass. No section contains both forms. |
| "Power BI consulting company" | **2** | S4 lede (71); S11 intro (323) | 1-2 | Pass |
| "Power BI solutions expert" | **2** | S10 Extend (302); S13 body (359) | 1-2 | Pass |
| "Certified Power BI Partner in UAE" | **0** | not placed | 0 (Section 13 #2) | Pass |

**Placement checks:**
- **Meta title** (line 1): "Power BI Service & Consulting Partner in the UAE | HLB HAMT". It is identical to brief Section 7 and leads with the primary keyword.
- **Meta description** (line 2): identical to brief Section 7 ("Power BI service from HLB HAMT: ..."). The primary keyword is the first three words.
- **H1 and first 100 words:** the primary keyword is in the H1 and in hero lede sentence 1 ("HLB HAMT designs, builds and runs your Power BI service").

**Branding (12.3a):**
- **B1:** the H1 opens "HLB HAMT:". Pass.
- **B2:** every required opening sentence is HLB-led. Pass.
  - Hero lede "HLB HAMT designs"; S4 "HLB HAMT is"; S5 "HLB HAMT delivers"; S6 "Our consultants begin"; S7 "We handle"; S9 "We prove"; S10 "We offer"; S11 "We expect".
- **B3:** every FAQ answer has an HLB/"we" sentence. Pass.
  - A1 "We set up both"; A2 "we advise"; A3 "we use it"; A4 "we set alerts"; A5 "We design"; A6 "We configure"; A7 "we plan it in stages"; A8 "which we prepare"; A9 "We work through"; A10 "HLB HAMT confirms".
- **B4 "HLB HAMT": 12** (range 10-16). Pass.
  - Counted at lines 22, 24, 51, 61, 71, 89, 91, 198, 263, 321, 347 and 397.
  - Excluded: eyebrows (20, 67, 319), structure headers (65, 194, 317), meta and Flags.
- **B5 "Microsoft": 6** (cap 12). Pass.
  - Counted at lines 41 (regions), 61 (Gartner), 91 (app ecosystem), 373 (list prices), 385 (audit scope) and 388 (vendor's data platform).
  - The S2b button (63) is excluded.
- **B6:** none of the retired framings appear. Pass.
  - No "Microsoft Power BI" eyebrow.
  - No "Why Power BI: From Raw Data...".
  - No "Power BI is Microsoft's...".
  - No "Microsoft Power BI PowerUP!".
  - No bare "Microsoft: named a Leader". S2b opens "HLB HAMT builds on Power BI."
- **B7:** attribution is honest. Pass.
  - The Gartner Leader recognition is attributed to Microsoft.
  - 200+ is Power BI's connector library ("we configure yours and build missing ones").
  - The regions are "Microsoft's".
  - No certified claim.

**Stuffing caps:**
- **"Power BI" (any form) on the page = 50** (cap 75; flag above 85). Hits were listed by line and hand-tallied; buttons (26, 361), the eyebrow (20) and structure headers are excluded.
- **"UAE" = 10** (cap 12): 22, 41 x2, 55, 83, 164, 321, 325, 367 and 384.
- **Titles containing "Power BI":** S7 items 0 of 6 (max 2); S9 steps 0 of 5 (max 1).
- No singular/plural in the same section. No awkward repetition of any secondary keyword.

## 2. Word count: PASS (3,477)

Counted fresh under the brief Section 1 rule, using the same conventions as test-report-v5/v6:
- **Included:** H1, H2s, H3s, ledes, card, tile and strip text, the 12 pills plus the pill-row label, tab names, the "Limited offer" badge, the price line, terms, deliverables, FAQ questions and answers, and CTA headings and bodies.
- **Excluded:** eyebrows, buttons, nav, breadcrumb, form, footnote markers, the Sources list, and the S5 structural labels ("Capability", "Key capabilities", "Platform layer").

| Section | v7 (fresh machine count) | v6 (Test) | Budget (12.4) | Status |
|---|---|---|---|---|
| S1 | **188** | 189 | 150-190 | OK (Fix 4a -1) |
| S2 + S2b | **77** | 77 | 45-70 | Over; accepted since v5 (content floor). S2b alone = 27, inside 12.5's 25-35. |
| S4 | **272** | 272 | 260-310 | OK |
| S5 | **396** | 396 | 380-440 | OK |
| S6 | **385** | 385 | 340-410 | OK |
| S7 | **414** | 414 | 380-440 | OK |
| S8 | **27** | 26 | 20-30 | OK (10 + 17; v6's 26 was a one-word hand-count slip) |
| S9 | **153** | 153 | 150-190 | OK |
| S10 | **406** (400 + "What's in scope" / "What you receive" 6) | 406 | 360-420 | OK |
| S11 | **152** | 152 | 150-190 | OK |
| S12 | **36** | 36 | 30-45 | OK |
| S13 | **29** | 29 | 20-30 | OK |
| S14 | **915** | 911 (+4 from Fix 7a = 915) | 780-920 | OK |
| S15 | **27** | 27 | 20-30 | OK |
| **Total** | **3,477** (3,471 without the S10 column labels) | 3,473 | 3,100-3,500 (fail <2,900 or >3,750) | **PASS** |

- Build's self-count (~3,476) agrees within 1 word.
- **Sub-units changed in v7, both in range:**
  - S1 deployment line: 33 words (25-35).
  - FAQ A3: 76 words (65-90).
- **Unchanged sub-units:** as recorded in test-report-v6 and all in range:
  - FAQ answers 75 / 82 / 76 / 76 / 71 / 88 / 84 / 84 / 77 / 77.
  - S7 items 55-65.
  - S11 tiles 10-18.

## 3. Zero em dashes: PASS

Whole-file ripgrep: `—` **0**, `–` (en dash) **0**, `--` **0**. The tables use `:-` separators.

## 4. Grammar, spelling, punctuation: PASS

- **Both changed sentences read correctly:**
  - "Dubai runs every data workload; Abu Dhabi supports Power BI only." Two independent clauses are correctly joined by a semicolon. "Dubai" and "Abu Dhabi" are defined in the preceding sentence's parentheses, so the referents are clear.
  - "Where a standard or partner-built connector exists, we use it, and we write custom connectors for legacy systems that have none." The subordinate clause comes first and the compound predicate is correctly comma-joined. "That covers..." refers back to the whole connector approach, which is clear.
- **Full re-read of every page line (22-403) found no new errors.** Constructions checked and confirmed correct:
  - A2's colon-plus-series.
  - A7's three parallel "once..." clauses.
  - S6 card 4's parallel "help put ... in place, activate ..., and shape ...".
  - A8's appositive plus semicolon.
  - S4 card 4's "each one", which refers to "your requests".
- **British spelling (ripgrep for -ize/-ization/-yze, color, center, program, license, behavior, toward, onward, modeling and similar):**
  - Every `visualization` hit is inside a URL (153, 416, 433, 510).
  - "licensed" (55, 71, 372) is the verb or adjective, which is correct in British English. "Licence" is used as the noun throughout (203, 312, 313, 359, 373, 388, 391).
  - "onward" appears only in Flags (461). The page has "onwards" (169).
  - Confirmed British forms: organisation, optimised, standardised, digitise, monetisation, behaviour, analyse, programme, modelling, cleansing.

## 5. Originality: PASS

- **Local check (ripgrep across all of `inputs/`)** for the two new v7 phrasings ("runs every data workload", "partner-built connector exists", "that have none", "accounting packages", "standard or partner"): **0 hits**.
- **Closest sibling-page material, side by side (not a violation):**

| draft-v7 A3 (376) | power-bi-dashboard-development-extracted.txt 751-753 (live sibling, reuse limit applies) |
|---|---|
| "Where a standard or partner-built connector exists, we use it, and we write custom connectors for legacy systems that have none. That covers accounting packages, ERP and CRM platforms, on-premises databases, cloud warehouses and REST APIs." | "Yes. Power BI integrates with ERP systems, CRM platforms, finance tools, cloud databases, and third-party applications. Custom connectors can also be developed for unique or legacy systems." |

  **Ruling:** not a close paraphrase.
  - The sentence order is reversed, the voice and subject differ (HLB "we" vs Power BI), and the item lists differ.
  - The only shared runs are "CRM platforms" and the "custom connectors ... legacy systems" idea.
  - Brief 12.5 FAQ 3 explicitly permits that idea, and it is under the 8-word limit.
- **Web searches (exact phrases, today):**
  - "Where a standard or partner-built connector exists": no match; only generic Fivetran, Tableau and Boomi connector docs came back.
  - "write custom connectors for legacy systems that have none": no match.
  - "Dubai runs every data workload" + "supports Power BI only": no match. beyondtheanalytics.com states the same Microsoft Learn fact in different words ("UAE Central (Abu Dhabi) and Qatar Central support Power BI only"). The only overlap is the factual 3-4-word label taken from Microsoft's own "Power BI only region" wording, which is not a violation.
  - "so a sold unit counts once, whichever team reports it": no match.
  - "our accountants and engineers make the numbers reconcile": no match. The search summariser attributed it to numeric.io, but I fetched that page and it does **not** contain the phrase or any sentence with both "accountants and engineers" and "reconcile".
  - "The tool is rarely the problem; how the report was built almost always is": no match.
  - "PowerUP! is for organisations sitting on useful data": no match.
- **Prescribed wording, not scored:** the earlier-loop web and local checks (test-report-v5/v6) still hold for the unchanged copy. Q7 and Q8 use the revision-3-notes.md example questions word for word, as prescribed.

## 6. Stat accuracy: PASS

**Every entry in the "Stats used" list checked:**

| Ref | Figure | Location | Check today | Result |
|---|---|---|---|---|
| [1] CS1 | 200+ | S2 item 1 only | Attributed to Power BI's connector library, with HLB configuring and building missing connectors (B7). Consistent with the Microsoft Learn list (~210-220, per brief 6a). | Pass |
| [2] CS2 | 33x | S2 item 2 only | "in one recent HLB HAMT engagement" qualifier present. It is self-published on the live data-viz page, and the Content Writer confirmed it (Section 10 #4). | Pass |
| [12] CS5 | Since 1999; HLB International since 2007 | S2 item 3; S11 tile 5 | Different facts from the same source, each once. No "25 years" on the page (only in the Source 12 title). | Pass |
| [3] S-3 | Leader, 2026 Gartner MQ, 19th consecutive year | S2b only | mwpro.co.uk verbatim repost fetched today: "named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and Business Intelligence Platforms for the nineteenth consecutive year." It is attributed to Microsoft. There is no "#1", "ranked" or "14+". | Pass |
| [6] CS3 | 7 days | S9 H2 only; intro carries "for a defined use case" | ripgrep: "7 Days" appears only at 232 on the page (the meta "7-day" is allowed per 12.6). | Pass |
| (none) | $4,500 PowerUP!, 5 terms, 6 deliverables | S10 featured card only | Matches brief 4 and 12.5; USD confirmed (Section 10 #4). | Pass |
| (none) | Timelines 2-4 wks / 6-10 wks / 3-6 months / prototype in 2 wks | FAQ 10 only | Match the brief and the sibling pages. | Pass |
| [7] F1 | Service vs Desktop | S5 row 2; A1 | Unchanged. Accurate. | Pass |
| [8] F2 | Pro US$14, PPU US$24 | FAQ 2 only | Pricing page fetched today: "$14.00 user/month, paid yearly" and "$24.00 user/month, paid yearly". | Pass |
| [9] F3 | Dubai all workloads; Abu Dhabi Power BI only | S1; A6 | Microsoft Learn (ms.date 2026-09-25) fetched today: "UAE Central ✅ ❌ Power BI only region"; "UAE North ✅ ✅". The v7 wording "Dubai runs every data workload" is a faithful generic rendering of "All Fabric workloads". | Pass |
| [10] F4 | Paid capacity; admin enablement; English prompts; cross-geo default | A6; A8 | Microsoft Learn (ms.date 2026-08-24) fetched today confirms all four points (see list below). | Pass |
| [11] F5 | ISO/IEC 27001 and SOC 2 scope | A6 only | "falls within the scope of ... audits". Not "compliant". | Pass |

The F4 quotes from Microsoft Learn behind the [10] row:
- "Paid Fabric capacity (F2 or higher) or Power BI Premium (P1 or higher)".
- "A Power BI Pro or Premium Per User (PPU) license alone isn't sufficient".
- "multilingual use isn't officially supported at this time".
- "If your tenant or capacity is outside the United States or EU data boundary, Copilot is disabled by default unless your Fabric tenant admin enables..."

**Checks across all stats:**
- **Retired stats:** [4] (Fabric 40,000+) and [5] (73.3%) appear nowhere on the page. ripgrep for `40,000|60%|73\.3|18\.8` found hits only in Stats used and Flags.
- **Nothing invented, misattributed or duplicated:** no stat appears in more than one section, and no FAQ restates 200+, 33x, 1999, 19th, 7 days or $4,500.
- **Sibling-page variants not used:** none of the inaccurate sibling variants appear ("14+ Yrs Gartner #1", "~$15", "ISO 27001/SOC 2 compliant", the demo 90% / 1.6x / 60%).

## 7. Human tone / AI-detection heuristics: PASS

**Stock-phrase sweep:** 0 hits in the page copy. The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just", "in conclusion", cutting-edge, game-changing, revolution, unleash, delve, landscape, ever-evolving, state-of-the-art, world-class, best-in-class, synergy, supercharge, transformative, navigate, pivotal, crucial, furthermore, moreover, additionally, ensure, comprehensive, innovative, dynamic, effortless and stunning. The only hits are "unlock" inside the L4 URL slug (379) and in Flags (507).

**The loop-2 failure is resolved:**
- FAQ A3 no longer recycles S5 row 3's sentence frame (see V).
- The two now read as distinct: S5 row 3 says what our engineers reach and how; A3 answers the reader's question conversationally ("Most of them. Where a ... connector exists, we use it ...").

**Openers checked:**
- The S6 card backs open three different ways (We / Group P&L / Dashboards / We / CRM / We).
- The S7 items open We / Our engineers / We / When / We / We. This is acceptable for a provider-led services list, and B2 requires it.
- Three FAQ answers open "Yes." (A4, A5, A8), which is the template's direct-answer style. Each continues differently, so this is not a finding.

**Advisory (not scored):** S5 row 3 and A3 both end their lists with "cloud warehouses ... and REST APIs". That is a 2-3-word generic overlap, fine as is.

## 8. Section structure, links and schema: PASS

- **Order (12.2 renumbering):** S0 breadcrumb, S1 hero, S2 strip + S2b, S3 anchor nav, S4 Why HLB HAMT, S5 The Platform, S6 Use cases, S7 Services, S8 CTA 1, S9 PoC (highlighted band), S10 Engagement models + PowerUP!, S11 Why UAE businesses, S12 See it in action, S13 CTA 2, S14 FAQ, S15 Contact, S16 Footer. All present and in order.
- **Headings:** exactly **one H1** (22) and 12 H2s. The S5 platform block keeps its H3 and 4 bullets. S7 has 6 items, S9 has 5 steps, and S10 has a featured card plus 4 tabs, with 5 Support items. S11 has 6 tiles.
- **AI Insights fully absent:**
  - ripgrep `AI Insights|aiinsights|key influencer|decomposition|narrative|anomal|Q&A` has 0 hits on the page.
  - Hits appear only in Flags (457, 479, 500) and Stats used (446).
  - The anchor nav (16) has 7 items in DOM order: Why HLB HAMT · The Platform · Use Cases · Services · Proof of Concept · Engagement Models · FAQ. `#explorepowerbi` is kept.
  - AI content appears only in FAQ 6 and FAQ 8, unnamed (ripgrep `\bAI\b` on the page: 385, 390, 391).
- **Internal links (12.9):**

| Link | Anchor | Target | Location | Result |
|---|---|---|---|---|
| L1 | digital transformation and analytics services | /services/digital-transformation-uae/ | S4 lede (71) | Exact |
| L2 | SugarAI CRM | /sugarai-crm-2/ | S11 tile 4 (335) | Exact |
| L3 | UAE Corporate Tax advisory | /services/corporate-tax-advisory-services-in-uae/ | S6 card 2 (164) | Exact |
| L4 | Power BI automation | /insights/unlocking-power-bi-automation-with-power-automate/ | FAQ 4 (379) | Target exact. Anchor shortened under Revision 3 (accepted in v6). |
| L5 | data protection advisory | /services/data-privacy-and-security-uae/ | FAQ 6 (385) | Exact |
| L6 | Power BI dashboard development | /services/power-bi-dashboard-development/ | S7 item 03 (209) | Exact |
| L7 | data visualisation services | /services/data-visualization-uae/ | S6 intro (153) | Exact |
| P2 | advanced analytics services | PLACEHOLDER:/services/advanced-analytics-services/ | S6 card 6 (188) | Exact |

- **Other link checks:**
  - In-page links: "proof of concept" (80) and "above" (286) go to #methodology; "PowerUP!" (373) goes to #packages.
  - **Excluded pages:** `/power-bi-partner-in-dubai-uae/` and `/microsoft-power-bi-consulting-in-dubai-uae/` appear only in Flags (513). Neither is linked.
- **Schema:** Service, FAQPage and BreadcrumbList.
  - The FAQPage has **10** Q&As (Q1-Q10, lines 369-397), matching the 10 FAQ H3s.
  - Deliver must regenerate the FAQPage text from the v7 on-page answers (A3 changed in v7), with `[n]` markers stripped and link anchors as plain text.

## 9. Client requirements: PASS

**No "certified" language:**
- ripgrep `(?i)certif` has 0 hits on the page (only Flags 492, 499).
- "Leading" has 0 hits on the page. "Leader" (61) is Gartner's category name for Microsoft, correctly attributed.
- S11 tile 1 reads "Power BI reselling partner in the UAE" (Section 13 #2). "Certified" appears nowhere near "Microsoft" or "Power BI partner".

**Section 13:**
- #1: the redirect-page reuse follows the rule (unchanged since v5).
- #3: the offer is named "PowerUP!: HLB HAMT's Fixed-Price Power BI Accelerator" (263).
- #4: there is no case-study block.

**Section 10 #7 corrections all hold:**
- No "Gartner #1", "ranked" or "14+".
- No Arabic AI-prompt claim. A8 says "Prompts are officially supported in English only for now".
- No Q&A feature.
- No Windows mobile claim.
- No "Salesforce (60+ modules)".
- No competitor price comparison.
- No Hebrew. Urdu and Persian are kept.

**Revision 3:**
- All 11 affected locations in revision-3-notes.md are handled (verified in v6 and unchanged except the two fixes).
- The full name sweep is clean (R3-A).
- The SugarAI CRM cross-link is kept.
- The region names are kept, as the notes allow.

**Content Writer decisions:**
- iOS/Android and Windows removals: approved and intentional; not flagged.
- Region names (test-report-v6 decision D) and the dropped capacity tiers in A8 (decision E): both are items the notes allow. They remain for the Content Writer to overrule if desired, and they do not block PASS.

**No transcript was supplied** for this requirement, so there is nothing further to reconcile.

---

## Overall: PASS

Every checklist item passes on a full, fresh pass:
- Both loop-2 fixes are applied verbatim, and nothing else in the page copy changed.
- The word count is 3,477, in range.
- Keywords and branding counts are all in range (6 / 3 / 2 / 2 / 0; "HLB HAMT" 12; "Microsoft" 6; "UAE" 10; "Power BI" 50).
- There are zero em dashes.
- Spelling is British throughout.
- No banned product name appears in the page copy.
- All stats were re-verified against live sources today.

**draft-v7.md is ready for Deliver.** No fix instructions are needed, and the loop budget is not exceeded.

### Carry to Deliver (mandatory rendering rules, not draft failures)
1. **Source link text:**
   - Render every Sources entry with its v7 description as the visible link text, and put the raw URL in `href` only.
   - Do **not** restore the quoted Microsoft page titles ("Fabric region availability", "Copilot for Power BI overview").
   - This covers Sources 3, 9 and 10, which Build flagged, **and Source 8** (`https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing`, which contains "power-platform"), which Build's Flags item 6 omitted.
   - The previous output rendered all four raw URLs as visible text (`output/power-bi-services-homepage.html` lines 883, 886, 890 and 892).
2. **Buttons:** keep the S2b button label "Read Microsoft's announcement", with the forum URL as its target only. Keep the L4 anchor as "Power BI automation" (slug in `href` only).
3. **Regenerate, do not patch:**
   - Regenerate every output file (HTML, DOCX, PDF, insurance-format DOCX, sources log) and the FAQPage schema (10 Q&As, v7 text including the new A3) from draft-v7.
   - The current outputs still contain pre-Revision 3 copy, such as "Excel and SharePoint sources" and "Azure Data Factory pipelines".
4. **Other carry-forwards unchanged from Build's Flag 15:**
   - The Gartner disclaimer.
   - Footnote renumbering in order of appearance ([4] and [5] retired, [12] new).
   - The SugarAI reverse-link edit.
   - The 12.12 live-site notes.
   - The open final URL and redirects (Section 10 #3), which still block go-live but not Deliver.

### For the Content Writer's awareness (non-blocking, no action required to proceed)
- The UAE North (Dubai) / UAE Central (Abu Dhabi) region names are kept in S1, as revision-3-notes.md allows. Fallback if overruled: "in Microsoft's Dubai or Abu Dhabi cloud region".
- FAQ A8 cannot state the precise capacity tiers (F2+/P1+) under the no-tool-names rule. It is accurate but less specific.

---

Sources consulted for verification:
- [Microsoft Learn, region availability (ms.date 2026-09-25)](https://learn.microsoft.com/en-us/fabric/admin/region-availability): UAE Central "Power BI only region"; UAE North all workloads
- [Microsoft Learn, Copilot for Power BI overview (ms.date 2026-08-24)](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction): F2+/P1+, Pro/PPU insufficient, English-only, off by default outside the US/EU boundary
- [Microsoft Power BI pricing](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing): Pro $14.00, PPU $24.00 user/month
- [mwpro.co.uk repost of Microsoft's Gartner announcement](https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/): 2026 MQ Leader, nineteenth consecutive year
- [Numeric, "Here Comes The Finance Engineer"](https://www.numeric.io/blog/finance-engineer): fetched to rule out a search-summary false positive (no match)
- [Beyond The Analytics, Power BI data residency](https://beyondtheanalytics.com/blog/data-residency-power-bi-gcc-compliance): same Microsoft fact, different wording (no copy)
- Web exact-phrase searches with no match: "Where a standard or partner-built connector exists"; "write custom connectors for legacy systems that have none"; "Dubai runs every data workload"; "so a sold unit counts once, whichever team reports it"; "our accountants and engineers make the numbers reconcile"; "The tool is rarely the problem; how the report was built almost always is"; "PowerUP! is for organisations sitting on useful data"
