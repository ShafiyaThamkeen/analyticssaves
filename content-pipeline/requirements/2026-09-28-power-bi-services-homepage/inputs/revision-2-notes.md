# Revision 2 — Content Writer feedback (2026-09-29)

The Content Writer reviewed the delivered v1 (draft-v4.md / output/power-bi-services-homepage.*)
and asked for a content-quality revision, not a structural rebuild. Re-plan against the same
structural sample (`inputs/structural-sample/sugarai-crm-hlbhamt-homepage.html`) and the same
17-section (S0-S17) mapping already recorded in brief.md, but with a materially deeper and more
accurate source base and two explicit content changes.

## What's wrong with v1

The Content Writer judged the content "not up to the mark" — under-sourced relative to what HLB
HAMT already has, and too generic/Microsoft-led in places rather than being clearly HLB HAMT's
own Power BI service offering.

## New sources to fold in (in addition to the original content-source and structural-sample)

`inputs/hlbhamt-sibling-pages/` — 4 real, live HLB HAMT pages (uploaded as HTML since
hlbhamt.com blocks automated fetching with a bot-check; use the `*-extracted.txt` plain-text
versions, skip the shared nav/footer chrome at the top/bottom of each):
- `power-bi-partner-in-dubai-uae-extracted.txt` — https://hlbhamt.com/services/power-bi-partner-in-dubai-uae/
- `microsoft-power-bi-consulting-in-dubai-uae-extracted.txt` — https://hlbhamt.com/services/microsoft-power-bi-consulting-in-dubai-uae/
- `data-visualization-uae-extracted.txt` — https://hlbhamt.com/services/data-visualization-uae/
- `power-bi-dashboard-development-extracted.txt` — https://hlbhamt.com/services/power-bi-dashboard-development/

These are existing HLB HAMT pages covering overlapping/adjacent ground (Power BI partner
positioning, Power BI consulting, data visualization, dashboard development). Treat them as
real, authoritative, already-published HLB HAMT copy — genuine service detail, credentials,
and positioning language can be drawn from them directly (not just as inspiration).

`inputs/competitor-content/` — real page text pulled directly from 4 of the 5 competitor URLs
already named in the original brief (zenzero, ranosys, dsp, bcn — yesdynamic.com couldn't be
fetched, JS bot-check). As before: positioning/structure/gap-analysis only, nothing may be
copied or paraphrased closely — use these to spot what competitors cover that HLB HAMT's own
sources don't, and to sanity-check depth/credibility bar.

## Sourcing priority for this revision

1. **Primary**: Bala's Power BI tab content (`inputs/content-source/`) — this remains the core
   spine of the page's content and structure.
2. **Secondary**: the 4 real HLB HAMT sibling pages above — pull in genuine service detail,
   proof points, and positioning that Bala's draft doesn't cover, and use them to sharpen
   HLB HAMT-specific claims (see branding note below).
3. **Tertiary**: competitor content — gap-filling and positioning only, never copied language.

Re-verify stats against these new sources; if a sibling page states a number Bala's draft
doesn't have (or states it differently), reconcile and footnote accordingly. Don't drop any
previously-verified stat without a reason.

## Content change 1: remove the AI Insights section

Drop S5 "AI Insights" (Answers/Explains/Alerts numbered-dash block) from the page entirely.
Renumber subsequent sections accordingly in the rebuilt brief/draft.

## Content change 2: HLB HAMT branding, not Microsoft's

The Content Writer's instruction: *"I want the content to have nice HLB HAMT branding not
microsoft. HLB HAMT providing Power BI service."*

Concretely: frame the page throughout as HLB HAMT's own Power BI service — HLB HAMT is the
provider, Power BI is the platform/technology it delivers on top of, not the other way round.
Audit the current draft and brief for places where Microsoft or "Power BI" reads as the actor/
subject of a sentence and HLB HAMT as an afterthought (e.g. hero framing, the "Why Power BI"
section, platform/capability descriptions) and rewrite so HLB HAMT's delivery, expertise, and
service are the lead, with Power BI named as the technology. This does not mean removing
legitimate Power BI/Microsoft facts (e.g. the Gartner Magic Quadrant recognition, connector
counts) — those stay, correctly attributed — but the page's voice and structure should read as
"HLB HAMT delivers/builds/supports Power BI for you," not as a Power BI product page HLB HAMT
happens to appear on. This should show up in section framing choices, hero copy, and section
intros throughout, not just a single section.

## What stays the same

- Structural sample and 17-section (now 16-section, after dropping AI Insights) mapping.
- Keyword plan (primary/secondary keywords, singular/plural handling).
- Word count scale (homepage-appropriate, not subpage-length).
- All previously-approved Content Writer decisions from brief.md Section 10, except where this
  note explicitly supersedes them (AI Insights removal, HLB HAMT-led branding).
