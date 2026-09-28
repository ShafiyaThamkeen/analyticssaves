# Sources log: Microsoft Power BI Services homepage

- Page: `power-bi-services-homepage` (`.docx`, `.html` and `.pdf` in this folder). This is a working file name only. The final URL is still undecided (brief Section 10, point 3).
- Content version: `draft/draft-v4.md` (approved; R1-R5 from `draft/test-report-v3.md` applied).
- Compiled from: the "Stats used" table and "Sources" footnote list in draft-v4. Nothing was added or dropped. The only change is the footnote numbering (see below).

## Verification status

**Every URL in this log needs a human click-check before publication.** WebFetch was blocked for this whole pipeline run, so no agent has opened these pages in this session:

- The Plan agent got HTTP 403 from `community.fabric.microsoft.com` and `powerbi.microsoft.com`. It confirmed the Gartner 2026 claim through search results and a verbatim repost on mwpro.co.uk.
- The Plan agent reports that it opened the Microsoft investor, Microsoft Learn and Microsoft On the Issues pages directly.
- The Test agent re-confirmed [4], [6] and [7] through search in loop 3.

| Source | Status |
|:-|:-|
| Microsoft Learn pages (footnotes 1, 2, 5, 8, 11) | Read by the Plan agent. Needs a click-check to confirm the pages still resolve and still say the same thing. |
| Gartner 2026 announcement (footnote 4) | **Not opened directly** (403). Confirmed through search results and the mwpro.co.uk repost. Click-check required. |
| Microsoft FY26 Q4 earnings call (footnote 6) | Read by the Plan agent. Re-confirmed by the Test agent through search. |
| Microsoft On the Issues, AI diffusion (footnote 7) | Read by the Plan agent. Re-confirmed by the Test agent through search. |
| Microsoft pricing blog and pricing page (footnote 10) | **Not opened directly**, because `powerbi.microsoft.com` returned 403. Click-check the US$14 / US$24 list prices. |
| HLB HAMT internal claims (footnotes 3 and 9, plus the PowerUP! and timeline facts) | No public source. Approved for publication by the Content Writer (brief Section 10, point 4). |

## Footnote renumbering (test-report-v3, carry item (h))

The brief and draft numbered footnotes 1-11 by source type. The rendered page now numbers them **by order of first appearance**. The same numbers are used in the `.html`, `.docx` and `.pdf`.

| Draft / brief ref | Page footnote | First appears in |
|:-|:-|:-|
| [9] (F3) | **1** | S1 deployment line |
| [1] (CS1) | **2** | S2 strip, item 1 |
| [2] (CS2) | **3** | S2 strip, item 2 |
| [3] (S-3) | **4** | S2b recognition bar |
| [7] (F1) | **5** | S5 row 2 |
| [4] (S1) | **6** | S5 platform layer |
| [5] (S2) | **7** | S6 lede |
| [10] (F4) | **8** | S6 point 1 ("Answers") |
| [6] (CS3) | **9** | S10 H2 |
| [8] (F2) | **10** | FAQ 2 |
| [11] (F5) | **11** | FAQ 6 |

## Stats and verified facts (in page footnote order)

| Page fn | Draft ref / brief ID | Stat or fact exactly as it appears on the page | Section | Source URL |
|:-|:-|:-|:-|:-|
| 1 | [9] / F3 | S1: "Data can stay in-country in Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud regions. The Dubai region runs the full Fabric platform; the Abu Dhabi region supports Power BI only." FAQ 6: "Your data can be hosted in Microsoft's Dubai or Abu Dhabi cloud regions" | S1 deployment line; S15 FAQ 6 | https://learn.microsoft.com/en-us/fabric/admin/region-availability |
| 2 | [1] / CS1 | `200+` / "Data connectors in Power BI, from ERP and CRM to cloud databases." | S2 strip, item 1 only | https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-data-sources |
| 3 | [2] / CS2 | `33x` / "Faster report load times in one recent HLB HAMT engagement." | S2 strip, item 2 only | None. HLB HAMT internal engagement, per HLB HAMT's prepared content. On-page source note reads "HLB HAMT client engagement (internal). No public source." |
| 4 | [3] / S-3 | "Microsoft: named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." | S2b recognition bar only | https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Microsoft-named-a-Leader-in-the-2026-Gartner-Magic-Quadrant-for/ba-p/5262403 (repost confirming the text: https://mwpro.co.uk/blog/2026/07/03/microsoft-named-a-leader-in-the-2026-gartner-magic-quadrant-for-analytics-and-business-intelligence-platforms/) |
| 5 | [7] / F1 | S5 row 2: "It is the cloud side of the platform, where finished reports are published, bundled into apps, refreshed on schedule and secured." FAQ 1: "Power BI Desktop is Microsoft's free Windows application for connecting to data, building the semantic model and designing reports." | S5 row 2; S15 FAQ 1 | https://learn.microsoft.com/en-us/power-bi/fundamentals/service-service-vs-desktop |
| 6 | [4] / S1 | "Microsoft reports more than 40,000 paid Fabric customers, up more than 60% year on year." | S5 platform layer only | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4 |
| 7 | [5] / S2 | "in Q2 2026, 73.3% of the UAE's working-age population used generative AI tools, against 18.8% worldwide." | S6 lede only | https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/ |
| 8 | [10] / F4 | S6 point 1: "Copilot answers questions about an open report, summarises what each page shows and drafts DAX measures and new report pages..." FAQ 6: "Outside the US and EU data boundaries, Copilot is off by default unless an admin allows cross-region processing..." FAQ 8: "Fabric F2 or higher, or Premium P1 or higher, because Pro or Premium Per User licences alone do not include it" and "Microsoft officially supports English prompts only at present" | S6 point 1; S15 FAQ 6; S15 FAQ 8 | https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction (Q&A retirement context, not stated on the page: https://learn.microsoft.com/en-us/power-bi/natural-language/q-and-a-limitations) |
| 9 | [6] / CS3 | "A Working Power BI Dashboard on Your Data in 7 Days" | S10 H2 only | None (HLB HAMT service commitment) |
| 10 | [8] / F2 | "At the time of writing, Microsoft lists Power BI Pro at US$14 and Premium Per User at US$24 per user per month, the list prices since 1 April 2025." | S15 FAQ 2 only | https://powerbi.microsoft.com/en-us/blog/important-update-to-microsoft-power-bi-pricing/ ; https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing |
| 11 | [11] / F5 | "the platform sits within the scope of Microsoft's ISO/IEC 27001 certification and SOC 2 reports" | S15 FAQ 6 only | https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-27001 ; https://learn.microsoft.com/en-us/compliance/regulatory/offering-soc-2 |

### Gartner disclaimer (footnote 4)

This text is rendered in the page's Sources note directly under footnote 4, in all three formats:

> Gartner does not endorse any vendor, product or service depicted in its research publications. GARTNER and MAGIC QUADRANT are registered trademarks of Gartner, Inc. and/or its affiliates.

## HLB HAMT commercial facts (no footnote)

| Fact | Exact wording on the page | Section | Source |
|:-|:-|:-|:-|
| PowerUP! price, 5 terms and 6 deliverables | "$4,500 fixed-price accelerator", plus the terms and deliverables as listed | S11 featured card only | HLB HAMT prepared content. Confirmed current, in USD (brief Section 10, point 4). |
| Implementation timelines | "two to four weeks" / "six to ten weeks" / "three to six months" / "a working prototype arrives within two weeks" | S15 FAQ 9 only | HLB HAMT prepared content. Confirmed by the brief (Section 10, point 4). |

No stat appears in more than one section. No FAQ restates 200+, 33x, 19th year, 40,000, 73.3% or 7 days. The meta description's "7-day" is meta copy, not on-page copy.

## Internal links (also to be click-checked before publication)

| Anchor text | Target | Location | Status |
|:-|:-|:-|:-|
| digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ | S4 lede | Live (from the site nav) |
| Power BI automation with Power Automate | https://hlbhamt.com/insights/unlocking-power-bi-automation-with-power-automate/ | S6 point 3 ("Alerts") | Live (existing insight) |
| UAE Corporate Tax advisory | https://hlbhamt.com/services/corporate-tax-advisory-services-in-uae/ | S7 card 2 (back) | Live |
| SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ | S12 tile 4 ("Dual intelligence") | Live (brief Section 10, point 6) |
| data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ | S15 FAQ 6 | Live |
| advanced analytics services | `/services/advanced-analytics-services/` | S6 lede | **PLACEHOLDER. The sibling page is not built yet.** Confirm the slug before go-live. |
| data visualisation services | `/services/data-visualisation-services/` | S8 item 03 | **PLACEHOLDER. The sibling page is not built yet.** Confirm the slug before go-live. |
| Breadcrumb: Home / Technology Consulting Services / Digital Transformation & Analytics | https://hlbhamt.com/ ; https://hlbhamt.com/services/technology-consulting-services-dubai-uae/ ; https://hlbhamt.com/services/digital-transformation-uae/ | S0 | Live (from the site nav) |
| Read Microsoft's announcement (button) | The footnote 4 URL above | S2b | External, returned 403 to the Plan agent |

**Reverse link (manual edit to the LIVE SugarAI CRM page; not part of these files):** on https://hlbhamt.com/sugarai-crm-2/, "Why UAE Businesses Choose HLB HAMT for SugarAI" grid, tile "Dual AI intelligence" ("SugarAI prediction plus Power BI analytics, from one partner."), link the words "Power BI analytics" to this page's final URL once it is decided. Optionally, also link "dashboards" in the Packages › Integration tab item "Data & Analytics Integrations" ("Consolidate customer and business data for reporting, dashboards, and informed decision-making.").
