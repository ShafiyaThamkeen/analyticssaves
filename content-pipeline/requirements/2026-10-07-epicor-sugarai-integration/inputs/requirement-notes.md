# Requirement notes

- **Content type**: Webpage — a service/integration subpage for "SugarAI CRM + Epicor ERP
  Integration" (CRM integration with Epicor ERP). NOT a homepage. Structural approach discussed
  and agreed with the Content Writer before this requirement was submitted:
  - **Base template**: the Insurance subpage (`inputs/structural-sample/hlbhamt-sugarai-insurance.html`
    + `SugarAI CRM — Insurance draft2.docx`/`.pdf`, reused from the earlier Field Service
    Management subpage requirement), the same mandatory template style used for Insurance and
    Field Service Management subpages in this project.
  - **Not an exact section-for-section copy.** The Content Writer explicitly asked for:
    1. **Hero**: follow the Insurance/FSM hero pattern exactly (eyebrow, H1, lede, buttons).
    2. **Body sections**: do NOT put everything in cards/tiles/boxes the way Insurance, FSM, and
       the three recent homepages did. Mix in real paragraph-form content — explaining how the
       integration actually works, the business case, the data flow — with cards/tiles used only
       where they genuinely suit the content (e.g. a benefits list), not as the default
       structure for every section.
    3. **Images**: build in actual image placeholders through the section flow (not just one
       teaser screenshot near the end like the homepages had). Each section that would benefit
       from a visual (e.g. an integration architecture diagram, a workflow diagram, a dashboard
       screenshot) should name what the image should show and reserve space for it in both HTML
       and docx output.
  - Plan should produce a section skeleton that reflects this — reusing the Insurance subpage's
    overall shape/flow (hero → stats/credibility band → platform/why-us → proof → FAQ → CTA) as
    a loose guide, not a rigid block-for-block copy, and explicitly design in prose sections and
    image slots.

- **Primary keyword**: CRM integration with Epicor ERP
- **Secondary keywords**: CRM integration services; CRM integration partner; CRM implementation;
  SugarAI with Epicor ERP

- **Word count target**: 1,500-1,700 words. **Primary keyword: 3-4 times on-page.**

- **Avoid plagiarism**: explicit Content Writer instruction (standing project rule, restated
  here). Nothing may be copied or closely paraphrased from any reference site or content source
  below.

- **Reference websites** (competitors/adjacent vendors offering Epicor-SugarCRM integration —
  for positioning, technical-accuracy checking, and gap analysis only; nothing copied or
  paraphrased):
  - https://www.codelessplatforms.com/solutions/epicor-sugarcrm-integration/
  - https://www.tcpamericas.com/en/pages/sugar-epicor-integration
  - https://www.fluenterp.com/en/integrations/epicor-sugarcrm
  - https://marketplace.sugarai.com/addons/epicorsugar-crm-integration-by-tcp
  - https://www.linkedin.com/pulse/boost-sales-service-epicor-erp-sugarcrm-sugarcrm-42lqf/

- **Content source — webinar slide deck (IMPORTANT, read the caveat below)**:
  `inputs/content-source/tcp-sugarcrm-epicor-kinetic-webinar-slides.pdf`
  - The given URL, https://www.tcpamericas.com/en/events/sugarcrm-for-epicor-kinetic-users, is a
    webinar registration/landing page (no embedded video or transcript available — video content
    itself is not accessible to this pipeline). However, the page links to a downloadable 20-slide
    PPT/PDF deck ("CRM for Epicor Kinetic Users," presented by TCP Americas), which was
    successfully retrieved and is saved as the content source above. All 20 slides were read.
  - **CRITICAL CAVEAT — treat this deck like a competitor reference, not like HLB HAMT's own
    prepared content.** This deck is **TCP Americas'** own sales/marketing material (TCP is a
    third-party Epicor Kinetic + SugarCRM implementation partner — "Platinum Epicor Kinetic ERP
    Partner," "Premier SugarCRM Partner," 200+/150+ their own customer counts), not something
    HLB HAMT wrote or owns. This is exactly the same situation that caused the Softcrylic/
    PowerUP! problem on the Power BI and Data Visualization pages earlier in this project.
    **Do NOT reuse, rename, or re-attribute any of the following as HLB HAMT's own:**
    - The branded integration product name **"Fluent" / "Fluent Integration by TCP"** (TCP's own
      integration middleware product). HLB HAMT should describe its own integration approach/
      method in generic terms (e.g. "a bi-directional sync," "a live-data connector"), not name
      or imply use of TCP's specific product, unless HLB HAMT genuinely resells/uses Fluent
      (unconfirmed — flag as an open question).
    - TCP's own **"Exclusive Offer: Try It Free" / 14-day free trial** package (dedicated Epicor
      Kinetic instance, personal guide from TCP, etc.) — this is TCP's commercial offer, not
      HLB HAMT's. Do not reuse its terms or structure as if it were an HLB HAMT offer.
    - TCP's own **client testimonials** (Southern Aluminum/James Palazzi; West Coast Metals/Joe
      Towle quotes) — these are TCP's client proof, not HLB HAMT's. Cannot be presented as
      HLB HAMT's own results or attributed to HLB HAMT's work.
    - TCP's own **customer/partner counts** ("200+ customers on Epicor Kinetic," "150+ Sugar
      implementations") — these are TCP's business stats, not HLB HAMT's.
  - **What IS safe and useful to draw on** (generic technical/industry facts, not TCP-branded
    claims):
    - The **pain-point framing**: "two sales days per seller lost every week" to disconnected
      systems (8 hours searching for customer info across ERP/other systems, 35% of the week not
      spent engaging customers, 10 hours coordinating with other functional groups). TCP cites
      this to three named sources: "Reorder Management — 31 Manufacturer Rep Statistics and
      Trends (2025)," Bureau of Labor Statistics ("Wholesale and Manufacturing Sales
      Representatives"), and Forrester ("Use Science to Improve Sales Team Productivity"). **If
      this stat is used, independently re-verify it against these primary sources** (per this
      project's standing stat-accuracy rule) rather than trusting TCP's packaging of it — do not
      just copy TCP's number without checking the actual source documents say what TCP claims.
    - **What data typically syncs** between a CRM and an ERP in this kind of integration, as a
      generic pattern: customers, contacts, quotes, orders, invoices, cases (bi-directional);
      price lists and parts lists (often one-way from ERP to CRM). Useful for describing HLB
      HAMT's own integration capability in generic terms.
    - **The "live view into ERP data inside the CRM record" concept** (e.g. open orders, open/
      closed quotes visible on a Sugar account record) — a generic integration pattern/concept,
      not TCP-specific branding, safe to describe generically.
    - **The lead-to-order workflow pattern** (quote created in CRM → draft quote in ERP → quote
      ready → CRM opportunity updated → sales order created in ERP → CRM opportunity marked
      complete) — a generic bi-directional workflow concept, useful for explaining the business
      value of an integration, not TCP-specific.
    - **Native SugarCRM/SugarAI platform capabilities** mentioned (Sugar Connect for Outlook —
      view/create/update Sugar records from Outlook, bidirectional calendar sync, email
      sync/tracking; the SugarCRM mobile app for iOS/Android) — these are real SugarAI platform
      features, not TCP-specific, safe to describe as SugarAI's own capabilities since HLB HAMT
      deploys SugarAI.
    - **General reasons an Epicor+SugarCRM pairing is valuable** (bidirectional sync, native
      Microsoft 365 integration, ease of use/administration, AI-powered insights, strong mobile
      client, marketing automation on combined data) — useful as a generic value-proposition
      angle, written in HLB HAMT's own words, not copied from TCP's "Why Epicor + SugarCRM
      Excels" slide.

- **Call transcript**: none provided for this requirement (an earlier draft of this request
  mentioned a `healthcare-review-call-transcript.docx`, but that filename doesn't match this
  Epicor/SugarAI context — likely a copy-paste artifact from a different/older template, and it
  was dropped from the final request. No transcript file was attached. Proceeding without one.)

- **Parent webpage**: https://sugarai.com/ (SugarAI's own site, not an HLB HAMT page — likely
  intended as background/context on the SugarAI product itself, similar to how Microsoft's own
  product pages were treated as background-only parents for the Power BI/Data Visualization
  pages, not the literal site-hierarchy parent). Flag as an open question whether the real
  HLB HAMT breadcrumb/parent should instead be the live SugarAI CRM homepage
  (`https://hlbhamt.com/sugarai-crm-2/`) or its eventual industries/integrations section, since
  this new page is presumably a sibling to the Insurance/FSM subpages under that same product.

- **No existing HLB HAMT page for this integration** has been identified or uploaded — if Plan's
  research finds one already live, flag and compare per this project's standing practice
  (replace-in-place vs. new page), same as prior requirements.

- **Standing project conventions to apply from the start** (established across the Power BI,
  Advanced Analytics, and Data Visualization requirements): HLB HAMT-led branding throughout; no
  third-party tool/platform names beyond what's necessary for accuracy (in this case, "Epicor"
  and "SugarCRM"/"SugarAI" are the actual subject of the page so naming them is required and
  expected — but avoid naming unrelated third-party tools); British spelling; zero em dashes;
  every stat independently verified and footnoted; no fabricated or recycled stats from sibling
  pages; honest sourcing throughout, with particular care this time around the TCP webinar
  material per the caveat above.
