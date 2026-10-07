# Sources log: SugarAI CRM + Epicor ERP Integration (service/integration subpage)

- Page: `epicor-sugarai-integration` (`.docx`, `.html`, `.pdf` in this folder)
- Content version: `draft/draft-v3.md` (Test PASS, `draft/test-report-v3.md`, loop 3 of 3). Two optional QA advisories were applied at delivery: G5 (closing CTA row 3 drops "Then") and T7 (process step 6 reads "supported by our service desk"). Neither line carries a stat or a sourced fact.
- Compiled from: the draft-v3 "Stats used" table, its "Unfootnoted facts" list and its Sources note [1] to [5]. Nothing added or dropped.
- Footnote convention: inline markers `[n]` in Blocks 2, 5, 7 and 9 link to one Sources note placed after the FAQ and before the closing CTA. FAQ answers carry no inline markers, so the FAQPage JSON-LD can repeat them word for word. Source [5] supports FAQ 4 without a marker.

## Verification status

| Source | Status |
|:-|:-|
| [1] Nucleus Research, Z56 case study | **Verified.** Fetched by Plan; re-fetched by Test on 2026-10-07 (test-report-v3, item 6). The 7% and ~50% figures and their metric names match. |
| [2] Avasant, "Breaking Down Data Silos" | **Verified.** Fetched by Plan; re-fetched by Test on 2026-10-07. The 2.3x figure (with its mid-sized-enterprise cohort qualifier) and the "over 60%" figure match. |
| [3] Nucleus SFA Technology Value Matrix 2026 | **Partly verified.** The 01net reprint was fetched and re-checked by Test. **The Business Wire original returned 403 and still needs a human click-check.** |
| [4] Khaleej Times, 10 June 2026 | **Verified.** Fetched by Plan; re-fetched by Test on 2026-10-07. |
| [5] SugarAI rebrand press release | **Not verified: search-result text only.** Needs a human click-check (sugarai.com press release and the Business Wire original). |
| F3, F4 support.sugarai.com user guides | **Not verified: search-result text only.** Needs a click-check. |
| F5 knowledgelib.io Epicor REST v2 explainer | **Not verified: search-result text only.** Needs a click-check. |

**Every URL below should be click-checked once more before publication.**

## Stats and data points (footnoted)

| ID | Stat exactly as it appears on the page | Section where it appears | Source | Source URL | Footnote | Verified? |
|:-|:-|:-|:-|:-|:-|:-|
| N1 | "7%" / "Higher win rates" / "The win-rate improvement Nucleus Research found among Sugar customers who brought CRM and ERP data together." | Block 2, "What connected CRM and ERP data delivers" (stats band), stat 1 | Nucleus Research ROI case study Z56, "How unifying CRM and ERP with Sugar drives sales performance", 8 April 2025 (source text: "improvement in win rates") | https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/ | [1] | Yes (re-fetched 2026-10-07) |
| N2 | "~50%" / "Shorter customisation timelines" / "The approximate reduction in customisation timelines reported by Sugar customers in that same Nucleus Research study." | Block 2, stat 2 | Same Nucleus study (source text: "approximate 50 percent reduction in customization timelines") | https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/ | [1] | Yes (re-fetched 2026-10-07) |
| A1 | "2.3×" / "Customer satisfaction gains" / "How much likelier mid-sized enterprises that prioritise interoperability and eliminate data silos are to see measurable satisfaction gains, Avasant found." | Block 2, stat 3 | Avasant article, data from Avasant's Cloud CRM Suites 2024 RadarView, September 2025 (source text: "mid-sized enterprises that prioritize interoperability and eliminate data silos are 2.3x more likely to achieve measurable improvements in customer satisfaction") | https://avasant.com/report/breaking-down-data-silos-why-crm-integration-is-now-a-boardroom-priority/ | [2] | Yes (re-fetched 2026-10-07) |
| A2 | "according to Avasant, more than 60% of enterprises still operate with fragmented data environments." | Block 5, "The business case for one shared customer record", prose sentence 2 | Same Avasant article (source text: "over 60% of enterprises") | https://avasant.com/report/breaking-down-data-silos-why-crm-integration-is-now-a-boardroom-priority/ | [2] | Yes (re-fetched 2026-10-07) |
| U1 | "UAE industrial exports passed AED 262 billion in 2025." | Block 9, "Why choose HLB HAMT as your CRM integration partner", paragraph sentence 1 | Khaleej Times, "UAE industrial exports hit Dh262b as sector's GDP contribution climbs by 70%", 10 June 2026 (UAE Ministry of Industry and Advanced Technology figure) | https://www.khaleejtimes.com/business/uae-industrial-exports-hit-dh262b-as-sectors-gdp-contribution-climbs-by-70 | [4] | Yes (re-fetched 2026-10-07) |

## Sourced non-stat facts

| ID | Fact exactly as it appears on the page | Section where it appears | Source | Source URL | Footnote | Verified? |
|:-|:-|:-|:-|:-|:-|:-|
| F1 | "Nucleus Research named Sugar a Leader in its 2026 Sales Force Automation Technology Value Matrix, Sugar's sixth straight year as a Nucleus Leader, and listed ERP-informed insight among its strengths." | Block 7, "Epicor data wherever your teams work", paragraph 2 | Business Wire release, 25 February 2026 | https://www.businesswire.com/news/home/20260225695547/en (reprint: https://www.01net.it/sugarcrm-named-a-leader-in-the-nucleus-research-sales-force-automation-technology-value-matrix-2026/) | [3] | Reprint yes; **Business Wire original not opened (403)** |
| F2 | "The April 2026 rebrand from SugarCRM to SugarAI left existing instances running as they were." | Block 11, FAQ 4 answer ("We already run SugarCRM. Can you connect our existing instance to Epicor?") | SugarAI press release, "SugarCRM Unveils New Brand Identity as SugarAI", 13 April 2026 | https://sugarai.com/press-releases/sugarcrm-unveils-new-brand-identity-as-sugarai-declaring-the-next-generation-of-crm (Business Wire original per brief Section 6b: https://www.businesswire.com/news/home/20260413034429/en/SugarCRM-Unveils-New-Brand-Identity-as-SugarAI-Declaring-the-Next-Generation-of-CRM) | [5], no inline marker | **No** (search snippet only) |

## Unfootnoted facts (sources log only, per brief Section 6b)

| ID | Fact as it appears on the page | Section where it appears | Source URL | Verified? |
|:-|:-|:-|:-|:-|
| F3 | "Sugar Connect, SugarAI's add-in for Outlook, lets people look up, create and update SugarAI records from their inbox, sync contacts and calendars, and file emails to the right account." | Block 7, paragraph 1 | https://support.sugarai.com/documentation/plug-ins/sugar_connect/sugar_connect_user_guide/ | **No** (search snippet only) |
| F4 | "On the road, the SugarAI mobile app for iOS and Android opens the same account." | Block 7, paragraph 1 | https://support.sugarai.com/documentation/mobile_solutions/sugarai-mobile-app/sugarai-mobile-app-user-guide/ | **No** (search snippet only) |
| F5 | "Both use Epicor's REST services and saved queries (BAQs)." (Block 3); "The connection runs on Epicor's REST services, available in both" (FAQ 1 answer) | Block 3, paragraph 2; Block 11, FAQ 1 answer | https://knowledgelib.io/business/erp-integration/epicor-rest-api-v2/2026 (secondary explainer; Epicor's own REST help is per-instance) | **No** (search snippet only) |
| F6 | HLB HAMT company facts: "26 years in the UAE and GCC", "Certified SugarAI partner", "backed by the global HLB network", "Six to ten weeks", "2.5 to 5 months", "rehearsed at least twice", retesting after SugarAI releases, named service manager, service desk | Block 9 tiles; Block 10 steps and callout; Block 8 item 06; FAQ 5 | Live hub https://hlbhamt.com/sugarai-crm-2/ | Company facts (series convention: no footnote). Test matched them to the saved hub text. |

## Not used or not sourced (by design)

- No stat from the FSM, Insurance or homepage briefs is reused. The Nucleus 8% recurring-revenue figure (FSM proof tile) is not used (brief Section 10 point 6).
- The page contains no pricing or cost figures.

## Internal links (also to be click-checked before publication)

Deliver could not confirm these resolve: hlbhamt.com returns a captcha interstitial to automated requests, for real and non-existent paths alike.

| Anchor text | Target | Location |
|:-|:-|:-|
| CRM Solutions (SugarAI) | https://hlbhamt.com/sugarai-crm-2/ | Breadcrumb parent (brief Section 10 point 3) and footer |
| Technology Consulting Services | https://hlbhamt.com/services/technology-consulting-services-dubai-uae/ | Breadcrumb |
| manufacturers and distributors | https://hlbhamt.com/industries/manufacture-and-distribution/ | Block 1, hero side-panel sub-line; footer ("Manufacturing & distribution") |
| SugarAI CRM services | https://hlbhamt.com/sugarai-crm-2/ | Block 8, item 02 body |
| ERP practice | https://hlbhamt.com/services/erp-integration-add-ons/ | Block 9, tile 3; footer ("ERP integration & add-ons") |
| Talk to our integration team | /contact/ | Block 12 (closing CTA) button |
| SugarAI for manufacturers (conditional link 4) | /sugarai-crm/industries/manufacturing/ | **Omitted**, as in draft-v3 Flag 8, because the URL could not be confirmed |
