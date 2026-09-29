# Competitor methodology/engagement/support research (2026-09-29)

Follow-up to Section 10 point 4's expanded OQ5 instruction. Build's draft-v1 could not do this
research (no web tools available to that agent). Done directly instead, since 4 of 6 competitor
pages are fetchable and the other 2 are blocked (softcrylic.com returns the same sgcaptcha
bot-check redirect as hlbhamt.com; apexon.com resets the TLS connection to this environment) —
WebSearch used as fallback for those two, consistent with this project's established practice.

**Raw fetched text:** `drcsystems.txt`, `ometis.txt`, `protiviti.txt`, `insightconsulting.txt`
(full page text, includes nav/footer chrome — the relevant sections are grepped below).
Apexon and Softcrylic have no raw file; findings are from WebSearch summaries only.

## What each page actually says about methodology, engagement tiers and support

**DRC Systems** ("Our Development Approach", drcsystems.txt lines 491-528) — a clean, named
5-stage methodology: **01 Data Discovery & Strategy** (understand the data landscape, build a
strategy) → **02 Data Preparation** (cleansing, mining, transformation) → **03 Analytics
Development** (build models/solutions) → **04 Deployment** (integrate into client processes) →
**05 Maintenance and Support** ("closely monitor, refine, and optimize your analytics solution
and ensure it keeps adding value"). Also promises "flexible engagement models tailored to you"
(no named tiers) and a fast-response free-consultation hook (24hr response, no-obligation).

**Ometis** (ometis.co.uk/services/data-analytics, lines ~145-291) — frames one of its service
lines as **"Strategy and support"**: aligning data initiatives with business objectives, "best
practice advice, ongoing consultancy and training to build internal capability." Separately, a
dedicated **"Technical Support"** section lists 3 concrete support channels: email, a support
portal, and phone — i.e. real support infrastructure, not just a vague promise. Also offers
instructor-led training so client teams "build confidence" using the tools themselves.

**Protiviti** (protiviti.com, lines ~240-330) — doesn't present a stage-by-stage methodology;
instead frames its advanced-analytics work around **risk-oriented outcomes**: "operational
resilience" (risk identification, mitigation, ongoing monitoring), "data driven decisions"
(prescriptive analytics), "emerging risks development" (trend/trigger analysis), "preventive
not responsive" (detect risk before it becomes an issue). Useful mainly as a reminder that
"ongoing monitoring" is a recurring theme across multiple competitors, not a one-off DRC idea.

**Insight Consulting** (insightconsulting.co.uk, lines ~65-98) — describes an approach that
starts with "a thorough business requirements meeting", selects a technology stack, delivers
"a comprehensive blueprint for the project", then an iterative build, and closes with
**"training, maintenance, and ongoing support for your investment."** Emphasises a
collaborative, partnership framing throughout ("we partner with our clients").

**Apexon** (WebSearch only, page not fetchable) — names its methodology **"The 4 C's": Curate,
Catalog, Context, Consume**. Applies automation "from the start, and at every opportunity."
Frames engagements around bringing business context to "frame the problem worth solving" before
building. No explicit support/maintenance line found in the search summary.

**Softcrylic** (WebSearch only, page not fetchable) — offers **"Managed Services"** as a
distinct support offering: monitoring, running recurring reports, and **"Data Quality
Management... consistent monitoring and fixing"** to keep analytics reliable over time. Frames
its team as "tool-agnostic."

## The pattern across all 6 (safe to build original HLB HAMT content on)

A **discovery/strategy → data preparation → model/solution build → deployment → ongoing
monitoring-and-support** stage sequence is genuinely the common shape across DRC, Insight
Consulting and (implicitly) Softcrylic/Ometis — this validates that Build's independently
drafted 5-stage S9 methodology in draft-v1 (Assess readiness → Engineer the foundation → Build
and validate models → Deliver where decisions happen → Monitor, retrain and refine) already
matches the real, common industry pattern closely. **No rewrite of the stage count/order is
needed** — but S9 stage 5 and the S4 card 4 / S10 Extend "support" framing can now be written
with more specific, credible texture drawn from what DRC, Ometis, Protiviti and Softcrylic
actually offer: **ongoing monitoring, periodic model refinement/retraining, and (per Ometis)
concrete support channels** — without naming any competitor or copying their wording.

**No competitor publishes specific durations, prices, or SLA terms for advanced analytics
work** (Protiviti and Insight Consulting are both fully qualitative; DRC's only quantified claim
is its own 24-hour response promise, which is DRC's, not HLB HAMT's, and must not be borrowed).
This confirms Section 10's instruction to keep HLB HAMT's own methodology/support content
qualitative, with no invented numbers, is the right call, not just a fallback.

## Instruction for the next Build pass

Revise S9 (particularly the framing of stage 5), S4 card 4, and the S10 Extend tab's "Managed
model care" item to draw on this real substance: ongoing monitoring, periodic review/retraining,
and (optionally, inspired by Ometis) naming a concrete support channel or two if it reads
naturally for HLB HAMT (e.g. "a named point of contact" rather than literally "email/portal/
phone", since those specific channels are Ometis's own setup, not confirmed for HLB HAMT). Keep
every sentence original. Do not name any competitor or copy any distinctive phrase ("The 4 C's",
"Curate, Catalog, Context, Consume", "preventive not responsive", "tool-agnostic", etc.).
