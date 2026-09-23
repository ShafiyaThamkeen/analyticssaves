# Sources log: SugarAI for Field Service Management (industry subpage)

- Page: `sugarai-field-service-management` (`.docx`, `.html`, `.pdf` in this folder)
- Content version: `draft/draft-v5.md` (approved; replaces v3). The Block 7 H2 is "What the service desk and ERP layers deliver", per the fix in `draft/test-report-v5-revision.md`.
- Compiled from: draft-v5 "Stats used" table and "Sources" footnote list. Nothing added or dropped.
- Removed since the v3 delivery: Grand View Research (MEA FSM market), Mordor Intelligence (GCC FM), Mordor Intelligence (UAE FM), Aquant 2025 benchmark, Mordor Intelligence (global FSM) and DataReportal (UAE). None of them appears on the page any more.

## Verification status

| Source | Status |
|:-|:-|
| Sugar Sell data sheet (AWS Marketplace copy) | **Verified.** The Plan agent read the PDF in full and Test re-checked it (see `draft/test-report-v5-revision.md`, item 2). The +23% / +30% / 3x figures and their metric names match. |
| Sugar Serve data sheet (AWS Marketplace copy) | **Verified.** The Plan agent read the PDF in full and Test re-checked it. The -27% / +30% figures and their metric names match. |
| Official sugarcrm.com / sugarai.com copies of both data sheets | **Not verified.** Neither could be reached from the sandbox. Someone should confirm that the figures still match there after the rebrand. |
| Nucleus Research, 8% figure | **Not verified: search-result text only.** Nobody opened the Nucleus page or the sugarai.com resource page ("Sugar's ERP integration increases recurring revenue by 8%"). Confirm the 8% figure, that it measures recurring revenue, and that it applies to Sugar customers with ERP integration. One search summary tied it to the sales-i integration; see the Test report, advisory 2b. |
| FAQ 7 press release (source 1) | **Not verified: search-result text only.** Needs a click-check. |

**Every URL below needs a human click-check before publication.** The two AWS Marketplace PDFs have been read, but they should still be opened once more to confirm the links resolve.

## Stats and data points

These figures carry no on-page footnote, per the site's convention for vendor figures. Where each one comes from is stated in the visible copy instead: the Block 2 lede names SugarCRM and Sugar Sell, the Block 7 lede names SugarCRM and Sugar Serve, and the Block 7 tile 3 label names Nucleus Research.

| # | Stat exactly as it appears on the page | Section where it appears | Source | Source URL | Verified? |
|:-|:-|:-|:-|:-|:-|
| W1 | "+23%" / "Increased revenue" / "Sugar Sell customers grew revenue by this margin." | Block 2, "Why SugarAI earns its place in field operations", stat 1 | Sugar Sell data sheet, "Sugar Sell: AI-Powered Sales and Intelligent Account Management", © 2024 SugarCRM Inc. (source text: "Increased Revenue + 23%") | https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Sell.pdf | Yes (AWS copy read in full) |
| W2 | "+30%" / "Improved win rate" / "Win rates rose across that customer group." | Block 2, stat 2 | Same Sugar Sell data sheet (source text: "Improved Win Rate + 30%") | https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Sell.pdf | Yes (AWS copy read in full) |
| W3 | "3×" / "Pipeline volume" / "Pipelines tripled in volume for those customers." | Block 2, stat 3 | Same Sugar Sell data sheet (source text: "Pipeline Volume 3x") | https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Sell.pdf | Yes (AWS copy read in full) |
| P1 | "-27%" / "Reduced case error rate" | Block 7, "What the service desk and ERP layers deliver", tile 1 | Sugar Serve data sheet, "Platform for Customer Service Heroes", Rev. 08152022 (source text: "Reduced Case Error Rate - 27%") | https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Serve.pdf | Yes (AWS copy read in full) |
| P2 | "+30%" / "Revenue contribution from support teams" | Block 7, tile 2 | Same Sugar Serve data sheet (source text: "Revenue Contribution from Support Team + 30%") | https://sugarcrm-aws-marketplace-public-assets.s3.amazonaws.com/Sugar+Serve.pdf | Yes (AWS copy read in full) |
| P4 | "8%" / "Higher recurring revenue with ERP integration (Nucleus Research)" | Block 7, tile 3 | Nucleus Research, "How unifying CRM and ERP with Sugar drives sales performance", 2025 (search-result text: "8% average boost in recurring revenue") | https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/ | **No** (search snippet only) |

## Non-stat fact with a source (the page's only footnote)

| # | Footnote | Fact exactly as it appears on the page | Section where it appears | Source URL | Verified? |
|:-|:-|:-|:-|:-|:-|
| 1 | Source 1 (`<li id="src-1" value="1">` in the Sources note under the FAQ). There is no inline marker, so the FAQPage JSON-LD can repeat the visible answer word for word. | "SugarCRM became SugarAI in April 2026, and existing instances keep running." | Block 13, FAQ 7 answer ("Questions field service teams ask us") | https://sugarai.com/press-releases/sugarcrm-unveils-new-brand-identity-as-sugarai-declaring-the-next-generation-of-crm | **No** (search snippet only) |

## Not sourced (by design)

- "26 years" (Block 12, "Regional delivery depth" card) is an HLB HAMT company fact that the Content Writer confirmed in brief Section 10.4. It is not a sourced stat.
- The page contains no pricing or cost figures.

## Internal links (also to be click-checked before publication)

| Anchor text | Target | Location |
|:-|:-|:-|
| CRM Solutions (SugarAI) | https://sugarai.com/ | Breadcrumb parent and footer (brief Section 10.2) |
| SugarAI CRM solutions | https://sugarai.com/ | Block 3 (Platform) lede |
| SugarAI for manufacturers | /sugarai-crm/industries/manufacturing/ | Block 9 (Who we serve), tile 3 |
| technology consulting services | /services/technology-consulting-services-dubai-uae/ | Block 12 (Why HLB HAMT), card 3; also the breadcrumb |
| Manufacturing / Real Estate / Distributors / All industries | /sugarai-crm/industries/manufacturing/, /real-estate/, /distributors/, /sugarai-crm/industries/ | Footer (reused from the template) |
| Talk to our field service team | /contact/ | Block 14 (closing CTA) button |
