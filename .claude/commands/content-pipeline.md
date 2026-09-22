---
description: Start the HLB HAMT SEO content pipeline for a new requirement (Plan -> approval -> Build -> Test -> Deliver)
---

You are running the HLB HAMT content pipeline for a new requirement. The
Content Writer's request, pasted after this command, may include any
combination of: content type, primary/secondary keywords, reference
websites, content sources, a call transcript, the parent webpage, and a
required template/output format. Treat `$ARGUMENTS` as that request.

Follow these steps in order. Do not skip the approval pause.

## 1. Set up the requirement folder

- Derive a short slug from the requirement (e.g. `sugarai-manufacturing-blog`).
- Create `content-pipeline/requirements/<YYYY-MM-DD>-<slug>/inputs/`,
  `draft/`, and `output/`.
- Save every input the Content Writer provided into `inputs/` (paste
  transcripts as `.txt`, save reference URLs and content source notes as
  `.md` files, note the parent page URL and required template/format in an
  `inputs/requirement-notes.md`).
- If the content type, or a template/format, is genuinely unclear from what
  was provided, ask the Content Writer now, before invoking the Plan agent.
  If a transcript or document is mentioned but not attached, ask for it
  rather than proceeding without it. Do not ask about things that aren't
  critical, use sensible defaults and note the assumption in
  `inputs/requirement-notes.md` instead.

## 2. Plan

Invoke the `seo-plan-agent` subagent with this requirement's folder path
and all inputs. It will research, plan, and write
`content-pipeline/requirements/<slug>/brief.md`.

## 3. Pause for approval

Show the Content Writer the full contents of `brief.md`. Explicitly ask
them to approve it, or tell you what to change. **Do not invoke the Build
agent until they approve.** If they ask for changes, re-invoke the Plan
agent with their feedback and show the revised brief again.

## 4. Build

Once approved, invoke the `seo-build-agent` subagent with the approved
`brief.md` and the `inputs/` folder. It writes `draft/draft-v1.md`.

## 5. Test

Invoke the `seo-test-agent` subagent with `brief.md`, `inputs/`, and the
latest draft. It writes `draft/test-report-vN.md`.

- If **PASS**: proceed to step 6.
- If **FAIL** and this is loop 1 or 2: invoke `seo-build-agent` again with
  the test report's fix instructions to produce the next draft version,
  then re-run `seo-test-agent`. Repeat.
- If **FAIL** on loop 3 (`test-report-v3.md`): stop. Report the remaining
  issues to the Content Writer exactly as the Test agent listed them, and
  ask whether to keep iterating, hand off as-is, or address it manually.
  Do not proceed to Deliver without their instruction.

## 6. Deliver

Invoke the `seo-deliver-agent` subagent with the final passed draft. It
produces the `.docx`, `.html`, `.pdf`, and sources log in `output/`, and
gives a handoff summary.

## 7. Wrap up

Relay the Deliver agent's summary to the Content Writer: files produced,
final word count, keywords used, and anything they should review manually.
