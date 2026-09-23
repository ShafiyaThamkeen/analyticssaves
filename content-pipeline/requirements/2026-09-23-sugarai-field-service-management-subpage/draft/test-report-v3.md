# Test report v3: SugarAI for Field Service Management (industry subpage)

- Draft tested: `draft/draft-v3.md`
- Checked against: `brief.md` (Sections 1-10, with Section 10 overriding earlier sections), `inputs/requirement-notes.md`, `inputs/template-source/hlbhamt-sugarai-insurance.html`, `draft/draft-v2.md`, `draft/test-report-v2.md`, the 5 reference sites, and the wider web
- Loop: **3 of 3** (`test-report-v1.md` and `test-report-v2.md` exist)
- Tester: Test agent, 2026-09-23

**Tooling limitation (same as loops 1 and 2).** I checked stats and originality through WebSearch result text, which quotes the source pages. WebFetch is egress-blocked. Every source URL still has to be click-verified before publication (brief Section 10.5).

**How I tested.** I compared the page copy in v2 and v3 block by block, from the hero through the closing CTA and the Sources list. **Exactly three page-copy sentences changed**, and they are the three listed in "Changes from v2":
- the Block 4 lede
- Process step 6
- the first sentence of FAQ A3

Every other line of page copy, the footnotes and the Stats-used table are identical to v2. Build's claim that it changed nothing else is accurate. I still ran all 9 checks against the whole v3 page and did a fresh full read for anything earlier loops missed.

| # | Check | Result |
|---|---|---|
| 1 | Keyword placement and density | PASS |
| 2 | Word count | PASS |
| 3 | Zero em dashes | PASS |
| 4 | Grammar, spelling, punctuation | PASS (optional notes only) |
| 5 | Originality | PASS |
| 6 | Stat accuracy | PASS |
| 7 | Human tone / AI-detection heuristics | PASS |
| 8 | Section structure | PASS |
| 9 | Brief and requirement accuracy (no transcript) | PASS |

---

## 1. Keyword placement and density: PASS

I used the brief Section 2 rule: exact phrase, case-insensitive, on-page copy only, meta excluded. I ran a regex over v3 and kept only the matches inside page copy (lines 31-347). Matches in the meta lines, the title line, "Changes from v2", "Stats used" and "Flags" were dropped.

| Keyword | Target | Actual | Location(s) in v3 |
|---|---|---|---|
| SugarAI for Field Service Management (primary) | 3-4 | **4** | H1; hero lede sentence 1; Block 3 lede; Block 4 lede ("In SugarAI for Field Service Management, these six capabilities...") |
| field service CRM software | 2 | 2 | Block 2 lede; FAQ A1 |
| field service automation | 1-2 | 1 | Block 6 H2 |
| field service management in the UAE | 1-2 | 1 | Block 10 lede |
| technician scheduling software | 1 | 1 | Benefits tile 5 |
| work order management software | 1 | 1 | Services 05 |
| mobile field service management | 1 | 1 | Services 08 H4 |
| field service asset management | 1 | 1 | Benefits tile 6 |
| SugarAI field service CRM | 1 | 1 | Services 01 |
| SugarAI CRM for field service | 1 | 1 | Process H2 |
| SugarCRM field service management | 1 | 1 | FAQ 7 question |
| **Total** | 14-17 | **15** | Same positions as v1 and v2 |

- **Placement:**
  - The meta title (58 characters) and meta description (157 characters) both start with the primary keyword.
  - The H1 is exactly the primary keyword.
  - The primary keyword also appears in the first 100 words (hero lede, sentence 1).
- **The T3 edit kept primary instance 4 in the Block 4 lede, as required.**
- **Density:**
  - All keywords: 15 / 1,676 = 0.89%.
  - Primary keyword alone: 4 / 1,676 = 0.24%.
  - There is no stuffing and no under-use.
- **Keyworded headings** are only the H1, Services H2, Services 08 H4, Process H2 and FAQ 7 question. No H2 contains the primary keyword.
- **No sentence contains two different exact-match keywords.**
- **Excluded phrases:** a regex for all 12 excluded phrases returns 0 matches. That includes "SugarAI Field Service Management" without "for".

## 2. Word count: PASS

I used the brief Section 1 count rule. **Total: 1,676 words** (1,691 with the 4 Platform tags and 7 stat figures). Both are inside the 1,500-1,700 range, and 1,676 is under the 1,680 write-to ceiling.

**How I verified it:**
- **The three edits are word-neutral:**
  - Block 4 lede: 20 → 20
  - Process step 6: 11 → 11
  - FAQ A3, sentence 1: 10 → 10
- **The rest of the page copy is identical to v2**, which loop 2 audited at 1,676.
- **Full recount of the two edited blocks:**
  - Benefits = 191 (H2 9 + lede 20 + H3s 34 + tile bodies 128)
  - Process = 145 (H2 10 + lede 18 + step H4s 14 + step bodies 69 + callout H4 10 + callout body 24)
  - Both match Build's figures.
- **Flag 1's per-block figures** now add up to 1,676:
  - Hero 136
  - Stats band 104
  - Platform 125
  - Benefits 191
  - CTA 1 21
  - Services 183
  - Proof 88
  - CTA 2 13
  - Segments 112
  - UAE/GCC 143
  - Process 145
  - Why HLB HAMT 97
  - FAQs 267
  - Closing CTA 51
- **The loop-2 reporting error is fixed.** Flag 1 now gives Benefits as 191, not 193.

**Per-block budget variances are unchanged from v2 and informational only.** Loops 1 and 2 established that the brief's sub-budgets can't all be met at the same time, so the page total is the binding target.
- Over budget:
  - Proof (Section 10 gives tiles 3 and 4 descriptions)
  - Why HLB HAMT (+2)
  - UAE/GCC (+3)
- Under budget:
  - Stats band (-1)
  - CTA 1 (-1)
  - FAQs (-3)

## 3. Zero em dashes: PASS

I searched the whole v3 file for `—` (em dash), `–` (en dash) and `--`. **0 matches for all three.**

## 4. Grammar, spelling, punctuation: PASS (optional notes only)

- **British spelling is consistent.** I searched for -ize/-ise variants, -yze, optimiz-, color, center, labor, program, behavior, catalog, defense, license, specialized and analyz-. There were 0 matches.
- **The three new sentences are grammatical and correctly punctuated:**
  - "In SugarAI for Field Service Management, these six capabilities carry each job from the first request to the customer's sign-off."
  - "Hypercare covers each launch phase; an SLA then governs managed support." The semicolon correctly joins two independent clauses.
  - "Response and resolution targets come from the customer's contract entitlements."
- **I found no errors anywhere else on the page on a fresh full read.**
- **Optional polish for the Content Writer or Deliver.** None of these is a failure, and all were carried over from earlier loops.
  1. **Why card 4:** "Your build team stays on after launch..." A reader could take this to mean the client's own team. Suggested: "The team that built your system stays on after launch under agreed service levels, and one named manager takes escalations." (+3 words; the page has 4 words of headroom to 1,680.)
  2. **FAQ A2:** "a checklist that takes photos, readings and the customer's signature". Suggested: change "takes" to "captures" (word-neutral).
  3. **Closing row 1:** "First, we talk through..." The row already carries the number "1", so "First," can go.
  4. **Other items still unapplied:**
     - Platform card 3 serial comma
     - Stat 3 `.d` missing "market"
     - Callout "follow next" (see item 7, note N1)

## 5. Originality: PASS

### 5a. The three new sentences, checked against the Insurance template

| Location | v3 sentence | Nearest template text | Verdict |
|---|---|---|---|
| Block 4 lede | "In SugarAI for Field Service Management, these six capabilities carry each job from the first request to the customer's sign-off." | "Six ways SugarAI, purpose-built insurance CRM software, helps your teams sell, service and retain more effectively." | Original. The only thing shared is the idea of "six", which comes from the brief's structural role. The sentence structure and wording are different. |
| Process step 6 | "Hypercare covers each launch phase; an SLA then governs managed support." | "Phased go-live with hypercare, then managed support under SLA." | Original. Hypercare is now the subject with its own verb, and the SLA clause is inverted. Only the methodology terms "hypercare" and "managed support" are shared, and the brief (Section 4) allows them as reusable facts. It does not fall back to the template's noun-phrase shape. |
| FAQ A3, sentence 1 | "Response and resolution targets come from the customer's contract entitlements." | No template FAQ covers SLAs or entitlements. | Original against the template. It is close to the brief's own FAQ 3 guidance, which is an internal instruction, not a published source. |

### 5b. The 9 loop-1 findings: no regression

Each of these sentences in v3 is identical to the v2 wording that loop 2 marked resolved:

| Loop-1 finding | Location |
|---|---|
| O1 | Why card 4 |
| O2 | Why card 3 |
| O3 | Why card 1 |
| O4 | Process step 6. It changed again in v3, but still does not follow the template shape (see 5a). |
| O5 | Process step 4 |
| O6 | Process step 1 |
| O7 | Hero lede, sentence 2 |
| O8 | Closing row 1 |
| O9 | Closing row 3 |

The loop-1 borderline items are also unchanged, and they are still acceptable under the structural-label and reusable-fact exceptions:
- Services 01 blueprint
- Services 07 Power BI
- "role-based training"
- the brief-prescribed H2/H3 labels

### 5c. Wider web and reference sites

I ran exact-phrase searches on the three new sentences:
- "Response and resolution targets come from the customer's contract entitlements"
- "Hypercare covers each launch phase"
- "these six capabilities carry each job from the first request"

**None of them matched anything verbatim or nearly verbatim.** The results were only topical pages:
- Salesforce and Oracle entitlement guides
- hypercare explainers
- unrelated "six capabilities" pages

The new wording uses no distinctive vocabulary from Ambit, KINAMU, MSI Data, Tokara or the Mobileforce release.

## 6. Stat accuracy: PASS

No stat, label or footnote changed in v3. On this final loop I re-confirmed every figure against search-quoted source text anyway:

| Draft stat | Brief ID | Source text (via search) | Verdict |
|---|---|---|---|
| US$809.8M, MEA FSM revenue 2025, 8.3% a year to 2033 | S1 | Grand View Research: "generated a revenue of USD 809.8 million in 2025 and is expected to grow at a CAGR of 8.3% from 2026 to 2033" | Matches |
| US$70.25B, GCC FM 2025, hard services led by MEP and HVAC hold the largest share | S2 | Mordor Intelligence: "reached USD 70.25 billion in 2025"; "hard services led with 59.3% revenue share in 2024, dominated by MEP and HVAC maintenance" | Matches. The d-line doesn't pin the share to a year, so the 2024 share date isn't misstated. |
| 64.88%, outsourced share of UAE FM, 2025 | S3 | Mordor Intelligence: "Outsourced service delivery captured 64.88% of the UAE facility management market share in 2025" | Matches |
| 86%, first-time fix at top performers | P1 | Aquant 2025 Benchmark (13 Feb 2025): "Top companies boast a First Time Fix Rate (FTFR) of 86%" | Matches |
| 39%, faster resolution for top performers using AI | P2 | Same report: "AI-powered solutions enable top-performing organizations to achieve a 39% faster Resolution Time" | Matches |
| 28.16%, scheduling and dispatch share of 2025 global FSM software revenue | R1 | Mordor Intelligence: "scheduling-dispatch and route-optimization led with 28.16% of 2025 revenue" | Matches. Source 5 still names the full category (the loop-1 fix is intact). Route optimisation appears only in the footnote, not on the page. |
| 100%, share of the UAE's 21.9 million mobile connections classed as broadband (3G, 4G or 5G), early 2025 | R2 | DataReportal Digital 2025 UAE: "21.9 million mobile connections in early 2025"; "100% of mobile connections in the UAE can now be considered 'broadband'" | Matches. **Proof tile 4 still uses the stat-accurate v2 wording.** The "so technicians stay connected on site" inference has not come back. |

**Recency:** every source is from 2025-2026, so all of them fall within 2-3 years.

**Other checks:**
- **No invented or misattributed figures.**
- **No source is named in page copy.** Footnotes [1]-[6] map correctly.
- **No duplication with other pages in the project.** A repo-wide search for 809.8, 70.25, 64.88, 28.16 and "21.9 million" finds them only in this requirement's brief, drafts and test reports.
- **No Salesforce figures appear anywhere.**
- **Source 7** (the rebrand fact) is correctly listed as a non-stat fact.

## 7. Human tone / AI-detection heuristics: PASS

**Stock phrase check.** I searched for:
- unlock, seamless, revolution-, unleash
- leverag-, empower, robust, streamlin-
- cutting-edge, game-chang-, "in today's", elevat-
- harness, transform, effortless, world-class
- "in conclusion", supercharg-, delve, synerg-
- holistic, journey, landscape, next-level
- best-in-class, state-of-the-art, ever-changing, navigate

There were **0 matches in page copy**. "Tailored" appears once (Block 2 lede), which loop 2 accepted.

**The three loop-2 tone findings are all resolved:**

| Loop-2 item | What was flagged | v3 | Verdict |
|---|---|---|---|
| T1 FAQ A2-A4 openers | A3 "**Each** customer's contract entitlements define..." / "**Every** work order..." / A4 "Yes. **Each** subcontractor..." formed an Each/Every/Each run | A3 now opens "**Response** and resolution targets come from the customer's contract entitlements." The openers across A2-A4 are now "Technicians work..." / "Response and resolution..." / "Every work order..." / "Yes." / "Each subcontractor..." | **Resolved.** The three-in-a-row determiner run is broken. One "Every" followed by one "Each" in the next answer, with "Yes." between them, is normal variation. This is the exact wording loop 2 prescribed. |
| T2 Process lede → step 6 echo | Lede "**Each** stage ends with your sign-off." / step 6 "**Each** phase launches with hypercare..." | Step 6 now reads "**Hypercare** covers each launch phase; an SLA then governs managed support." | **Resolved.** Step 6 no longer opens with the lede's "Each [stage/phase] [verb]s..." construction. "Each" is now mid-sentence and modifies a different noun. Sentences opening with "Each" fall from 8 in v2 to 6 page-wide, back to the v1 level that loop 1 accepted. |
| T3 "configured/tailored by HLB HAMT" in the Block 2-4 ledes | B2 "Tailored by HLB HAMT, ..." / B4 "With SugarAI for Field Service Management configured by HLB HAMT, ..." | B4 now reads "**In SugarAI for Field Service Management**, these six capabilities carry each job from the first request to the customer's sign-off." | **Resolved.** Only Block 2 uses the "[participle] by HLB HAMT" opener now. Block 3 states the configuration framing once ("HLB HAMT delivers ... by configuring core SugarAI"). Block 4 moves on to the capabilities. Read in sequence, the three ledes no longer sound like boilerplate. |

**Fresh full read.** I read every block in order, looking for templated or robotic passages, including in text that earlier loops had passed. I found no fail-level issues. There are two low-priority notes for the Content Writer. Neither is robotic phrasing or stock AI language, and neither is a failure:

- **N1, Process block, "follow" three times.**
  - The three uses:
    - Lede: "...mobile job sheets and scheduling **follow**."
    - Step 1: "Workshops **follow** a typical job end to end..."
    - Callout: "Scheduling rules, mobile job sheets and ERP integration **follow next**."
  - The lede and the callout also make the same phasing point. The brief asks for that in both places (Block 11 lede and callout specs), so the content overlap is intended. The shared verb is the only thing a reader might notice.
  - Loop 1 already listed "follow next" as optional polish.
  - Optional word-neutral rewrite of the callout's second sentence: "Scheduling rules, mobile job sheets and ERP integration come next."
- **N2, "configure" appears 6 times as a verb across the page:**
  - hero lede
  - Block 3 lede
  - Services 01
  - Segments H2
  - Block 10 lede
  - Process step 3

  This is the framing brief Section 10.1 asks for ("configured by HLB HAMT"). The instances are spread across separate sections and never sit in adjacent ledes after the T3 fix, so it reads as consistent positioning, not repetition. No change is needed.

**Loop-2 optional note, still unapplied (not a failure):** the Proof H2 "...achieve" and the lede "...show what leading service organisations achieve" echo each other. Optional rewrite: "These industry benchmarks come from top-performing service organisations, alongside market data on software spending and UAE mobile networks. Our projects are designed around them." (-1 word)

## 8. Section structure: PASS

I rechecked v3 block by block against `hlbhamt-sugarai-insurance.html`. Nothing structural changed from v2.

- **Order (all 14 blocks present):** hero + side panel → stats band → platform → benefits → CTA band 1 → services → proof → CTA band 2 → segments → UAE/GCC market → process + callout → why HLB HAMT → FAQ → closing CTA.
- **Item counts match the template:**
  - 3 side rows
  - 3 stats
  - 4 platform cards
  - 6 benefit tiles
  - 8 services (01-04 and 05-08 in two columns)
  - 4 proof tiles
  - 6 segments
  - 6 market items
  - 6 process steps + callout
  - 4 why tiles
  - 7 FAQs (first one open)
  - 3 "What happens next" rows
- **Heading levels:**
  - H1 in the hero; H3 in the side panel
  - H2 in each section
  - H4 on platform cards, services, segments, process steps and the callout
  - H3 on benefit tiles and why tiles
- **Template details:**
  - Block 12 has no lede.
  - Block 8 has no body line.
  - Block 14's H2 is identical to Block 8's.
  - The closing button links to `/contact/`.
  - Eyebrows and nav anchors match the template.
- **H2 wording:** every H2 matches the brief's "use as written" text, and none repeats an Insurance H2.
- **Notes for Deliver (carried over):**
  - **Draft-only sections:** strip "Changes from v2", "Stats used" and "Flags" from the page.
  - **Proof tiles 3 and 4:** render with a `<strong>` lead-in and a smaller second line, so they balance with tiles 1 and 2.
  - **FAQPage JSON-LD:** build it from the 7 visible **v3** answers, word for word. A3 changed in this loop.
  - **Footnote list:** render it as a small sources note (brief Section 3).

## 9. Brief and requirement accuracy (no transcript): PASS

There is no transcript and no client content source. I checked v3 against `requirement-notes.md` and the brief, including Section 10.

- **Section 10.1, framing:**
  - The Block 3 lede ("HLB HAMT delivers SugarAI for Field Service Management by configuring core SugarAI, with no bolt-on product.") and the Block 2 lede ("Tailored by HLB HAMT, SugarAI works as field service CRM software...") are unchanged from the v2 fixes.
  - The new Block 4 lede makes no product or bolt-on claim.
- **Section 10.1, capability guardrail.** I searched page copy for:
  - route/routing, GPS, offline
  - IoT, augmented, AR, drag
  - real-time, live tracking, remote monitoring
  - dispatch board, "predicts failure", "out of the box"

  There were **0 matches in page copy**. "Route optimisation" appears only in the Source 5 footnote, the Stats-used table and the Flags. Other points:
  - Benefits tile 5 describes rules-based allocation only.
  - FAQ A2 mentions "the site address for directions" (a link to the address, as the brief allows) and makes no routing claim.
  - Nothing is described as working offline.
  - There is no dispatch board.
  - None of the three v3 edits adds a capability claim.
- **Section 10.2 (parent link):** the breadcrumb parent link and the Block 3 anchor both point to https://sugarai.com/.
- **Section 10.3 (Salesforce stats):**
  - No Salesforce stats are used; R1 and R2 are.
  - The tile 3 label and description are verbatim.
  - The tile 4 label is verbatim. The tile 4 description is still the stat-accurate v2 wording, pending the Content Writer's decision D1 below.
- **Section 10.4 (years in region):** "26 years" appears once (Why card 1). "More than 25 years" appears nowhere.
- **Hero:**
  - The page opens on the capability, not a pain point.
  - The hero carries no stat.
  - Sentence 2 includes every fact the brief requires: HLB HAMT, service businesses, the UAE and GCC, and cloud or on-premise.
- **Competitor and data-source names:** none appear on the page. Salesforce, Ambit, KINAMU, Mobileforce, MSI, Tokara, Aquant, Mordor, Grand View and DataReportal appear only in the footnotes and the draft notes.
- **Other brief requirements:**
  - The callout gives no number of days.
  - The FAQs carry no stats.
  - FAQ 7 states the April 2026 rebrand fact (Source 7).
  - Internal links 1, 2 and 4 are present. Links 3 and 5 are optional and are omitted, with Build's reasons in Flag 7.
  - The segments stay focused on equipment service, not patient CRM.
- **Requirement notes:** the primary keyword appears 3-4 times (actual: 4), the word count is within 1,500-1,700, the Insurance H2s are not reused, and the template structure is matched.

---

## Content Writer decision items (separate from the pass/fail verdict, carried over)

These do not block Deliver. They need your decision or a manual step before publication.

**D1. Proof tile 4 description: needs your sign-off.**
- **You prescribed (Section 10.3):** "...of the UAE's 21.9 million mobile connections are 3G, 4G or 5G, so technicians stay connected on site."
- **The draft uses:** "Share of the UAE's 21.9 million mobile connections classed as broadband (3G, 4G or 5G) in early 2025."
- **Why it was changed:** DataReportal says its broadband share "should not be considered a proxy for mobile internet use", so the "so technicians stay connected on site" clause overstated the source.
- **Test recommends:** approve the current wording. If you restore the original clause, the stat-accuracy check would fail.
- **Shorter option, if you want one:** "Share of the UAE's 21.9 million mobile connections on 3G, 4G or 5G, early 2025."

**D2. Source freshness (advisory).**
- **Aquant** published a 2026 benchmark on 19 Feb 2026. Search snippets conflict on its top-performer first-time fix figure (88% vs 92%).
- **DataReportal Digital 2026: UAE** shows 23.0 million connections, still 100% broadband.
- **What to decide:** whether to keep the 2025 figures or refresh P1/P2 and tile 4. Both 2025 figures fall within the 2-3 year window, so either choice passes item 6.

**D3. Click-verification.** Every source URL and internal link was checked through search only. They must be opened and confirmed before publication (Section 10.5). The Deliver handoff must flag this as an outstanding manual step.

**D4. Optional polish (not required).** These are listed under items 4 and 7 above:
- Why card 4 "The team that built your system..."
- FAQ A2 "captures"
- Closing row 1 without "First,"
- Proof lede "achieve" echo
- Callout "come next"
- Platform card 3 serial comma
- Stat 3 "market"

The page has 4 words of headroom to the 1,680 write-to ceiling (9 to 1,700 with tags and figures).

---

## Overall: PASS

All 9 items pass on loop 3 of 3.
- **The three loop-2 tone fixes are resolved:**
  - FAQ A3 no longer continues the Each/Every/Each opener run.
  - Process step 6 no longer echoes the Process lede.
  - The Block 4 lede no longer repeats the "configured/tailored by HLB HAMT" construction.
- **Nothing that passed before has regressed:**
  - the 9 originality fixes
  - proof tile 4's stat-accurate wording
  - the Block 2/3 framing fixes
  - the tile 3 footnote
  - 15 keyword instances in total, 4 of them the primary keyword, all in the same positions
  - 1,676 words
  - 0 em dashes
  - all 14 blocks with the correct item counts
  - no unconfirmed capability claims
- **My fresh full read found nothing at fail level.**

**`draft/draft-v3.md` is ready for the Deliver agent.** Deliver should:
1. strip the draft-only sections
2. build the FAQPage JSON-LD from the 7 visible v3 answers, word for word
3. render the footnote list as a small sources note
4. carry decision items D1-D3 into the handoff summary for the Content Writer, especially D1 (tile 4 sign-off) and D3 (click-verification before publication)
