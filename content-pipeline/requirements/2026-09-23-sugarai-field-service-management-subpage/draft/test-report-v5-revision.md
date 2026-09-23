# Test report: v5 targeted revision, second pass (Blocks 2 and 7 only)

This is a focused post-delivery check, not a numbered Test loop. It compares `draft/draft-v5.md` with `draft/draft-v4.md` and checks it against `draft/test-report-v4-revision.md` and `inputs/extracted/stats-research-v2.md`. As Flag 2 of v5 asks, I do not fail v5 for naming data sources on-page (brief Section 1) or for departing from brief Sections 3 and 4 on Blocks 2 and 7. The Content Writer overrode those.

| # | Check | Result |
|:-|:-|:-|
| 1 | The 3 v4 echo issues (5a, 5b, 5c) are gone | PASS |
| 2 | Labels match the sources; Block 7 has 3 tiles; Nucleus is named in the tile text | PASS (advisories) |
| 3 | No figure is framed as field-service-specific | **FAIL** (Block 7 H2 only) |
| 4 | Word count | PASS: 1,649 (1,663 with tags and figures) |
| 5 | Em dashes | PASS: 0 |
| 6 | Keywords: 15, same locations, "field service CRM software" once in Block 2 | PASS |
| 7 | Originality of the new Block 2 and Block 7 copy | PASS |
| 8 | Everything outside Blocks 2 and 7 unchanged from v4 | PASS |

**Overall: FAIL, one item, fixed with a one-line edit.** Build's rewrite of the ledes, descriptions and tiles is clean. The one problem is the Block 7 H2, "What well-run field service operations achieve". v5 left it unchanged, and it now captions three figures that are not field service results. Build raised this itself (v5 Flag 3) but did not change it because it was out of scope. The brief says to use this H2 as written, so the Content Writer has to approve the change. The fix is under "Fix instructions". Once it is applied, the content is ready for Deliver (see the last section).

---

## 1. v4 echo issues removed: PASS

- **5a (Block 2 lede, sentence 2):** the phrase "...as reported by SugarCRM customers who run their sales and service operations on the platform" is gone. The new sentences are "SugarCRM publishes the figures below for Sugar Sell, its sales module. They span that module's whole customer base, not field service specifically." Neither has the Insurance frame "reported by ... customers running ... on the platform".
- **5c (Block 2 stat 3):** "keep moving towards signature" is gone. Searching v5 for "toward" and "moving" finds nothing in page copy. The only hits are in the "Changes from v4" notes, where the old wording is quoted.
- **5b (Block 7 lede):** the new lede is "The first two figures are SugarCRM's own numbers for Sugar Serve, its customer service module. The third is analyst research on Sugar's ERP integration." It contains no "results/outcomes", no "customers report" and no "on the platform". It does not follow the Insurance sentence shape "Outcomes SugarCRM customers report from X, Y and Z campaigns run on the platform".
- **Other stock phrases:** a search of v5 page copy for "report", "platform", "actual business results", "benchmark" and "market data" finds no match in Blocks 2 or 7.

## 2. Label accuracy against the sources: PASS (advisories)

The proxy let me open both SugarCRM AWS Marketplace PDFs, so I checked Block 2 and tiles 1-2 against the primary documents myself, not against the research note.

- **Sugar Sell sheet** (https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Sell.pdf). The title is "Sugar Sell: AI-Powered Sales and Intelligent Account Management", © 2024. It shows "Increased Revenue + 23%", "Improved Win Rate + 30%" and "Pipeline Volume 3x", with the footer "Actual business results from SugarCRM customers."
  - Stat 1 is `+23%` "Increased revenue". This matches.
  - Stat 2 is `+30%` "**Improved win rate**". This matches; it no longer says "conversion rate". Its description, "Win rates rose across that customer group.", also names the right metric.
  - Stat 3 is `3×` "**Pipeline volume**". This matches; it no longer says "growth" or implies speed. Its description, "Pipelines tripled in volume for those customers.", describes volume only.
- **Sugar Serve sheet** (https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Serve.pdf). The title is "Platform for Customer Service Heroes", Rev. 08152022, © 2022. It shows "Reduced Case Error Rate - 27%" and "Revenue Contribution from Support Team + 30%".
  - Tile 1 is `-27%` "Reduced case error rate". This matches.
  - Tile 2 is `+30%` "Revenue contribution from support teams". This matches; the plural "teams" is harmless.
  - The lede credits both tiles to Sugar Serve: "The first two figures are SugarCRM's own numbers for Sugar Serve".
  - The +17% "Revenue Increase" from the same sheet is correctly not used, because it would conflict with the +23% in Block 2.
- **Tile 3** is `8%` "Higher recurring revenue with ERP integration **(Nucleus Research)**". The attribution is part of the visible `.proof-l` label text (draft line 201), not only in the notes. The lede also calls it "analyst research on Sugar's ERP integration".
  - sugarai.com and nucleusresearch.com are still blocked, so I checked the figure through search. Results show the Nucleus page and the sugarai.com resource page titled "Sugar's ERP integration increases recurring revenue by 8%", with the text "8% average boost in recurring revenue" for SugarCRM customers with ERP integration.
- **Tile count:** there are exactly 3 tiles. The 95%, 50%, 25% and 180+ figures are gone from page copy.

**Advisories (not failures):**
- **a. Tile 3 sign.** Tiles 1 and 2 carry a sign (`-27%`, `+30%`) but tile 3 is a bare `8%`. For consistency, `+8%` would match the band. This is optional.
- **b. Nucleus nuance for the human click-check.** One search summary words the finding as "an eight percent average increase in recurring revenue per account" and ties it to the "sales-i integration" (Sugar's ERP-connected sales intelligence tool). When someone opens the Nucleus page, they should confirm the label "Higher recurring revenue with ERP integration" still fits. If the figure is per account, the label is still accurate. If Nucleus attributes it to sales-i specifically, "with ERP integration" still matches the vendor's own page title.
- **c. Typographic minus.** `-27%` uses a hyphen-minus. Deliver may render it as a true minus sign (U+2212, "−27%"). It is not a dash issue.
- **d. Note contradiction (not page copy).** Stats used says "None of these sources could be fetched directly in this sandbox" (line 377), but the next line says the Plan agent opened both PDFs. As of this check, both AWS PDFs have been opened and verified twice (Plan agent and Test). Deliver's sources log should say that the AWS copies are verified, while the official sugarcrm.com and sugarai.com copies and the Nucleus page still need a human click-check.

## 3. No figure framed as field-service-specific: FAIL (one line)

I re-read every heading and sentence in both bands.

**Block 2: all pass.**
- H2 "Why SugarAI earns its place in field operations": this is a positioning claim, not a caption on the figures. The lede disclaims the figures straight after it.
- Lede sentence 1 (the keyword sentence, unchanged): it describes capability and contains no figure.
- "SugarCRM publishes the figures below for Sugar Sell, its sales module." / "They span that module's whole customer base, not field service specifically.": this is an explicit disclaimer. Good.
- Stat 1: "Sugar Sell customers grew revenue by this margin." gives the figure as a general result. "Configured for field service, Sugar Sell turns repairs spotted on site into quotes." is a capability statement with no number, already on the page in Platform card 2.
- Stat 2: "Win rates rose across that customer group." is general. "AMC and warranty proposals follow the same quote-to-close stages." links the capability by analogy but does not claim that the 30% was measured on AMC proposals. This is acceptable.
- Stat 3: "Pipelines tripled in volume for those customers." is general. "Contract renewals join the pipeline well before they fall due, alongside new business." is a capability statement already on the page in Services 06.

**Block 7: the lede and tiles pass; the H2 fails.**
- Lede: it credits the figures to Sugar Serve and to analyst research on ERP integration. Good.
- Tiles: none uses "technician", "work order", "job", "dispatch" or "maintenance reminder". Good.
- **H2: "What well-run field service operations achieve"** (draft line 187). **FAIL.**
  - The H2 captions the band, so it tells the reader that the three figures below are what field service operations achieve. None of them is: two are Sugar Serve customer-service results across SugarCRM's whole customer base, and one is a Nucleus figure for Sugar customers with ERP integration.
  - The brief wrote this H2 for industry benchmarks measured at field service organisations (brief Block 7: Aquant first-time fix and resolution figures). That evidence was removed in v4, so the H2 no longer describes what sits under it.
  - The lede then contradicts the H2 straight away ("The first two figures are SugarCRM's own numbers for Sugar Serve..."), so the band now reads inconsistently as well as overclaiming.
  - This is exactly the implication stats-research-v2.md section E1 says the copy must avoid.

## 4. Word count: PASS

I counted by hand using the brief's Section 1 rule. Eyebrows, buttons and figures are excluded.

- **Block 2 = 118** (Build: 117).
  - H2: 8
  - Lede: 24 + 11 + 11 = 46. Build's 45 undercounts sentences 2 and 3 by one. "SugarCRM publishes the figures below for Sugar Sell, its sales module." is 11 words, and "They span that module's whole customer base, not field service specifically." is 11 words.
  - Labels: 2 + 3 + 2 = 7
  - Descriptions: 21 + 16 + 20 = 57
- **Block 7 = 47** (Build: 48).
  - H2: 6
  - Lede: 15 + 9 = 24. Build's 25 is one high.
  - Tiles: 4 + 5 + 8 = 17
- **Page total:** 1,633 - 111 + 118 - 38 + 47 = **1,649**. Adding the 4 Platform tags (8 words) and the 6 figures gives **1,663**. The two one-word errors in Build's block counts cancel out, so Build's totals are correct. Both totals are inside 1,500-1,700.
- **Baseline check:** I recounted four unchanged blocks from scratch and got the same figures as the v4 record: CTA 1 = 21, CTA 2 = 13, Why HLB HAMT = 97, Closing CTA = 51. The v4 per-block figures for unchanged blocks add up to 1,484, and 1,484 + 111 + 38 = 1,633.
- **Block budgets:** Block 2 (118) is inside 105-120. Block 7 (47) is under the brief's 55-65 because of the Content Writer's label-only, 3-tile instruction. With the recommended 8-word H2 (see Fix instructions), the page total becomes 1,651, still in range.

## 5. Em dashes: PASS

A search of the whole v5 file, notes included, for `—` (em dash), `--`, `–` (en dash), `―` and `‒` found **0 matches**.

## 6. Keywords: PASS

An exact-phrase, case-insensitive search of on-page copy for all 11 in-use keywords finds **15 instances**. They are in the same elements as in v4:
- H1
- hero lede
- Block 2 lede
- Block 3 lede
- Block 4 lede
- Benefits tiles 5 and 6
- Services H2, 01 and 05
- Services 08 H4
- Market lede
- Process H2
- FAQ A1
- FAQ Q7

**"field service CRM software":** it appears once in Block 2 (line 64, lede sentence 1, unchanged) and once in FAQ A1 (line 318), which matches the brief's required count of 2.

**New copy:** it contains "field service" twice ("not field service specifically", "Configured for field service,"). Neither forms a tracked or excluded keyword, and no sentence holds two keywords. The meta title and meta description are unchanged.

## 7. Originality: PASS

- **Against the Insurance template (HTML lines 283-300 and 437-444) and the Insurance draft extract:**
  - The new stat descriptions share no sentence frame with the Insurance descriptions:
    - Insurance: "Actual business results reported by...", "More quotes convert when...", "...keep more opportunities moving toward bind."
    - v5: "Sugar Sell customers grew revenue by this margin", "Win rates rose across that customer group", "Pipelines tripled in volume for those customers".
  - The new Block 7 lede shares no frame with "Outcomes SugarCRM customers report from renewal, cross-sell and service campaigns run on the platform."
  - I searched the inputs folder for the distinctive new phrases ("quote-to-close", "fall due", "customer base", "analyst research", "figures below", "own numbers", "by this margin", "tripled", "spotted on site"). The only hit is "customer group", which the template uses in a different sense (a corporate group across GCC entities). That is a common phrase, not an echo.
- **Against the SugarCRM data sheets:** the lede does not repeat their footer wording, "Actual business results from SugarCRM customers."
- **Web:** I searched these exact phrases:
  - "Contract renewals join the pipeline well before they fall due"
  - "AMC and warranty proposals follow the same quote-to-close stages"
  - "Sugar Sell turns repairs spotted on site into quotes"
  - "first two figures are SugarCRM's own numbers for Sugar Serve"
  - "publishes the figures below for Sugar Sell"

  None returned a matching or near-matching page. Results were generic renewal, AMC and Sugar support articles.
- **Metric labels:** the metric labels copy the source wording ("Improved win rate", "Pipeline volume", "Reduced case error rate"). That was required for accuracy, and it counts as source labelling, not copying.

## 8. Outside Blocks 2 and 7 unchanged from v4: PASS

- **Exact-line matches:** I ran anchored, exact-line regex searches for 68 page-copy lines outside Blocks 2 and 7. They covered:
  - the hero lede, sub-line and side rows
  - the Platform lede and cards
  - the Benefits lede and all 6 tiles
  - the CTA 1 body
  - the Services lede and all 8 items
  - the CTA 2 and closing H2s
  - the Segments lede and all 6 tiles
  - the Market lede and all 6 items
  - the Process lede, all 6 steps and the callout
  - all 4 Why cards
  - FAQ A1-A7
  - all 3 closing rows

  Each matched the same number of times in v4 and v5 (21/21 and 48/48 occurrences across the two searches).
- **Heading-line counts:** a count of heading, label, tag, question and button lines gives 76 in each file.
- **Read-through:** a side-by-side read confirms that meta lines, page chrome, links and the Sources entry are identical.
- **What did change:** only the notes, the intro paragraph, Stats used and Flags. The Block 7 eyebrow and H2 are also identical to v4, which is the problem in item 3.

---

## Fix instructions (for Build, after the Content Writer approves the H2 change)

1. **Block 7 H2 (item 3).** Replace `What well-run field service operations achieve` with **`What the service desk and ERP layers deliver`** (8 words).
   - It captions the figures accurately: the service desk layer (Sugar Serve, tiles 1-2) and the ERP layer (tile 3).
   - It contains no keyword, so the brief's "keywords in exactly 4 subheadings" rule still holds.
   - It does not echo the Insurance H2 "Results insurers report".
   - "Layer" already appears on the page in the callout "then add the field layer".
   - Build's own option, "Figures behind the service and ERP layers" (7 words), is also acceptable.
   - Do not use any H2 that contains "field service", "technicians", "results ... report" or "customers report".
   - This overrides brief Block 7's "H2 (use as written)" line. Record it in brief Section 10 together with the other two overrides already listed in v5 Flag 2.
2. **Update the notes.**
   - Set Block 7 to 49 words and the page total to 1,651 (1,665 with tags and figures).
   - Correct the Block 2 lede breakdown to 24 + 22 = 46 (Block 2 = 118) and the Block 7 lede to 24.
   - Close v5 Flag 3.
3. **Optional.**
   - Change tile 3's figure to `+8%` (advisory 2a).
   - Correct Stats used line 377 (advisory 2d).
4. **Recheck.** Only the H2 line needs rechecking: 0 em dashes and no keyword. A full retest is not needed.

## Hand-off status

**Not ready for Deliver yet.** It becomes ready once fix 1 is applied, or once the Content Writer explicitly decides to keep the brief's H2 and records that decision in brief Section 10. Everything else in v5 passes. After that, Deliver must rebuild all four outputs from the corrected v5/v6 copy:
- `output/sugarai-field-service-management.html`
- `output/sugarai-field-service-management.docx`
- `output/sugarai-field-service-management.pdf`
- `output/sugarai-field-service-management-sources-log.md`

The HTML rebuild must include:
- **Proof grid:** change `.proof-row` from `repeat(4,1fr)` to **`repeat(3,1fr)`**. At the `max-width:820px` breakpoint, use `1fr` or make tile 3 span both columns so it does not sit alone. Check that the 8-word tile 3 label wraps cleanly.
- **Band labels:** replace the Block 2 and Block 7 copy with the new labels and descriptions, and remove the old 95%/50%/25%/180+ tiles.
- **FAQ 7 source:** change `<li id="src-7" value="7">` to `<li id="src-1" value="1">`.
- **Band cleanup:** remove the stats and proof `src-note` blocks, their `<sup class="fn">` markers, and the `.proof-sub` and `.proof-l strong` markup and CSS.
- **Sources log:** rebuild it from the v5 Stats used table. Show the two AWS PDFs as verified and the Nucleus page plus the official sugarcrm.com and sugarai.com copies as awaiting a human click-check.

**Noted, not failed:** the Block 2 figures (+23%, +30%, 3×) also appear on the Insurance page. The system rules normally flag a stat reused from another page in the same project. Here it is the series convention the Content Writer ordered in v4, so I have not failed it.
