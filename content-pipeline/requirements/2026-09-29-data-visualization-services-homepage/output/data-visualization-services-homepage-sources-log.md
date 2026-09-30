# Sources log: Data Visualisation Services homepage

- **Page:** `data-visualization-services-homepage` (`.docx`, `.html` and `.pdf` in this folder).
- **Target URL:** `https://hlbhamt.com/services/data-visualization-uae/`. This page replaces the existing live page at that URL (brief Section 10, point 1). No redirect is needed. The `.html` canonical tag and the schema URL fields use this address.
- **Content version:** `draft/draft-v2.md`, the final draft (QA PASS in `draft/test-report-v2.md`, loop 2 of 3). No wording was changed in delivery, and none of Test's optional advisories was applied.
- **Compiled from:** the "Stats used" list and the "Sources" list in draft-v2. Nothing was added or dropped.
- **Link text rule:** every source link in this log and in the page files uses the draft's source description as its visible text. The raw URL is used only as the link target. No bare URLs appear in the page copy or the Sources note.

## Footnote numbering (draft to page)

Footnotes are numbered by order of first appearance on the rendered page. The draft's numbering already follows page order, so the numbers are unchanged. The `.html`, `.docx` and `.pdf` all use the same numbers.

| Draft ref | Brief ID | Page footnote | First appears in |
|:-|:-|:-|:-|
| [1] | S-1 | **1** | S2b recognition line |
| [2] | S-2 | **2** | S5 foundation layer block |
| [3] | S-3 | **3** | S9 delivery method intro |
| [4] | F1 | **4** | S14 FAQ 6 |

Page order of markers: 1 (S2b), 2 (S5), 3 (S9), 4 (FAQ 6). Each footnote is cited exactly once, and each marker has a matching entry in the page's Sources note. This was checked in the `.html` by anchor resolution (`#src-1` to `#src-4`), and in the `.docx` and `.pdf` by reading the text back.

## Stats and verified facts (in page footnote order)

| Page fn | Draft ref / brief ID | Stat or fact exactly as it appears in the content | Section | Source |
|:-|:-|:-|:-|:-|
| 1 | [1] / S-1 | "We build from the UAE, which ranked 9th of 69 economies in IMD's World Digital Competitiveness Ranking 2025 and 1st for talent." | S2b only | [UAE Government portal, "Global digital competitiveness" (updated 25 Nov 2025)](https://u.ae/en/about-the-uae/uae-competitiveness/global-digital-competitiveness) |
| 2 | [2] / S-2 | "the 1,579 professionals surveyed for BARC's Data, BI and Analytics Trend Monitor 2026 ranked data quality management first, level with data security and privacy." | S5 foundation layer block only | [BARC, "BARC publishes the Data, BI and Analytics Trend Monitor 2026" (12 Nov 2025)](https://barc.com/news/barc-publishes-the-data-bi-and-analytics-trend-monitor-2026/) |
| 3 | [3] / S-3 | "Only 22% of organisations Gartner surveyed had defined, tracked and communicated business impact metrics for most of their data and analytics use cases." | S9 intro only | [Gartner, "Gartner Survey Finds One-Third of CDAOs Cite Measuring Data, Analytics and AI Impact as Top Challenge" (20 Feb 2025)](https://www.gartner.com/en/newsroom/press-releases/2025-02-20-gartner-survey-finds-one-third-of-cdaos-cite-measuring-data-analytics-and-ai-impact-as-top-challenge) (corroborated by [BigDATAwire](https://bigdatawire.com/2025/02/24/cdoas-are-struggling-to-measure-data-analytics-and-ai-impact-gartner-report)) |
| 4 | [4] / F1 | "the UAE Personal Data Protection Law, Federal Decree-Law No. 45 of 2021." | S14 FAQ 6 only | [UAE Government portal, "Data protection laws"](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws) |

## HLB HAMT facts (no footnote)

| Fact | Exact wording in the content | Section | Source |
|:-|:-|:-|:-|
| CS1, 9 sectors | `9 sectors` / "with dashboard blueprints ready to adapt to your data." | S2 strip, item 1 only | HLB HAMT prepared content, Tab 1 industry cards 01-09. HLB HAMT's own content, so no footnote. |
| FAQ 4 timelines | "two to four weeks", "six to ten weeks", "three to six months", "Within the first two weeks, you normally have a working prototype on your own data to review." | S14 FAQ 4 only | Tab 1 FAQ 4, confirmed as HLB HAMT's by the Content Writer (brief Section 10, point 5b). No footnote. |

- No stat appears in more than one section.
- No FAQ restates 9 sectors, 9th of 69, BARC or 22%.
- None of the sibling-page figures appears, and neither do the brief Section 5b exclusions (the competitor-traced load-time result and fixed-price offer). Deliver checked this in every output file (see the handoff).

## Verification status

- **Confirmed by Test** in test-report-v2, item 6 (stat accuracy and footnoting: PASS; all four sources re-checked on 30 Sep 2026).
- **Access limits recorded in the brief (Section 6):** gartner.com returned HTTP 403 to automated fetches. The 22% figure, sample and dates were confirmed from the search extract of Gartner's release and from BigDATAwire's report of it.
- **Not independently re-fetched by Deliver.** Click-check every link once before publication.

## Internal links (click-check before publication)

| Ref | Anchor text | Target | Location |
|:-|:-|:-|:-|
| L1 | digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ | S4 lede |
| L2 | Power BI services | https://hlbhamt.com/services/power-bi-partner-in-dubai-uae/ (real link, live URL). **Go-live condition:** do not publish this page until that URL is confirmed to 301-redirect to the new Power BI homepage. In the uploaded snapshot the URL still carries its legacy content, which the Power BI Revision 4 correction removed from the new page. Swap L2 to the Power BI homepage's final URL once it is decided. In the `.html` the link carries `data-golive-check="l2-redirect"` and an HTML comment stating the condition. | S14 FAQ 3 |
| L3 | advanced analytics services | https://hlbhamt.com/services/advanced-data-analytics-uae/ | S14 FAQ 2 |
| L4 | data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ | S14 FAQ 6 |
| L5 | SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ | S6 card 2 (back) |
| In-page | five-stage method; agree the measures | #methodology | S4 card 3; FAQ 7 |
| S0 | Breadcrumb: Home / Technology Consulting Services / Digital Transformation & Analytics | https://hlbhamt.com/ ; https://hlbhamt.com/services/technology-consulting-services-dubai-uae/ ; https://hlbhamt.com/services/digital-transformation-uae/ | S0 |
| S2b | Read the ranking (link-button in the recognition bar; not a conversion CTA) | Same target as footnote 1 | S2b |

**Not linked anywhere, per brief Section 8:**
- The page's own URL, `/services/data-visualization-uae/`. It appears only in the canonical tag and in the schema, never as a link.
- The other HLB HAMT Power BI and analytics pages on the brief's "do not link" list.

## Carry-forward notes (outside these files)

- **Reverse link, a manual edit to the delivered Advanced Analytics homepage (brief Section 10, point 1; not yet done):** its L3 "data visualisation services" link (S6 card 6 back) still has `href="/services/data-visualisation-services/"`, `data-placeholder-link="true"` and a placeholder comment. Set it to `https://hlbhamt.com/services/data-visualization-uae/` and remove the placeholder attributes and comment. Its `.docx`/`.pdf` and sources log show the same placeholder and need the matching update.
- **The Power BI homepage's L7** already points to this page's URL. No edit is needed.
- **Before go-live:**
  - Confirm the L2 redirect (above).
  - Supply the S12 executive-dashboard screenshot or GIF.
