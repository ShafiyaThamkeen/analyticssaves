# Revision 3 — Content Writer feedback (2026-09-29, same day as Revision 2)

While Revision 2's Test loop was running, the Content Writer gave a further instruction that
applies on top of Revision 2: **"Do not use any competitor terms, or any other tool names."**

Clarified scope (via follow-up questions):
1. Remove **all named software/products**, not just competing BI tools — this includes source
   systems named as connector/integration examples (SAP, Oracle, NetSuite, Salesforce,
   SugarCRM, Snowflake, Google BigQuery, Azure Data Factory) and competing BI platforms
   (Tableau, Qlik).
2. Remove **Microsoft's own related product names too** — Excel, Teams, SharePoint, Outlook,
   Azure, Dynamics 365, **Microsoft Fabric, and Copilot**. Replace with generic descriptions.

**What stays:** "Power BI" itself (the page's actual subject/service — removing it would defeat
the page's purpose) and "Microsoft" as the platform vendor where factually necessary (e.g. "HLB
HAMT resells Power BI licences", the Gartner recognition line, which is about Microsoft's
platform, ISO/SOC 2 scope). "HLB HAMT" branding rules from Revision 2 (Section 12.3) are
unchanged. The Gartner Magic Quadrant reference is not a "tool name" — Gartner is an analyst
firm, not software — so it stays, but do not name any other analyst firm's rival products.

**Precedence:** this note applies on top of Sections 1-13 and supersedes any specific wording
in those sections that names a non-Power-BI product. Where Section 12/13 gave exact suggested
wording that includes a now-banned name, rewrite it to the same intent using generic language.

## Sections/content materially affected

- **S5 "The Platform We Deliver" intro** (12.5 S5): currently "...works natively with Excel,
  Teams, SharePoint, Outlook, Azure and Dynamics 365..." → generalize, e.g. "...works natively
  with the Microsoft productivity and business apps your teams already use..." (no product
  names).
- **S5 row 3 "Connected to the systems you run"**: currently names SAP, Oracle, NetSuite and
  "the rest" as connector examples → generalize to "your ERP, CRM and finance systems" /
  "the systems you already run", without naming any of them. Same for the bullet list ("ERP
  and CRM integration" is fine as a generic bullet; a bullet naming a specific product is not).
- **S5 platform-layer block** ("Fabric readiness and a medallion lakehouse", 12.5): cannot name
  Microsoft Fabric. Rework as a generic "unified data platform" / "single data platform that
  brings reporting, data preparation and storage together" without the Fabric brand name. The
  **40,000+ Fabric customers stat [4] cannot be used**, since it is specifically a Fabric
  adoption figure and can't be stated without naming Fabric — drop it (do not force a vague
  substitute that misattributes the figure). "Medallion lakehouse" / "Bronze, Silver, Gold" are
  architecture-pattern terms, not product names, and may stay.
- **FAQ "What is Microsoft Fabric, and should we plan for it?"** (old FAQ 7): cannot ask about
  or answer around a named product. Either drop this FAQ (moving to 9 total) or rewrite it as a
  generic question or answer, e.g. "What if our data comes from many different systems?" /
  "Do we need a data platform beyond Power BI, and when?" answered without naming Fabric.
- **FAQ "What do we need to use Copilot in Power BI?"** (old FAQ 8): same problem. Rewrite
  generically, e.g. "Does Power BI include AI features, and what do we need to use them?" —
  answer covers AI-assisted analytics (natural-language Q&A, summaries, narrative insights)
  without naming Copilot. The specific capacity/licensing requirement (paid Fabric F2+ or
  Premium P1+) can't be stated either without naming Fabric — generalize to "a paid, higher-tier
  Power BI licence" or similar, and flag in Test/Deliver notes that the precise SKU requirement
  had to be dropped for the no-tool-names rule.
- **S7 item 05 "Migration, embedded analytics and Fabric readiness"**: remove "Tableau to Power
  BI and Qlik to Power BI migration" naming → "migration from other reporting tools to Power
  BI, preserving business logic and redesigning visuals". Remove "Fabric readiness" naming from
  the title/body → generic "a unified data platform" per above. "Power BI Embedded" may stay,
  since "Embedded" here is a Power BI licensing/deployment mode, not a separate third-party
  tool — it's still naming Power BI, the page's own subject.
- **S10 Support tab "Licence advisory and Fabric migration support"**: → "Licence advisory and
  data platform migration support" (no Fabric name).
- **S2b recognition bar** ("We build on Microsoft Power BI and Fabric..."): → "We build on
  Power BI..." (drop "and Fabric").
- **Azure Data Factory** (wherever named, e.g. S7 item 02): → generic "automated data
  pipelines".
- **S1 deployment line** ("Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud
  regions"): these are Microsoft **data-centre region names**, not third-party product names,
  and the underlying fact (in-country hosting) is important to the page's UAE-data-residency
  claim. **This may stay** — it does not name a product like Fabric/Azure/Copilot, only a
  physical hosting region. Flag this judgment call in Test's report for the Content Writer to
  overrule if they disagree.
- **Sectors/industries named** (real estate, construction, hospitality, etc.) are not tool
  names — unaffected.
- **"SugarAI CRM" internal link (S11 tile 4)**: SugarAI CRM is HLB HAMT's own product (not a
  competitor or third-party tool), so this cross-link stays.

## What Test should check for this revision

Search the full draft for: SAP, Oracle, NetSuite, Salesforce, SugarCRM (except the HLB HAMT
cross-link, which is fine), Snowflake, BigQuery, Tableau, Qlik, Azure Data Factory, Excel,
Teams, SharePoint, Outlook, Azure (as a named product, not "UAE North/Central" region wording),
Dynamics 365, Fabric, Copilot. None should appear. "Power BI" (all forms) and "Microsoft" (as
vendor, where factually necessary) are exempt. Gartner is exempt (analyst firm, not software).
