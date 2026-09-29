# Extracted: `inputs/content-source/HLB_HAMT_Data_Viz_Content_Documentation (1).docx`, in-scope parts only

Extracted by the Plan agent, 2026-09-29, for the Advanced Analytics services homepage requirement.

**How this was produced.** The .docx had already been converted to text before planning (`inputs/content-source/data-viz-documentation-extracted.md`). That is the same conversion the Power BI homepage requirement used. I planned from that existing extraction and did not re-run a conversion: this agent session has no shell, so the docx skill's conversion scripts could not run. I read the existing extraction in full (1,076 lines). It has 9 sections, and **Section 5 "Tab 2: Advanced Analytics Services"** (lines 495-642) is the part for this page, parallel to how Section 6 covered Tab 3 for Power BI. Its content matches HTML Tab 2 (see `hlb-data-viz-v4 (1).html.md`) apart from the one discrepancy noted below.

**Left out on purpose:** Section 4 (Tab 1, Data Visualization), Section 6 (Tab 3, Power BI), the Section 8 FAQ reference for those tabs, and Section 9 PPC notes, which are about Power BI and industry landing pages.

---

## Document metadata (Section 0)

- Title: "HLB HAMT Data Visualization Services: Website Content & Developer Documentation"
- Target URL stated in the docx: `hlbhamt.com/services/microsoft-power-bi-consulting-in-dubai-uae/` (this is the **Power BI** consulting page. It is not relevant to this page's URL. See brief OQ1 for the URL recommendation.)
- Version 4.0, April 2026. Prepared by Himanshu (Senior .NET Architect & CA).

## Section 2 (SEO): in-scope items only

- The docx's primary keyword list includes **"Advanced analytics services"**, "Data analytics consulting" and "Enterprise reporting solutions". These are consistent with this requirement's keyword set.
- Schema recommendation: Service, Organization, FAQ.
- Each tab has its own FAQ "for featured snippet eligibility".

## Section 3 (Hero): in-scope items only

- Hero mini-card: **"Advanced Analytics: ML, forecasting & segmentation"**
- Hero mini-card: **"Finance + Technology: Licensed audit firm & tech consultancy"**
- The hero stats (200+ / 33x / 7 Days / 14+ Yrs Gartner #1) are **not** for this page (see the HTML extraction for the reason).

## Section 5: Tab 2, Advanced Analytics Services

**Dev notes:** "Navy dark background for intro section. White background for offerings section." Offerings: "3-column card grid. Each card has a colored top border (blue/teal/gold), large icon, service count badge, tagline, and checklist of services." The note then says the section must be visually impactful, with a premium card design.

- **5.1 Introduction (dark section).** Eyebrow "Deeper Intelligence, Better Outcomes". The two intro paragraphs are identical to the HTML's, and both are **[DO NOT REUSE]** (competitor-derived wording; see Warning A in the HTML extraction). The three pillar cards are Data Transformation ("Clean, integrate, transform"), Advanced Statistical Modeling ("Predict, forecast, segment") and Enterprise Reporting ("Dashboards, scorecards, automation").
- **5.2 Service offerings (WOW cards):**
  - Card 1, **Data Transformation** (blue #3B82F6). Tagline "From raw chaos to analytics-ready gold". Badge "5 Services": ETL (Extract, Transform, Load) Pipelines; Data Migration and Integration; Data Marts and Data Warehousing; Self-Service Data Preparation; Optimized Data Models and Star Schemas.
  - Card 2, **Advanced Statistical Modeling** (teal #0099A8). Tagline "See the future before it happens". Badge "3 Services": Machine Learning and Predictive Analytics; Time Series Analysis and Forecasting; Audience and Customer Segmentation.
  - Card 3, **Enterprise Reporting** (gold #C5993E). Tagline "Insights that reach every stakeholder". Badge "3 Services": Interactive Dashboards and Scorecards; Automated Reporting and Scheduled Delivery; Custom Data Views and Self-Service Analytics.
- **5.3 Advanced Analytics FAQ** ("Accordion FAQ within the Advanced Analytics tab"). It has the same 7 questions and answers as the HTML.
  - **Discrepancy:** the docx answer to "What is customer segmentation and how does it drive revenue?" **ends after "better resource allocation."** The HTML and the live page add a sentence: "Our segmentation models use machine learning to identify high-value cohorts that manual analysis would miss." The brief treats the HTML/live version as current, because it is what HLB HAMT published.

## Section 7 (CTA and footer): shared

- Headline "Ready to Transform Your Data Into Strategic Intelligence?". Subtitle "Let's discuss how HLB HAMT can accelerate your data journey."
- Buttons: "Schedule a Consultation" (teal), "$4,500 PowerUP! Offer" (gold).
- Footer: "© 2026 HLB HAMT. All rights reserved. Member of HLB International."
