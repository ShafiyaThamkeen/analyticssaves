# Test report: v4 targeted revision (Blocks 2 and 7 only)

This is a post-delivery spot check, not a numbered Test loop. It compares `draft/draft-v4.md` with `draft/draft-v3.md`. It does not fail v4 for departing from brief Sections 3 and 4 on Blocks 2 and 7, because the Content Writer overrode those sections. The brief's word-count rule (Section 1) and keyword rules (Section 2) still apply.

| # | Check | Result |
|:-|:-|:-|
| 1 | Zero em dashes (whole file) | PASS |
| 2 | Word count | PASS |
| 3 | Keywords unchanged (15, same locations) | PASS |
| 4 | Revised sections read naturally; Block 7 tiles are short labels | PASS (advisories) |
| 5 | Originality of new Block 2 and Block 7 copy | **FAIL** |
| 6 | Everything outside Blocks 2 and 7 identical to v3 | PASS |
| 7 | Factual framing (no pricing claim; no "benchmark"/"market data" framing) | PASS as scoped (see extra finding A) |

**Overall: FAIL.** One item fails. The fixes are small: two lede sentences and one clause in Block 2 stat 3. There is also a factual accuracy issue in how the figures are labelled (extra finding A). The Content Writer needs to decide that before republishing.

---

## 1. Em dashes: PASS
I searched the whole v4 file for `—`, `--` and `–` (en dash). There are **0 matches** for all three, including the notes, Sources and Flags sections.

## 2. Word count: PASS
I recounted both changed blocks by hand, using the Section 1 rule. Stat figures and eyebrows are excluded.
- **Block 2, v4 = 111 words.**
  - H2: 8
  - Lede: 24 + 22 = 46
  - Labels: 2 + 3 + 2 = 7
  - Descriptions: 17 + 17 + 16 = 50
- **Block 2, v3 = 104 words**, which matches the v3 audit. Build's "103 to 110" is one word low on both ends, but the change of +7 is correct.
- **Block 7, v4 = 38 words.**
  - H2: 6
  - Lede: 15
  - Tiles: 4 + 4 + 5 + 4 = 17
  - v3 was 88, which I re-verified.
- **Page total:** 1,676 - 104 + 111 - 88 + 38 = **1,633**. Adding the 4 Platform tags (8 words) and the 7 figures gives **1,648**. Both match Build's figures and are inside 1,500-1,700.
- **Budget variance (not a failure):** Block 7 is below its 55-65 budget. That follows from the Content Writer's request for label-only tiles.

## 3. Keywords: PASS
An exact-phrase, case-insensitive search of the page copy finds **15 instances**, the same as v3.
- **Positions:** each one sits at the same place as in v3. Line numbers moved by +3 through Block 2, +5 through Block 7 and +7 after it. That is exactly the effect of the added lines in the changed blocks.
- **field service CRM software:** still appears once in the Block 2 lede (v4 line 65), in the unchanged sentence "Tailored by HLB HAMT, SugarAI works as field service CRM software, giving sales, service and field teams one shared record with AI built in."
- **New copy:** the new Block 2 and Block 7 copy contains no keyword and no excluded phrase. No sentence holds two different keywords.
- **Meta lines:** the meta title, meta description and H1 are unchanged.

## 4. Revised sections read naturally: PASS (advisories only)
- **Grammar and spelling:** no errors. British spelling is consistent ("enquiries", "towards").
- **Tone:** no stock AI phrases. The three stat descriptions open differently ("Repairs and upgrades...", "More enquiries...", "AMC renewals...") and use different sentence shapes.
- **Block 7 tile length:** all four tiles are short labels with no full stop, so they meet the brief.
  - "Quicker service campaign creation" (4 words)
  - "Reduced service team workload" (4 words)
  - "Higher click-through on maintenance reminders" (5 words)
  - "ERP and back-office integrations" (4 words)
- **Advisories (optional):**
  - **Tile 1 misreads at first.** "Quicker service campaign creation" first reads as "quicker service". Suggested: "Quicker creation of service campaigns". Also see A.
  - **Stat 3 description is about speed, not growth.** The label is "Pipeline growth", but "enter the pipeline sooner" describes speed. The rewrite in 5c below also fixes this.
  - **Block 7 lede has no main verb.** "Results SugarCRM customers report after moving..." is a fragment. The Insurance template's lede is one too, so this is acceptable as series style.

## 5. Originality: FAIL
I compared v4 with `inputs/template-source/hlbhamt-sugarai-insurance.html` (lines 284-300 and 437-444). I also searched the web for the distinctive new phrases and found no matches elsewhere.

The short metric labels ("Increased revenue", "Pipeline growth", tile labels) are tied to the series' vendor figures. Reusing them is a structural convention, not a violation. Two sentences and one clause, though, repeat the template's sentence frame and swap in synonyms:

**5a. Block 2 lede, sentence 2: close paraphrase of Insurance stat 1's description.**
- Insurance: "Actual business results **reported by SugarAI customers running sales and** quotation **on the platform**."
- v4: "The figures below show SugarAI's own impact, as **reported by SugarCRM customers** who run their **sales and** service operations **on the platform**."
- The matching clause is about 12 words long, in the same order, with synonyms swapped in.

**5b. Block 7 lede: close paraphrase of the Insurance proof lede.**
- Insurance: "**Outcomes SugarCRM customers report from** renewal, cross-sell and service **campaigns run on the platform**."
- v4: "**Results SugarCRM customers report after** moving service desk, **campaign** and field workflows **onto the platform**."
- Both have the same frame, "[Outcomes/Results] SugarCRM customers report [from/after] X, Y and Z ... on(to) the platform", and both are 15 words.

**5c. Block 2 stat 3 description: tail clause echoes the template (minor).**
- Insurance: "...keep more opportunities **moving toward** bind."
- v4: "...and **keep moving towards** signature."
- Only the insurance closing word ("bind") has been swapped for a field service one ("signature").

## 6. Outside Blocks 2 and 7 identical to v3: PASS
- **Line-by-line comparison:** I compared every page-copy line in Blocks 1, 3-6 and 8-14, plus the meta lines and page chrome. None differ.
- **Exact-match searches:** I ran anchored, exact regex searches for 30 full-line strings in both files. They covered:
  - the hero lede and side row 3
  - the Platform lede and card 4
  - the Benefits lede and tiles 1, 5 and 6
  - Services 01, 05 and 08, and the Services H2
  - the segments tile 3 link line
  - the UAE lede and market item 6
  - the Process H2 and callout body
  - Why HLB HAMT cards 1, 3 and 4
  - FAQ A1-A7 and Q7
  - both CTA H2s and closing row 3
- **Result:** each string matches exactly once in v3 and once in v4 (13/13 and 18/18). The only other differences are outside page copy: the notes, the intro paragraph, Sources, Stats used and Flags.

## 7. Factual framing: PASS (as scoped)
- **No pricing or cost claims in either band.** Neither band contains a currency, price or saving. The words "cost" and "pricing" appear only in unchanged v3 copy: Services 04, Why card 1, FAQ Q1/A1 and closing row 3.
- **No benchmark or market framing.** "benchmark", "market data" and "market figures" appear nowhere in page copy. The Block 7 lede now attributes the figures to SugarCRM customers.
- **Footnotes removed.** There are no `[n]` footnote markers left in page copy.

## Extra finding A: the figures are relabelled as metrics their sources don't claim (Content Writer decision, not a Build defect)

I found the source of the Block 7 figures: SugarCRM's Sugar Market data sheet, the marketing automation product (https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Market.pdf, Rev. 08092022). It reads: "Accelerate Campaign Creation +95%", "Reduce Team Workload -50%", "Increase Click-Through Rates +25%", "Actual business results from SugarCRM customers."

These are **marketing team** outcomes from a 2022 document. The Block 2 figures, according to search results for the Sugar Sell overview (sugarcrm.com is blocked here, so I could not open it), are "+23% improved revenue, +30% improved win rate, 3x pipeline volume". Those are sales metrics.

v4 narrows or changes several of them:
- **Tile 2, "Reduced service team workload":** the source says marketing team workload, not service team workload.
- **Tile 3, "Higher click-through on maintenance reminders":** the source gives click-through across campaigns in general. Maintenance reminders are not a measured category.
- **Block 7 lede:** "after moving service desk, campaign and field workflows onto the platform" suggests results from service and field workflows. The source measured only marketing.
- **Block 2, stat 2, "Improved conversion rate":** the source metric is win rate, which is a different metric.
- **Tile 4, "180+":** it is not in the Sugar Market sheet. I found no source for it.

Build's Flag 3 already raises the general risk. These specific labels make it concrete.

**Recommended source-faithful labels.** These keep the site convention and stay short:
- Tile 1: "Quicker creation of service campaigns" (Sugar Market campaigns can fairly include service campaigns)
- Tile 2: "Reduced campaign team workload"
- Tile 3: "Higher campaign click-through rates"
- Stat 2: "Improved win rate"

## Fix instructions (for Build, once the Content Writer has ruled on A)

1. **Block 2 lede, sentence 2 (fixes 5a and addresses A).** Replace "The figures below show SugarAI's own impact, as reported by SugarCRM customers who run their sales and service operations on the platform." (22 words) with "The three figures below are SugarAI's own results: sales gains that SugarCRM customers across industries have recorded." (16 words). Do not touch sentence 1, which carries the keyword.
2. **Block 7 lede (fixes 5b and addresses A).** Replace "Results SugarCRM customers report after moving service desk, campaign and field workflows onto the platform." (15 words) with "These figures come from SugarCRM customers and the platform itself, and cover campaign work and system integration." (17 words). Do not use "report ... on the platform" or "results ... report" framing.
3. **Block 2 stat 3 description (fixes 5c and the label-fit advisory).** Replace "...enter the pipeline sooner and keep moving towards signature." with "...enter the pipeline sooner and stall less often before signature." (17 words, +1).
4. **Labels (only if the Content Writer accepts A).** Apply the four labels listed under A. They are word-neutral as a set. If stat 2 becomes "Improved win rate", change its description to "More quotes are won when the desk builds them from each customer's contract and asset history." (17 words, neutral).
5. **Recheck after editing.** Fixes 1-3 give a page total of 1,633 - 6 + 2 + 1 = **1,630** (1,645 with tags and figures), and Block 2 becomes 106 words. Recheck the em dash count (0) and the keyword count (15).
6. **Brief record.** As Build's Flag 2 says, the override should still be recorded in brief Section 10.
