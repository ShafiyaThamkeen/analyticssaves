# Revision 4 — urgent correction (2026-09-29)

While planning the Data Visualization sibling requirement, Plan found that Softcrylic's own
Data Visualization page independently documents both the **33x** stat and the **PowerUP!**
offer currently on this delivered page, as Softcrylic's own material — not HLB HAMT's.

**Independently verified via two separate WebSearch queries against softcrylic.com's own
published page content** (the page itself is JS-rendered and returns a bot-check redirect to
automated fetches, same as hlbhamt.com, so this is confirmed via consistent, specific search
extracts rather than a direct page read — someone should still eyeball the live Softcrylic page
in a browser before this is treated as settled):

1. **33x**: Softcrylic's page states *"a real-world engagement documented 33x improvement in
   report load times and interactive performance... optimization work occurs at the pipeline,
   data model, and semantic layers"* — presented as **Softcrylic's own** engagement result. This
   page currently states *"33x faster report load times in one recent HLB HAMT engagement"*
   with the same "pipeline, data model, and semantic layers" framing (S2 item 2, footnote [2]).
   The match is specific enough (identical technical framing, not just a similar number) that
   this cannot be coincidence.

2. **PowerUP!**: Softcrylic's page describes its own *"Microsoft Power BI PowerUP offer... $4,500
   fixed-price accelerator... Custom Power BI Visual Dashboard Proof of Concept in 5 Days"* with
   deliverables *"Requirements Workshop, Data Transformation Scripts, Data Model Diagram, Data
   Dictionary, Completed Reports, and Published App."* This page's S10 featured card has the
   **same name pattern, same $4,500 price, and the same 6 deliverables**, with only the
   turnaround time differing (7 days here vs. Softcrylic's 5).

**Conclusion:** Bala's original prepared content (which this page's S2 item 2 and S10 featured
card were built from) appears to have been adapted from Softcrylic's own marketing material,
not from genuine HLB HAMT results or a genuine HLB HAMT-created offer. Continuing to present
these as HLB HAMT's own achievement and HLB HAMT's own accelerator package is both a stat-
accuracy problem (misattributed/fabricated result) and a commercial-risk problem (reproducing a
named competitor offer's exact price and deliverable list).

**Content Writer's decision: pull both immediately.** Remove the 33x stat and the PowerUP!
offer entirely from this page — do not hold for confirmation, do not wait to check with HLB
HAMT first. This is urgent because the page is already delivered (and the S2 item 2 / S10
featured-card content may already be live).

## What must be removed and how to handle the resulting gaps

1. **S2 stats strip, item 2 (33x)**: remove entirely. The strip drops to 3 items (200+, Since
   1999, Arabic and English). **Do not force in a low-effort replacement stat under time
   pressure** — a 3-item strip is a fine, honest structure. If a genuinely verified, HLB HAMT-
   specific Power BI stat surfaces later, it can be added in a future revision.
2. **S10 featured card (PowerUP!)**: remove entirely, including its badge, price line, terms,
   and deliverables list. S10 becomes just the 4-tab engagement matrix (Explore / Implement /
   Extend / Support) with no featured offer, the same structure the Advanced Analytics sibling
   page already uses (it also has no featured offer card, for the same reason: no verified real
   HLB HAMT offer to feature). Adjust S10's intro line so it doesn't reference "start with the
   fixed-price PowerUP!" as an option.
3. **Hero button "See the PowerUP! offer" → `#packages`**: replace with a different secondary
   CTA that doesn't reference PowerUP!, e.g. "See our engagement models" → `#packages` (still
   points to the same section, just without naming the removed offer).
4. **S11 (Why UAE businesses choose HLB HAMT) tile 3**: currently reads "Begin with the fixed-
   price PowerUP! or a working dashboard on your data, then scale once it proves itself." Reword
   to remove the PowerUP! reference, e.g. "Begin with a working dashboard on your own data, then
   scale once it proves itself." (or similar, keeping the same low-risk-start idea without the
   removed offer).
5. **Any other PowerUP!/33x mentions**: search the whole page (search "PowerUP" and "33x"
   case-insensitively) and remove/reword every instance, including button labels like "Enquire
   about PowerUP!" and any FAQ or footnote references.
6. **Footnote renumbering**: footnote [2] (33x) is removed; Deliver renumbers the rest by
   appearance as usual.
7. **Word count**: removing S2 item 2's description (~15 words) and the entire S10 featured card
   (~130-140 words) will drop the page below its original 3,100-3,500 target range. **This is
   expected and acceptable** — do not pad back to the old word count with filler. Report the new
   total; if it falls meaningfully short of a reasonable homepage length, that's a known,
   accepted consequence of removing misattributed content, not a defect to paper over.

## What stays unchanged

Everything else: the 7-day proof-of-concept commitment (S9, a separate claim independently
corroborated across multiple live HLB HAMT pages, not tied to the specific Softcrylic PowerUP
structure), the "Power BI reselling partner" framing, the rest of S10's tabs, all other stats
and sections. This is a targeted removal, not a broader content rewrite.

## Downstream effects (for awareness, not required to fix now)

- The Data Visualization sibling requirement's brief already avoided reusing 33x/PowerUP!
  (Plan caught the same issue independently while researching that page), so no cross-page fix
  is needed there.
- Both sibling pages (Advanced Analytics, and the forthcoming Data Visualization page) link to
  this Power BI page; those links are unaffected by this content change (same URL, same general
  topic), no link updates required.
