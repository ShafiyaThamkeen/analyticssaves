# Test report v2: SugarAI for Field Service Management (industry subpage)

- Draft tested: `draft/draft-v2.md`
- Checked against: `brief.md` (Sections 1-10, with Section 10 overriding earlier sections), `inputs/requirement-notes.md`, `inputs/template-source/hlbhamt-sugarai-insurance.html`, `draft/draft-v1.md`, `draft/test-report-v1.md`, the 5 reference sites, and the wider web
- Loop: **2 of 3** (`test-report-v1.md` exists)
- Tester: Test agent, 2026-09-23

**Tooling limitation (same as loop 1).** WebFetch is still egress-blocked (I tried datareportal.com again and it failed). I checked stats and originality through WebSearch result text, which quotes the source pages. Click-verification before publication is still required (brief Section 10.5).

**How I tested.** I diffed v2 against v1 line by line. The only changed page-copy sentences are the ones listed in "Changes from v1": hero lede sentence 2, Block 2 lede sentence 2, Block 3 lede, Benefits tiles 5 and 6, proof lede, proof tile 4, process steps 1, 4 and 6, Why cards 1, 3 and 4, FAQ A2 and A3, and closing rows 1 and 3. No other page copy changed. I still ran all 9 checks against the whole v2 page.

| # | Check | Result |
|---|---|---|
| 1 | Keyword placement and density | PASS |
| 2 | Word count | PASS |
| 3 | Zero em dashes | PASS |
| 4 | Grammar, spelling, punctuation | PASS (optional notes) |
| 5 | Originality | PASS (all 9 loop-1 findings resolved) |
| 6 | Stat accuracy | PASS |
| 7 | Human tone / AI-detection heuristics | **FAIL** (minor, 3 sentence-level edits) |
| 8 | Section structure | PASS |
| 9 | Brief and requirement accuracy (no transcript) | PASS |

**Decision item for the Content Writer (separate from pass/fail):** proof tile 4's description now differs from the wording you prescribed in Section 10.3. See "Content Writer decision items" near the end of this report.

---

## 1. Keyword placement and density: PASS

I used the brief Section 2 rule: exact phrase, case-insensitive, on-page copy only, meta excluded. I ran a regex over the draft, then dropped matches in the meta lines, the draft title line, "Changes from v1", "Stats used" and "Flags".

| Keyword | Target | Actual | Location(s) in v2 |
|---|---|---|---|
| SugarAI for Field Service Management (primary) | 3-4 | **4** | H1; hero lede sentence 1; Block 3 lede ("HLB HAMT delivers SugarAI for Field Service Management by configuring core SugarAI..."); Block 4 lede |
| field service CRM software | 2 | 2 | Block 2 lede ("...SugarAI works as field service CRM software..."); FAQ A1 |
| field service automation | 1-2 | 1 | Block 6 H2 |
| field service management in the UAE | 1-2 | 1 | Block 10 lede |
| technician scheduling software | 1 | 1 | Benefits tile 5 ("...the assignment work many teams buy technician scheduling software for.") |
| work order management software | 1 | 1 | Services 05 |
| mobile field service management | 1 | 1 | Services 08 H4 |
| field service asset management | 1 | 1 | Benefits tile 6 ("Contracts drive field service asset management: ...") |
| SugarAI field service CRM | 1 | 1 | Services 01 |
| SugarAI CRM for field service | 1 | 1 | Process H2 |
| SugarCRM field service management | 1 | 1 | FAQ 7 question |
| **Total** | 14-17 | **15** | Same positions as v1 |

- **Build's figure checks out:** 15 in total, 4 of them primary, all in the same locations as v1.
- **Density:** 15 / 1,676 = 0.89% for all keywords; primary alone 4 / 1,676 = 0.24%. No stuffing, no under-use.
- **Meta title** (58 characters) and **meta description** (157 characters) are unchanged. Both start with the primary keyword.
- **H1** is exactly the primary keyword. The primary keyword is also in the first 100 words (hero lede, sentence 1).
- **Keyworded headings** are only the H1, Services H2, Services 08 H4, Process H2 and FAQ 7 question. No H2 contains the primary keyword.
- **No sentence has two different exact-match keywords.**
- **Excluded phrases:** none of the 12 excluded phrases appears (regex returned 0 matches, including "SugarAI Field Service Management" without "for").

## 2. Word count: PASS

I used the brief Section 1 count rule. I recounted every changed sentence by hand, applied the difference to the loop-1 audited v1 total of 1,643, and fully recounted Benefits, Services, Hero and Why HLB HAMT as cross-checks.

| Block | v2 actual | Brief budget | Note |
|---|---|---|---|
| 1 Hero + side panel | 136 | 130-145 | Now in range (v1: 128). Lede is 54 words, inside 50-60. |
| 2 Stats band | 104 (107 with figures) | 105-120 | 1 under |
| 3 Platform | 125 (133 with tags) | 115-130 | OK. Lede is 34 words, inside 30-35. |
| 4 Benefits | **191** | 180-200 | OK. Build reported 193; the full recount gives 191. |
| 5 CTA band 1 | 21 | 22-28 | 1 under (unchanged) |
| 6 Services | 183 | 170-185 | OK (full recount matches) |
| 7 Proof band | 88 (92 with figures) | 55-65 | Over, as in v1, because Section 10 gives tiles 3 and 4 labels plus descriptions |
| 8 CTA band 2 | 13 | 12-16 | OK |
| 9 Segments | 112 | 110-125 | OK |
| 10 UAE/GCC | 143 | 125-140 | 3 over (unchanged) |
| 11 Process | 145 | 130-145 | At the ceiling |
| 12 Why HLB HAMT | **97** | 85-95 | 2 over |
| 13 FAQs | 267 | 270-300 | 3 under |
| 14 Closing CTA | 51 | 50-60 | OK |
| **Total** | **1,676** (1,691 with 8 tag words and 7 figures) | 1,500-1,700 (write-to ceiling 1,680) | **In range** |

**Changes since v1, by sentence:**

| Sentence | Change |
|---|---|
| Hero lede sentence 2 | +8 |
| Block 2 lede | +3 |
| Block 3 lede | +6 |
| Benefits tile 5 | +2 |
| Benefits tile 6 | +2 |
| Proof lede | +6 |
| Proof tile 4 | -2 |
| Process step 1 | +2 |
| Process step 4 | +1 |
| Process step 6 | -1 |
| Why card 1 | +3 |
| Why card 3 | +2 |
| Why card 4 | +2 |
| FAQ A2 | -1 |
| FAQ A3 | 0 |
| Closing row 1 | 0 |
| Closing row 3 | 0 |
| **Net** | **+33** (1,643 + 33 = 1,676) |

- **Why HLB HAMT at 97 words (budget 85-95).** I confirmed this by recount: H2 6 + H3s 19 + bodies 22/15/18/17. It doesn't push anything else out of range:
  - The page total is 1,676, under the 1,680 write-to ceiling.
  - With tags and figures it is 1,691, under 1,700.
  - Per-block budgets are informational. Loop 1 established that the brief's sub-budgets can't all be met at once, and the page total is the binding target.
- **Headroom is now tight.** With tags and figures the page has 9 words left before 1,700. The fixes below are word-neutral.
- **Minor reporting error, not a failure.** In Flag 1, Build's per-block figures add up to 1,678, not the 1,676 it states. The gap is the Benefits figure: it should be 191, not 193. The 1,676 total is correct.

## 3. Zero em dashes: PASS

I searched the whole v2 file for `—` (em dash), `--` and `–` (en dash). **0 matches for all three.**

## 4. Grammar, spelling, punctuation: PASS (optional notes)

- **British spelling is consistent.** I searched for -ize/-yze/-ization, optimiz-, color, center, labor, program, behavior, catalog, defense and license: 0 matches.
- **No errors in the new sentences.**
- **Optional notes on the new text.** None of these is required to pass.
  1. **Why card 4:** "Your build team stays on after launch..." A reader could take "your build team" to mean the client's own internal team. Suggested: "The team that built your system stays on after launch under agreed service levels, and one named manager takes escalations." (+3 words, so only use it if you trim elsewhere.)
  2. **FAQ A2:** "a checklist that takes photos, readings and the customer's signature". A checklist doesn't take photos. "Captures" is more exact: "...and a checklist that captures photos, readings and the customer's signature." (word-neutral)
  3. **Closing row 1:** "First, we talk through..." sits next to the row's own number "1", so "First," is redundant. Suggested: "We talk through your job types, contracts, crews and today's systems." (-1 word)
  4. **Why card 1:** "...conventions, which 26 years in the UAE and GCC have taught us." It's grammatical, but ending on the inverted relative clause is a little stiff. It's acceptable as written.
- **Optional polish carried over from loop 1, still unapplied.** Build was right to leave these alone:
  - Platform card 3 serial comma
  - "FSM" in proof tile 3 (Content Writer wording)
  - Stat 3 `.d` missing "market"
  - Callout "follow next"

## 5. Originality: PASS

### 5a. The 9 loop-1 findings against the Insurance template

For each one I checked whether v2 is only the same skeleton with new words, or whether the sentence is actually built differently.

| # | Location | Insurance template | v2 | Verdict |
|---|---|---|---|---|
| O7 | Hero lede, sentence 2 | "HLB HAMT implements SugarAI for insurers, brokers and agencies across the UAE and GCC, cloud or on-premise." | "Whether it runs in the cloud or on your own servers, HLB HAMT configures it for service businesses throughout the UAE and GCC." | **Resolved.** The deployment choice is now a leading "Whether..." clause with its own verb, not the template's trailing "cloud or on-premise" tag. The main clause still says who does what for whom and where. That fact is required by the brief, and the loop-1 suggested fix kept it too. |
| O3 | Why card 1 | "26 years across the UAE and GCC, with consultants who know how insurance is sold and serviced here." | "Gulf maintenance contracts have their own tendering, pricing and delivery conventions, which 26 years in the UAE and GCC have taught us." | **Resolved.** The subject changes from tenure to the contracts. "26 years" moves into a relative clause at the end. The "with consultants who know how X is Y-ed here" frame is gone. |
| O2 | Why card 3 | "Consulting, implementation, integration and support under one engagement, with no subcontracting and no gaps." | "No part of your project is subcontracted: our technology consulting services team designs, builds, integrates and supports it." | **Resolved.** The verbless noun list becomes a statement plus a subject-verb clause, and the no-subcontracting point moves from the tail to the lead. The four activities are a fact the brief explicitly allowed to be reused (Section 4). |
| O1 | Why card 4 | "A dedicated team on agreed service levels, with a named manager and a clear escalation path." | "Your build team stays on after launch under agreed service levels, and one named manager takes escalations." | **Resolved.** The verbless noun phrase becomes two finite clauses with new content (the build team staying on after launch). "Agreed service levels" and "named manager" are the brief's reusable facts, not distinctive template phrasing. This is the closest of the nine to the template, but it no longer follows the template's structure. |
| O6 | Process step 1 | "We map how a quote becomes a policy, claim and renewal today." | "Workshops follow a typical job end to end: call, visit, invoice and renewal." | **Resolved.** The "how a X becomes a Y" construction is gone. A new subject and verb are followed by a colon list. |
| O5 | Process step 4 | "Policyholder and claims data cleansed, mapped and rehearsed before load." | "We trial-load customer, site, asset and contract records, removing duplicates before cutover." | **Resolved.** The passive participle triplet becomes an active "We" clause plus a participle phrase. |
| O4 | Process step 6 | "Phased go-live with hypercare, then managed support under SLA." | "Each phase launches with hypercare; an SLA then governs managed support." | **Resolved.** The noun phrase becomes two clauses, and the second is inverted so the SLA is the subject. The only shared words are "hypercare" and "managed support", both methodology terms. (See item 7 T2 for a separate opener issue in this sentence. The replacement wording there keeps the new structure.) |
| O8 | Closing row 1 | "A discovery call on your product lines, channels and current systems." | "First, we talk through your job types, contracts, crews and today's systems." | **Resolved.** The noun phrase becomes a first-person clause. The remaining overlap is the generic "your [list] and current/today's systems" object. Loop 1's suggested fix kept that too, and it describes a standard discovery step. |
| O9 | Closing row 3 | "A written proposal covering scope, timeline and investment." | "Scope, phases, timeline and cost, in writing for your sign-off." | **Resolved.** The order is inverted: the list comes first, "A written proposal covering" is gone, and it ends on the sign-off. |

**New or changed sentences outside the 9.** I checked each against the template:
- Block 2 lede
- Block 3 lede
- Benefits tiles 5 and 6
- Proof lede and tile 4
- FAQ A2 and A3

None follows a template sentence. The Block 3 lede shares only the product term "Time-Aware Customer Data Platform" with the template's platform lede ("built as one Time-Aware Customer Data Platform where marketing, sales and service run on a single record"), and the rest of the sentence is different.

The loop-1 borderline items (Services 01 blueprint, Services 07 Power BI, "role-based training", and the brief-prescribed H2/H3 labels) are unchanged. They remain acceptable under the structural-label and reusable-fact exceptions.

### 5b. Wider web and reference sites

I ran exact-phrase searches on the distinctive new sentences:
- "Gulf maintenance contracts have their own tendering"
- "Each phase launches with hypercare"
- "the assignment work many teams buy technician scheduling software for"
- "Contracts drive field service asset management"
- "Workshops follow a typical job end to end"
- "No part of your project is subcontracted"
- "Whether it runs in the cloud or on your own servers"
- "These industry benchmarks show what leading service organisations achieve"
- "Your build team stays on after launch"

**0 verbatim or near-verbatim matches.** Results were topical pages only (hypercare guides, subcontracting clauses, scheduling-software listicles). The new sentences use no distinctive vocabulary from Ambit, KINAMU, MSI Data, Tokara or the Mobileforce release.

## 6. Stat accuracy: PASS

| Draft stat | Brief ID | Matches source? | Verdict |
|---|---|---|---|
| US$809.8M, MEA FSM 2025, 8.3% a year to 2033 | S1 | Unchanged from v1 (verified in loop 1) | OK |
| US$70.25B, GCC FM 2025, hard services largest | S2 | Unchanged from v1 (verified) | OK |
| 64.88%, outsourced share of UAE FM, 2025 | S3 | Unchanged from v1 (verified) | OK |
| 86%, first-time fix at top performers | P1 | Unchanged from v1 (verified, Aquant Feb 2025) | OK |
| 39%, faster resolution for top performers using AI | P2 | Unchanged from v1 (verified) | OK |
| 28.16%, scheduling and dispatch share of 2025 global FSM revenue | R1 | Re-confirmed this loop. Mordor Intelligence per search: "Scheduling-dispatch and route-optimization software captured 28.16% of 2025 revenue". **Source 5 now names the full category** ("solution segment: scheduling, dispatch and route optimisation, 28.16% of 2025 revenue"). The on-page label is unchanged. Loop-1 Fix 6b is done. | OK |
| 100%, share of the UAE's 21.9 million mobile connections classed as broadband (3G, 4G or 5G) in early 2025 | R2 | Re-confirmed this loop: "21.9 million cellular mobile connections in the United Arab Emirates at the beginning of 2025" and "100% of mobile connections are broadband (3G, 4G, or 5G)". **The clause "so technicians can stay connected on site" is gone.** See below. | OK |

**Proof tile 4 in detail.** The description is now "Share of the UAE's 21.9 million mobile connections classed as broadband (3G, 4G or 5G) in early 2025."
- "Classed as broadband" matches DataReportal's "can now be considered 'broadband'".
- "Early 2025" matches "beginning of 2025".
- The description no longer implies anything about mobile data use, technician behaviour or signal on site, which is the inference DataReportal warns against ("should not be considered a proxy for mobile internet use").
- The label "UAE mobile connections run on broadband." is the Content Writer's and is unchanged. It is a fair plain-English reading of "100% of connections are 3G/4G/5G".
- The proof lede now calls this "market data on ... UAE mobile networks", which is accurate.
- It doesn't overstate the source.

**Other checks:**
- **No invented stats.** No new figures were added.
- **Footnotes [1]-[6] map correctly.** No source is named on-page.
- **No duplication across the project.** A repo-wide search for 809.8, 70.25, 64.88, 28.16 and "21.9 million" finds them only in this requirement's brief, drafts and test report.
- **No Salesforce figures on the page.**

**Advisories A1/A2 carried over (not failures):**
- **A1:** Aquant 2026 benchmark edition exists.
- **A2:** DataReportal Digital 2026 UAE shows 23.0 million connections, still 100% broadband.

Build correctly listed both as Content Writer decisions (Flag 4) and changed no copy.

## 7. Human tone / AI-detection heuristics: FAIL (minor)

**Stock phrase check:** I searched for unlock, seamless, revolutionise, unleash, leverage, empower, robust, streamline, cutting-edge, game-changer, "in today's", elevate, harness, transform, effortless, world-class, "in conclusion", supercharge, delve, synergy, holistic, journey and landscape. **0 matches.** "Tailored" appears once (Block 2 lede). It's a mild marketing word but not a stock AI phrase, and it's fine.

**Loop-1 tone fixes: all four resolved.**

| Loop-1 item | v2 | Verdict |
|---|---|---|
| T1 Benefits tile 5 | "Rules allocate jobs by skill, zone, priority and SLA: the assignment work many teams buy technician scheduling software for. Administrators edit approval rules without code." | Resolved. The keyword sits naturally mid-sentence, "configured SugarAI works as" is gone, and there is no route optimisation claim. |
| T2 Benefits tile 6 | "Contracts drive field service asset management: preventive maintenance is scheduled from them, warranty and AMC renewals surface early, and repeat faults are traced per asset." | Resolved. It opens on a subject and verb, not a bare keyword fragment. |
| T3 FAQ A1-A3 openers | A1 "Through integration." / A2 "Technicians work from their phone: ..." / A3 "Each customer's contract entitlements define..." | Resolved as to the loop-1 problem: the three answers no longer share the clipped two-word opener. But the A3 rewrite creates a new cluster (T1 below). |
| T4 Proof lede | "These industry benchmarks show what leading service organisations achieve, alongside market data on software spending and UAE mobile networks. Our projects are designed around them." | Resolved. It reads as a natural lead-in, not a disclaimer, and it still frames the tiles as industry benchmarks and market data, not SugarAI or HLB HAMT results. |

**New issues introduced by the v2 edits.** All are small, and each fix below is a one-sentence change with no change to the word count.

| # | Location | Current | Problem | Suggested rewrite |
|---|---|---|---|---|
| T1 | FAQ A3 → A4 | A3: "**Each** customer's contract entitlements define the response and resolution targets. **Every** work order runs its own SLA clock..." A4: "Yes. **Each** subcontractor has a record..." | The rewritten A3 opens on "Each", its second sentence opens on "Every", and the next answer's first full sentence opens on "Each" again. That is three determiner-led openers in a row, in the block where loop 1 asked specifically for opener variety. | A3: "Response and resolution targets come from the customer's contract entitlements. Every work order runs its own SLA clock, with alerts before a breach and attainment reported per contract." (same word count) |
| T2 | Process, lede → step 6 | Lede: "**Each** stage ends with your sign-off." Step 6: "**Each** phase launches with hypercare; an SLA then governs managed support." | The rewritten step 6 repeats the lede's "Each [stage/phase] [verb]s with..." opener in the same section. With it, the page has 8 sentences opening "Each" (v1 had 6), and two of those clusters are new. | Step 6: "Hypercare covers each launch phase; an SLA then governs managed support." (11 words, same count; still structurally distinct from the template's "Phased go-live with hypercare, then managed support under SLA") |
| T3 | Block 2, 3 and 4 ledes | B2: "**Tailored by HLB HAMT**, SugarAI works as field service CRM software..." B3: "HLB HAMT delivers SugarAI for Field Service Management by configuring core SugarAI, with no bolt-on product." B4: "With SugarAI for Field Service Management **configured by HLB HAMT**, these six capabilities..." | After the Section 10.1 framing fix, three consecutive section ledes deliver the same "HLB HAMT configures SugarAI" message, two of them with the same opening "[configured/tailored] by HLB HAMT" phrase. Read in sequence it sounds boilerplate. Block 3 now states the framing clearly, so Block 4 doesn't need to repeat it. | B4 lede: "In SugarAI for Field Service Management, these six capabilities carry each job from the first request to the customer's sign-off." (20 words, same as now; keeps primary keyword instance 4) |

**Optional, not required:**
- **Proof H2 and lede echo each other.** The H2 "What well-run field service operations **achieve**" sits directly above the lede "...show what leading service organisations **achieve**". If you want to avoid the repeat: "These industry benchmarks come from top-performing service organisations, alongside market data on software spending and UAE mobile networks. Our projects are designed around them." (-1 word)
- **Benefits tiles 3 and 4 both open "Each...".** This is unchanged from v1 and was accepted in loop 1. Leave it unless you are editing those tiles anyway.

## 8. Section structure: PASS

I rechecked v2 block by block against `hlbhamt-sugarai-insurance.html`. Nothing structural changed from v1.

- **Order:** hero + side panel → stats band → platform → benefits → CTA 1 → services → proof → CTA 2 → segments → market → process + callout → why HLB HAMT → FAQ → closing CTA.
- **Counts:** 3 side rows, 3 stats, 4 platform cards, 6 benefit tiles, 8 services (4 + 4), 4 proof tiles, 6 segments, 6 market items, 6 process steps + callout, 4 why tiles, 7 FAQs (first open), 3 next-step rows.
- **Heading levels and template details:**
  - Heading levels are unchanged.
  - Block 12 has no lede.
  - Block 8 has no body line.
  - Block 14's H2 is identical to Block 8's.
  - Eyebrows, buttons, the `/contact/` closing link and nav anchors match the template.
  - Every H2 matches the brief's "use as written" text, and none repeats an Insurance H2.
- **Note for Deliver (carried over):**
  - **Proof tiles:** tiles 3 and 4 are 19 and 24 words, against 7 and 7 for tiles 1 and 2. Use a `<strong>` lead-in and a smaller second line to balance the row.
  - **Draft-only sections:** strip "Changes from v1", "Stats used" and "Flags" from the page.
  - **FAQPage JSON-LD:** rebuild it from the final visible answers, since A2 and A3 changed.

## 9. Brief and requirement accuracy (no transcript): PASS

- **Section 10.1 framing, now fixed:**
  - **Block 3 lede:** "HLB HAMT delivers SugarAI for Field Service Management by configuring core SugarAI, with no bolt-on product. The Time-Aware Customer Data Platform beneath all [SugarAI CRM solutions](https://sugarai.com/) keeps every site and asset history in sequence."
    - It now presents the offering as core SugarAI configured by HLB HAMT, not as a vendor product line.
    - The sugarai.com anchor now points to the platform family underneath it, not to a catalogue this page belongs to.
    - "No bolt-on product" matches the Content Writer's "not a separate third-party FSM add-on".
  - **Block 2 lede:** "Tailored by HLB HAMT, SugarAI works as field service CRM software..." The definite-article "SugarAI is *the* field service CRM software" that implied an out-of-the-box FSM suite is gone.
- **Section 10.1 capability guardrail:**
  - A search for route, routing, GPS, offline, IoT, augmented, AR, drag, real-time, live tracking, remote monitoring, dispatch board, "predicts failure" and "out of the box" finds **0 matches in page copy**.
  - The only "route optimisation" mentions are in the Source 5 footnote, the Stats-used table and the Flags, which is where Fix 6b put them. None is on-page.
  - Benefits tile 5 describes rule-based allocation only.
  - The Why card 4 claim that the build team stays on for support agrees with Why card 3 and with the template's "one accountable team" fact. It is not a new capability claim.
- **Section 10.2:** the breadcrumb parent link and the Block 3 anchor both point to https://sugarai.com/.
- **Section 10.3:**
  - Salesforce figures are removed, and R1 and R2 are used.
  - The tile 3 label and description are verbatim.
  - The tile 4 label is verbatim. The tile 4 description is deliberately changed and needs the Content Writer's sign-off (decision item D1 below). This is a sign-off question, not a failure, because the change makes the copy match the source more accurately.
- **Section 10.4:** "26 years" appears once (Why card 1). "More than 25 years" appears nowhere.
- **Hero:** positive, stat-free, and the brief's sentence-2 facts are all present (HLB HAMT, service businesses, UAE and GCC, cloud or on-premise).
- **No competitor or data-source names in page copy.** Salesforce, Ambit, KINAMU, Mobileforce, MSI, Tokara, Aquant, Mordor, Grand View and DataReportal appear only in the footnotes, Stats-used table, Changes section and Flags.
- **Other brief requirements:**
  - The callout gives no day count.
  - FAQs carry no stats.
  - FAQ 7 carries the April 2026 rebrand fact.
  - Internal links 1, 2 and 4 are present.

---

## Content Writer decision items (separate from the pass/fail verdict)

**D1. Proof tile 4 description: needs your sign-off.** Section 10.3 prescribed:
> "of the UAE's 21.9 million mobile connections are 3G, 4G or 5G, so technicians stay connected on site."

v2 uses:
> "Share of the UAE's 21.9 million mobile connections classed as broadband (3G, 4G or 5G) in early 2025." [6]

- **Why it changed:** DataReportal says its broadband share "should not be considered a proxy for mobile internet use". "So technicians stay connected on site" treats it as exactly that proxy, and it also implies signal at any given job site, which the source doesn't cover. The v2 wording states only what the source reports. I checked it this loop, and it doesn't overstate.
- **Your label is unchanged:** "UAE mobile connections run on broadband."
- **Options:**
  - (a) **Approve the v2 wording as is.** Test recommends this.
  - (b) **Restore your original clause.** Test advises against it. If you do, item 6 will fail on stat accuracy for the reason above.
  - (c) **Supply a shorter alternative closer to your 6-12 word spec.** For example: "Share of the UAE's 21.9 million mobile connections on 3G, 4G or 5G, early 2025." (15 words; the current text and your original are both 18).
  - Changing the proof lede isn't necessary whichever option you choose.

**D2. Source freshness (carried over, advisory).**
- **Aquant:** published a 2026 benchmark on 19 Feb 2026. Search snippets give conflicting top-performer first-time fix figures for it (88% vs 92%), so someone needs to click through before P1/P2 are changed.
- **DataReportal Digital 2026 UAE:** reports 23.0 million connections, still 100% broadband. A reader who clicks today may land on the newer figure.
- **What to decide:** whether to refresh tile 4 (and Source 6) and P1/P2, or keep the 2025 values. Both 2025 figures are inside the 2-3 year window, so either choice passes item 6.

**D3. Click-verification** of every source URL and internal link is still an outstanding manual step before publication (Section 10.5).

---

## Overall: FAIL (loop 2 of 3)

Items 1, 2, 3, 4, 5, 6, 8 and 9 pass. **Item 7 fails on three repeated sentence patterns introduced by the v2 edits**; everything loop 1 flagged has been fixed. All nine originality findings are resolved, proof tile 4 no longer overstates DataReportal, the Section 10.1 framing is fixed, and the Source 5 footnote names the full category.

If Build applies the three edits below exactly and changes nothing else, I expect loop 3 to pass on every item.

## Fix instructions (for the Build agent, draft-v3)

Change only these three sentences. All three are word-count neutral, so the total stays at 1,676 (1,691 with tags and figures). The keyword total stays at 15, with the primary keyword still in the Block 4 lede. Leave everything else in v2 exactly as it is, including proof tile 4. Tile 4 waits on the Content Writer's D1 decision, not on Build.

**Fix 7 (tone: repeated openers and repeated framing).**

- **T1, Block 13, FAQ A3.** This breaks up the three "Each / Every / Each" openers in a row across A3 and A4.
  - Replace: "Each customer's contract entitlements define the response and resolution targets. Every work order runs its own SLA clock, with alerts before a breach and attainment reported per contract."
  - With: "Response and resolution targets come from the customer's contract entitlements. Every work order runs its own SLA clock, with alerts before a breach and attainment reported per contract."
- **T2, Block 11, Step 6 (Go-live and support).** This removes the second "Each..." opener in the Process block, which clashes with the lede's "Each stage ends with your sign-off." Keep the hypercare-as-subject structure; do not revert to anything shaped like "Phased go-live with hypercare, then...".
  - Replace: "Each phase launches with hypercare; an SLA then governs managed support."
  - With: "Hypercare covers each launch phase; an SLA then governs managed support."
- **T3, Block 4 lede.** Block 3 now carries the "configured by HLB HAMT" framing, so Block 4 no longer needs to repeat it straight after Block 2's "Tailored by HLB HAMT, ...". Primary keyword instance 4 is kept.
  - Replace: "With SugarAI for Field Service Management configured by HLB HAMT, these six capabilities carry each job from request to sign-off."
  - With: "In SugarAI for Field Service Management, these six capabilities carry each job from the first request to the customer's sign-off."

**Also update:**
- **Flag 1:** correct the Benefits figure to 191. With that change the per-block counts add up to the 1,676 total.
- **Optional:** apply item 4 notes 1-3 (Why card 4 "The team that built your system...", A2 "captures", closing row 1 without "First,") and the item 7 optional proof-lede rewrite. Keep the total at or below 1,680 (on-page rule), and at or below 1,700 with tags and figures. Note 1 adds 3 words, so pair it with note 3 (-1) and the proof lede (-1), or skip it.
