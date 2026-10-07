# Content brief: SugarAI CRM + Epicor ERP Integration (service/integration subpage)

Requirement folder: `content-pipeline/requirements/2026-10-07-epicor-sugarai-integration/`
Prepared by: Plan agent, 2026-10-07
Status: **AWAITING CONTENT WRITER APPROVAL.** Build must not start until Section 9 is answered or waived.

> **Inputs read in full**
> - `inputs/requirement-notes.md` (authoritative spec).
> - `inputs/structural-sample/hlbhamt-sugarai-insurance.html` (base template; the live HTML is authoritative over the draft).
> - `inputs/structural-sample/SugarAI CRM — Insurance draft2.pdf.md` (already-extracted draft text; the `.docx`/`.pdf` twins are the same draft per the FSM brief, Section 10.6).
> - `inputs/content-source/tcp-sugarcrm-epicor-kinetic-webinar-slides.pdf`: all 20 slides read; I loaded the `anthropic-skills:pdf` skill first, then extracted the slides with the Read tool's PDF renderer (no shell was available). The result is saved as **`inputs/extracted/tcp-sugarcrm-epicor-kinetic-webinar-slides.pdf.md`**. Build and Test read that file, not the PDF.
> - The FSM worked example (`../2026-09-23-sugarai-field-service-management-subpage/brief.md`, `draft/draft-v5.md`, `output/...-sources-log.md`, `inputs/extracted/stats-research-v2.md`), including the Content Writer's decisions in its Sections 10 and 11.
> - The live HLB HAMT SugarAI CRM hub text (`../2026-09-29-data-visualization-services-homepage/inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`, saved from https://hlbhamt.com/sugarai-crm-2/). This is the source for every HLB HAMT company fact used below.
> - The stats lists in the three homepage briefs (Power BI, Advanced Analytics, Data Visualization), checked so no stat is recycled.
>
> **Research access this run:** WebFetch worked for tcpamericas.com, fluenterp.com, linkedin.com, nucleusresearch.com, avasant.com, khaleejtimes.com, 01net.it and forrester.com. It failed for codelessplatforms.com (403), marketplace.sugarai.com (empty page), businesswire.com (403) and epicor.com (403), so those were covered with WebSearch only. Section 6 records the verification status of each stat.
>
> **No call transcript** (per requirement notes; the earlier healthcare transcript mention was a copy-paste artefact). **No existing HLB HAMT Epicor page found** (searched hlbhamt.com, nothing on Epicor), so this is a new page, not a replace-in-place.

---

## 1. Requirement summary

| Item | Detail |
|---|---|
| Content type | Webpage: **service/integration subpage** in HLB HAMT's SugarAI CRM product line ("SugarAI CRM + Epicor ERP Integration"). It sits beside the industry subpages (Insurance, Field Service Management and others) but is an **integration** page, not an industry page, so the industry-specific blocks (Who we serve segments, UAE/GCC market list) are dropped or merged (see Section 3). |
| Target audience | UAE and wider GCC **manufacturers and distributors that already run Epicor ERP** (Epicor Kinetic, cloud or on-premise; earlier Epicor ERP 10 estates) and either run SugarAI/SugarCRM already or are choosing a CRM to sit beside Epicor. Roles: Sales Director / Head of Sales, Customer Service Manager, CFO / Finance Controller (orders, invoices, credit), CIO / IT Manager / ERP owner (integration design, support). |
| Business goal | Rank for "CRM integration with Epicor ERP" and the four secondary terms. Position HLB HAMT as the UAE/GCC SugarAI partner that designs, builds and supports the CRM-to-Epicor connection as part of a SugarAI implementation. Drive demo requests and integration conversations. |
| Word count range | **1,500-1,700 words, target about 1,620.** The Content Writer set this range. For comparison, the two competing pages I could measure are shorter: the TCP/Fluent integration page is about 1,100-1,200 words of main body and the fluenterp.com Epicor-SugarCRM page about 650-700 (WebFetch estimates). The extra length here goes into the prose explanation, data map and workflow that those pages compress into bullets. That is the content gap this page is meant to fill. **Count rule (same as the FSM page):** count all visible body text: H1, headings, lede and body copy, table text, card and tile text, figure captions, stat labels and descriptions, FAQ questions and answers, CTA headings and body, and the "What happens next" rows. **Exclude** nav, breadcrumb, eyebrow labels, button labels, footer, meta tags, JSON-LD, the Sources/footnote list, image-placeholder labels and alt text. |
| Positioning | Positive and capability-led. HLB HAMT connects SugarAI with Epicor so sales, service and finance work from one customer record: Epicor stays the system of record for parts, prices, stock, orders and invoices, and SugarAI is where customer-facing teams work. HLB HAMT agrees the exact data flows with you in discovery, then builds, tests and supports the connection. **No pain-point opening** in the hero. The business-case section (Block 5) may use one fragmented-data stat, framed constructively. |
| Tone and style | Technically specific in headings and body (system of record, bi-directional synchronisation, live views, data map, quote-to-order, matching rules), plain-English outcomes. **British spelling** (synchronisation, customisation, organisation, prioritise, programme, licence). **Zero em dashes** (also avoid en dashes and double hyphens in copy). HLB HAMT-led from the first sentence of the lede. |
| Template | Insurance subpage as a **loose** guide (Section 3). Hero mirrors it exactly; the body uses a deliberate mix of prose, one data table, a numbered list, one card grid, one numbered services list, one 4-tile credential row, a process timeline and four image slots. |

---

## 2. Keyword placement plan

**Count rule for Test:** exact phrase, case-insensitive, in on-page copy only (H1, headings, body, table, captions, cards, FAQs, CTA text). The meta title and meta description are placed as specified but **not** counted toward on-page frequency.

| Keyword | Meta title | Meta description | H1 | Subheading | First 100 words | Required on-page count | Exact placements |
|---|---|---|---|---|---|---|---|
| **CRM integration with Epicor ERP** (primary) | Yes, at the very start | Yes, at the very start | **Yes** (H1 is `SugarAI CRM Integration with Epicor ERP`, which contains the exact phrase) | **Block 3 H2** | **Yes, via the H1** (the H1 is word 1-6 of the page) | **Exactly 4** (Content Writer range 3-4; do not exceed 4) | (1) H1; (2) Block 3 H2 `How CRM integration with Epicor ERP works`; (3) Block 5 prose, sentence 1; (4) FAQ 2 answer, sentence 1. Do **not** put it in the hero lede (the H1 already covers the first 100 words, and repeating it there is what tips into stuffing). |
| SugarAI with Epicor ERP | No | No | No | **FAQ 1 question** | **Yes**: hero lede, sentence 1 | **Exactly 2** | (1) Hero lede sentence 1: `HLB HAMT connects SugarAI with Epicor ERP ...`; (2) FAQ 1 question. Everywhere else write "SugarAI and Epicor". |
| CRM integration services | No | No | No | **Block 8 H2** | No | **Exactly 2** | (1) Block 8 H2; (2) FAQ 5 answer. |
| CRM integration partner | No | No | No | **Block 9 H2** | No | **Exactly 1** | Block 9 H2 only. A second instance would land in the same section and read as padding. |
| CRM implementation | No | No | No | **Block 8 item 02 H4** (`SugarAI CRM implementation`) | No | **Exactly 2** | (1) Block 8 item 02 H4; (2) Block 10 lede. |

**Meta keywords tag:** the five phrases above, primary first.

**Stuffing-risk flags**
- Total exact-match instances on-page: **11** in about 1,620 words (about 0.7%). **Hard cap: 12.**
- Keywords sit in the H1 and **exactly 4 subheadings** (Block 3 H2, Block 8 H2, Block 8 item 02 H4, Block 9 H2) plus one FAQ question. No other heading may contain an exact-match keyword.
- **Never put two different keywords in the same sentence.**
- Watch for accidental matches. Writing "connect SugarAI with Epicor ERP" or "CRM implementation" in passing anywhere else **adds a count**. Use "SugarAI and Epicor", "the integration", "the connection" or "your rollout" instead.
- "Epicor" on its own will appear 30+ times and "integration" 15+ times. That is expected topical vocabulary, but vary it with "the connection", "both systems" and "ERP".

---

## 3. Section structure

### 3a. How this departs from the Insurance/FSM template (and why)

The Content Writer asked for the Insurance shape as a **loose** guide (hero → credibility/stats → platform/why-us → proof → FAQ → CTA), **real prose** in place of cards-by-default, and **image slots through the flow**. Decisions:

| Insurance block | This page | Why |
|---|---|---|
| Hero + side panel | **Kept exactly** (eyebrow, H1, lede, 2 buttons, side panel with H3, sub-line and 3 rows) | Content Writer instruction 1. |
| Stats band ("Why SugarAI") | **Kept**, retitled for integration (3 stats) | Credibility band directly after the hero, as in the template. |
| Platform (4 product cards) | **Replaced by prose + data table + IMG-1** (Block 3) | How the integration works is explanation, not a card list. |
| Benefits (6 tiles) | **Kept as the one card grid**, but preceded by business-case prose + IMG-3 (Block 5) | Benefits are the content that genuinely suits cards (instruction 2's own example). |
| Services 01-08 | **Kept as a numbered list, cut to 6 items** (Block 8) | Numbered rows are a list, not tiles, and suit a services scope. Cut to 6 to fund the prose. |
| Proven band | **Merged into Block 9** (prose + 4 credential tiles) | The stats band already carries the analyst figures. A second figures band would mean thin or recycled stats (see FSM Section 11 history). |
| Segments, UAE/GCC market list | **Dropped as blocks.** The regional points (multi-entity groups, Arabic/English, cloud or on-premise) are folded into Block 9 prose and FAQ 1 | This is an integration page, not an industry page, and the word budget goes to prose. |
| Process (6 steps + callout) | **Kept** (Block 10) | A timeline is sequence content, not cards. |
| Why HLB HAMT (4 cards) | **Merged into Block 9** | |
| FAQ (7) | **Kept, 5 Q&As** | Word budget. |
| Mid CTA bands (2) | **1 mid-page band** + closing CTA | Two extra prose blocks need the room. |
| *(new)* | **Block 4 quote-to-order workflow** (prose + numbered list + IMG-2) and **Block 7 "where teams work"** (prose + IMG-4) | Content Writer instruction 2: explain how the integration works and the data flow in paragraphs. |

### 3b. Section skeleton (mandatory for Build)

Page chrome (Deliver, not counted):
- **Sticky nav (new labels for this page):** How it works `#how` · Workflow `#workflow` · Benefits `#benefits` · Services `#services` · Why HLB HAMT `#why` · Process `#process` · FAQ `#faq` · button `Request a demo` → `#start`.
- **Breadcrumb text:** `Home › Technology Consulting Services › CRM Solutions (SugarAI) › Epicor ERP Integration`. Link targets follow Open Question 3. **Default until answered:** follow the FSM precedent (Content Writer decision, FSM brief Section 10.2), so "CRM Solutions (SugarAI)" links to `https://sugarai.com/`.
- **Eyebrows (navigation labels, not counted):** Block 1 `Integrations · Epicor ERP`; Block 2 `Why integrate`; Block 3 `How it works`; Block 4 `Workflow`; Block 5 `Benefits`; Block 6 `Get started`; Block 7 `Everyday use`; Block 8 `Our capabilities`; Block 9 `Why HLB HAMT`; Block 10 `How we work`; Block 11 `Common questions`; Block 12 `Get started`.

| # | Block | Format | Template classes to reuse / add | Image slot | Word budget |
|---|---|---|---|---|---|
| 1 | Hero + side panel | Template pattern exactly | `header.hero` > `.hero-grid`; `.eyebrow`, `h1`, `.lede`, `.hero-cta`; `aside.side` with `h3`, `.sub`, 3 × `.side-row` | none | 120-135 |
| 2 | Stats band | 3 stats (dark band) | `section.stats.plain` > `.stats-head` + `.stats-in` × 3 `.stat` (`.n`, `.l`, `.d`) + `<sup>` footnote markers | none | 85-100 |
| 3 | How it works `#how` | **PROSE** (3 paragraphs) + **IMG-1** + **data table** | `section#how.wash`; `.sec-head` (eyebrow + H2 only); new `.prose` wrapper (max-width 70ch, body size); `figure.img-slot`; new `table.datamap` | **IMG-1** integration architecture diagram | 240-275 |
| 4 | Quote-to-order workflow `#workflow` | **PROSE lede + numbered list** beside **IMG-2** | `section#workflow`; `.wrap.grid-2` (list left, figure right) | **IMG-2** swimlane workflow diagram | 120-140 |
| 5 | Business case + benefits `#benefits` | **PROSE** beside **IMG-3**, then **6 CARDS** | `section#benefits.wash`; `.grid-2` (prose left, figure right); then `.grid-3` of 6 × `.card` (`.card-icon`, `h3`, `p`) | **IMG-3** SugarAI account dashboard screenshot | 225-250 |
| 6 | Mid-page CTA | Template pattern | `section.cta-band.plain` centred; eyebrow, H2, p, 1 × btn-light | none | 20-26 |
| 7 | Where teams work | **PROSE** (2 paragraphs) beside **IMG-4** | `section`; `.grid-2` (figure left, prose right, mirroring Block 5) | **IMG-4** Outlook sidebar + mobile composite | 117-132 |
| 8 | Services `#services` | **Numbered list**, 6 items in 2 columns | `section#services.wash`; `.sec-head`; `.svc-cols` 2 × 3 `.svc` (`.k`, `h4`, `p`) | none | 140-160 |
| 9 | Why HLB HAMT `#why` | **PROSE** paragraph + **4 credential tiles** | `section#why`; `.sec-head` (eyebrow, H2, lede-sized prose paragraph); `.grid-4` of 4 × `.card` (`h3`, `p`) | none | 130-150 |
| 10 | Process `#process` | Timeline (6 steps) + **PROSE callout** | `section#process.wash`; `.proc` × 6 `.proc-step`; `.proc-note` | none | 115-135 |
| 11 | FAQ `#faq` | 5 Q&As (first open) | `section#faq`; `details.faq` × 5 | none | 204-254 |
| 12 | Closing CTA `#start` | Template pattern | `section#start.cta-band` > `.cta-grid`; H2, btn-light; `.cta-card` H4 + 3 `.row` | none | 46-52 |
| | **Total** | | | **4 image slots** | **1,562-1,809 budgeted; write to 1,580-1,680, aim ~1,620, hard ceiling 1,700** |

**Format tally:** prose-led blocks = 3, 4, 5 (first half), 7, 9 (paragraph) and the 10 callout; card blocks = 5 (benefits grid) and 9 (4 credential tiles); list/table formats = 3 (table), 4 (numbered list), 8 (numbered services), 10 (timeline). That is deliberately far fewer cards than Insurance/FSM, which used cards or tiles in 7 blocks.

If the draft runs long, trim in this order: FAQ answers (to about 30 words), Block 8 item bodies (to about 15 words), the Block 9 paragraph, the side panel rows. **Do not drop any block, image slot, table row, list step, card, services item, process step or FAQ.**

### 3c. Image placeholders (all four are mandatory, in both HTML and docx)

- **HTML:** `<figure class="img-slot" data-slot="IMG-n" style="aspect-ratio:W/H">` containing a dashed-border box (`border:2px dashed var(--line)`, `background:var(--wash-2)`, `border-radius:var(--radius)`, centred `.img-label` text `Image placeholder IMG-n: <short name>`) and a `<figcaption>` holding the caption. Put the brief description below in an HTML comment inside the figure for the designer. Deliver adds the `.img-slot` CSS (template has none). Give each slot an `alt` value for later use on the real image.
- **Docx:** a one-cell bordered table, grey-shaded and at least 6 cm tall, containing `[IMAGE PLACEHOLDER IMG-n: <short name>]` followed by the designer description, with the caption as a normal paragraph under it.
- **Originality rule for all images:** do **not** recreate or trace any TCP slide (slides 7, 8, 9, 11, 12 show a data-flow diagram, a Sugar record screenshot, a swimlane, an Outlook screenshot and phone screenshots). Build original diagrams in the template's colour variables, with HLB HAMT's own labels and layout. **No TCP, "fluent", Codeless or other vendor logos.** Screenshots must come from an HLB HAMT demo instance with fictional data, or else be clearly captioned as illustrative (see Open Question 4).

| Slot | Block | Short name | What it must show | Aspect | Caption (counts toward words; use as written) | Alt text (not counted) |
|---|---|---|---|---|---|---|
| IMG-1 | 3 | Integration architecture | Three-column system diagram. **Left:** SugarAI block (Sell, Serve, Market; small Outlook add-in and mobile icons). **Right:** Epicor ERP block (labelled "Epicor Kinetic, cloud or on-premise"). **Centre:** a connection layer labelled "Integration configured by HLB HAMT" with two lanes: (a) **Synchronised records**: two-way arrows for customers/accounts, contacts, quotes, cases; one-way arrows Epicor → SugarAI for parts, price lists, invoices, order status; (b) **Live views**: dotted arrow for credit status, stock and open orders, read on demand. A small "monitoring and error log" icon under the centre. | 16:9 (min 1200×675) | `How SugarAI and Epicor exchange records, and where live Epicor views appear.` | Diagram of SugarAI and Epicor ERP connected by a synchronisation lane and a live-view lane |
| IMG-2 | 4 | Quote-to-order swimlane | Two horizontal lanes, "SugarAI" (top) and "Epicor" (bottom), with **six numbered steps whose wording matches the Block 4 list exactly** (Build writes the list first; the designer copies it). Hand-off arrows between lanes at steps 2, 3, 5 and 6. HLB HAMT teal for SugarAI steps, blue for Epicor steps. **Must not** reuse TCP's box labels ("Opportunity stage: Quoting", "New Draft Quote", "Quote Ready", "New Draft Sales Quote") or its 4-column grid layout. | 2:1 (min 1200×600) | `Each step updates the other system, so no one re-keys the order.` | Swimlane diagram of a quote moving from SugarAI to an Epicor sales order |
| IMG-3 | 5 | Account dashboard screenshot | A SugarAI account record for a **fictional** UAE distributor (for example "Gulf Fasteners Trading LLC"; do **not** use "Northern Depot" or any TCP sample name) showing: opportunity pipeline on the left, and an **Epicor panel** on the right with payment terms, credit status, open sales orders and the last five invoices. Standard SugarAI theme (no TCP "Kinetic theme"). | 4:3 (min 1200×900) | `A SugarAI account record with Epicor orders, invoices and credit status alongside the pipeline.` | SugarAI account record showing Epicor order and invoice data |
| IMG-4 | 7 | Outlook + mobile composite | Left: Outlook with the Sugar Connect sidebar open on a contact, showing the related account. Right: the SugarAI mobile app on a phone showing the same account with its Epicor-synchronised fields (terms, recent orders). Fictional data only. | 4:3 (min 1200×900) | `The same customer record in the email sidebar and the SugarAI mobile app.` (Do not write "Outlook" here: Block 7 paragraph 1 holds the page's single permitted mention.) | Sugar Connect sidebar in Outlook beside the SugarAI mobile app showing one account |

### 3d. Footnotes, sources and schema
- Put a numbered marker (`<sup class="fn"><a href="#src-n">[n]</a></sup>`) after each stat or sourced fact in Blocks 2, 5, 7 and 9. The page has **one Sources note**, placed after the FAQ and before the closing CTA, listing [1]-[5] (Section 6). **FAQ answers carry no inline markers**, so the FAQPage JSON-LD can repeat the visible answers word for word (FSM precedent). FAQ 4's source is still listed in the Sources note.
- Build the **FAQPage JSON-LD from the 5 visible Q&As only, word for word.** Do not copy the Insurance template's 9-entry schema pattern.
- **Footer:** reuse the template footer. Replace the industry links with: `CRM Solutions (SugarAI)` (hub, per Open Question 3), `Manufacturing & distribution` → https://hlbhamt.com/industries/manufacture-and-distribution/, `ERP integration & add-ons` → https://hlbhamt.com/services/erp-integration-add-ons/.

---

## 4. Section-by-section outline

### Use of the TCP webinar deck (applies to every block)

The deck is **TCP Americas' own sales material** and is treated as a competitor reference.

- **Never reuse, rename or re-attribute, in copy, images, alt text or schema:**
  - the "fluent" / "Fluent Integration by TCP" product name;
  - the 14-day free trial and its contents (dedicated instance, personal guide, no credit card);
  - the Southern Aluminum (James Palazzi) and West Coast Metals (Joe Towle) testimonials;
  - "200+ customers on Epicor Kinetic" and "150+ Sugar implementations";
  - TCP's partner tiers and its customer logos;
  - any slide heading or line, or a close paraphrase of one (for example "Two sales days per seller lost every week", "Perfectly integrated, out of the box", "Work where you are", "Why Epicor + SugarCRM excels", "Purpose-built for Epicor").
- **May inform the page, rewritten from scratch:**
  - the generic sync pattern (Block 3 table);
  - the generic "Epicor data visible on the CRM record" concept (Blocks 3, 5, IMG-3);
  - the generic quote-to-order workflow, re-sequenced with an HLB HAMT approval/credit step (Block 4);
  - SugarAI's native Sugar Connect and mobile app (Block 7, verified separately against support.sugarai.com);
  - generic value reasons (Block 5 cards).
- **Not usable even though the deck shows it:**
  - offline mobile ("even offline on the factory floor", slide 14): not verified as a SugarAI capability;
  - "live views into **any** Epicor data" (slide 8): an overclaim;
  - the "two sales days" figures (slide 5): failed re-verification, see Section 6c.

### Accuracy guardrails (Build must follow; Test checks)

**Allowed wording:**
- "bi-directional synchronisation" or "two-way sync";
- "live views of Epicor data inside SugarAI" (current Epicor data shown when the record is opened);
- "on change, or on a schedule agreed with you";
- "through Epicor's REST services and saved queries (BAQs)";
- "matching rules for duplicates and conflicts";
- "agreed field by field in discovery";
- "Epicor Kinetic, in the cloud or on-premise".

**Not allowed** (unconfirmed, or competitor claims):
- "real-time" as a blanket claim. It is OK only when describing a live view at the moment a record opens.
- "out of the box", "pre-built connector", "no code", "zero code", "plug and play", "live in hours".
- "certified Epicor partner", "Epicor implementation", or any Epicor partner tier (see Open Question 1).
- Any named middleware, iPaaS or connector product.
- "offline".
- "any Epicor data".
- Specific Epicor version numbers.
- AI that "forecasts demand" or "predicts" stock.
- Naming sales-i (Open Question 6).
- Pricing.
- Any customer name or testimonial.

**HLB HAMT facts available** (from the live hub, rewritten, not copied):
- 26 years in the UAE and GCC;
- certified SugarAI (SugarCRM) implementation partner;
- backed by the HLB network in 150+ countries;
- consulting, implementation, integration and support from one team;
- data flows agreed in discovery rather than a generic connector promised;
- at least two full rehearsal migrations into a test environment;
- configurations and integrations retested when SugarAI releases new functionality;
- a sales-focused rollout goes live in 6-10 weeks, and a programme with ERP integration and data migration runs 2.5-5 months, in phases;
- cloud, customer's own cloud subscription, or on-premise;
- Guided Low-Touch onboarding;
- a single service desk with a named service manager.

**Third-party tool names:** Epicor and SugarAI/SugarCRM (with Sugar Sell, Sugar Serve, Sugar Market, Sugar Connect) are the subject, so name them. "Outlook" may appear **once** (Block 7, needed to describe Sugar Connect). "iOS and Android" may appear once (Block 7). Name **no other** tools or vendors. Analyst sources (Nucleus Research, Avasant) are named in stat lines for honest attribution, per FSM Section 11.3. They are analysts, not competitors.

---

### Block 1. Hero (120-135 words)

- **Job:** Say what HLB HAMT delivers and for whom, positively. No problem-led opening.
- **Eyebrow:** `Integrations · Epicor ERP`
- **H1 (use as written):** `SugarAI CRM Integration with Epicor ERP` (primary keyword, instance 1).
- **Lede (45-55 words, 2 sentences):**
  - **Sentence 1** must open `HLB HAMT connects SugarAI with Epicor ERP` (secondary keyword, instance 1 of 2). It goes on to say that sales and service teams see Epicor orders, prices, stock and invoices on the customer record they already work in.
  - **Sentence 2:** Epicor stays the system of record, and HLB HAMT designs, builds and supports the connection for manufacturers and distributors across the UAE and GCC, cloud or on-premise.
- **Buttons:** `Request a demo` (btn-primary, `#start`) · `Talk to our integration team` (btn-ghost, `#start`).
- **Side panel H3 (use as written):** `What changes once both systems are connected`
- **Sub-line (12-15 words):** set up for manufacturers and distributors running Epicor across the UAE and GCC.
- **3 side rows** (strong label as written + a 12-14 word line each):
  1. `Orders and invoices on the account`: open orders, invoice status and payment terms from Epicor, visible on the SugarAI account.
  2. `Quotes priced from Epicor`: quotes built from Epicor parts and price lists, then passed to Epicor as orders without re-keying.
  3. `Service with the purchase history`: agents see what the customer bought, and when, before replying to a case.
- **Content source:** generic concepts only (live ERP view; quote-to-order). **Stat:** none.

### Block 2. Stats band (85-100 words)

- **H2 (use as written):** `What connected CRM and ERP data delivers`
- **Lede (18-22 words):** analyst research on Sugar customers that unified CRM and ERP data, and on CRM interoperability more widely, shows gains in selling and customer satisfaction. **Do not** call the research "independent" (the Nucleus study is hosted by SugarAI as a vendor resource), and do not present any figure as an HLB HAMT result.
- **3 stats** (`.n` / `.l` / `.d`; `.d` 16-20 words with the source named, then a footnote):
  1. **N1** `7%` / `Higher win rates` / d: average win-rate improvement Nucleus Research found among Sugar customers that brought CRM and ERP data together. [1]
  2. **N2** `~50%` / `Faster customisation` / d: approximate cut in customisation timelines that Sugar customers reported in the same Nucleus Research study. [1]
  3. **A1** `2.3×` / `Customer satisfaction gains` / d: how much more likely mid-sized firms that prioritise interoperability are to see measurable satisfaction gains, according to Avasant. [2]
- **Keywords:** none. **Content source:** none.

### Block 3. How it works `#how` (240-275 words): PROSE + IMG-1 + TABLE

- **H2 (use as written):** `How CRM integration with Epicor ERP works` (primary, instance 2).
- **Paragraph 1 (50-60 words). Division of labour:** Epicor remains the system of record for parts, pricing, stock, credit, sales orders, shipments and invoices. SugarAI is where sales, service and marketing teams manage accounts, opportunities, quotes, cases and campaigns. The connection lets each system read what it needs from the other, so a customer is created once and every team sees the same details.
- **Paragraph 2 (60-70 words). Two mechanisms, explained plainly:**
  - **Synchronisation:** records such as customers, contacts and quotes are copied between the systems when they change, or on a schedule agreed with you, with matching rules that catch duplicates and decide which system wins a conflict.
  - **Live views:** SugarAI reads Epicor at the moment a user opens a record, showing open orders, quote history or credit status without storing a second copy.
  - The paragraph should also mention that the connection works through Epicor's REST services and saved queries (BAQs).
- **Paragraph 3 (25-30 words). Scoping:** which records move, in which direction and how often is agreed field by field in discovery. The table below is the usual starting point, not a fixed package. (This reflects HLB HAMT's hub position on discovery. Do not reuse the hub's sentence.)
- **IMG-1** goes after paragraph 3 (Section 3c), with caption.
- **Table** `table.datamap`, 3 columns: `Record` | `Direction` | `What it gives your teams`. **7 rows, cell text as short as shown** (about 70-85 words in total). Build may tighten the third column but must keep every row and direction exactly:
  1. Customers and accounts | Both ways | One customer record for sales, service and finance
  2. Contacts | Both ways | The same buyer details in both systems
  3. Quotes | Both ways | Built in SugarAI, costed and confirmed in Epicor
  4. Sales orders | Created in Epicor from SugarAI; status returns | Order progress on the opportunity and account
  5. Invoices and payment status | Epicor to SugarAI | Account managers see what is billed and outstanding
  6. Parts and price lists | Epicor to SugarAI | Quotes use current part numbers and prices
  7. Credit status, stock, open orders | Live view | Current Epicor figures when the record opens
- **Content source:** deck slide 7 informs the generic pattern only. The direction choices differ deliberately (orders are created in Epicor rather than "bi-directional"; invoices are one-way), which is also the more accurate system-of-record model. **Keywords:** primary in H2 only. **Stat:** none.

### Block 4. Quote-to-order workflow `#workflow` (120-140 words): PROSE LEDE + NUMBERED LIST + IMG-2

- **H2 (use as written):** `From SugarAI quote to Epicor sales order`
- **Lede (20-25 words):** a typical workflow HLB HAMT configures, in which each system moves the deal forward and updates the other at every hand-off.
- **Ordered list, 6 steps** (13-16 words each; IMG-2 copies this wording):
  1. A salesperson builds the quote in SugarAI from Epicor parts and prices, and the opportunity moves to quoting.
  2. The quote is created in Epicor, where costing, lead time and any credit check are applied.
  3. Once Epicor confirms the quote, SugarAI updates the quote and opportunity automatically.
  4. The customer accepts and the salesperson marks the opportunity as won in SugarAI.
  5. Epicor creates the sales order from the won quote, with nothing typed twice.
  6. Order, shipment and invoice status flow back to the SugarAI account, and the opportunity closes.
- **IMG-2** sits in the right column of `.grid-2` (list on the left), with caption.
- **Content source:** deck slide 9 informs the generic pattern. Step 2's costing and credit check is an HLB HAMT addition. Do not reuse the slide's stage names. **Keywords:** none. **Stat:** none.

### Block 5. Business case + benefits `#benefits` (225-250 words): PROSE + IMG-3, then 6 CARDS

- **H2 (use as written):** `The business case for one shared customer record`
- **Prose (65-80 words, left column; IMG-3 in the right column):**
  - **Sentence 1** must contain `CRM integration with Epicor ERP` (primary, instance 3). Its message is that the integration turns two accurate systems into one working view of each customer.
  - **Sentence 2** cites **A2** constructively: Avasant found that more than 60% of enterprises still work with fragmented data environments [2]. Connecting SugarAI and Epicor removes that split for sales, service and finance.
  - **Closing sentence:** salespeople quote from real prices and stock, service sees what was shipped, finance stops re-keying orders, and managers forecast from orders as well as pipeline.
- **IMG-3** with caption.
- **6 cards** in `.grid-3` (H3 as written; body 18-20 words each):
  1. `One customer record across teams`: sales, service and finance work from the same account, contacts and terms, maintained once.
  2. `Quotes built on current prices and stock`: Epicor part numbers, price lists and availability inside the SugarAI quote, so fewer quotes need rework.
  3. `Orders without re-keying`: won quotes become Epicor sales orders automatically, cutting manual entry and the errors that come with it.
  4. `Service that knows the order history`: agents see shipments, invoices and past cases before they reply, so answers are faster and accurate.
  5. `Campaigns based on what customers buy`: Sugar Market segments accounts by Epicor order history, so campaigns can target reorders and lapsed buyers.
  6. `Forecasts grounded in orders`: managers see pipeline next to booked orders and invoiced revenue, and SugarAI's AI works from fuller account history.
- **No stats inside the cards.** The deck's slide 17 reasons inform cards 1, 5 and 6 generically. Do not reuse its headings. **Keywords:** primary in prose only.

### Block 6. Mid-page CTA (20-26 words)

- **H2 (use as written):** `Ready to bring Epicor data into every sales conversation?`
- **Body (one sentence, 10-14 words):** see SugarAI working with your own Epicor customers, quotes and orders.
- **Button:** `See SugarAI in Action` (series-standard label).

### Block 7. Where teams work (117-132 words): PROSE + IMG-4

- **H2 (use as written):** `Epicor data wherever your teams work`
- **IMG-4** in the left column, prose in the right column.
- **Paragraph 1 (55-60 words):** with **Sugar Connect**, SugarAI's add-in for Outlook (the single permitted "Outlook" mention), people can view, create and update SugarAI records from their inbox, keep contacts and calendars in sync, and file emails to the account. Epicor details synchronised to the account travel with it. The **SugarAI mobile app** for iOS and Android shows the same account record on the road. **Do not** claim offline use or live Epicor views on mobile; synchronised fields only.
- **Paragraph 2 (45-55 words):** SugarAI's built-in AI (lead and deal scoring, account summaries, next-best-action guidance) works better when order and invoice history sits on the record. Then cite **F1**: SugarAI was named a Leader in the Nucleus Research Sales Force Automation Technology Value Matrix 2026, its sixth consecutive year as a Nucleus Leader, with ERP-informed insight among the strengths cited [3].
- **Content source:** deck slides 11-12 confirm the feature set. They are verified independently against support.sugarai.com (Section 6d). The TCP testimonial on slide 11 is not used. **Keywords:** none. **Stat:** F1 (credential).

### Block 8. Services `#services` (140-160 words): NUMBERED LIST

- **H2 (use as written):** `CRM integration services for SugarAI and Epicor` (secondary, instance 1 of 2).
- **Lede (12-15 words):** one HLB HAMT team from data map to support, on the SugarAI side and the connection.
- **6 items** in 2 columns × 3 (H4 as written; body 16-19 words):
  - **01** `Integration discovery and data mapping`: workshops with sales, service, finance and your Epicor owner to agree every record, field, direction and frequency.
  - **02** `SugarAI CRM implementation` (secondary "CRM implementation", instance 1 of 2): opens "Our SugarAI CRM services configure ..." (internal link 1 on that phrase), then says the platform is set up for your sales and service process, ready to receive Epicor data from day one.
  - **03** `Synchronisation and live views`: two-way sync, one-way reference data and live Epicor views built and configured to the agreed data map.
  - **04** `Data migration and de-duplication`: existing CRM and Epicor customer records matched, cleaned and rehearsed in a test environment before cutover.
  - **05** `Testing, monitoring and error handling`: end-to-end tests of the quote-to-order flow, sync logs, and alerts when a record fails to transfer.
  - **06** `Support and upgrade testing`: support under agreed service levels, with the integration retested when SugarAI or Epicor releases change.
- **Keywords:** H2 and item 02 H4 only. **Stat:** none.

### Block 9. Why HLB HAMT `#why` (130-150 words): PROSE + 4 CREDENTIAL TILES

- **H2 (use as written):** `Why choose HLB HAMT as your CRM integration partner` (secondary, the only instance).
- **Paragraph (50-60 words, `.lede` style):**
  - Manufacturing and distribution are expanding fast in the region: UAE industrial exports passed **AED 262 billion in 2025** [4].
  - Many groups run mainland, free zone and GCC entities as separate Epicor companies. HLB HAMT maps each one to the right SugarAI teams and records, sets SugarAI up in Arabic and English, and works alongside your Epicor partner or in-house ERP team.
  - **Do not** imply HLB HAMT implements or is certified on Epicor (Open Question 1).
- **4 tiles** in `.grid-4` (H3 as written; 14-16 words each):
  1. `26 years in the UAE and GCC`: advising and building business systems for organisations across the region. **Do not add a founding year:** "since 1999" would conflict with "26 years" in 2026.
  2. `Certified SugarAI partner`: implementation, customisation and integration of SugarAI, cloud, private cloud or on-premise.
  3. `ERP and CRM under one roof`: an ERP practice and a CRM practice in one firm, so integration questions get answered on both sides. Link to https://hlbhamt.com/services/erp-integration-add-ons/ (internal link 3).
  4. `Support after go-live`: one service desk, agreed service levels, a named service manager and a clear escalation path.
- **Stat:** U1 in prose only.

### Block 10. Process `#process` (115-135 words): TIMELINE + PROSE CALLOUT

- **H2 (use as written):** `How we deliver your SugarAI and Epicor integration`
- **Lede (15-18 words):** must contain `CRM implementation` (secondary, instance 2 of 2). The idea: the same staged method applies whether this is a new CRM implementation or an existing SugarAI instance being connected to Epicor, with sign-off at each stage.
- **6 steps.** Keep the series step names as H4s: `Discovery`, `Solution design`, `Configure and build`, `Data migration`, `Test and train`, `Go-live and support`. Write new descriptions (8-10 words each) specific to integration:
  1. Map how a quote becomes an order and invoice today.
  2. Data map, sync rules and conflict rules agreed and signed off.
  3. SugarAI configured; synchronisation and live views built to the map.
  4. Customer records matched and cleaned, with two full rehearsals.
  5. Quote-to-order tested end to end; role-based training delivered.
  6. Phased go-live with hypercare, then managed support under SLA.
- **Callout `.proc-note`, H4 (use as written):** `Realistic timelines, delivered in phases`
  - **Body (28-34 words):** a sales-focused SugarAI rollout usually goes live in six to ten weeks. A programme that adds Epicor integration and data migration typically runs 2.5 to 5 months, so first users are working well before the last phase. (These are HLB HAMT's own published figures from the live hub FAQ: company facts, no footnote.)

### Block 11. FAQ `#faq` (204-254 words; 5 Q&As; answers 30-36 words; direct answer first; no inline footnote markers)

- **H2 (use as written):** `Questions about connecting SugarAI and Epicor`
1. **Q (use as written):** `Does SugarAI with Epicor ERP work for Kinetic in the cloud and on-premise?` (secondary, instance 2 of 2)
   **A:** Yes. The connection uses Epicor's REST services, which are available for both. Older Epicor ERP versions are assessed during discovery. SugarAI itself can also run in the cloud, in your own cloud subscription, or on-premise.
2. **Q:** `Which system owns the customer data?`
   **A:** Sentence 1 must contain `CRM integration with Epicor ERP` (primary, instance 4). The gist: in most of these projects ownership is agreed field by field. Epicor usually owns terms, credit and billing details, SugarAI owns contacts and activities, and matching rules settle duplicates and conflicts.
3. **Q:** `How quickly do changes appear in the other system?`
   **A:** It depends on the pattern. Live views show current Epicor data when the record opens. Synchronised records update when they change or on a schedule you agree, and every transfer is logged.
4. **Q:** `We already run SugarCRM. Can you connect our existing instance to Epicor?`
   **A:** Yes. SugarCRM became SugarAI in April 2026 and existing instances carry on (source [5] in the Sources note, no inline marker). HLB HAMT reviews your current configuration and any existing connector, then extends, repairs or replaces it.
5. **Q:** `Who supports the integration after go-live?`
   **A:** Must contain `CRM integration services` (secondary, instance 2 of 2). The gist: HLB HAMT's support team, under agreed service levels; sync monitoring, error follow-up and retesting after SugarAI releases or Epicor updates are part of our CRM integration services, with a named service manager.
- None of these duplicates an Insurance or FSM FAQ. The FSM FAQ 7 rebrand fact is reused as a fact only, in new wording. **FAQs carry no stats.**

### Block 12. Closing CTA `#start` (46-52 words)

- **H2 (use as written):** `See your own Epicor quotes and orders working inside SugarAI.`
- **Button:** `Talk to our integration team` → `/contact/`.
- **`.cta-card` H4:** `What happens next`
- **3 rows** (11-13 words each):
  1. A discovery call on your Epicor setup, sales process and current CRM.
  2. A demonstration of SugarAI working with sample Epicor quotes and orders.
  3. A written proposal with the data map, phases, timeline and investment.
- **No "free trial" or trial-instance offer of any kind** (TCP's offer, per caveat).

---

## 5. Competitive and reference analysis

**Direction only.** Nothing from these pages, or from the TCP deck, may be copied or closely paraphrased: no sentences, headings, slide titles or distinctive phrases. The Test agent's originality check must cover all five reference URLs, the TCP deck extraction and the Insurance template. **Do not name any of these companies or products on the page.**

- **TCP / "Fluent" (tcpamericas.com page, fetched; marketplace.sugarai.com listing, via search; the TCP deck).** Product-led: a cloud subscription connector with a self-service portal, point-and-click configuration, a "no code" and "hours, not weeks" pitch, sync for accounts/customers, contacts, quotes, orders, invoices and cases, one-way price and parts lists, BAQ-powered dashlets, Epicor 10.2.500+, cloud or on-premise. It also repeats the "two selling days a week" claim with no source on the page.
  - **What it does well:** concrete data-flow and workflow visuals.
  - **Gaps:** it sells a tool, not an outcome-owned project. There is little on discovery, data cleansing, migration, conflict ownership or support, and nothing regional.
  - **Our angle:** partner-led and scoped. Agree the data map first, then build, test and support it as part of a SugarAI implementation, in the UAE/GCC.
- **fluenterp.com Epicor-SugarCRM page (fetched).** Apparently the same TCP product under another domain, so two of the five references are one vendor. It has a strong FAQ set (what syncs, live views, conflict handling, duplicate data, sync timing), a sync-monitoring panel and published per-workflow pricing.
  - **Takeaway:** these are the buyer's real questions. Our FAQ 2 and 3 answer ownership and timing in our own words, and services item 05 covers monitoring.
  - **Do not** publish pricing or monitoring metrics.
- **Codeless Platforms (403 on fetch; search-result text only).** An iPaaS/BPA tool: a drag-and-drop mapping layer that syncs accounts, contacts, products, price lists, quotes, sales orders and invoices.
  - **Takeaway:** it confirms the standard record set (our table matches it).
  - **Gap:** generic and tool-centred, with no CRM implementation, process design or service angle.
- **SugarAI's LinkedIn article "Boost sales and service with Epicor ERP and SugarCRM" (fetched; published by SugarAI, 3 April 2025).** Benefit-led (360° view, automation, scale, cross-team alignment, AI), with high-level "API-driven, bi-directional" wording, no figures and no workflow detail. It also suggests AI "demand forecasting", which we do not claim.
  - **Takeaway:** this is the vendor's own benefit language. Our Block 5 covers similar ground but adds the mechanics, the data map and visuals.
- **Wider market (from search):** Epicor itself offers integration tooling with prebuilt CRM templates, and other Epicor connectors are listed on the SugarAI marketplace. Buyers therefore have several tool options, and the differentiator is the partner.
- **Positioning angle:** none of the references combines (a) a SugarAI implementation partner, (b) a scoped, documented Epicor data map agreed in discovery, (c) migration, testing, monitoring and post-release retesting under one support contract, and (d) UAE/GCC delivery (multi-entity groups, Arabic/English, cloud or on-premise). Own that combination, and explain it in prose with diagrams, which none of them does in full.

---

## 6. Stats and data points

Ages are as of October 2026. **Every stat is used in exactly one place.** None appears on the Power BI, Advanced Analytics or Data Visualization homepages (their sources were PwC, HLB Global, Gartner, McKinsey, BARC, UAE Government and Microsoft), and none repeats an Insurance or FSM figure.

### 6a. Stats planned for use

| ID | Exact figure | Context (one line) | Used in | Source URL | Date / age | Verification |
|---|---|---|---|---|---|---|
| N1 | **7%** "improvement in win rates" | Nucleus Research ROI case study (doc Z56), "How unifying CRM and ERP with Sugar drives sales performance": Sugar customers that unified CRM and ERP data. | Block 2, stat 1, footnote [1] | https://nucleusresearch.com/research/single/how-unifying-crm-and-erp-with-sugar-drives-sales-performance/ (vendor-hosted copy: https://sugarai.com/resources/nucleus-research-how-unifying-crm-and-erp-with-sugar-drives-sales-performance) | 8 April 2025 (~18 months) | **Fetched** from the Nucleus page this run. Sample size not disclosed. |
| N2 | **"approximate 50 percent reduction in customization timelines"** (display `~50%`) | Same Nucleus study, same Sugar customers. | Block 2, stat 2, footnote [1] | Same as N1 | 8 April 2025 (~18 months) | **Fetched** this run. The label must say "customisation timelines", not "integration time" or "implementation time". |
| A1 | **2.3×** "more likely to achieve measurable improvements in customer satisfaction" | Avasant: mid-sized enterprises that prioritise interoperability, from Avasant's Cloud CRM Suites 2024 RadarView, published in the article "Breaking Down Data Silos: Why CRM Integration Is Now a Boardroom Priority" (Acklin and Frederick). | Block 2, stat 3, footnote [2] | https://avasant.com/report/breaking-down-data-silos-why-crm-integration-is-now-a-boardroom-priority/ | Article Sept 2025 (~13 months); underlying data 2024 (~2 years) | **Fetched** this run. Avasant is an independent research and advisory firm. The figure applies to **mid-sized enterprises**, so keep that qualifier. |
| A2 | **"over 60% of enterprises"** still operate with fragmented data environments | Same Avasant article and RadarView. | Block 5 prose, footnote [2] | Same as A1 | Same as A1 | **Fetched** this run. Write "more than 60%". |
| U1 | UAE industrial exports **surpassed AED 262 billion in 2025** | Announced by Hassan Al Nowais, Undersecretary, UAE Ministry of Industry and Advanced Technology; the industrial sector's GDP contribution rose nearly 70% since 2021. | Block 9 prose, footnote [4] | https://www.khaleejtimes.com/business/uae-industrial-exports-hit-dh262b-as-sectors-gdp-contribution-climbs-by-70 | Published 10 June 2026 (~4 months) | **Fetched** this run. Government figure reported by a reputable UAE publication. Write "AED 262 billion" (not "Dh262b"). |

### 6b. Sourced non-stat facts (footnoted or logged)

| ID | Fact | Used in | Source URL | Date | Verification |
|---|---|---|---|---|---|
| F1 | Sugar named a **Leader in the Nucleus Research Sales Force Automation Technology Value Matrix 2026**, its sixth consecutive year as a Nucleus Leader. ERP-order-data insight is cited among its strengths. | Block 7, footnote [3] | https://www.businesswire.com/news/home/20260225695547/en (Business Wire original; 403 here). Fetched reprint: https://www.01net.it/sugarcrm-named-a-leader-in-the-nucleus-research-sales-force-automation-technology-value-matrix-2026/ | 25 Feb 2026 | Reprint fetched. The Business Wire original needs a click-check. The live HLB HAMT hub already shows this badge, so it is consistent with the site. |
| F2 | SugarCRM rebranded as SugarAI in April 2026 | FAQ 4 (Sources note [5], no inline marker) | https://www.businesswire.com/news/home/20260413034429/en/SugarCRM-Unveils-New-Brand-Identity-as-SugarAI-Declaring-the-Next-Generation-of-CRM (also https://sugarai.com/press-releases/sugarcrm-unveils-new-brand-identity-as-sugarai-declaring-the-next-generation-of-crm) | 13 Apr 2026 | Search only. Click-check. |
| F3 | Sugar Connect: Outlook add-in to view, create and update Sugar records, sync contacts and calendars, archive email | Block 7 (sources log only, no footnote) | https://support.sugarai.com/documentation/plug-ins/sugar_connect/sugar_connect_user_guide/ | Current docs | Search only. |
| F4 | SugarAI mobile app on iOS and Android (cloud or on-site instances) | Block 7 (sources log only) | https://support.sugarai.com/documentation/mobile_solutions/sugarai-mobile-app/sugarai-mobile-app-user-guide/ | Current docs | Search only. |
| F5 | Epicor Kinetic exposes business objects and BAQs through REST (v2) services | Block 3, FAQ 1 (sources log only) | Epicor's own REST help is per-instance (Swagger). Secondary explainer: https://knowledgelib.io/business/erp-integration/epicor-rest-api-v2/2026 | 2026 | Search only. A technical fact, so the page carries no version numbers. |
| F6 | HLB HAMT company facts (26 years, certified SugarAI partner, HLB network, one team, discovery-agreed data flows, two rehearsal migrations, post-release retesting, 6-10 weeks / 2.5-5 months) | Blocks 9, 10, FAQ | Live hub https://hlbhamt.com/sugarai-crm-2/ (saved text in `../2026-09-29-data-visualization-services-homepage/inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`, lines 399-459, 1365-1418) | Live | Company facts; no footnote (series convention). |

### 6c. Considered and rejected (Build must not use)

- **TCP "two sales days per seller lost every week" (8 hours searching for customer information / 35% of the week not engaging customers / 10 hours coordinating).** Re-verification failed:
  - The deck prints three sources but does not map any figure to any source.
  - "Reorder Management: 31 Manufacturer Rep Statistics and Trends (2025)" could not be found.
  - The BLS Occupational Outlook page for wholesale and manufacturing sales representatives covers work schedules (often over 40 hours) but none of the three figures.
  - Forrester's sales activity study page gives a **different** figure ("about 14 out of 51 hours a week on admin tasks", undated). Search snippets attribute "8 hours per week finding, updating and personalising communications" to Forrester, which is a different measure from "looking for customer information in ERP".
  - The claim is also problem-led.
  - **Not used anywhere, including in reworded form.**
- **Forrester "14 of 51 hours on admin".** Undated on the page, not about ERP data, negative framing.
- **Nucleus "8% average increase in recurring revenue per account" (same Z56 study).** The most on-topic figure, but it is already the FSM page's proof tile 3. **Reserve only**, if the Content Writer explicitly allows reuse from a sibling subpage (swap for N2).
- **Sugar Sell +23% / +30% / 3×, Sugar Serve -27% / +30%.** Already used on Insurance and FSM.
- **"180+ ERP integrations"** (sugarai.com resource page). A vendor count, not Epicor-specific; it was the Insurance proof tile that FSM removed.
- **Fluent/TCP monitoring figures** (2,847 runs, 99.2% success). Product UI sample data.
- **Aggregator figures** ("87% say CRM-ERP integration is critical", "95% of CRM users see higher conversion", "20-30% of revenue lost to silos", "35.31% cite synchronisation as top challenge"). Vendor blogs with no traceable primary source.
- **Salesforce/MuleSoft connectivity benchmark figures.** Competing-CRM-vendor research, rejected by the Content Writer on the FSM page.
- **Epicor "Future of Work in Manufacturing" survey figures.** Workforce topic, off-subject.
- **Epicor Middle East data centre news.** 2023 and could not be opened (403).

---

## 7. Draft meta title and meta description

- **Meta title (54 characters):** `CRM Integration with Epicor ERP for SugarAI | HLB HAMT`
  - Alternate that matches the H1 (50 characters): `SugarAI CRM Integration with Epicor ERP | HLB HAMT`. I recommend the first because the exact primary keyword leads.
- **Meta description (153 characters):** `CRM integration with Epicor ERP by HLB HAMT: SugarAI and Epicor share customers, quotes, orders and invoices, with live ERP data on every account record.`
  - Primary keyword at the front. No em dash. If the Content Writer wants the geo term, use this 155-character alternate: `CRM integration with Epicor ERP by HLB HAMT in the UAE: SugarAI and Epicor share customers, quotes, orders and invoices, with live ERP data on each record.`

---

## 8. Internal linking suggestions

URLs 1-4 come from the live HLB HAMT site navigation (in the saved hub HTML). Deliver should still confirm they resolve.

| # | Anchor text (use as written) | Target | Placement |
|---|---|---|---|
| 1 | `SugarAI CRM services` | https://hlbhamt.com/sugarai-crm-2/ | Block 8, item 02 body: open the body with "Our SugarAI CRM services configure ..." and link that phrase. Do not link the H4. |
| 2 | `manufacturers and distributors` | https://hlbhamt.com/industries/manufacture-and-distribution/ | Hero side-panel sub-line |
| 3 | `ERP practice` | https://hlbhamt.com/services/erp-integration-add-ons/ | Block 9, tile 3 |
| 4 (conditional) | `SugarAI for manufacturers` | `/sugarai-crm/industries/manufacturing/` (template footer path; **unverified**, as the FSM page notes) | Block 5, card 6 body. Include **only** if Deliver confirms the URL resolves; otherwise omit with no replacement. |

The breadcrumb already links Technology Consulting Services (https://hlbhamt.com/services/technology-consulting-services-dubai-uae/), so no body link to it is needed.

**Parent link:** see Open Question 3. Build uses the FSM precedent (`https://sugarai.com/`) unless the Content Writer decides otherwise.

---

## 9. Open questions / missing inputs

1. **HLB HAMT's relationship with Epicor (blocks claims in Blocks 1, 8, 9, FAQ 1).**
   - I found no Epicor partnership or Epicor page on hlbhamt.com.
   - HLB HAMT's ERP practice appears to be SAP Business One and Sage.
   - The brief therefore positions HLB HAMT as the **SugarAI** partner that integrates with the client's Epicor environment and works alongside their Epicor partner or in-house ERP team. It never claims Epicor certification, an Epicor partner tier or Epicor implementation.
   - Please confirm, or supply any Epicor credentials and Epicor integration projects HLB HAMT has delivered.
2. **How HLB HAMT actually builds the connection (Blocks 3, 8; FAQ 3, 4).**
   - The options are: a custom build on Epicor's REST services, an iPaaS, Epicor's own integration tooling with its SugarCRM template, or reselling a marketplace connector, possibly TCP's own product.
   - The brief keeps all wording method-neutral and bans "real-time", "pre-built", "no-code" and "out of the box" claims.
   - If HLB HAMT resells or deploys a third-party connector, tell me which. The copy must then stay accurate without naming it, unless you want it named.
3. **Parent and breadcrumb.**
   - The requirement gives https://sugarai.com/ as the parent, and for FSM you chose to keep the vendor URL as the link target. Build defaults to that precedent.
   - **My recommendation is to change it for this page.** Pointing the breadcrumb parent at an external vendor domain sends visitors off-site and passes no internal link value. The real hierarchy parent is HLB HAMT's live SugarAI CRM hub, https://hlbhamt.com/sugarai-crm-2/. Its "SugarAI System Integration" and "CRM & ERP Integrations" offerings are the natural parent topic.
   - Suggested slug: `/sugarai-crm/integrations/epicor-erp/`, or a sibling of the industry pages if no integrations section is planned.
   - Please choose: (a) keep `https://sugarai.com/` as in FSM, or (b) switch to `https://hlbhamt.com/sugarai-crm-2/` (and confirm the slug).
4. **Images.**
   - Is there an HLB HAMT SugarAI demo instance connected to an Epicor sandbox that can produce the IMG-3 and IMG-4 screenshots?
   - If not, they will be designer mock-ups, and each caption gains the word "Illustrative".
   - Who produces the IMG-1 and IMG-2 diagrams (HLB HAMT design team or Deliver as SVG)? The pipeline will reserve the slots either way.
5. **Which Epicor products are in scope.**
   - "Epicor ERP" covers several products: Kinetic and earlier Epicor ERP 10, but also Prophet 21, Eclipse and BisTrack, which have different APIs.
   - The brief assumes **Kinetic, plus earlier Epicor ERP 10 estates**, matching the webinar.
   - Confirm, or list the others HLB HAMT will support.
6. **Stats approval.**
   - Blocks 2 and 5 rely on one Nucleus study (vendor-hosted, sample size undisclosed) and one Avasant article (2024 data).
   - Approve them, or allow reuse of the Nucleus 8% recurring-revenue figure from the FSM page (Section 6c).
   - Separately, should SugarAI's ERP-analytics add-on (sales-i) be named as part of the offer? The default is not to name it.

---

Stopping here. No draft content has been written. Build starts after the Content Writer approves this brief and answers (or waives) the questions above.
