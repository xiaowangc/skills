# Fresh-context reader testing

Use this test to find gaps that authors miss because they remember the conversation behind the document.

## Prepare the test

Write three to five questions or tasks that a real reader would bring to the document. Cover the document's intended outcome, its core decision or recommendation, one important constraint, and any action the reader must take.

Use one fresh subagent for the full test when independent agents are available. Give it only:

- the document;
- the reader role, if the role changes how the document should be interpreted; and
- the questions or tasks.

Do not provide the author conversation, intended answers, suspected gaps, or a summary of what the document is supposed to say. Those would let the evaluator reconstruct missing context instead of testing the artifact.

If a fresh subagent is unavailable, give the user a compact test pack to run in a separate session with the same inputs.

## Evaluate the result

For each question or task, record:

- whether the reader reached the correct conclusion or action;
- which passage supports the answer;
- what was ambiguous, missing, contradictory, or assumed;
- whether the reader was forced to guess; and
- what additional question the document caused.

Also ask the reader to identify internal contradictions, undefined terms, unsupported claims, and knowledge the document assumes without supplying or pointing to it.

## Repair and stop

Revise the smallest section that owns each failure. Retest the failed questions and any question whose answer changed as a result.

Stop after one clean pass. If the same material gap survives two repair rounds, report the unresolved gap and the decision or evidence needed from the user instead of rewording it indefinitely.
