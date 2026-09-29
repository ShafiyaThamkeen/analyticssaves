# Test report v5: Power BI Services homepage (draft-v5.md, Revision 2)

Tested by: Test agent, 2026-09-29
Loop: **Revision 2, loop 1 of 3.** This is a fresh 3-loop budget. It is separate from the original v1-v3 loops (`test-report-v1.md` to `test-report-v3.md`) that led to the delivered v1 (draft-v4).

Inputs checked:
- `brief.md`, read in full. Section 12 (Revision 2) and Section 13 (Content Writer decisions) are treated as overriding Sections 1-10.
- `inputs/revision-2-notes.md`.
- `draft/draft-v5.md`: the whole page, the Sources list, the Stats used table and all 16 Flags.
- `draft/draft-v4.md` (the delivered v1), for the v4-echo check.
- `draft/test-report-v3.md`, for the standards used in the earlier loops.
- The 4 sibling pages in `inputs/hlbhamt-sibling-pages/*-extracted.txt`, at the in-scope line ranges from brief 12.0.
- `inputs/extracted/hlb-data-viz-v4 (1).html.md` (Tab 3).
- `inputs/structural-sample/sugarai-crm-homepage-extracted-text.txt`, all 772 lines.
- `inputs/competitor-content/zenzero.txt`, plus a ripgrep sweep of all 4 competitor files.
- The other project briefs in `content-pipeline/requirements/`, for the duplicate-stat check.

Method:
- No shell was available.
- Every on-page sentence was counted word by word under the brief Section 1 rule.
- Characters, keywords, brand names, stats, links and banned phrases were checked with ripgrep (`-o`) across the whole file. Non-page lines were then excluded: meta, the draft header, chrome, section structure headers, eyebrows, buttons, URLs, Sources, Stats used and Flags.
- Every changed or new sentence was compared against SugarAI, the four sibling pages, Tab 3 and v4.
- Distinctive phrases were web-searched.

---

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Keyword placement and density (incl. B4/B5 branding counts) | **PASS** |
| 2 | Word count | **PASS** (3,467) |
| 3 | Zero em dashes | **PASS** (0) |
| 4 | Grammar, spelling, punctuation | **FAIL** (2 errors, 1 British-usage fix) |
| 5 | Originality | **FAIL** (1 SugarAI echo: S11 tile 1, a regression of v3's R1) |
| 6 | Stat accuracy | **PASS** |
| 7 | Human tone / AI-detection heuristics | **FAIL** (all 6 S6 flip-card backs open "We + verb") |
| 8 | Section structure, AI Insights removal, anchor nav, links, schema | **PASS** |
| 9 | Client requirements (Revision 2 notes, Section 13, Section 10 corrections, B1-B7) | **PASS** |

Headline: the revision's substance is sound. These all pass:
- AI Insights is fully removed.
- There is no "certified" wording on the page.
- Every B1-B7 branding rule is met.
- Sibling-page reuse stays inside the limits.
- The stats are correct and single-slot. 73.3% is gone and the 33x footnote has been upgraded.
- The links are correct.

The failures are 5 sentence-level fixes, and none of them touches a keyword, stat, link or section.

---

## Hard checks requested by the caller

### A. AI Insights fully removed: PASS

- **No section:** there is no `#aiinsights` section, and no H2 "Ask Your Data a Question...".
- **No leftover points or AI features:** ripgrep for `key influencer|decomposition|narrative|anomal|smart narrative|Q&A|Azure M(achine )?L|generative|73.3|18.8` returns hits only in the draft header (line 7), Stats used (445) and Flags (455). None are on the page. There is no Answers/Explains/Alerts block.
- **Copilot:** it appears on the page only in FAQ 6 (line 385) and FAQ 8 (lines 390-391), as brief 12.2 requires. The only other "AI" hit (line 137) is Deliver's markup note "(mirrors the SugarAI 'AI Layer')", which is not page copy.
- **Relocated items:** L4 now sits in FAQ 4 (line 379) and P2 in S6 card 6 (line 188), both as 12.2 specifies.
- **Renumbering:** it matches the 12.2 table exactly (S0-S16, with S3 in chrome). S6 Use cases, S7 Services, S8 CTA 1, S9 PoC, S10 Engagement, S11 Why UAE, S12 See it in action, S13 CTA 2, S14 FAQ, S15 Contact, S16 Footer.
- **Anchor nav (line 16):** "Why HLB HAMT · The Platform · Use Cases · Services · Proof of Concept · Engagement Models · FAQ". This is identical to the 12.2 list, and `#explorepowerbi` is kept.

### B. No "certified" or "leading" language: PASS

- **Page copy:** ripgrep `(?i)certif|leading` returns 14 hits, all in the Flags section (lines 456-459). There are **0** on the page.
- **S11 tile 1 H3 (line 325):** "Power BI reselling partner in the UAE". This is exactly what Section 13 point 2 specifies.
- **Reselling wording:** licence copy describes the reselling relationship accurately in S7 item 01 (line 203) and FAQ 2 (line 373), as Section 13 permits.
- **Secondary keyword:** "Certified Power BI Partner in UAE" has **0** placements. Build did not swap "reselling" into the keyword string.
- **Meta title:** the primary Section 7 title is used, not the "Certified" alternate.

### C. HLB HAMT-led branding (B1-B7): PASS

| Rule | Evidence | Result |
|---|---|---|
| B1 | H1 (line 22): "HLB HAMT: Your Power BI Service Partner for Smarter Decisions in the UAE". This is verbatim from 12.3a. | Pass |
| B2 | First sentence of each opener: hero lede "HLB HAMT designs..."; S4 lede "HLB HAMT is a Power BI consulting company..."; S5 intro "HLB HAMT delivers your reporting..."; S6 intro "Our consultants begin..."; S7 intro "We handle..."; S9 intro "We prove..."; S10 intro "We offer..."; S11 intro "We expect...". None has Microsoft, Power BI, Fabric, Copilot, "the platform" or "data" as its subject. The 12.3c extras are also HLB-led: every S5 row description opens with an HLB action ("We build", "We set up", "Our engineers reach", "We design", "We assess"), and so does the deployment line ("We set up your environment...") | Pass |
| B3 | Every FAQ answer has an HLB HAMT or "we" subject: A1 "We set up both"; A2 "we advise on the right licence mix"; A3 "We reach sources"; A4 "we set alerts"; A5 "We design right-to-left"; A6 "We configure row-level security"; A7 "we plan it in stages"; A8 "we prepare those", "we put Arabic into report design"; A9 "We work through the pipeline"; A10 "HLB HAMT confirms the timeline". A1 and A7 open on the product, which B3 allows for factual definitions. | Pass |
| B4 | "HLB HAMT" on the page = **12** (range 10-16): H1 (22); lede (24); S2 item 2 (51); S2b (61); S4 lede (71); S5 H2 (89); S5 intro (91); S7 H2 (198); S10 featured H3 (263); S11 H2 (321); S12 H2 (347); A10 (397). Excluded: eyebrows (20, 67, 319), draft structure headers (65, 194, 317), meta, Sources and Flags. | Pass |
| B5 | "Microsoft" on the page = **7** (cap 12): S1 deployment line (41); S2b x2 (61); S5 platform (140); A2 (373); A6 (385); Q7 (387). Excluded: the S2b button label and URL (63), plus Sources and Flags. | Pass |
| B6 | Banned phrases: none present. There is no "Microsoft Power BI" eyebrow (the S1 eyebrow is "HLB HAMT POWER BI SERVICES"), no "Why Power BI: From Raw Data...", no "Power BI is Microsoft's business intelligence platform", no "Microsoft supplies a capable platform" and no "Microsoft Power BI PowerUP!" (S10 H3 is "PowerUP!: HLB HAMT's Fixed-Price Power BI Accelerator"). There is also no bare "Microsoft: named a Leader...": S2b opens "HLB HAMT builds on Microsoft Power BI and Fabric." "Microsoft Power BI" does occur once, inside that S2b sentence as a product name, which matches the brief's own 12.5 example. | Pass |
| B7 | Attribution is honest throughout. **200+:** S2 item 1 reads "Power BI connectors; we configure yours and build missing ones", so it is the platform's library and not HLB's. **Gartner:** S2b reads "Microsoft was named a Leader...". **UAE regions:** "Microsoft's UAE North (Dubai) or UAE Central (Abu Dhabi) cloud region". **Fabric:** "Microsoft reports more than 40,000...". **ISO/SOC:** "The Power BI platform falls within the scope of Microsoft's ISO/IEC 27001 and SOC 2 audits". **Partner status:** the tile 1 wording is uncertified. | Pass |

### D. Sibling-page sourcing and reuse limit (12.0 / Section 13.1): PASS (brief-level notes in 5d)

| Claim | Draft | Sibling source | Verdict |
|---|---|---|---|
| S7 item 04 (line 212) | "we tune across the pipeline, data model and semantic layers, cutting query load, adding aggregation tables over large fact tables and replacing heavy measures with efficient DAX patterns... we implement row-level security, workspace governance and access controls, so each person sees only the data their role allows" | dashboard page 549-557: "Optimisation of data models and reports through query reduction, indexing strategies, aggregation tables, and efficient DAX patterns..."; "Implementation of role-level security (RLS), workspace governance, access controls..."; data-viz 500: "Optimization across pipeline, data model, and semantic layers" | **Accurate.** Only terms and a 7-word phrase are reused; no sentence is copied. The "so each person sees..." benefit clause is original. |
| S4 card 3 (line 80) | "five stages: we define the KPIs and their metric logic, model the data, design the report architecture and user experience, validate accuracy and tune performance, then deploy and drive adoption" | dashboard page 566-600: "Context & KPI Definition / Data Modelling & Foundation Setup / Report Architecture & UX Design / Validation & Performance Tuning / Deployment & Adoption Enablement" | **Accurate**, and in the right order. It is condensed from the stage titles as a verb list, as 12.5 prescribes. It is unnumbered, has no H3s, no durations and no "7 days", and is distinct from the S9 PoC steps. |
| S7 item 05, Tableau/Qlik (line 215) | "We migrate Tableau and Qlik environments to Power BI, carrying your business logic across and redesigning each visual for the new platform instead of copying screens one for one." | data-viz 507-509: "Migrate your existing Tableau environment to Microsoft Power BI with minimal disruption. We preserve business logic, redesign visualizations for the Power BI ecosystem..."; data-viz 626-627 names Qlik | **Accurate.** There is no "zero business logic loss", no price comparison and no copied sentence. The unit order (migrate / preserve logic / redesign visuals) follows brief 12.5, which prescribes exactly this sequence ("preserving business logic and redesigning visuals for the new platform"). It is brief-level, so it is not scored; see 5d. |
| S2 "Since 1999" (lines 54-55) [12] | "Since 1999 / A licensed UAE audit, tax and advisory firm that also builds your data platform." | Brief 12.5 prescribes this description verbatim. Web search today: "HLB HAMT began as HAMT & Associates in 1999... and joined HLB International in 2007" (hlbhamt.com 25-years pages and press release) | **Accurate.** There is no "25 years" and no staff or client counts. |
| New slow-dashboards FAQ (A9, line 394) | "The tool is rarely the problem; how the report was built almost always is. Typical causes are a weak data model, inefficient DAX or queries, large datasets nobody has optimised, and missing aggregations or indexing. We work through the pipeline, the model and the semantic layer..." | dashboard page 755-764: "Poor data modelling / Inefficient queries or DAX calculations / Large, unoptimised datasets / Lack of aggregation or indexing strategies. Performance depends more on implementation quality than the tool itself." | **Accurate, and not copied.** The four causes keep the source's order, but brief 12.5 prescribes the list in that order, and each item is reworded. The tool-vs-build claim is moved and inverted. The retest-at-volume and "trimming what each visual asks for" content is original. No 33x. **Advisory 5d-3:** "almost always" is stronger than the source's "depends more on". |
| Partner page (redirecting; freer reuse) | S6 card 3 back, S9 steps, PowerUP! story, terms and deliverables, CxO lists, A4 "hours of weekly manual reporting" | partner page 480-605, 652-657, 687-688 | All are original sentences, not pasted blocks. The closest is S6 card 3 sentence 1, where the DLD metric list follows the source list order. That is allowed under Section 13 point 1 and is a brief-mandated fact list. |

**Undisclosed reuse (not a fail, for the record):** Flags item 11 lists only one phrase taken from the consulting page. However, the S7 intro (line 200) "We handle every stage of a Power BI programme ourselves, from strategy through to post-launch support" also follows the consulting page's "cover every stage of Power BI implementation, from crafting a solid strategy to deployment and ongoing support" (line 415-417). It is a common industry frame and matches the brief's Section 4 prescription ("end-to-end delivery from first workshop to ongoing support"), so it is scored as a brief-level echo (5d-1), not a violation.

---

## 1. Keyword placement and density: PASS

On-page copy only, per Section 2a. Ripgrep has no look-ahead, so the singular was matched with `(?i)Power BI services?` and each hit was classified by hand.

| Keyword | Count | Placements (draft line) | Target | Result |
|---|---|---|---|---|
| "Power BI service" singular | **6** | H1 (22); hero lede sentence 1 (24); S4 card 1 (74); S5 row 2 H3 (106); FAQ Q1 (369); FAQ A1, once (370) | 5-7 (max 8) | Pass |
| "Power BI Services" plural | **3** | S7 H2 (198); S11 H2 (321); S15 body (403) | 2-3 | Pass. No section contains both forms. The S1 eyebrow (line 20) holds the plural but is excluded (Flag 8 below). |
| "Power BI consulting company" | **2** | S4 lede (71); S11 intro (323) | 1-2 | Pass |
| "Power BI solutions expert" | **2** | S10 Extend (302); S13 body (359) | 1-2 | Pass |
| "Certified Power BI Partner in UAE" | **0** | not placed | 0 (Section 13) | Pass |

- **Meta title and description (lines 1-2):** identical to brief Section 7. The primary keyword leads both.
- **First 100 words:** the primary keyword appears in the H1 and in lede sentence 1.
- **Stuffing caps:**
  - "Power BI" (any form) on the page: **46** by my count. Build says "about 50". The cap is 75, and the flag threshold is 85.
  - "UAE" on the page: **10**, against a cap of 12. The hits are H1 (22), deployment line x2 (41), S2 item 3 (55), S4 card 4 "UAE-based" (83), S6 card 2 L3 anchor (164), S11 H2 (321), tile 1 (325), FAQ H2 (367) and Q6 (384).
- **Titles containing "Power BI":** S7 items 0 of 6 (max 2). S9 steps 0 of 5 (max 1).

## 2. Word count: PASS

My count uses the brief Section 1 rule:
- **Included:** tab names and the "Limited offer" badge.
- **Excluded:** the S5 "Capability", "Key capabilities" and "Platform layer" labels, eyebrows, buttons, and draft structure headers.

| Section | My count | Build | Budget (12.4) | Status |
|---|---|---|---|---|
| S1 | 189 | 189 | 150-190 | OK |
| S2 + S2b | 80 | 80 | 45-70 | Over; accepted (see Flag 5 evaluation) |
| S4 | 271 | 272 | 260-310 | OK |
| S5 | 393 | 394 | 380-440 | OK |
| S6 | 385 | 385 | 340-410 | OK |
| S7 | 410 | 410 | 380-440 | OK |
| S8 | 26 | 27 | 20-30 | OK |
| S9 | 153 | 154 | 150-190 | OK |
| S10 | 402 | 398 | 360-420 | OK |
| S11 | 151 | 151 | 150-190 | OK |
| S12 | 36 | 36 | 30-45 | OK |
| S13 | 29 | 28 | 20-30 | OK |
| S14 | 915 | 914 | 780-920 | OK (5 below cap) |
| S15 | 27 | 27 | 20-30 | OK |
| **Total** | **3,467** | ~3,465 | 3,100-3,500 (fail <2,900 or >3,750) | **PASS** |

- **Sub-units**, all in range:
  - Hero lede 58.
  - S4 lede 62. S4 card 3 body 50 (45-55).
  - S5 intro 55. S5 descriptions 44 / 39 / 43 / 43 (35-45). Platform body 56.
  - S6 intro 35. S6 backs 45 / 40 / 44 / 45 / 42 / 39. S6 taglines 7 / 10 / 8 / 8 / 8 / 6.
  - S7 item bodies 58 / 57 / 55 / 58 / 57 / 57 (55-65).
  - S9 intro 40. S9 steps 21 / 16 / 16 / 17 / 22.
  - S10 intro 30. PowerUP! card 124. Tab items 12-15.
  - S11 intro 24. S11 tiles 15 / 17 / 17 / 17 / 16 / 17.
  - FAQ answers 75 / 82 / 77 / 79 / 71 / 89 / 85 / 83 / 77 / 77 (65-90).
- If the S5 structural labels are counted, the total is 3,483, which still passes.
- **Headroom:** S14 has 5 words and the total has about 33. The fixes below net +2 words.

## 3. Zero em dashes: PASS

Whole-file ripgrep: `—` **0**, `–` **0**, `--` **0**.

## 4. Grammar, spelling, punctuation: FAIL

| # | Location | Text | Problem | Fix |
|---|---|---|---|---|
| **4a** | S4 lede, sentence 3 (line 71) | "Power BI gives us the platform; our accountants and engineers make the numbers reconcile. **It** anchors our [digital transformation and analytics services](...)" | Unclear antecedent. Grammatically, "It" points to "Power BI" or "the platform" (the subject of the previous sentence), but the intended referent is HLB HAMT's Power BI practice. That reading also makes Microsoft's product "anchor" HLB HAMT's services, which cuts against 12.3. The same class of error failed as G5/G6 in loop 2. | See Fix 4a. |
| **4b** | S11 tile 3 body (line 332) | "Begin with a working dashboard on your data or fixed-price PowerUP!, then scale once it proves itself." | A missing determiner creates a mis-parse. "on your data or fixed-price PowerUP!" reads as a dashboard built *on* PowerUP!, because "or" coordinates the two objects of "on". The brief's own wording has the article: "or the fixed-price PowerUP!". | See Fix 4b. |
| **4c** | S6 card 3 tagline (line 169) | "Units, brokers and collections tracked from EOI **onward**" | The adverb form "onward" is chiefly US. British usage (the page standard) is "onwards". A file-wide `-ize`/`-yze`/US-spelling sweep is otherwise clean: the only "visualization" hits are inside URLs, and the anchor text reads "visualisation". | See Fix 4c. |

**Checked and clean:**
- Every new or changed sentence was read: S1, S2, S4 cards, S5 rows, S6 backs, S7 01-06, S9 intro and steps, S10 story, tabs and Support, S11, S12, S13 and A1-A10.
- Subject-verb agreement: "Contextual documentation..., plus ongoing support, keeps" and "CRM and ERP data land" (plural data, consistent) are both correct.
- Parallelism: A7's three "once..." clauses and S6 card 4's "help put / activate / shape" are both parallel.
- Semicolons: correct in A6, A8, A9 and S1.

**Style advisories (not scored):**
- The serial comma in the S10 Implement tagline, "one department, several, or the whole group" (line 289), is still the only one on the page (carried from the v3 advisory).
- "on the step-two models" (S9 step 4, line 246) is slightly stiff. Optional: "on the models from step two" (+1).
- A10 (line 397): "HLB HAMT confirms the timeline after discovery, once **we** know..." shifts person inside one sentence. It is acceptable and keeps B4 at 12.

## 5. Originality: FAIL

**Standard (unchanged from loops 1-3):**
- Brief-mandated facts, lists and structural labels are not violations.
- A sentence that keeps a source's or SugarAI's unit sequence or verb frame, with synonyms swapped in, is a violation.
- Brief-prescribed echoes are listed for the Content Writer, not scored against Build.

### 5a. Failure

**5s. S11 tile 1 body (line 326).** "We supply your licences, then deliver the engineering, training and aftercare in-house, never through subcontractors."
- **SugarAI tile 1, same grid, same slot, under the same "[X] partner in the UAE" title pattern:** "Implementation, consulting, migration and support delivered locally."
- **Why it fails:** both keep the frame [service list ending in support/aftercare] + deliver(ed) + [locally/in-house].
- **Why this is a regression:** this exact frame failed as **R1 in test-report-v3** ("Consulting, build and support handled in-country"). v4 fixed it with "Our own staff handle everything from data engineering to aftercare; nothing is subcontracted." The v5 rewrite, done to add the reselling fact, brought the SugarAI frame back.

### 5b. Checked and clean

**Against SugarAI (every new or changed sentence):**
- **S1 sub-block** ("We define each measure once, so gross margin reads the same..."): the v3 R5 "[teams] working from the same..." frame is gone.
- **S10 intro:** there is no "choose one or combine them".
- **S11 intro:** the brief's SugarAI-like "any partner can install..." frame was avoided.
- **S12 H2:** brief-prescribed.
- **S13 H2** "Map Out Your Reporting Roadmap, Free of Charge": no longer mirrors "Plan your SugarAI rollout with our consultants". The body is covered in 5d.
- **S11 tile 6:** Build moved away from the brief's near-verbatim SugarAI "Consultants who scope, build and support from the UAE".

**Against v4, where content substantively changed:**
- S2, S2b, the S4 lede and card 3, S5 rows 1-4 and the platform block, the S6 intro, S7 01-06, the S9 intro, the S10 featured H3 and Support tab, S11 tiles 1 and 5, the S12 H2, A2, A6 (opening) and A9 (new) are all newly written.
- A3, A5, A7 and the S12 body are close rewordings of v4, but brief 12.5 marks that content as "unchanged", so reusing approved v4 wording there is acceptable.

**Against competitors:**
- The Zenzero support catalogue ("data refresh failures", "slow-loading dashboards", "connectivity issues") shares topic terms with the S10 Support item (line 307), but not wording.
- No other competitor overlap was found.

**Web check:** these distinctive phrases have no exact or near match online:
- "The tool is rarely the problem" (only generic "slow dashboard" articles come back)
- "gross margin reads the same on the executive dashboard"
- "migrate Tableau and Qlik environments to Power BI"

### 5c. Advisories (not scored)

- **S4 card 1 (line 74):** "Discovery, data preparation, modelling and DAX, and report design all sit with us." This loosely mirrors SugarAI's "What we do" card: "Process discovery, platform design, ... everything delivered by one team". It shares the list-then-ownership closer in the same card slot. The brief mandates "end-to-end ownership" here, so it is advisory. Optional: "Discovery comes first, then data preparation, modelling and DAX, and report design." (-1)
- **S11 tile 4 (line 335):** "Booked revenue in Power BI, open-deal scoring in SugarAI CRM, both configured and maintained by our team." This verbless [X in A, Y in B, from one provider] shape sits nearer SugarAI's "SugarAI prediction plus Power BI analytics, from one partner" than v4's two-clause version, which passed. It is acceptable. Optional: "Power BI reports booked revenue while SugarAI CRM scores open deals, and our team configures both." (16)

### 5d. Brief-level echoes (Build followed the brief; flagged for Content Writer awareness)

1. **S7 intro (line 200).** It follows Section 4's prescription ("end-to-end delivery from first workshop to ongoing support"). That prescription itself mirrors both:
   - SugarAI's Offerings intro: "end-to-end SugarAI CRM solutions, from initial consulting... to... ongoing support"
   - the live consulting page (lines 415-417)

   Optional: "Our team carries a Power BI programme from its first strategy workshop to support after launch; most clients need several of the services below." (24, -1)
2. **S7 item 01 sentence 1 (line 203) and item 05 sentence 1 (line 215).** Both keep the unit order of the dashboard page's step 01 and the data-viz page's Tableau migration text, because brief 12.5 prescribes those units in that order. Both pages stay live and are linked (L6, L7).
3. **A9 (line 394).** "how the report was built almost always is" overstates the source's "depends more on implementation quality than the tool itself". Optional: "...the way the report was built usually is." (0)
4. **S13 body (line 359).** "a Power BI solutions expert will scope sources, licences and phasing with you" is the brief's wording. It keeps SugarAI CTA 2's "We scope the packages, phasing and integrations around your team" frame (scope + 3-item list with "phasing"). v4's "map it to sources, licences and phases" was further away. Optional: "Tell us what you report on, and a Power BI solutions expert will map it to sources, licences and a phased plan." (22, +1; S13 = 30)

## 6. Stat accuracy: PASS

Each figure appears exactly once on the page, in its assigned slot (ripgrep across the whole file):

| Ref | Wording | Slot (line) | Check |
|---|---|---|---|
| [1] 200+ | "Power BI connectors; we configure yours and build missing ones." | S2 item 1 (46-47) | Attributed to Power BI's library (B7). Microsoft Learn source. Consistent with the ~210-220 count. |
| [2] 33x | "Faster report load times in one recent HLB HAMT engagement." | S2 item 2 (50-51) | The mandatory qualifier is present. The **footnote is upgraded to the live page, as 12.7 requires**, and quotes it verbatim: "In a recent engagement, we achieved a 33x improvement in report load times and interactivity" matches data-viz lines 501-502 exactly. It is self-published with no client or date, which the Content Writer has approved (Section 10 #4). |
| [12] Since 1999 | "Since 1999 / A licensed UAE audit, tax and advisory firm..." | S2 item 3 (54-55) | Web-verified today (HAMT & Associates 1999; HLB International 2007). There is no dated "25 years". |
| [3] Gartner | "Microsoft was named a Leader in the 2026 Gartner® Magic Quadrant™ for Analytics and BI Platforms for the 19th consecutive year." | S2b (61) | Wording is unchanged from the version re-confirmed in loop 3. There is no "#1", "ranked" or "14+". The disclaimer is in Sources item 3. |
| [4] Fabric | "more than 40,000 paid Fabric customers, up more than 60% year on year" | S5 platform (140) | FY26 Q4 earnings call, 29 July 2026. Attributed to Microsoft. |
| [6] 7 days | H2 "...in 7 Days" + intro "for a defined use case" | S9 (232, 234) | The qualifier matches the dashboard page, line 745-746 ("as little as 7 days for defined use cases"). The meta "7-day" is brief-allowed. |
| F1-F5 [7]-[11] | Desktop vs service; US$14 / US$24 "At the time of writing... unchanged since 1 April 2025"; UAE North full Fabric / UAE Central Power BI-only; Copilot F2+/P1+, admin enablement, English-only prompts, off by default outside the US/EU boundary; ISO/IEC 27001 and SOC 2 "within the scope of" | A1, S5 row 2, A2, S1, A6, A8 | Prices re-checked by web search today: Pro $14 and PPU $24 are still current. The "in scope of" framing is kept; the sibling pages' "compliant" is not used. |
| CS facts | $4,500, 5 terms, 6 deliverables; FAQ 10 timelines; HLB International since 2007 | S10 (264-278); A10 (397); S11 tile 5 (338) | All match partner page lines 537-569 and 783-786, and the 12.7 CS5 facts. |

- **73.3% does not appear** on the page. It is retired with the reason given in 12.2.
- No FAQ restates 200+, 33x, 1999, 19th, 40,000, 7 days or $4,500.
- **No fabricated or unsourced stats.** None of these appear: the consulting page's 90% / 1.6x / 60% theme-demo figures, "~$15", "14+ Yrs Gartner #1", "3,000+ clients" or competitor claims.
- **Duplicate-stat sweep of the other project folders:**
  - The only hit is the SugarAI healthcare subpage brief (line 82), which plans a "Local since 1999" tile.
  - That is a company-history fact, not a market stat, and brief 12.7 added it deliberately, so it is not a violation. Noted for Content Writer awareness.
  - 33x, 40,000 and the 19th year appear in no other project page.
- **Bookkeeping advisory for Deliver:**
  - The Stats used row for "HLB International member since 2007" lists Ref "(none)", but S11 tile 5 (line 338) carries [12]. So [12] appears twice on the page. This is fine, because it is the same source for two different facts, but the table should read [12].

## 7. Human tone / AI-detection heuristics: FAIL

**Stock AI phrases:** none. The sweep covered unlock, seamless, leverage, empower, robust, harness, journey, elevate, streamline, holistic, tailored, actionable, "in today's", "not just" and "in conclusion". It returned only "digital transformation" (a service name), "transform your extracts" (a PoC step verb), "Data transformation scripts" (a deliverable) and "unlock" inside the L4 URL.

### Failure

**7f. Six identical openers in S6 (lines 158-188).** Every flip-card back opens "We + verb":
- card 1 "We roll every entity..."
- card 2 "We track taxable income..."
- card 3 "We report on expressions of interest..."
- card 4 "We help put governance frameworks..."
- card 5 "We join CRM, e-commerce..."
- card 6 "We align business objectives..."

The cards are read in sequence as a grid, so six identical [We][verb][list] openings read as templated.

The pattern also runs into the surrounding sections:
- S5: 4 of 5 descriptions open "We" (brief-mandated by 12.3c, so not scored).
- S7: 4 of 6 items open "We".

B2 requires the HLB-led first sentence only for **section intros**, and 12.3b asks for HLB HAMT to own the verbs, not for every card to start with "We". Varying three of the six openers keeps HLB HAMT as the actor in every card. See Fix 7.

### Advisories (not scored)

- **"the same" x8 on the page**, with 3 in S6: the intro "The same KPI-first thinking" (153), card 2 "in the same firm" (164) and card 5 "on the same revenue measures" (182). Fix 7's card 5 text removes one.
- **"tied to" x2 in S6:** card 4 back "a roadmap tied to strategy" (176) and card 6 tagline "Analytics strategy tied to commercial return" (187). Optional card 6 tagline: "Analytics strategy measured by commercial return" (0).
- **The RTL claim appears twice in the same frame:**
  - S2 item 4 (59): "planned from the first mockup, not retrofitted"
  - A5 (382): "We design right-to-left from the first wireframe rather than mirroring a finished English report."

  The brief places the claim in both. Optional A5 sentence 2: "We plan right-to-left layouts at wireframe stage rather than mirroring a finished English report." (15, +1; A5 = 72)
- **"Extra" opens two S10 lines:** the Extend tagline (298) and the Support item "New dashboards" (311). Optional Support body: "More pages, measures and reports as the business starts asking different questions." (0)
- **S5 intro sentence 3,** "Below is what we build on each part of the platform." (91), is a signpost. It is acceptable because removing it would drop the intro under 45.

## 8. Section structure, links and schema: PASS

- **Order:** S0 through S16 are present in the 12.2 / 12.4 order. There is one H1.
- **S1:** lede, sub-block, 3 H3 cards (Leadership / Analysts / Teams on the move, iOS and Android only) and the deployment line in the 12.3c wording.
- **S2:** 4 strip items with no heading tags, plus the S2b bar and button.
- **S3:** 7 nav items.
- **S4:** H2 plus 4 H3 cards.
- **S5:** the eyebrow reads "THE PLATFORM WE DELIVER". The H2 is HLB-led. There are 4 rows, each with the brief's 5 bullets; the row 3 bullet is renamed (see Flag 1). The platform block has 4 bullets.
- **S6:** H2, intro with L7, 6 flip cards (front H3 plus tagline, back plus button), and 12 pills including Manufacturing and Wholesale Distribution.
- **S7:** H2 "HLB HAMT's Power BI Services" and items 01-06.
- **S8:** CTA.
- **S9:** highlighted band, the 7-day H2 and 5 H3 steps.
- **S10:** the featured PowerUP! card with badge, price, story, all 5 terms and all 6 deliverables, then 4 tabs. The Support tab has 5 items, including the Security and access reviews item (N8).
- **S11:** 6 tiles.
- **S12:** static asset and the "Inside an HLB HAMT Power BI Dashboard" H2.
- **S13:** CTA 2.
- **S14:** 10 H3 questions in the 12.5 order, including the new Q9.
- **S15:** "Technology Consulting" is the form default.
- **S16:** footer.

**Links (all exact):**

| Link | Anchor | Target | Location |
|---|---|---|---|
| L1 | digital transformation and analytics services | /services/digital-transformation-uae/ | S4 lede (71) |
| L2 | SugarAI CRM | /sugarai-crm-2/ | S11 tile 4 (335) |
| L3 | UAE Corporate Tax advisory | /services/corporate-tax-advisory-services-in-uae/ | S6 card 2 (164) |
| L4 | Power BI automation with Power Automate | /insights/unlocking-power-bi-automation-with-power-automate/ | FAQ 4, on the alert sentence (379) |
| L5 | data protection advisory | /services/data-privacy-and-security-uae/ | FAQ 6 (385) |
| **L6** | Power BI dashboard development | /services/power-bi-dashboard-development/ | S7 item 03 (209) |
| **L7** | data visualisation services | /services/data-visualization-uae/ | S6 intro (153) |
| P2 | advanced analytics services | PLACEHOLDER:/services/advanced-analytics-services/ | S6 card 6 (188) |

- **In-page links:** "proof of concept" and "above" → #methodology. "PowerUP!" → #packages.
- **Excluded pages:** `/power-bi-partner-in-dubai-uae/` and `/microsoft-power-bi-consulting-in-dubai-uae/` are linked **nowhere on the page**. Ripgrep finds them only in Stats used and Flags.
- **Schema (Flag 15):** Service, FAQPage with **10** Q&As matching on-page text, and BreadcrumbList.

## 9. Client requirements and accuracy corrections: PASS

**Revision 2 notes:**
- AI Insights is removed.
- The page is HLB HAMT-led throughout, including section framing, hero and intros, not just one section.
- The sibling pages are folded in (N1-N11).
- Stats are re-verified. The one retired stat has a stated reason.

**Section 13:**
1. Partner-page reuse is in original sentences.
2. Reselling-partner framing is used, with no "certified" wording and the keyword not placed.
3. The offer is renamed.
4. There is no case-study block.

**Section 10 #7 corrections, checked by ripgrep:**
- There is no "Gartner #1", "ranked" or "14+" on the page.
- There is no Arabic Copilot claim. A8 reads "we put Arabic into report design rather than into questions".
- "Windows" appears only in A1, where it correctly describes Desktop. Mobile is iOS and Android.
- There is no "Q&A" feature.
- Tableau and Qlik appear only as migration sources, with no price comparison.
- There is no "Salesforce (60+ modules)".
- The connector caveat is kept in S5 row 3.

**Also checked:**
- There is no Hebrew (12.5 FAQ 5).
- There is no "zero business logic loss".
- There is no "compliant" wording.
- There is no "~$15".
- The theme-demo content is excluded.

**Advisory, A3 connector caveat (line 376):** the listed systems, including Tally and SugarCRM, are said to be reached "through standard and partner-built connectors", with custom builds reserved for "legacy systems nothing else covers".
- This is defensible: partner-built and generic ODBC routes exist.
- The safer reading of the Section 4 caveat puts custom connectors in the same list. Optional: "...through standard, partner-built and custom connectors, including custom builds for legacy systems." (0 net if "and write custom connectors for legacy systems nothing else covers" is replaced.)

---

## Evaluation of Build's 8 flagged deviations

| # | Deviation (draft Flags item) | Verdict | Reasoning |
|---|---|---|---|
| 1 | "certified" → "partner-built" for connectors. S5 row 3 reads "native, partner-built and custom connectors"; the bullet reads "Native and partner connectors" (item 3) | **Accept** | Section 13 point 2 bans "certified" anywhere on the page, and it is later and more specific than the 12.5 S5 row 3 wording. Microsoft's certified connectors are built by partners, so the meaning holds. The bullet is 4 words, inside the 2-6 range. |
| 2 | FAQ 6 now reads "ISO/IEC 27001 and SOC 2 audits" instead of "...certification and SOC 2 reports" (item 3) | **Accept** | It is accurate: both are third-party audit outcomes, and the Power BI service is in scope of both. It keeps the "in scope of" framing and avoids "compliant". It also avoids putting "certification" beside "Microsoft", which is exactly the proximity Section 13 asks Test to check. The Content Writer may restore the brief wording (+1 word, A6 = 90), because Microsoft's ISO certification is not a partner claim. |
| 3 | Footnote [6] cites the dashboard-development page instead of the partner page (item 5) | **Accept** | Section 13 point 1 confirms that the partner page will redirect to this page, so citing it would be self-referential. 12.9 also bars linking it, and the sources note renders links. The dashboard page is live, linked (L6), and is the exact origin of the "defined use cases" qualifier the brief adopted (N2). The quote matches source lines 745-746. |
| 4 | Copilot left out of FAQ 2 (item 7) | **Accept** | This is a genuine brief-internal conflict. 12.5 FAQ 2 mentions Copilot, but 12.2 ("Appears only in FAQ 6 and FAQ 8") and 12.5 FAQ 8 ("This and FAQ 6 are now the only Copilot mentions") are explicit single-location rules, and they reflect the Content Writer's AI de-emphasis. The capacity requirement is covered fully in A8. |
| 5 | The S2 strip is 80 words, over the 45-70 budget (item 8) | **Accept** | The 12.4 budget cannot hold 12.5's mandated content. The stat lines are 7 words. The descriptions have a floor of 8 + 10 (33x, fixed wording) + 14 (the prescribed Since 1999 line) + 9 (Arabic, unchanged) = 41. S2b has a floor of 25. That gives a minimum of **73**. The brief's own example wording totals about 87. Build's 80 is compact, and the page total is well inside range. |
| 6 | FAQ 3 question reworded (item 9) | **Accept** | The brief's "Which of **your** systems can **we** connect..., and do **we** need..." switches speaker mid-question. Build's "Which of our systems can you connect to Power BI, and do we need a warehouse first?" keeps the reader's voice, matches Q4 and Q5, and meets 12.5's intent ("reader and HLB HAMT are the actors"). |
| 7 | S13 heading changed from the brief's suggestion (item 10) | **Accept** | The brief's "Plan Your Power BI Roadmap With Our Consultants" is near-verbatim SugarAI ("Plan your SugarAI rollout with our consultants"). The new H2 is clean. **However, the S13 body still uses the brief's SugarAI-like "scope... phasing... with you" wording.** See 5d-4, which is advisory only. |
| 8 | The S1 eyebrow contains the plural keyword (item 4 note) | **Accept** | The eyebrow text "HLB HAMT POWER BI SERVICES" is prescribed verbatim by 12.3c and 12.5. Eyebrows are excluded from counts under Section 2a. Section 2b's no-mixing rule covers paragraphs, cards and heading/lede pairs, not eyebrows. No change is needed. |

Build's other flags were also checked and accepted:
- Item 6, no timeline footnote: the footnote is optional, and the same redirect problem applies.
- Item 12, v4 problem phrases: verified absent ("before any", "side by side", ", giving", "which is what", "build and support", "delivered locally", "in one view", "one partner", "one team", "draw on" all return 0 on the page).
- Item 13, links: verified.

The only inaccuracy is in item 11: its reuse disclosure omits the S7 intro's consulting-page frame (see D).

---

## Overall: FAIL (loop 1 of 3, Revision 2)

Items 4, 5 and 7 fail. Items 1, 2, 3, 6, 8 and 9 pass. All five fixes are drop-in sentence edits. Change nothing else: keywords, stats, footnotes, links, section order and every other sentence passed.

## Fix instructions (for Build)

**Fix 4a: S4 lede, sentence 3 (line 71).**
- Replace "It anchors our [digital transformation and analytics services](https://hlbhamt.com/services/digital-transformation-uae/), where we build..." with "**That combination** anchors our [digital transformation and analytics services](https://hlbhamt.com/services/digital-transformation-uae/), where we build self-service BI ecosystems on figures your finance team has already approved."
- "That combination" refers back to the platform plus the accountants and engineers.
- Word count: +1. The lede becomes 63 (55-70) and S4 becomes 272. The L1 anchor is unchanged.

**Fix 4b: S11 tile 3 body (line 332).**
- Replace with "Begin with the fixed-price PowerUP! or a working dashboard on your data, then scale once it proves itself."
- Word count: 18 (+1). The tile stays inside 10-18 and S11 becomes 152.
- There is still no "7 days" and no "$4,500".

**Fix 4c: S6 card 3 front tagline (line 169).**
- Change "onward" to "**onwards**" (0 words).

**Fix 5: S11 tile 1 body (line 326).**
- Remove the [service list] + deliver + [in-house] frame that echoes SugarAI's "Implementation, consulting, migration and support delivered locally." (the v3 R1 failure).
- Use: "We supply your licences, and our own staff handle everything from data engineering to aftercare."
- Word count: 15 (0). S11 is unchanged.
- This keeps the reselling fact (Section 13 point 2) and the in-house claim (source FAQ 18). It reuses the in-house clause Test accepted in v4, where that content has not changed.
- If you write your own wording, it must not pair a service list with "delivered/deliver... in-house/locally/in-country".

**Fix 7: S6 flip-card backs 1, 3 and 5 (lines 158, 170, 182).**
- Vary the openers so the six backs no longer all start "We + verb". Keep HLB HAMT as the actor in each card. Cards 2, 4 and 6 stay as they are.
- **Card 1 back (45 → 45):** "Group P&L, balance sheet and cash flow roll up from every entity, across AED, USD, SAR, EUR and more, with budget variance and forecasts next to actuals. Our chartered accountants design intercompany eliminations, FX conversion and IFRS segment views so they stand up to audit."
- **Card 3 back (44 → 44):** "Dashboards cover expressions of interest, deal pipeline, lead conversion, unit availability, payment plans, broker performance and DLD compliance. We land CRM and ERP data in a lakehouse first and match them unit by unit, so a sold unit counts once, whichever team reports it."
- **Card 5 back (42 → 42):** "CRM, e-commerce and campaign data meet in a 360-degree customer view, from which we report omnichannel performance, cohort buying behaviour and segment response. Media teams compare DSPs, SSPs and ad channels on shared revenue measures, which sharpens targeting for the next campaign."
- Card 5 also drops one of the three "the same" instances in S6.
- S6 stays at 385. The backs stay inside 35-45.

**After all fixes:**
- **Totals:** S4 272, S11 152, S6 385, and the page about **3,469**, inside 3,100-3,500.
- **Unchanged counts:** keywords (6 / 3 / 2 / 2 / 0), "HLB HAMT" 12, "Microsoft" 7, "UAE" 10, links, stats and footnotes.
- **Banned phrases:** no fix text uses "certified", "delivered locally", "one partner/team", "side by side", "before any" or "in one view".
- **Optional:** the advisories in 4, 5c, 5d, 6, 7 and 9 are optional. Build may apply any of them, but none is required to pass.

---

Sources consulted for verification:
- [HLB HAMT Celebrates 25 Years of Unwavering Excellence (press release)](https://hlbhamt.com/press-room/hlb-hamt-celebrates-25-years-of-unwavering-excellence/) and [25 Years of Excellence](https://hlbhamt.com/25-years-of-excellence/), for 1999 and 2007
- [Microsoft Power BI pricing](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing) and [Important update to Microsoft Power BI pricing](https://powerbi.microsoft.com/en-us/blog/important-update-to-microsoft-power-bi-pricing/), for Pro $14 and PPU $24, current in 2026
- Web originality searches (no matches): "The tool is rarely the problem" Power BI; "gross margin reads the same on the executive dashboard"; "migrate Tableau and Qlik environments to Power BI"
