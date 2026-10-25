---
name: doc-coauthoring
description: Co-author substantial human-facing documents such as proposals, RFCs, decision records, PRDs, and technical designs when the content or structure still needs to be discovered with the user. Use to gather missing context, draft collaboratively, and test whether the document works for a fresh reader. For an already-settled issue-tracker spec use to-spec; for agent instructions use writing-for-agents; use a document-artifact tool for DOCX layout.
---

# Document co-authoring

Turn incomplete knowledge into a document that works without the conversation that produced it. Match the amount of ceremony to the uncertainty: take the fast path when the user has already supplied a complete brief, and guide the work in stages only where decisions or context are missing.

## Choose the lane

- **Collaborative lane:** use when the purpose, audience, structure, evidence, or core decision is still unsettled. Gather and close those gaps before drafting them as facts.
- **Fast lane:** use when the user has supplied complete source material or asks for a straightforward rewrite. Confirm the audience and desired effect, draft the whole document, then surface only consequential gaps.

Do not reopen settled decisions merely to run the workflow. Preserve the user's template, requested format, location, voice, and approval boundaries.

## 1. Establish the brief

Determine what is not already known about:

- document type and primary audience;
- what the reader should understand, decide, approve, or do;
- required template, format, location, length, tone, and deadline;
- source material, established facts, open decisions, and sensitive constraints.

Read provided files and connected sources that are already authorized. Let the user provide context in shorthand or as an unstructured dump. Ask a compact batch of questions only for gaps that would materially change the document; ask follow-ups when an answer exposes a new decision.

The brief is sufficient when you can state the audience, desired reader outcome, controlling facts, unresolved questions, and constraints without guessing.

## 2. Build the document

Propose a structure suited to the document and its audience. Start with the section carrying the most uncertainty or the core decision; write summaries after the substance is stable.

Create or update one source-of-truth artifact in the user's requested format and location. If none is specified, use a clearly named Markdown file in the workspace. Edit that artifact incrementally instead of reposting the entire document in chat.

For each genuinely uncertain section:

1. Ask targeted questions about the section's purpose and missing evidence.
2. Offer a small set of materially different content or framing options when a choice exists.
3. Capture what the user keeps, removes, combines, or reframes.
4. Draft the section and make surgical revisions from feedback.

Skip these steps for sections that are already determined. Near completion, reread the full artifact for narrative flow, duplicated claims, contradictions, unsupported assertions, missing transitions, and generic filler. Distinguish facts, assumptions, decisions, recommendations, and unresolved questions.

## 3. Test the reader

For a substantial, long-lived, high-impact, or explicitly reviewed document, read [references/reader-testing.md](references/reader-testing.md) and run a fresh-context reader test. For a low-risk short document, offer the test only when ambiguity remains or the user requests it.

Reader testing checks whether the artifact stands alone. It does not replace factual verification, domain review, compliance approval, or the user's final read.

## Completion

Finish when:

- the document produces the intended reader understanding, decision, or action;
- consequential claims are supported or clearly marked as assumptions;
- unresolved decisions and ownership are visible;
- the artifact has no known contradiction or unexplained dependency;
- any required reader test passes; and
- the user has reviewed the final artifact or explicitly delegated that review.

## Boundaries

- Use `to-spec` when the conversation is already settled and the job is to synthesize an issue-tracker specification without another interview.
- Use `writing-for-agents` when the reader is an agent and the task is to shape instructions, context pointers, or completion criteria.
- After content stabilizes, use the environment's document-artifact tool when the deliverable requires DOCX creation, tracked changes, comments, or visual layout verification.
