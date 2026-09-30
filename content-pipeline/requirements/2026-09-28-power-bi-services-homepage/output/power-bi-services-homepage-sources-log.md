# Sources log: Power BI Services homepage

- **Page:** `power-bi-services-homepage` (`.docx`, `.html` and `.pdf` in this folder, plus `power-bi-services-homepage-insurance-format.docx`). This is a working file name only; the final URL is still undecided (brief Section 10, point 3).
- **Content version:** `draft/draft-v8.md` (Test PASS in `draft/test-report-v8.md`; Revision 4 correction on top of Revisions 2 and 3). This log replaces the earlier 29 September log, which was built from draft-v7.
- **Compiled from:** the "Stats used" table and the "Sources" list in draft-v8. Nothing was added or dropped. The only change is the footnote numbering (see below).
- **Link text rule:** every source link in this log and in the page files shows the source's description as its visible text. The raw URL is used only as the link target.

## Footnote renumbering (draft IDs to page numbers)

The draft keeps the brief's source IDs. The rendered page numbers footnotes **by order of first appearance**, and the `.html`, `.docx`, `.pdf` and Insurance-format `.docx` all use the same numbers.

| Draft ref | Brief ID | Page footnote | First appears in |
|:-|:-|:-|:-|
| [9] | F3 | **1** | S1 deployment line |
| [1] | CS1 | **2** | S2 strip, item 1 |
| [12] | CS5 | **3** | S2 strip, item 2 |
| [3] | S-3 | **4** | S2b recognition bar |
| [7] | F1 | **5** | S5 row 2 |
| [6] | CS3 | **6** | S9 H2 |
| [8] | F2 | **7** | S14 FAQ 2 |
| [11] | F5 | **8** | S14 FAQ 6 |
| [10] | F4 | **9** | S14 FAQ 6 |

**Retired and absent from every output file:**
- **Draft [2]:** a single-engagement report load-time figure, retired in Revision 4. It was traced to a competitor's own published engagement result rather than an HLB HAMT result, and was removed with no substitute. Its source entry is gone too; the strip now has 3 items.
- **The fixed-price accelerator offer** (price, terms and deliverables; it carried no footnote), retired in Revision 4 for the same reason. S10 is now the 4-tab engagement matrix only.
- **Draft [4]:** the platform-adoption customer figure, retired in Revision 3.
- **Draft [5]:** the UAE generative-AI usage statistic, retired in Revision 2.

Page order of markers: 1 (S1), 2 (S2), 3 (S2), 4 (S2b), 5 (S5 row 2), 6 (S9), 3 (S11 tile 5), 5 (FAQ 1), 7 (FAQ 2), 8 (FAQ 6), 1 (FAQ 6), 9 (FAQ 6), 9 (FAQ 8).

Every marker points to a live source, and each of the 9 sources is cited at least once. No orphaned marker or source entry remains.

## Stats and verified facts (in page footnote order)

| Page fn | Draft ref / brief ID | Stat or fact exactly as it appears in the content | Section | Source |
|:-|:-|:-|:-|:-|
| 1 | [9] / F3 | S1: "in Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud region. Dubai runs every data workload; Abu Dhabi supports Power BI only." FAQ A6: "Data can be kept in-country in the Dubai or Abu Dhabi cloud region" | S1 deployment line; FAQ 6 | [Microsoft Learn, cloud region availability for Power BI and Microsoft's data platform](https://learn.microsoft.com/en-us/fabric/admin/region-availability) |
| 2 | [1] / CS1 | `200+` / "Power BI connectors; we configure yours and build missing ones." | S2 item 1 only | [Microsoft Learn, "Data sources in Power BI Desktop"](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-sources) |
| 3 | [12] / CS5 | `Since 1999` / "A licensed UAE audit, tax and advisory firm that also builds your data platform." | S2 item 2 | [HLB HAMT press release, "HLB HAMT Celebrates 25 Years of Unwavering Excellence"](https://hlbhamt.com/press-room/hlb-hamt-celebrates-25-years-of-unwavering-excellence/); also [HLB HAMT About Us anniversary page](https://hlbhamt.com/about-us/25-years-of-excellence/) (founded as HAMT & Associates in 1999; joined HLB International in 2007) |
| 3 | [12] / CS5 (optional) | "An HLB International member since 2007, bringing the standards and reach of a global advisory network." | S11 tile 5 | Same source as the row above (same source, different fact) |
| 4 | [3] / S-3 | "Microsoft was named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." | S2b only | [Microsoft, "Microsoft named a Leader in the 2026 Gartner Magic Quadrant for Analytics and BI Platforms" (Power BI Updates Blog)](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Microsoft-named-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for/ba-p/5262403); [verbatim repost](https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/) |
| 5 | [7] / F1 | S5 row 2: "the cloud service where your reports are published as apps, refreshed on schedule and secured by role." FAQ A1: "Power BI Desktop is a free, installable application for connecting to data, modelling it and designing reports." | S5 row 2; FAQ 1 | [Microsoft Learn, Power BI service vs Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/fundamentals/service-service-vs-desktop) |
| 6 | [6] / CS3 | H2 "A Working Power BI Dashboard on Your Data in 7 Days"; intro qualifier "for a defined use case" | S9 only | [HLB HAMT service commitment](https://hlbhamt.com/services/power-bi-dashboard-development/) ("a Power BI proof of concept can be delivered in as little as 7 days for defined use cases") |
| 7 | [8] / F2 | "At the time of writing, Microsoft's list prices are US$14 per user per month for Pro and US$24 for Premium Per User, unchanged since 1 April 2025." | FAQ 2 only | Microsoft Power BI [pricing update](https://powerbi.microsoft.com/en-us/blog/important-update-to-microsoft-power-bi-pricing/) and [pricing page](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing) |
| 8 | [11] / F5 | "Power BI falls within the scope of Microsoft's ISO/IEC 27001 and SOC 2 audits." | FAQ 6 only | Microsoft Learn, [ISO/IEC 27001](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001) and [SOC 2](https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2) offerings |
| 9 | [10] / F4 | FAQ A6: "Outside the US and EU data boundaries, Power BI's AI assistant stays off unless an admin allows cross-region processing". FAQ A8: "It runs only on paid capacity, a higher-tier licence bought for the whole organisation; Pro and Premium Per User on their own are not enough" and "Prompts are officially supported in English only for now" | FAQ 6; FAQ 8 | [Microsoft Learn, overview of the generative AI assistant in Power BI](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction) |

### Gartner disclaimer (footnote 4)

This text appears in the page's Sources note directly under footnote 4, in the `.html`, `.docx`, `.pdf` and the Insurance-format `.docx`:

> Gartner does not endorse any vendor, product or service depicted in its research publications. GARTNER and MAGIC QUADRANT are registered trademarks of Gartner, Inc. and/or its affiliates.

## HLB HAMT facts (no footnote)

| Fact | Exact wording in the content | Section | Source |
|:-|:-|:-|:-|
| Implementation timelines | "two to four weeks" / "six to ten weeks" / "three to six months" / "a working prototype inside the first two weeks" | FAQ 10 only | HLB HAMT prepared content (brief Section 10, point 4); no footnote, see Flags item 10 |

No stat appears in more than one section. Footnotes 1, 3, 5, 9 are each cited in more than one place, but they support a different fact or a factual explanation each time, as listed above. No FAQ restates 200+, 1999, the 19th year or 7 days. The meta description's "7-day" is meta copy, not on-page copy.

## Verification status

- **Re-checked live by the Test agent on 2026-09-29** (test-report-v7, item 6; test-report-v8 confirms no stat or its wording changed in v8):
  - Footnote 1: region availability page, ms.date 25 Sep 2026.
  - Footnote 9: AI-assistant overview, ms.date 24 Aug 2026.
  - Footnote 7: pricing page. Pro "$14.00 user/month" and PPU "$24.00 user/month".
  - Footnote 4: the verbatim repost of the announcement.
- **Confirmed by Test against the brief and earlier loops, and unchanged:** footnotes 2, 3, 5, 6, 8.
- **Not independently re-fetched by Deliver.** Click-check every link once before publication. In earlier runs the announcement's host (footnote 4) and the pricing-update blog (footnote 7) returned HTTP 403 to automated fetches.

## Internal links (click-check before publication)

| Ref | Anchor text | Target | Location |
|:-|:-|:-|:-|
| L1 | digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ | S4 lede |
| L2 | SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ | S11 tile 4 |
| L3 | UAE Corporate Tax advisory | https://hlbhamt.com/services/corporate-tax-advisory-services-in-uae/ | S6 card 2 (back) |
| L4 | Power BI automation | [HLB HAMT insight on Power BI automation](https://hlbhamt.com/insights/unlocking-power-bi-automation-with-power-automate/) | S14 FAQ 4 |
| L5 | data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ | S14 FAQ 6 |
| L6 | Power BI dashboard development | https://hlbhamt.com/services/power-bi-dashboard-development/ | S7 item 03 |
| L7 | data visualisation services | https://hlbhamt.com/services/data-visualization-uae/ | S6 intro |
| P2 | advanced analytics services | `/services/advanced-analytics-services/` | S6 card 6 (back). **Placeholder, kept exactly as in draft-v8.** The Advanced Analytics page has since been delivered for `https://hlbhamt.com/services/advanced-data-analytics-uae/` (its sources log asks for this link to be updated). Confirm and swap the target before go-live. |
| In-page | proof of concept; above | #methodology | S4 card 3; S10 Explore tab |
| In-page | engagement models; hero button "See our engagement models" | #packages | S14 FAQ 2; S1 |
| S0 | Breadcrumb: Home / Technology Consulting Services / Digital Transformation & Analytics | https://hlbhamt.com/ ; https://hlbhamt.com/services/technology-consulting-services-dubai-uae/ ; https://hlbhamt.com/services/digital-transformation-uae/ | S0 |
| S2b | Read Microsoft's announcement (button) | Same target as footnote 4 | S2b |

**Not linked anywhere, per brief 12.9:** the partner and consulting redirect-candidate pages.

## Carry-forward notes (outside these files)

- **Replace the live page promptly.** The page may already be live with the content Revision 4 removed; the regenerated `.html` should replace it as soon as the final URL is settled.
- **Reverse link, a manual edit to the live SugarAI CRM page:** on https://hlbhamt.com/sugarai-crm-2/, in the "Why UAE Businesses Choose HLB HAMT for SugarAI" grid, the "Dual AI intelligence" tile, link the words "Power BI analytics" to this page's final URL once it is decided.
- **Brief 12.12 live-site issues:**
  - The consulting page shows theme demo testimonials and demo "success story" percentages, none of them HLB HAMT results.
  - Sibling pages still carry outdated claims ("14+ Yrs Gartner #1", "~$15/user/month", an English-or-Arabic question feature, "ISO 27001/SOC 2 compliant", and a competitor price comparison). They will contradict this page once it is live.
  - The live Data Visualization page (`/services/data-visualization-uae/`) still publishes the retired single-engagement load-time claim (brief 12.1 N1; test-report-v8). That is outside this page's scope.
  - The site nav still says "Celebrating 25 Years".
- **Final URL and redirects** (brief Section 10, point 3, and Section 13, point 1): still open. This blocks go-live, not delivery.
