# Test report v8: Power BI Services homepage (draft-v8.md, Revision 4 urgent correction)

Tested by: Test agent, 2026-09-29
Loop: **Not a Build/Test loop.** This is the Content Writer's urgent Revision 4 correction (`inputs/revision-4-notes.md`), applied to draft-v7 (the last delivered draft; `test-report-v7.md` was PASS). It does not count against the 3-loop budget.

Inputs checked:
- `inputs/revision-4-notes.md` in full (the authoritative spec for this fix).
- `brief.md` in full (Sections 1-13; Section 12 overrides 1-10; Revision 4 overrides both for the removed items).
- `draft/draft-v8.md` in full (page, Sources, Stats used, all 16 Flags), compared against `draft/draft-v7.md`.
- `draft/test-report-v7.md` (count conventions and the v7 per-section baseline).
- The Advanced Analytics sibling draft (`2026-09-29-advanced-analytics-services-homepage/draft/draft-v5.md`, S10) for the structural comparison.
- `output/` (the previous delivery), to confirm what Deliver must replace.
- Web searches on Softcrylic's PowerUP!/PoC page and on the new v8 phrasing.

Method:
- No shell. Every check was done with ripgrep across the whole file. Hits outside the page copy were then set aside: meta, the draft header (line 7), chrome, structure headers, eyebrows, buttons, URLs, Sources, Stats used and Flags.
- **Unchanged lines were checked character for character, not by eye.** Each unchanged v8 line was run as a fully anchored regex (`^...$`) against both v7 and v8, and the hit counts had to match in both files.
- Word count is v7's fresh machine count (test-report-v7, 3,477) minus the removed text. I counted the removed text word by word and recounted every section this revision touched (S2, S10, S11, FAQ A2).

---

## Summary

| # | Item | Result |
|---|---|---|
| R4 | Revision 4 removal is clean (checks 1-8 in the task) | **PASS** |
| 1 | Keyword placement and density, branding B1-B7, stuffing caps | **PASS** ("HLB HAMT" = 10, exactly at the floor; see advisory A1) |
| 2 | Word count | **PASS** (3,338) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling (British), punctuation | **PASS** |
| 5 | Originality | **PASS** (advisories A2 and A3 for the Content Writer) |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI-detection heuristics | **PASS** |
| 8 | Section structure, internal links, schema | **PASS** |
| 9 | Client requirements (Revision 4 spec, plus brief Sections 10, 12 and 13 and Revision 3) | **PASS** |

---

## R4. Revision 4 removal: PASS

### Check 1. No "PowerUP", "Power UP", "33x", "33 x" or "$4,500" in page copy: PASS

- **Search run:** case-insensitive ripgrep over the whole file for `power\s*up|33\s*x|4,500|4500|fixed-price|fixed price|accelerator|limited offer`, plus a second search for `enquire|softcrylic|limited|featured|what you receive|what's in scope`.
- **Hits:** lines 7, 420, 427, 429, 434-436, 438, 440, 449, 450, 468 and 469.
- **Where they sit:** every hit is in the draft header note (7), the "Retired" paragraph under Stats used (420) or Flags (427-469). None is page copy.
- **Page copy (lines 9-385, S0-S16):** 0 hits.
- **Sources list:** entry 2 now reads "(Retired in Revision 4; the engagement-result stat it supported was removed from the page. Not used on the page.)" and names neither the figure nor the offer.
- Build's claim is confirmed.

### Check 2. S2 strip has exactly 3 items, no replacement stat, no orphaned marker: PASS

- **Items (lines 45-55):**
  - Item 1: `200+` with "Power BI connectors; we configure yours and build missing ones. [1]"
  - Item 2: `Since 1999` with "A licensed UAE audit, tax and advisory firm that also builds your data platform. [12]"
  - Item 3: `Arabic and English` with "Right-to-left dashboards planned from the first mockup, not retrofitted."
- All three are word-for-word the same as v7's items 1, 3 and 4. Nothing new was added.
- **Footnote markers:** ripgrep for `\[2\]` finds no page-copy hit (only line 7 and the Flags/Stats notes). The S2 markers are [1] and [12] only.
- The section header now says "3 items" (line 43).
- **Word count:** S2 + S2b = 66 (items 39, S2b 27). That is now **inside** the 12.4 budget of 45-70. v7 was 77, and the overage had been accepted since v5.

### Check 3. S10 is only the 4-tab matrix, and its intro names no fixed-price offer: PASS

- **What S10 contains (lines 249-291):** the eyebrow, H2 "Engagement Models That Match Where You Are Today", the intro, then Tabs 1-4 (Explore / Implement / Extend / Support). The whole featured card is gone: badge, H3, price line, story, terms label and list, deliverables label and list, and button.
- **The tabs are unchanged:** an anchored-regex check of all 32 tab lines (4 tab names, 4 taglines, 12 item H3s, 12 item bodies) matched 32 in v7 and 32 in v8.
- **The intro (255) is identical to v7:** "We offer four ways in: explore before you spend, implement in phases, extend your own team, or hand us the ongoing care. You can switch models as your needs change."
  - It never named PowerUP! or a fixed price, so Build was right to leave it alone. It describes the four tabs exactly.
  - revision-4-notes item 2 expected the intro to say "start with the fixed-price PowerUP!". It did not, in v6 or v7.
- **It matches the sibling structure.** The Advanced Analytics draft-v5 S10 (lines 244-275) has the same shape: eyebrow, H2, "We..." intro, tabs, and "(No featured-offer card. No button.)".
- The section header is now "S10: Engagement models (`#packages`)", the same label the sibling uses.

### Check 4. Hero secondary button: PASS

- Line 26 reads: "Book a Power BI consultation (#contact) · See our engagement models (#packages)".
- The target is unchanged, and the old label "See the PowerUP! offer" is gone.

### Check 5. S11 tile 3: PASS

- Line 308: "Begin with a working dashboard on your own data, then scale once it proves itself."
- This is revision-4-notes item 4's example, word for word.
- **Word count:** 15, down from 18. The brief's tile range is 10-18.
- The H3 "Low-risk start" is unchanged.
- It keeps the low-risk-start idea, and it still meets brief 4 S12 tile 3's rule of no "7 days" and no "$4,500".

### Check 6. FAQ A2 rewording: PASS

- **v7 final sentence:** "...and [PowerUP!](#packages) gives you a fixed-price way to start."
- **v8 final sentence:** "As a reselling partner, we advise on the right licence mix and supply it, and our [engagement models](#packages) let you start small."
- **Reads naturally:** yes. The plural subject "engagement models" takes "let", which is correct.
- **No overclaim.** "Start small" is supported by S10's Explore tab (a no-cost live demo and a scoped proof of concept) and the Implement tab's single-department rollout. It promises no price, no fixed fee and no timeframe.
- **Consistency:** "fixed-price" appears nowhere on the page.
- **The rest of A2 is unchanged.** A prefix-anchored regex covering everything up to "...supply it, and " matched once in v7 and once in v8.
- **B3 still holds:** "we advise".
- **Word count: A2 = 81** (21 + 27 + 11 + 22), inside the 65-90 range. Build's Flags item 1 says 73, which is a counting slip. See advisory A4; it does not affect the result.

### Check 7. S9 is untouched: PASS

- Every S9 line (224-247) was checked as a fully anchored regex against both files, 15 lines in all:
  - the section header, eyebrow, H2 "A Working Power BI Dashboard on Your Data in 7 Days [6]", intro, 5 step H3s, 5 step bodies and the button.
- Result: 15 matches in v7 and 15 in v8. S9 is character-for-character identical.

### Check 8. Nothing else changed from v7: PASS

- **Spot-checks with fully anchored regexes, all matching once in each file:**
  - S1 hero lede
  - S1 deployment line
  - S5 intro
  - S7 intro and item 01 (including "As a Power BI reselling partner...")
  - S8 H2 and body
  - S10 intro
  - S11 tile 1 H3 "Power BI reselling partner in the UAE" and its body
  - FAQ A1 and A3-A10 in full
  - FAQ A2 up to the changed clause
- **Reselling-partner framing:** the "Power BI reselling partner" wording in S7 item 01, S11 tile 1 and FAQ A2 ("As a reselling partner") is intact.
- **Full visual comparison of the other page lines:** S0 chrome, S1 cards, S2b, S4, S5 rows 1-4 and the platform block, S6, S7 items 02-06, S11 tiles 2 and 4-6, S12, S13, the FAQ questions and S15. No other differences.
- **Complete list of page-copy changes from v7:**
  - the hero button label (26)
  - S2 item 2 removed and items renumbered (49-55)
  - the S10 featured card removed (v7 261-279)
  - S11 tile 3 (308)
  - the FAQ A2 final clause (349)
- **Non-page changes:** the structure headers for S2 (43) and S10 (249), and the header note, Sources, Stats used and Flags. All are consistent with the page.

---

## 1. Keyword placement and density: PASS

Counted on page copy only, under brief Section 2a. Eyebrows, buttons, nav, meta and structure headers are excluded.

| Keyword | v8 | v7 | Target | Result |
|---|---|---|---|---|
| "Power BI service" singular | **6** (22, 24, 70, 102, 345, 346) | 6 | 5-7 (max 8) | Pass |
| "Power BI Services" plural | **3** (194, 297, 379) | 3 | 2-3 | Pass |
| "Power BI consulting company" | **2** (67, 299) | 2 | 1-2 | Pass |
| "Power BI solutions expert" | **2** (278, 335) | 2 | 1-2 | Pass |
| "Certified Power BI Partner in UAE" | **0** | 0 | 0 (Section 13 #2) | Pass |

- **Meta and placement** are unchanged from v7:
  - Meta title: "Power BI Service & Consulting Partner in the UAE | HLB HAMT".
  - Meta description: opens "Power BI service from HLB HAMT".
  - The primary keyword is in the H1 and in hero lede sentence 1, so it falls within the first 100 words.
  - Neither meta line mentions the removed items.
- **B1:** the H1 opens "HLB HAMT:".
- **B2:** the hero and every section intro open HLB-led. The S10 intro still opens "We offer".
- **B3:** every FAQ answer has a "we" or HLB HAMT sentence. A2's is "we advise".
- **B4 "HLB HAMT" = 10.** Pass, at the floor of 10-16.
  - Counted at lines 22, 24, 57, 67, 85, 87, 194, 297, 323 and 373.
  - Excluded: eyebrows (20, 63, 295), structure headers (61, 190, 293), meta, nav and Flags.
  - v7's 12 included the 33x description and the featured-card H3, both now removed. Build's figure of 10 is confirmed. See advisory A1.
- **B5 "Microsoft" = 6** (cap 12), unchanged.
- **B6 and B7:** unchanged. There is no "certified" or "leading" on the page, and the Gartner recognition is attributed to Microsoft.
- **"Power BI" (any form) = 48** (cap 75; flag above 85).
  - Every ripgrep hit was listed by line and hand-tallied.
  - Excluded: meta (1, 2), header (5, 7), breadcrumb (11), eyebrow (20), buttons (26, 337) and structure header (190).
  - v7 had 50. The two removed instances were the featured-card H3 and "A published Power BI app". Build's ~48 is confirmed.
- **"UAE" = 10** (cap 12), unchanged. None of the removed lines contained "UAE".
- **"Power BI" in titles:** 0 of 6 in S7 and 0 of 5 in S9.
- No stuffing and no singular/plural clash.

## 2. Word count: PASS (3,338)

The count rule is the same as test-report-v7: headings, body, strip text, tab names, pills and FAQ count; eyebrows, buttons, nav, form, footnote markers and Sources do not.

**What was removed from v7's 3,477:**

| Removed | Words |
|---|---|
| S2 item 2: "33x" (1) + description (10) | 11 |
| S10 featured card: badge 2, H3 7, price line 3, story 50 (15 + 25 + 10), "What's in scope" 3, terms 36 (10 + 6 + 5 + 6 + 9), "What you receive" 3, deliverables 20 (3 + 3 + 3 + 2 + 4 + 5); button not counted | 124 |
| S11 tile 3 (18 → 15) | 3 |
| FAQ A2 final clause (9 → 8) | 1 |
| **Total removed** | **139** |

**Per-section totals:**

| Section | v8 | Budget (12.4) | Status |
|---|---|---|---|
| S1 | 188 | 150-190 | OK. The button change is not counted. |
| S2 + S2b | **66** | 45-70 | OK. Now inside budget (v7 was 77). |
| S4 | 272 | 260-310 | OK |
| S5 | 396 | 380-440 | OK |
| S6 | 385 | 340-410 | OK |
| S7 | 414 | 380-440 | OK |
| S8 | 27 | 20-30 | OK. Build's Flags use 26; test-report-v7 corrected this to 27. |
| S9 | 153 | 150-190 | OK, unchanged |
| S10 | **282** | 360-420 (set for card + tabs) | Below budget. **Expected and accepted** (revision-4-notes item 7). I recounted it fresh: H2 8 + intro 30 + tab names 4 + taglines 36 + items 204. |
| S11 | **149** | 150-190 | One word under. **Accepted** as a direct result of the required tile 3 reword; revision-4-notes item 7 says not to pad. I recounted it fresh: H2 10 + intro 24 + tiles 115. Build's Flags item 1 does not list S11 among the sections now below budget. |
| S12 | 36 | 30-45 | OK |
| S13 | 29 | 20-30 | OK |
| S14 | 914 | 780-920 | OK. A2 is 81, and every other answer is unchanged, all within 65-90. |
| S15 | 27 | 20-30 | OK |
| **Total** | **3,338** | 3,100-3,500 (fail below 2,900 or above 3,750) | **PASS** |

- Build's ~3,337 agrees within 1 word; the difference is the S8 26/27 slip.
- **Does the range still make sense?** Yes:
  - The page removed about 139 words and still sits 238 words above the floor, close to the brief's ~3,300 target.
  - revision-4-notes item 7 expected the total to fall below range, but that did not happen: the featured card was 124 words, not the estimated 130-140, and v7 started near the top of the range.
  - Nothing was padded back, which is correct. Brief 12.4 says "Do not pad back to 3,300."
  - The only budget effects are S10 (structural, and accepted) and S11 (one word under).
  - No re-budgeting is needed.

## 3. Zero em dashes: PASS

- Whole-file ripgrep: `—` **0**, `–` **0**, `--` **0**. The tables use `:-` separators.

## 4. Grammar, spelling, punctuation: PASS

- **The three changed strings read correctly:**
  - "See our engagement models" is a clear imperative button label.
  - Tile 3 is a single clean imperative sentence: "Begin with a working dashboard on your own data, then scale once it proves itself."
  - A2's new clause "and our engagement models let you start small" is correct: plural subject, plural verb.
  - The "...and supply it, and our..." double "and" was already in v7's sentence shape and reads acceptably.
- **British spelling:** "licence" (noun) in A2. There are no new -ize, -or or -er forms. Every other line is unchanged from v7, which passed.

## 5. Originality: PASS

- **Only new page copy:** tile 3's sentence and A2's final clause (the button label is not counted).
- **Local ripgrep over `inputs/`** for "proves itself", "start small", "engagement models let" and "working dashboard on your own data": the only hit is revision-4-notes.md lines 56-58, the Content Writer's own suggested wording. Using it is prescribed, not copied.
- **Web exact-phrase searches:**
  - "working dashboard on your own data, then scale once it proves itself": no match.
  - "advise on the right licence mix and supply it" / "engagement models let you start small": no match.
  - "Start small" is a common idiom (Adobe's pricing copy uses "start small and grow"), not a copied passage.
- **The removed Softcrylic-derived material is gone from the page.** That covers the 33x result and the PowerUP! name, price, terms and deliverables.
- **Two remaining overlaps with Softcrylic material.** Neither is a sentence-level copy, and the spec explicitly keeps S9 unchanged, so neither is a failure. Both are raised for the Content Writer as advisories A2 and A3.

## 6. Stat accuracy: PASS

- **Stats used (v8) now lists:** [1] 200+ (S2 item 1); [12] Since 1999 (S2 item 2) and HLB International since 2007 (S11 tile 5); [3] Gartner 2026 / 19th year (S2b); [6] 7 days (S9 H2); the FAQ 10 timelines; and [7]-[11] F1-F5.
- **No new facts.** Every one of these stats and their wording is unchanged from v7, so no fact was introduced or altered.
- **Re-verification:** test-report-v7 checked every one against live sources today (2026-09-29): the Microsoft Learn region and Copilot pages, the pricing page and the Gartner repost. No re-fetch is needed for this same-day correction.
- **Retirements are handled correctly:**
  - [2] (33x): the Stats used row is removed, the marker is removed from S2, and Sources entry 2 is marked retired.
  - The PowerUP! price, terms and deliverables row is removed. It carried no footnote.
  - The "Retired" paragraph records why both were removed.
- **Footnote markers on the page, in order:** [9] S1; [1] [12] S2; [3] S2b; [7] S5; [6] S9; [12] S11; [7] A1; [8] A2; [11] [9] [10] A6; [10] A8.
  - Every marker has a live Sources entry, and every live entry (1, 3, 6-12) is used.
  - [2], [4] and [5] are used nowhere. There are no orphans.
- **No duplicates across sections.** No FAQ restates 200+, 1999, the 19th year or 7 days.
- **No engagement result remains on the page.** R2-4 said "33x stays the only engagement result". With 33x removed, the page now has no quantified client result, which is the honest position.

## 7. Human tone / AI-detection heuristics: PASS

- **Stock-phrase sweep on the changed lines:** there are no hits from the test-report-v7 list (unlock, seamless, leverage, empower, robust, streamline and so on). The rest of the copy is unchanged from v7, which passed.
- **Tile 3** now reads a little plainer than its neighbours but is specific ("on your own data", "once it proves itself"), not templated.
- **A2's close** ("let you start small") is conversational and ties to the section it links to.
- **Removing the card did not leave S10 feeling cut off.** The intro introduces exactly the four tabs that follow, so there is no dangling setup.

## 8. Section structure, links and schema: PASS

- **Order:** S0, S1, S2/S2b, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S14, S15, S16. All are present and in order.
- **Headings:** one H1 (22) and 12 H2s. S10 now has H2 + 4 tabs with no featured H3, as revision-4-notes item 2 requires. S2 has 3 items.
- **Anchor nav (16):** unchanged, with 7 items. "Engagement Models (#packages)" still points to a live section.
- **Internal links:** L1 (67), L2 (311), L3 (160), L4 (355), L5 (361), L6 (205), L7 (149) and P2 (184) are unchanged from v7, with identical anchors and targets.
  - In-page links: "proof of concept" → #methodology (76); "above" → #methodology (262); "engagement models" → #packages (A2, 349, replacing the "PowerUP!" anchor); hero button → #packages.
  - The two excluded pages are still unlinked.
- **FAQ:** 10 Q&As (Q1-Q10, lines 345-373), each answer 65-90 words, in a single accordion.
  - The text is schema-ready apart from the A2 change.
  - Deliver must build FAQPage from the v8 on-page text, with [n] markers stripped and anchors as plain text. A2 now ends "...and our engagement models let you start small."

## 9. Client requirements: PASS

- **revision-4-notes.md:** every required action (items 1-6) is done, and the word-count guidance (item 7) is followed.
  - Item 1: 33x removed, no replacement stat.
  - Item 2: the card is removed, and the intro needed no change.
  - Item 3: hero button replaced.
  - Item 4: tile 3 reworded.
  - Item 5: whole-page sweep. Build also caught A2, which the notes did not list.
  - Item 6: [2] retired, with renumbering left to Deliver.
  - Item 7: no padding.
  - "What stays unchanged" is honoured: S9, the reselling-partner framing, the S10 tabs, and all other stats and sections.
- **Brief items that Revision 4 overrides, now correctly inactive:**
  - brief Section 1 conversion (3), the PowerUP! enquiry
  - 4 S1 button "See the PowerUP! offer"
  - 4 S2 item 2 and 12.5 S2 item 2 (33x)
  - 4 S11 and 12.5 S10, the featured card
  - 12.5 FAQ 2's "fixed-price starter engagement" pointer, now a pointer to the engagement models
  - Section 13 #3, the offer name
- **Standing requirements still met:**
  - Section 13 #2: no "certified"; tile 1 reads "Power BI reselling partner in the UAE".
  - Section 10 #7 corrections: no "#1" or "14+", no Arabic AI-prompt claim, no Q&A, no Windows, no Hebrew.
  - The Revision 3 name sweep is unaffected: the removed text contained no product names, and no new names were added.
- There was no transcript for this requirement.

---

## Advisories (non-blocking; for the Content Writer's awareness)

**A1. "HLB HAMT" sits exactly at the B4 floor (10).**
- It passes. However, any future edit that removes one more instance fails B4, and the 33x and card removals already took out 2.
- No action is recommended now, because Revision 4 is a targeted removal, not a rewrite.
- If a later revision wants margin, the lowest-risk slot is the S10 intro, which B2 allows to open with HLB HAMT: "HLB HAMT offers four ways in: ...". Using it needs Content Writer sign-off.

**A2. S9's 5-step proof of concept loosely parallels Softcrylic's PowerUP! methodology.**
- Softcrylic's steps, from a web search of its PowerUP! page ([softcrylic.com/power-bi-poc](https://www.softcrylic.com/power-bi-poc/attachment/published-app/)): "Step 1 - Understand desired Goals, KPIs, Visuals (Requirements workshop); Step 2 - Data Analysis and Source Preparation; Step 3 - Dashboard Design & Data Visualization; Step 4 - Addressing Gaps and Fine Tuning; Step 5 - Final Delivery". The page's terms include "design approval in mockup with 1 round of revision after functional delivery" and the deliverable "published app".
- S9's steps: Requirements (workshop) / Data preparation / Design and mockup / Development / Delivery and review. The step 5 body is "Users get hands-on training and give feedback, one revision round follows, and we publish the finished Power BI app to your tenant."
- **Why it is not a finding:**
  - No sentence is copied. Steps 3-5 are divided and named differently.
  - A requirements → data prep → design → build → deliver sequence is a generic delivery shape.
  - revision-4-notes explicitly keeps S9, as a claim corroborated across live HLB HAMT pages.
- **Why the Content Writer should know:** the "mockup approval" + "one revision round" + "published app" combination in S9 steps 3 and 5 matches the same Softcrylic terms that Revision 4 removed from the card. Since the provenance of Bala's source content is now in question, the Content Writer may want to confirm with HLB HAMT that this PoC structure is genuinely theirs.
- Softcrylic's page is JS-rendered: WebFetch returned an empty page, as revision-4-notes predicted. This evidence comes from search extracts and needs the same browser check the notes recommend.

**A3. The "pipeline, data model and semantic layers" phrasing remains in S7 item 04 and, reworded, in FAQ A9.**
- S7 04 (207): "When reports drag, we tune across the pipeline, data model and semantic layers, ..."
- A9 (370): "We work through the pipeline, the model and the semantic layer: ..."
- revision-4-notes cites this exact framing ("optimization work occurs at the pipeline, data model, and semantic layers") as part of the evidence that 33x came from Softcrylic.
- **Why it is not a violation:**
  - Here it describes where tuning happens, not a result.
  - The shared run is a 6-word list of generic technical layers, also used by unrelated vendors (e.g. Pythian's semantic-layer performance article).
  - Brief 12.0 and 12.1 N1 sourced it from HLB HAMT's live data-viz page.
  - revision-4-notes says to leave everything else unchanged.
- **Optional reword for S7 04, if the Content Writer wants a clean break:** "When reports drag, we trace the slowdown to its source, whether that is the data feed, the model or a heavy measure, then cut query load, add aggregation tables over large fact tables and replace slow measures with efficient DAX patterns."

**A4. Build's self-count slips (bookkeeping only; nothing on the page is affected).**
- Flags item 1 gives FAQ A2 as 73 words; it is 81.
- It uses S8 = 26; Test's figure is 27.
- It omits S11 (149, one under its 150-190 budget) from its list of sections now below budget.

## Carry to Deliver (mandatory; the delivered files still contain the removed content)

The current `output/` files must be **regenerated from draft-v8, not patched**. Ripgrep evidence:
- **`output/power-bi-services-homepage.html`:**
  - Lines 56-58: **a JSON-LD `"@type": "Offer"`** named "PowerUP!: HLB HAMT's Fixed-Price Power BI Accelerator" with "$4,500 fixed-price accelerator". The Offer markup must not be carried into the new Service schema.
  - Line 82: FAQPage schema A2 ("...and PowerUP! gives you a fixed-price way to start.").
  - Line 509: the hero button "See the PowerUP! offer".
  - Line 530: the 33x strip item.
  - Lines 712-726: the featured card, including "$4,500 fixed-price accelerator" and "Enquire about PowerUP!".
  - Line 791: tile 3 with "fixed-price PowerUP!".
  - Line 842: on-page FAQ A2 with the `#packages` "PowerUP!" link.
  - Line 881: source 3, the 33x data-viz citation.
- **`output/power-bi-services-homepage-sources-log.md`:** lines 37, 57 and 60 (the 33x and PowerUP! rows).
- **The DOCX, PDF and insurance-format DOCX** are binary and could not be searched, but they were generated from the same v7 draft and must be assumed to contain the same content.

Also:
- **S2 strip layout:** render 3 items. If the previous markup or CSS set a 4-column grid, adjust it so the strip does not show an empty slot.
- **FAQPage schema:** 10 Q&As from the v8 text. A2 changed; A3 changed in v7.
- **Footnotes:** renumber by order of appearance. [2], [4] and [5] are retired, and [12] is new. The old 33x data-viz citation must not appear.
- **Unchanged carry-forwards from test-report-v7:**
  - Source link text uses the descriptions, not raw URLs, and this includes Source 8.
  - The Gartner disclaimer.
  - The SugarAI reverse-link edit.
  - The 12.12 live-site notes.
  - The open final URL and redirects.
- **Handoff notes to add:**
  - The live hlbhamt.com page may already show the 33x stat and PowerUP! card (revision-4-notes, "Why this is urgent"), so the regenerated HTML should replace it promptly.
  - The Data Visualization sibling page (`/services/data-visualization-uae/`) still publishes the 33x claim live (brief 12.1 N1). That is outside this page's scope, but it belongs in the live-site notes for the Content Writer.

---

## Overall: PASS

The Revision 4 correction is clean:
- Page copy has zero instances of "PowerUP", "Power UP", "33x", "33 x" or "$4,500".
- S2 has 3 items with no orphaned marker.
- S10 is the 4-tab matrix only, matching the Advanced Analytics sibling.
- The hero button, S11 tile 3 and FAQ A2 are correctly reworded.
- S9 is character-for-character unchanged.
- Nothing else in the page copy changed from v7.
- The full QA pass also holds:
  - word count 3,338, in range
  - keyword counts unchanged (6 / 3 / 2 / 2 / 0)
  - "HLB HAMT" 10 (at the floor), "Power BI" 48, "Microsoft" 6, "UAE" 10
  - 0 em dashes, British spelling
  - no stat or fact changes
  - internal links intact
  - FAQ at 10 schema-ready Q&As

**draft-v8.md is ready for Deliver to regenerate all output files.** There are no fix instructions. Advisories A1-A3 are for the Content Writer and do not block delivery.

---

Sources consulted for verification:
- [Softcrylic PowerUP! Offer page (search extract; page is JS-rendered, WebFetch returned empty)](https://www.softcrylic.com/power-bi-poc/attachment/published-app/): 5-step methodology, terms and deliverables (advisory A2)
- [Softcrylic Dashboard Performance page (search extract)](https://www.softcrylic.com/dashboard-performance-optimization-tableau-power-bi-data-studio/attachment/tableau-logo-2/): pipeline, data model and semantic-layer optimisation framing (advisory A3)
- [Pythian, "Increase your data visualization/reporting velocity and performance with proper semantic layers"](https://www.pythian.com/blog/technical-track/increase-your-data-visualization-reporting-velocity-and-performance-with-proper-semantic-layers): shows the layer terminology is generic (advisory A3)
- [Adobe Learning Manager pricing](https://www.adobe.com/products/captivateprime/pricing.html): "start small" idiom (no copy)
- Web exact-phrase searches with no match: "working dashboard on your own data, then scale once it proves itself"; "advise on the right licence mix and supply it"; "engagement models let you start small"
