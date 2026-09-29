# Sources log: Advanced Analytics Services homepage

- **Page:** `advanced-analytics-services-homepage` (`.docx`, `.html` and `.pdf` in this folder).
- **Target URL:** `https://hlbhamt.com/services/advanced-data-analytics-uae/`. This page replaces the existing live page at that URL (brief Section 10, point 1). No redirect is needed. The `.html` canonical tag and the schema URL fields use this address.
- **Content version:** `draft/draft-v5.md`. It is the final draft: the test-report-v4 loop-3 pass, plus the FAQ A6 sentence fix documented in v5's header.
- **Compiled from:** the "Stats used" list and the "Sources" list in draft-v5. Nothing was added or dropped.
- **Link text rule:** every source link in this log and in the page files uses the draft's source description as its visible text. The raw URL is used only as the link target. No bare URLs appear in the page copy or the Sources note.

## Footnote numbering (draft to page)

Footnotes are numbered by order of first appearance on the rendered page. The draft's numbering already follows page order, so the numbers are unchanged. The `.html`, `.docx` and `.pdf` all use the same numbers.

| Draft ref | Brief ID | Page footnote | First appears in |
|:-|:-|:-|:-|
| [1] | S-1 | **1** | S2 strip, item 2 |
| [2] | S-3 | **2** | S2b HLB network line |
| [3] | S-2 | **3** | S5 foundation layer block |
| [4] | F1 | **4** | S14 FAQ 8 |

Page order of markers: 1 (S2), 2 (S2b), 3 (S5), 4 (FAQ 8). Each footnote is cited exactly once, and each marker has a matching entry in the page's Sources note (checked in the `.html` by anchor resolution, and in the `.docx` and `.pdf` by reading the text back).

## Stats and verified facts (in page footnote order)

| Page fn | Draft ref / brief ID | Stat or fact exactly as it appears in the content | Section | Source |
|:-|:-|:-|:-|:-|
| 1 | [1] / S-1 | `85%` / "of UAE CEOs surveyed say their organisation's culture enables AI adoption." | S2 strip, item 2 only | [PwC, 29th Global CEO Survey: UAE findings (2026)](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026/29th-ceo-survey-uae-findings-2026.html) (corroborated by [Middle East AI News](https://www.middleeastainews.com/p/middle-east-ceos-lead-globally-in)) |
| 2 | [2] / S-3 | "HLB HAMT is a member of HLB, the global advisory and accounting network, which reported network-wide revenue of US$6.67 billion for 2025, up 12%." | S2b only | [HLB, "HLB reports 12% global growth, reaching US$6.67 billion in FY2025"](https://www.hlb.global/press-room/hlb-reports-12-global-growth-reaching-us6-67-billion-in-fy2025/) (corroborated by [Consultancy.com.au](https://www.consultancy.com.au/news/12048/hlb-joins-the-6-billion-global-revenue-club-in-return-to-double-digit-growth)) |
| 3 | [3] / S-2 | "only 16% of GCC CEOs surveyed agree their most-used AI tools have access to all the relevant documents and data." | S5 foundation layer block only | [PwC, 29th Global CEO Survey: Middle East findings (2026)](https://www.pwc.com/m1/en/ceo-survey/29th-ceo-survey-middle-east-findings-2026.html) (corroborated by [Middle East AI News](https://www.middleeastainews.com/p/middle-east-ceos-lead-globally-in), as above) |
| 4 | [4] / F1 | "in the UAE its processing is governed by the Personal Data Protection Law, Federal Decree-Law No. 45 of 2021." | S14 FAQ 8 only | [UAE Government portal, "Data protection laws"](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws) |

## HLB HAMT facts (no footnote)

| Fact | Exact wording in the content | Section | Source |
|:-|:-|:-|:-|
| CS1, 11 services | `11 services` / "across data transformation, statistical modelling and enterprise reporting." | S2 strip, item 1 only | HLB HAMT prepared content (Tab 2 offering badges: 5 + 3 + 3). HLB HAMT's own catalogue, so no footnote. |

- No stat appears in more than one section.
- No FAQ restates 11 services, 85%, 16% or US$6.67 billion.
- None of the sibling-page figures appears (200+, 33x, 7 days, Since 1999, 25/26 years, 150+ countries, 19th consecutive, 14+).

## Verification status

- **Confirmed by Test** in test-report-v4, item 6 (stat accuracy and footnoting: PASS).
- **Access limits recorded in the brief (Section 6):**
  - pwc.com returned HTTP 403 to automated fetches. Both PwC figures were confirmed from search extracts of PwC's pages plus Middle East AI News.
  - The HLB press release rendered only its title, which carries both figures. Consultancy.com.au corroborates them.
- **Not independently re-fetched by Deliver.** Click-check every link once before publication.

## Internal links (click-check before publication)

| Ref | Anchor text | Target | Location |
|:-|:-|:-|:-|
| L1 | digital transformation and analytics services | https://hlbhamt.com/services/digital-transformation-uae/ | S4 lede |
| L2 | Power BI services | **Placeholder, URL pending.** The Power BI homepage is delivered, but its final URL is not yet decided. In the `.html`: `href="#"`, `data-placeholder-link="true"`, `data-placeholder-target="power-bi-services-homepage-final-url"`, with the HTML comment "PLACEHOLDER LINK: Power BI homepage delivered, final URL pending; set before go-live". Dotted underline in the `.docx`/`.pdf`. | S11 tile 5 |
| L3 | data visualisation services | **Placeholder, page not yet built.** In the `.html`: `href="/services/data-visualisation-services/"` (the brief's placeholder path, not a confirmed URL), `data-placeholder-link="true"`, with the HTML comment "PLACEHOLDER LINK, sibling page not yet built". Dotted underline in the `.docx`/`.pdf`. | S6 card 6 (back) |
| L4 | data protection advisory | https://hlbhamt.com/services/data-privacy-and-security-uae/ | S14 FAQ 8 |
| L5 | SugarAI CRM | https://hlbhamt.com/sugarai-crm-2/ | S6 card 4 (back) |
| In-page | five-stage method; use cases above; readiness assessment | #methodology; #usecases; #contact | S4 card 3; FAQ 4; FAQ 7 |
| S0 | Breadcrumb: Home / Technology Consulting Services / Digital Transformation & Analytics | https://hlbhamt.com/ ; https://hlbhamt.com/services/technology-consulting-services-dubai-uae/ ; https://hlbhamt.com/services/digital-transformation-uae/ | S0 |
| S2b | Read HLB's announcement (link-button in the recognition bar; not a conversion CTA) | Same target as footnote 2 | S2b |

**Not linked anywhere, per brief Section 8:**
- The page's own URL, `/services/advanced-data-analytics-uae/`. It appears only in the canonical tag and in the schema, never as a link.
- The six other HLB HAMT analytics pages on the brief's "do not link" list.

## Carry-forward notes (outside these files)

- **Reverse link, a manual edit to the delivered Power BI homepage:** its placeholder P2 ("advanced analytics services", S6 card 6) points to `/services/advanced-analytics-services/`, which does not exist. Update it to `https://hlbhamt.com/services/advanced-data-analytics-uae/`.
- **Before go-live:**
  - Set L2 once the Power BI homepage URL is decided.
  - Set L3 once the Data Visualisation homepage exists.
  - Supply the S12 forecast-dashboard screenshot or GIF.
  - Confirm with HLB HAMT (test-report-v4 carry-forwards):
    - (a) Post-go-live monitoring, retraining and reviews are part of analytics engagements (S4 card 4, S9 step 5, S10 Extend).
    - (b) A named consultant is the support contact (S10 Extend). Fallback wording if not: "We watch pipelines, data quality and model drift...".
