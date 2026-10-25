## What it does

`doc-coauthoring` helps you turn incomplete knowledge into a substantial human-facing document: a proposal, RFC, decision record, PRD or technical design. It closes consequential context gaps, develops the structure and content with you, and checks whether the finished artifact works for a reader who was not part of the conversation.

It matches the process to the uncertainty. A complete brief takes the fast lane to a full draft; an unsettled decision gets focused questions and collaborative refinement. It never forces every section through the same interview ceremony.

## When to reach for it

Type `/doc-coauthoring`, or the agent reaches for it automatically when a substantial document still needs discovery, structure or reader validation.

Choose by the job in front of you:

| The job | The skill |
|---|---|
| Develop the substance of a human-facing proposal, RFC, PRD or decision document | `doc-coauthoring` |
| Synthesize an already-settled conversation into an issue-tracker spec | [to-spec](https://aihero.dev/skills-to-spec) |
| Write instructions that an agent will consume | [writing-for-agents](https://aihero.dev/skills-writing-for-agents) |
| Turn stable content into a visually verified Word document | The environment's document-artifact skill or tool |

## The fresh-reader test

The leading idea is **fresh context**. Authors remember the discussion, so they unconsciously supply definitions, evidence and decisions that never reached the page. A fresh [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) receives only the artifact, a reader role when relevant, and a few realistic questions or tasks. If it must guess, the document still depends on the conversation that produced it.

One evaluator handles the whole test. Failed questions are repaired at the smallest owning section and retested; the workflow does not start one evaluator per question or continue rewriting indefinitely.

## Common questions

**Will it interview me even when I already supplied everything?**

No. A complete brief takes the fast lane: confirm the audience and intended effect, draft the document, and surface only gaps that materially change it.

**Does reader testing prove every claim is true?**

No. It proves the document can be understood from its own contents. Factual verification, domain review, compliance approval and your final read remain separate responsibilities.

**Does this replace `to-spec`?**

No. `to-spec` deliberately avoids another interview and synthesizes decisions already made. Use `doc-coauthoring` while the document's substance or structure is still being discovered.

## It's working if

- Questions shrink as the brief improves instead of repeating for every section.
- Facts, assumptions, decisions and unresolved questions are visibly distinct.
- The artifact is edited as one source of truth rather than reprinted in chat after every change.
- A fresh reader reaches the intended conclusion or action without access to the author conversation.
- Reader-test failures produce narrow repairs instead of a wholesale rewrite.

## Where it fits

`doc-coauthoring` is a **reach-for-it-anytime standalone** for developing human-facing documents. It sits before [to-spec](https://aihero.dev/skills-to-spec) when decisions are still open, and beside [writing-for-agents](https://aihero.dev/skills-writing-for-agents), which serves agent readers rather than human readers. When you are unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
