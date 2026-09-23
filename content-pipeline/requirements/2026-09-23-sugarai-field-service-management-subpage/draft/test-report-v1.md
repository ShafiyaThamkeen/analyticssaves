# Test report v1: SugarAI for Field Service Management (industry subpage)

- Draft tested: `draft/draft-v1.md`
- Checked against: `brief.md` (Sections 1-10, with Section 10 overriding earlier sections), `inputs/requirement-notes.md`, `inputs/template-source/hlbhamt-sugarai-insurance.html`, the 5 reference sites, and the wider web
- Loop: **1 of 3** (no earlier test report exists)
- Tester: Test agent, 2026-09-23

**Tooling limitation (same as the Plan run).** WebFetch was egress-blocked for grandviewresearch.com, mordorintelligence.com, datareportal.com and globenewswire.com. I checked stats and originality through WebSearch result text, which quotes the source pages. Click-verification before publication is still required (brief Section 10.5).

| # | Check | Result |
|---|---|---|
| 1 | Keyword placement and density | PASS |
| 2 | Word count | PASS |
| 3 | Zero em dashes | PASS |
| 4 | Grammar, spelling, punctuation | PASS (minor optional notes) |
| 5 | Originality | **FAIL** |
| 6 | Stat accuracy | **FAIL** |
| 7 | Human tone / AI-detection heuristics | **FAIL** (minor) |
| 8 | Section structure | PASS |
| 9 | Brief and requirement accuracy (no transcript) | **FAIL** |

---

## 1. Keyword placement and density: PASS

Counting rule from brief Section 2: exact phrase, case-insensitive, on-page copy only, meta excluded. I counted independently with a regex over the draft and then removed the matches that fall in the meta lines, the draft title line and the Flags notes.

| Keyword | Target | Actual | Location(s) in draft |
|---|---|---|---|
| SugarAI for Field Service Management (primary) | 3-4 | **4** | H1; hero lede sentence 1; Block 3 lede; Block 4 lede |
| field service CRM software | 2 | 2 | Block 2 lede; FAQ A1 |
| field service automation | 1-2 | 1 | Block 6 H2 |
| field service management in the UAE | 1-2 | 1 | Block 10 lede ("Field service management in the UAE means...") |
| technician scheduling software | 1 | 1 | Benefits tile 5 |
| work order management software | 1 | 1 | Services 05 |
| mobile field service management | 1 | 1 | Services 08 H4 |
| field service asset management | 1 | 1 | Benefits tile 6 |
| SugarAI field service CRM | 1 | 1 | Services 01 |
| SugarAI CRM for field service | 1 | 1 | Process H2 |
| SugarCRM field service management | 1 | 1 | FAQ 7 question |
| **Total** | 14-17 | **15** | |

- **The Build agent's figures check out:** 15 instances in total, 4 of them primary.
- **Density:** 15 / 1,643 = 0.91% across all keywords; the primary alone is 4 / 1,643 = 0.24%. Neither is stuffed or under-used.
- **Meta title** (`SugarAI for Field Service Management in the UAE | HLB HAMT`, 58 characters) and **meta description** (157 characters) both start with the primary keyword and match brief Section 7 exactly.
- **H1** is exactly the primary keyword. The primary keyword also appears in the first 100 words (hero lede, sentence 1).
- **Keyworded headings** are only the H1, the Services H2, the Services 08 H4, the Process H2 and the FAQ 7 question, as Section 2c requires. No other H2, H3 or H4 contains an exact-match keyword. The primary keyword is in no H2.
- No sentence contains two different exact-match keywords.
- None of the 12 deliberately excluded phrases appears anywhere (regex check returned zero matches, including "SugarAI Field Service Management" without "for").
- The implicit phrases are present: "SugarAI for Field Service" (inside the primary), "CRM for field service" (Process H2) and "SugarCRM field service" (FAQ 7).
- **Note:** two of the keyword placements read forced (Benefits tiles 5 and 6). They are scored under item 7, not here, because the counts and positions are correct.

## 2. Word count: PASS

I counted every block by hand using the brief Section 1 rule (headings, ledes, body, card and tile text, stat labels and descriptions, FAQs, CTA headings and body, "What happens next" rows; nav, breadcrumb, eyebrows, button labels, footer, meta and sources excluded).

| Block | Actual | Brief budget | |
|---|---|---|---|
| 1 Hero + side panel | 128 | 130-145 | 2 under |
| 2 Stats band | 101 (104 with figures) | 105-120 | under |
| 3 Platform | 119 (127 with `.tag` labels) | 115-130 | OK |
| 4 Benefits | 187 | 180-200 | OK |
| 5 CTA band 1 | 21 | 22-28 | 1 under |
| 6 Services | 183 | 170-185 | OK |
| 7 Proof band | 84 (88 with figures) | 55-65 | over (Section 10 tiles 3-4 add label + description) |
| 8 CTA band 2 | 13 | 12-16 | OK |
| 9 Segments | 112 | 110-125 | OK |
| 10 UAE/GCC | 143 | 125-140 | 3 over |
| 11 Process | 143 | 130-145 | OK |
| 12 Why HLB HAMT | 90 | 85-95 | OK |
| 13 FAQs | 268 | 270-300 | 2 under |
| 14 Closing CTA | 51 | 50-60 | OK |
| **Total** | **1,643** (1,658 with tags and figures) | 1,500-1,700 (aim about 1,600, write-to ceiling 1,680) | **In range** |

- **The Build agent's figures check out:** 1,643 words, or 1,658 with the 8 tag words and 7 figures, matching the draft's self-report exactly.
- **The Build agent's claim about the budgets is correct.** Adding up the brief's own sub-ranges gives more than the block ceiling in Blocks 1, 3, 4, 6, 10 and 11. For example, Block 1's H1, lede, H3, sub-line, labels and rows add up to 144-174 words against a 145 ceiling. The small per-block misses above follow from that and do not fail the item.
- **The Build agent under-reported its per-item shortfalls.** These are also below the brief's per-item minimums but are missing from Flag 1:
  - Side rows: 11 / 13 / 9 words (brief 15-20)
  - Hero lede: 46 (brief 50-60)
  - Block 3 lede: 28 (brief 30-35)
  - Benefits tiles 1-4: 17-21 (brief 22-28)
  - Services bodies: 13-17 (brief 16-20)
  - Process lede: 18 (brief 20-25)
  - Process callout body: 24 (brief 35-45)
  - Why cards 2-4: 15-16 (brief 18-22)
  - Closing row 3: 10 (brief 12-15)

  These are informational only. The page total, which is the binding target, passes.

## 3. Zero em dashes: PASS

I searched the whole draft file for `—` (em dash), `--` and `–` (en dash). **0 matches for all three.**

## 4. Grammar, spelling, punctuation: PASS (minor optional notes)

- **British spelling is consistent.** I searched for -ize/-yze, color, center, labor, program, behavior, license, catalog, defense and similar US forms: 0 matches. British forms in use include organisations, catalogue and defence.
- No outright errors found. Four optional polish points:
  1. **Platform card 3** has a serial comma ("renewal nurture, and campaigns targeted by equipment type or age") in a list that doesn't need it. The rest of the page drops the comma in simple lists, e.g. "customer, site, equipment and contract". Suggested fix: "Reminders for visits falling due, renewal nurture and campaigns targeted by equipment type or age." The commas in the Block 10 lede and Benefits tile 6 are needed for clarity, so keep those.
  2. **Proof tile 3:** "FSM" appears only here and is never spelled out. Suggested fix: "Scheduling and dispatch leads field service software investment." The acronym is not needed.
  3. **Stat 3 `.d`:** "Share of UAE facility management delivered by outsourced providers in 2025" leaves out the noun. Suggested fix: "Share of the UAE facility management market delivered by outsourced providers in 2025." This adds 2 words.
  4. **Process callout:** "follow next" is redundant. Suggested fix: "...and ERP integration come in the next phase."

## 5. Originality: FAIL

**Reference sites and the wider web: no matches.** I ran exact-phrase web searches on distinctive draft lines and got no matches:
- "one record of customer, site, equipment and contract"
- "Designed around the job, the technician and the asset"
- "Planned maintenance that stays on the calendar"
- "screens technicians use each morning"
- "counts down to the contract's response and resolution times"
- "Rules assign jobs by skill, zone, priority and SLA"
- "Job sheets adapt to the job type and asset"

I also compared the draft against search-quoted copy from all 5 reference sites (Ambit, KINAMU, MSI Data, Tokara, and the SugarCRM + Mobileforce release). The only overlap is shared industry vocabulary (SLA escalation, skills-based assignment, parts, first-time fix), which is allowed.

**Insurance template: FAIL.** Brief Section 4 says: "No Insurance sentence may be reused or closely paraphrased." Nine sentences keep the template's sentence skeleton and swap in synonyms or field service nouns. Several follow the brief's outline, which itself echoed the template wording, but the rule still applies.

| # | Draft location | Insurance template | Draft |
|---|---|---|---|
| O1 | Why HLB HAMT, card 4 | "A dedicated team on agreed service levels, with a named manager and a clear escalation path." | "A dedicated support team works to agreed service levels, with a named manager owning escalation." |
| O2 | Why HLB HAMT, card 3 | "Consulting, implementation, integration and support under one engagement, with no subcontracting and no gaps." | "Advisory, build, ERP integration and support all sit with our technology consulting services team, never subcontracted." (the same four-item list with each item swapped for a synonym, plus "no subcontracting") |
| O3 | Why HLB HAMT, card 1 | "26 years across the UAE and GCC, with consultants who know how insurance is sold and serviced here." | "After 26 years in the UAE and GCC, we know how service contracts are tendered, priced and run here." |
| O4 | Process step 6 | "Phased go-live with hypercare, then managed support under SLA." | "Hypercare through each phased launch, then managed support under an agreed SLA." |
| O5 | Process step 4 | "Policyholder and claims data cleansed, mapped and rehearsed before load." | "Customers, sites, assets and contracts cleaned, mapped and trial-loaded before cutover." |
| O6 | Process step 1 | "We map how a quote becomes a policy, claim and renewal today." | "Workshops chart how requests currently move from first call to renewal." |
| O7 | Hero lede, sentence 2 | "HLB HAMT implements SugarAI for insurers, brokers and agencies across the UAE and GCC, cloud or on-premise." | "HLB HAMT deploys it for service businesses across the UAE and GCC, cloud or on-premise." |
| O8 | Closing CTA, row 1 | "A discovery call on your product lines, channels and current systems." | "A first call about your job types, contracts, crews and current systems." |
| O9 | Closing CTA, row 3 | "A written proposal covering scope, timeline and investment." | "A written proposal setting out scope, phasing, timeline and cost." |

**Borderline, not required to fix:**
- Services 01 ("configure ... around your request-to-invoice cycle, from a ready-made blueprint") echoes template 01 ("built around your quote-to-bind process ... blueprint").
- Services 07 ("..., with group reporting in Power BI") echoes the template's "..., with ... Power BI reporting".
- Process step 5 reuses "role-based training", which is a methodology term.
- The H3 "Regional delivery depth" and the H2s "Why service businesses choose HLB HAMT" and "See SugarAI running your own jobs..." share template patterns. They are structural labels that the approved brief prescribed word for word, so under the structural-label exception they do not count as violations.

## 6. Stat accuracy: FAIL

| Draft stat | Brief ID | Matches source? | Credible and recent? | Verdict |
|---|---|---|---|---|
| US$809.8M, MEA FSM 2025, 8.3% a year to 2033 | S1 | Yes. Grand View Research: "USD 809.8 million in 2025 ... CAGR of 8.3% from 2026 to 2033." | Research firm, 2025 data | OK |
| US$70.25B, GCC FM 2025; hard services led by MEP/HVAC hold the largest share | S2 | Yes. Mordor: USD 70.25B in 2025; "hard services led with 59.3% revenue share in 2024, dominated by MEP and HVAC maintenance." | Research firm, about 1 year old | OK |
| 64.88%, outsourced share of UAE FM, 2025 | S3 | Yes. Mordor: "Outsourced service delivery captured 64.88% of the UAE facility management market share in 2025." | Research firm, 2025 | OK |
| 86%, first-time fix at top performers | P1 | Yes. Aquant 2025 release: "Top companies boast a First Time Fix Rate (FTFR) of 86%, compared to just 53% for bottom performers." | Feb 2025, about 19 months old. Within the 2-3 year window, but see advisory A1. | OK |
| 39%, faster resolution for top performers using AI | P2 | Yes. "AI-powered solutions enable top-performing organizations to achieve a 39% faster Resolution Time." | Feb 2025 | OK |
| 28.16%, scheduling and dispatch share of 2025 global FSM revenue, the largest category | R1 | Figure, year and "largest" all match. Mordor: "by solution type, scheduling-dispatch and route-optimization led with 28.16% of 2025 revenue." | Research firm, 2025 | OK, see note on Build Flag 4 below |
| 100% of the UAE's 21.9 million mobile connections on 3G/4G/5G, "so technicians can stay connected on site" | R2 | **The figures match, but the conclusion drawn from them goes beyond what the source supports.** DataReportal: "21.9 million cellular mobile connections ... at the beginning of 2025" and "100% ... can now be considered 'broadband' ... However, devices that connect to 'broadband' mobile networks do not necessarily use cellular mobile data ... **this broadband figure should not be considered a proxy for mobile internet use**." The draft's clause "so technicians can stay connected on site" treats the figure as exactly that proxy, and it says nothing about signal at a given job site. | Early 2025, about 20 months old. A newer edition exists (advisory A2). | **FAIL** |

- **No invented stats.** No other figures appear in the copy.
- **No stat is misattributed.** No source is named on-page; the footnotes map [1]-[6] correctly.
- **No stat duplicates the Healthcare project.** I searched the whole repo for 809.8, 70.25, 64.88, 86%, 39%, 28.16 and 21.9 million; they appear only in this requirement's brief and draft.
- **Salesforce P3/P4 are gone.** Salesforce appears nowhere in the page copy. It appears only in the draft's internal notes, which the Deliver agent must strip.
- **"26 years"** is used once, in Why card 1, as Section 10.4 requires. "More than 25 years" appears nowhere.

**Answer to Build Flag 4 (tile 3):**
- **"Investment":** acceptable. The 28.16% is revenue by solution type, which is what buyers spent, so "investment" is a fair plain-English reading. "Spending" would be more literal, but the Content Writer prescribed this label.
- **Dropping "route optimisation":** narrows the category name but does not change the figure. Putting "route optimisation" on-page would risk implying a capability the page must not claim (Section 10.1), so keeping the Content Writer's label is the right call.
- **Required change:** Source 5 in the footnote list must name the full category (see Fix 6b), so the page cites its source accurately.

**Advisories for the Content Writer (not failures on their own, since both figures are inside the 2-3 year window):**
- **A1.** Aquant published a **2026** Field Service Benchmark on 19 Feb 2026 (https://www.globenewswire.com/news-release/2026/02/19/3241231/0/en/Aquant-s-2026-Field-Service-Benchmark-Companies-Can-Unlock-up-to-26-in-Service-Cost-Savings-by-Scaling-Knowledge-Across-the-Workforce.html). Search results give conflicting top-performer first-time-fix figures for it (88% in one snippet, 92% in another). One snippet repeats the 39% AI resolution figure. Someone needs to click through before deciding whether to update P1/P2. Keeping both at 2025 values is defensible as a matched pair from one report.
- **A2.** DataReportal **Digital 2026: UAE** (https://datareportal.com/reports/digital-2026-united-arab-emirates) reports **23.0 million** cellular connections in late 2025 (202% of population), still **100% broadband**. A reader who clicks through to DataReportal today will see 23.0 million, not 21.9 million.

## 7. Human tone / AI-detection heuristics: FAIL (minor)

**Stock phrase check:** I searched for unlock, seamless, revolutionise, unleash, leverage, empower, robust, streamline, cutting-edge, game-changer, "in today's", elevate, harness, transform, effortless, world-class, "in conclusion", supercharge and delve. **0 matches.** Most of the copy is specific to field service and reads as written for it (e.g. "Each work order counts down to the contract's response and resolution times").

Four places read templated or keyword-forced:

| # | Location | Current | Problem | Suggested rewrite |
|---|---|---|---|---|
| T1 | Benefits tile 5 | "Rules assign jobs by skill, zone, priority and SLA, so configured SugarAI works as technician scheduling software." | "configured SugarAI" is an awkward adjective + product name, and the clause exists only to carry the keyword | "Rules assign jobs by skill, zone, priority and SLA, letting SugarAI stand in for separate technician scheduling software. Administrators edit approval rules without code." |
| T2 | Benefits tile 6 | "Field service asset management tied to the contract: preventive maintenance schedules, early warranty and AMC renewal alerts, and repeat faults traced per asset." | Opens with a keyword-led fragment that has no verb, so it reads like keyword placement | "Field service asset management runs off the contract: preventive visits are scheduled from it, warranty and AMC renewals surface early, and repeat faults are traced per asset." |
| T3 | FAQ A1, A2, A3 | "Through integration." / "On their phone." / "Against the contract." | Three answers in a row open with the same clipped two-word fragment and a full stop, and A4, A6 and A7 all open with "Yes." Six of seven answers share one opening device. Keep A1 and the "Yes." answers; vary A2 and A3. | **A2:** "From their phone, technicians see the day's jobs, open the site address for directions, check the asset's history and complete the checklist with photos, readings and a signature." **A3:** "Each customer's contract entitlements set the response and resolution targets. Every work order runs its own SLA clock, alerts fire before a breach, and attainment is reported per contract." |
| T4 | Proof band lede | "Industry benchmarks and market figures, not SugarAI results: the outcomes and conditions our field service projects are designed around." | Reads like a legal disclaimer (a verbless fragment followed by a colon) | "These are industry benchmarks and market figures, not SugarAI results. They describe the outcomes and conditions our field service projects are built for." |

## 8. Section structure: PASS

I checked the draft block by block against `hlbhamt-sugarai-insurance.html`.

- **Block order matches the template:** hero + side panel → stats band → platform → benefits → CTA band 1 → services → proof → CTA band 2 → segments → market → process + callout → why HLB HAMT → FAQ → closing CTA.
- **Item counts match:**
  - 3 side rows
  - 3 stats
  - 4 platform cards
  - 6 benefit tiles
  - 8 services (4 + 4 columns)
  - 4 proof tiles
  - 6 segments
  - 6 market items
  - 6 process steps + 1 callout
  - 4 why tiles
  - 7 FAQs (first open)
  - 3 next-step rows
- **Heading levels match:**
  - H1
  - side panel H3
  - platform H4s
  - benefit H3s
  - service H4s
  - segment H4s
  - market `strong` labels
  - process H4s and callout H4
  - why H3s
  - FAQ `summary`
  - `.cta-card` H4 "What happens next"
- **Template details are kept:**
  - Block 12 has no lede.
  - Block 8 has no body line.
  - Block 14's H2 is identical to Block 8's.
  - Every eyebrow matches the template.
  - Buttons are "Request a demo", "Talk to our field service team", "See SugarAI in Action", the btn-ghost in the market section, and `/contact/` on the closing button.
  - Nav anchors match the template.
- **H2s:** every H2 matches the brief's "use as written" text exactly. None repeats an Insurance H2.
- **Note for Deliver:** proof tiles 3 and 4 carry 19 and 26 words against 7 each for tiles 1 and 2. In a 4-column `.proof-row` this will look unbalanced. Build Flag 2 already raises this. Consider a `<strong>` lead-in plus a smaller second line.

## 9. Brief and requirement accuracy (no transcript): FAIL

**What passes:**
- **Section 10.1 (no prohibited capability claims):** a search for route, GPS, offline, IoT, augmented/AR, drag, real-time, live tracking and remote monitoring finds 0 matches in page copy. FAQ 2 mentions only opening the site address for directions. Card 4 makes no equipment-failure prediction claim.
- **Section 10.2 (parent link):** the breadcrumb's "CRM Solutions (SugarAI)" and the Block 3 anchor both link to https://sugarai.com/.
- **Section 10.3 (proof stats):** Salesforce stats are removed; R1/R2 are used, with the tile 3 label and description verbatim. Tile 4's description was adapted for grammar (Build Flag 3); apart from the conclusion flagged in item 6, the meaning is kept.
- **Section 10.4:** "26 years" is used.
- **No competitor names:** a search for Salesforce, Ambit, KINAMU, Mobileforce, MSI, Tokara, ServiceNow, ServiceTitan, Dynamics, Oracle, IFS, Zoho and HubSpot finds none in page copy.
- **Sources stay off the page:** no data source is named on-page.
- **Brief content:** the hero is stat-free and opens positively; the callout gives no day count; FAQ 7 carries the April 2026 rebrand fact; FAQs carry no stats.
- **Internal links:** 1, 2 and 4 are present. Link 3 is optional and was omitted. Link 5 was omitted because its URL is unverified.
- **Keywords and word count:** meet the requirement notes (primary 3-4 times, 1,500-1,700 words).

**Failure:**
- **Block 3 lede frames the offering as a SugarAI product line.** The lede reads: "Like all SugarAI CRM solutions, SugarAI for Field Service Management sits on a Time-Aware Customer Data Platform...". With "SugarAI CRM solutions" linked to sugarai.com, this tells the reader that "SugarAI for Field Service Management" is one of the vendor's own solutions. They will not find it on sugarai.com. Section 10.1 requires "SugarAI configured/extended by HLB HAMT ... customization of SugarAI itself, not a bolt-on product."
- **Related, lower severity: Block 2 lede, sentence 2.** "SugarAI is the field service CRM software that gives sales, service and field teams one shared record, with AI built in." The definite article presents core SugarAI as field service software out of the box, which comes close to Section 4's ban on implying "SugarAI alone includes a full FSM suite out of the box."

**Minor, optional:**
- The side panel sub-line leaves out "across the UAE and GCC", which brief Block 1 specified. GCC still appears 5 times on the page, which meets Section 2b.
- FAQ A7 opens "Yes." and then offers to "add field service capabilities to yours". That implies the reader may not have field service capabilities to carry over. Consider: "Yes, your instance carries over. SugarCRM became SugarAI in April 2026 and existing instances keep running; we can add field service capabilities or audit and clean up an implementation that stalled."

---

## Overall: FAIL (loop 1 of 3)

Items 1, 2, 3, 4 and 8 pass. Items 5, 6, 7 and 9 fail. The page's structure, keywords, word count and guardrails are sound. The fixes are sentence-level rewrites; no block needs restructuring.

## Fix instructions (for the Build agent, draft-v2)

After applying the fixes, recount the words. The page should stay between 1,500 and 1,680, and the keyword total must stay at 15. None of the rewrites below adds or removes a keyword instance, except T1 and T2, which keep their one instance each.

**Fix 5: Originality (rewrite 9 sentences so none keeps the Insurance sentence skeleton).** Suggested wording is given below; any wording is fine as long as it doesn't follow the template's structure.
- **O1, Why card 4.** Replace "A dedicated support team works to agreed service levels, with a named manager owning escalation." with "Once you are live, the same team stays on under agreed service levels, and one named manager handles every escalation."
- **O2, Why card 3.** Replace the whole body with "The same [technology consulting services](/services/technology-consulting-services-dubai-uae/) team designs your setup, builds it, connects your ERP and supports it, with no work handed to subcontractors."
- **O3, Why card 1.** Replace with "For 26 years our consultants have worked with UAE and GCC firms, so they know how maintenance contracts are tendered and delivered." Keep "26 years".
- **O4, Process step 6.** Replace with "Hypercare cover for every launch phase, followed by SLA-backed managed support."
- **O5, Process step 4.** Replace with "Customer, site, asset and contract records deduplicated and proven in a test load first."
- **O6, Process step 1.** Replace with "Workshops trace a typical job from the first call through visit, invoice and renewal."
- **O7, Hero lede sentence 2.** Replace "HLB HAMT deploys it for service businesses across the UAE and GCC, cloud or on-premise." with "Our Dubai-based team sets it up for service businesses in the UAE and wider GCC, hosted in the cloud or on your own servers." (This also brings the lede up to about 55 words, inside the brief's 50-60.)
- **O8, Closing row 1.** Replace with "A call to map your job types, contracts, crews and today's systems."
- **O9, Closing row 3.** Replace with "Finally, a costed plan covering scope, phases and timeline for your sign-off."

**Fix 6: Stat accuracy (Proof band tile 4).**
- **6a (required).** Remove the conclusion the source warns against. Change `.proof-l` to: "**UAE mobile connections run on broadband.** Share of the UAE's 21.9 million mobile connections that run on 3G, 4G or 5G networks. [6]" Delete "so technicians can stay connected on site".
  - This changes wording the Content Writer prescribed in Section 10.3, so list the change in "Flags for Test/Deliver" for Content Writer sign-off.
  - Optional, and also needs Content Writer sign-off: update to DataReportal Digital 2026 (23.0 million connections, still 100% broadband; URL https://datareportal.com/reports/digital-2026-united-arab-emirates) and change Source 6 to match.
- **6b (required, footnote only).** Change Source 5 to "Mordor Intelligence, global field service management market (solution segment: scheduling, dispatch and route optimisation, 28.16% of 2025 revenue): https://www.mordorintelligence.com/industry-reports/field-service-management-market". This keeps the on-page label the Content Writer set while naming the source's full category accurately.
- **6c (flag only, no copy change unless the Content Writer decides).** Add a line to "Flags for Test/Deliver" noting the Aquant 2026 benchmark (19 Feb 2026) and Digital 2026 UAE editions so the Content Writer can decide whether to refresh P1/P2 and R2.

**Fix 7: Tone.**
- **T1, Benefits tile 5.** Replace with "Rules assign jobs by skill, zone, priority and SLA, letting SugarAI stand in for separate technician scheduling software. Administrators edit approval rules without code."
- **T2, Benefits tile 6.** Replace with "Field service asset management runs off the contract: preventive visits are scheduled from it, warranty and AMC renewals surface early, and repeat faults are traced per asset."
- **T3, FAQ A2.** Replace with "From their phone, technicians see the day's jobs, open the site address for directions, check the asset's history and complete the checklist with photos, readings and a signature."
- **T3, FAQ A3.** Replace with "Each customer's contract entitlements set the response and resolution targets. Every work order runs its own SLA clock, alerts fire before a breach, and attainment is reported per contract."
- **T4, Proof band lede.** Replace with "These are industry benchmarks and market figures, not SugarAI results. They describe the outcomes and conditions our field service projects are built for."

**Fix 9: Section 10.1 framing.**
- **Block 3 lede (required).** Replace "Like all [SugarAI CRM solutions](https://sugarai.com/), SugarAI for Field Service Management sits on a Time-Aware Customer Data Platform that keeps the history of every site and asset in sequence." with "SugarAI for Field Service Management is core SugarAI configured by HLB HAMT, so it shares the Time-Aware Customer Data Platform behind all [SugarAI CRM solutions](https://sugarai.com/) and keeps every site and asset history in sequence." (34 words, inside the brief's 30-35.) Primary keyword instance 3 and internal link 1 are kept.
- **Block 2 lede, sentence 2 (recommended).** Replace "SugarAI is the field service CRM software that gives sales, service and field teams one shared record, with AI built in." with "Configured by HLB HAMT, SugarAI works as field service CRM software, giving sales, service and field teams one shared record with AI built in." Keyword instance 1 of 2 is kept.

**Optional polish (not required to pass):** the item 4 grammar notes (Platform card 3 comma, "FSM" in proof tile 3, Stat 3 "market", callout "follow next") and the item 9 minor notes (side panel sub-line geo, FAQ A7 wording).
