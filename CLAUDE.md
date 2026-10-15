# Content writing rules for HLB HAMT pages

## Word documents (always use this format)

Every page-content document ("give me the doc") must follow the sample in
`docs/doc-format/SugarAI_CRM_-_Hospitality_SAMPLE.docx`. Do not invent another layout.
A working generator that builds this format from a finished HTML page is in `tools/make_invoice_doc.py`
(python-docx + bs4). Reuse or adapt it for new pages, and check the result by converting to PDF and viewing it.

Format rules (taken from the sample):
- Letter page, margins 0.75" top/bottom, 0.85" left/right. Arial throughout, body 10 pt, text colour `#0A1F33`, line spacing 1.15, justified.
- Title: centred, bold, 20 pt, blue `#10538F`, gold rule underneath (`#B8761C`, 1.5 pt). Form: `<Product or topic> - <Page name> Sub-page`.
- Section headings: bold 15 pt blue `#10538F` with the same gold underline, numbered (`1. Hero`, `2. ...`) in page order.
  First heading is always `Page metadata & SEO`, unnumbered.
- Metadata table (blue header row `Element | Content`): Page title, Meta description, Primary keywords, Secondary keywords (add Supporting keywords and Menu location when the brief has them).
- Section body is a list of `● Label: text` lines (hanging indent, no space after): Eyebrow, H1/H2, Intro, Buttons, Body, Copy.
  The label part (`Eyebrow:`, `H1:`, `H2:`, `Intro:`, `Buttons:`, `Copy:` and so on) is always bold; the text after it is regular.
  Sub-labels that introduce groups are bold too, for example `Hero side panel`, `Four cards (heading / copy):`, `Six-step timeline:`.
- Card groups, stats and steps go in tables: header row filled `#10538F` with bold white 9 pt text, black 0.5 pt borders, 9 pt cells,
  columns such as `Item | Copy`, `Tag | Heading | Copy`, `Figure | Label | Description`. Rows never split across pages.
  Six-card lists may instead be numbered lines: bold `1. Heading` then ` - copy`.
- Blank line after each table and between sections. CTA sections are their own numbered section (Eyebrow, H2, Body, Button).
- FAQ: section `FAQ` with Eyebrow, H2, then `Q: question` in bold and the answer as a plain paragraph beneath.
- Anything to verify is marked `[CONFIRM]` inline and listed in a final `Items to confirm before publishing` section.

## Copy rules
- No competitor names or competitor product terms, and no ERP or software brand names (SAP, Oracle, Dynamics, Sage, Odoo, Zoho, Power BI and the like). Say "enterprise ERP platforms", "accounting systems" instead.
- Do not copy or closely paraphrase reference pages. Do not use outside statistics; mark any needed figure `[CONFIRM]`.
- Brand colours for HLB HAMT pages (from the SugarAI CRM page): deep blue `#005A77`, gold `#FBBA00`, text `#111827`, secondary text `#4B5563`, borders `#E5E7EB`.
- HAMT AI naming: HAMT stands for Human-centric, Automation, Machine learning, Transformation (H = Human-centric, not "Human-integrated").
- HAMT AI tone: always positive and confident. HAMT AI is accurate from day one and the client's reviewers add expertise that adapts it to their business.
  Never say or imply that HAMT AI "needs to learn", makes errors, guesses, or is unready. Avoid "learns", "flags uncertain", "corrections", "retrains", "keeps learning".
  Use "expert review", "reviewer decisions are built into the models", "adapts to your suppliers", "refine", "tune".
