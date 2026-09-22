# HLB HAMT content pipeline

A 4-agent Claude Code pipeline for writing SEO content for the HLB HAMT
website: webpages, blog posts, landing pages, social posts, and case
studies. All four agents run on Opus.

## The agents

| Agent | File | Job |
|---|---|---|
| Plan | `.claude/agents/seo-plan-agent.md` | Analyses inputs, researches competitors and stats, writes `brief.md` |
| Build | `.claude/agents/seo-build-agent.md` | Writes the draft from the approved brief |
| Test | `.claude/agents/seo-test-agent.md` | QAs the draft against the brief and content standards, up to 3 fix loops |
| Deliver | `.claude/agents/seo-deliver-agent.md` | Produces the .docx / .html / .pdf / sources log |

## Running it

Start a new requirement with:

```
/content-pipeline <describe the requirement here>
```

Paste or attach whatever you have for this requirement: content type,
primary/secondary keywords, reference websites, content sources, a call
transcript, the parent webpage, and the required template/output format.
You don't need every input for every requirement; the Plan agent works with
what you give it and flags anything critical that's missing.

The pipeline will:
1. Set up `content-pipeline/requirements/<date>-<slug>/`
2. Run the Plan agent and **pause for your approval of `brief.md`**
3. Run Build -> Test -> (revise up to 3 loops) -> Deliver
4. Give you a summary and the final files in `.../output/`

## Folder layout per requirement

```
content-pipeline/requirements/<date>-<slug>/
  inputs/     everything you provided (transcripts, source notes, template)
  brief.md    the Plan agent's content brief (approve this before Build runs)
  draft/      draft-v1.md, test-report-v1.md, draft-v2.md, ... (Build<->Test history)
  output/     <slug>.docx, <slug>.html, <slug>.pdf, <slug>-sources-log.md
```

## Content standards

These apply to every piece the pipeline produces (encoded into each agent's
prompt):

1. SEO keyword placement per on-page best practice, no stuffing
2. 100% original, never copied or closely paraphrased from any source
3. Correct grammar, punctuation, consistent tone
4. Human-sounding writing, varied sentence structure, no stock AI phrases
5. Zero em dashes, anywhere
6. Word count matched to content type (or proposed in the brief)
7. Stats sourced from credible, recent (2-3 year) sources, with the URL
   logged for every one used

See `examples/quality-bar-notes.md` for lessons distilled from a prior
project, used to calibrate the agents' quality bar.
