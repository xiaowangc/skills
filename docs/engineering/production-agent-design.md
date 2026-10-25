## What it does

`production-agent-design` turns a business goal into a design for an [agent](https://www.aihero.dev/ai-coding-dictionary/agent) system that can be evaluated, governed and operated in production. It covers the task contract, system boundary, autonomy level, tool permissions, context and memory, security controls, evaluation, observability, release gates and AgentOps.

It starts from the minimum sufficient system. Deterministic code and workflows own permissions, validation, calculations, state transitions, approvals, idempotency, retries and compensation unless model judgment is genuinely required. It does not add autonomy, memory, multiple agents or open tool protocols merely because they are available.

## When to reach for it

Type `/production-agent-design`, or the agent reaches for it automatically when a task fits.

Reach for it when you are designing a new business agent, reviewing an existing agent architecture, deciding between one and many agents, or checking whether a demo is ready for production. Pick the neighbouring skill when the problem is narrower:

| The problem | The skill |
|---|---|
| Production architecture, autonomy, permissions, evaluation and operations | `production-agent-design` |
| The interface, seam and depth of one software module | [codebase-design](https://aihero.dev/skills-codebase-design) |
| The vocabulary and concepts of the business domain | [domain-modeling](https://aihero.dev/skills-domain-modeling) |
| Evidence from current frameworks, protocols or vendor documentation | [research](https://aihero.dev/skills-research) |

## The minimum sufficient system

The skill first asks whether the task needs language understanding, open analysis, dynamic planning or judgment under incomplete information. If ordinary software or a fixed workflow can do the job with less risk, that is the recommendation. If only one step needs judgment, the result is a deterministic skeleton with a model decision node, not an agent wrapped around the whole process.

The same rule controls autonomy. Start with a single model call, then add bounded tools, dynamic planning, multiple agents or controlled self-improvement only when the business boundary, permissions, context isolation or independent evaluation justify the added complexity.

## Production-ready means provable

The design is not production-ready until it has measurable success criteria, a risk owner, versioned contracts, deterministic authorization for write actions, traceable execution, realistic evaluation data, budgets and termination conditions, plus a rollout and rollback path. Missing gates stay visible as explicit conditions rather than being buried in implementation notes.

High-risk actions follow a concrete chain: proposal, policy check, human approval, execution, verification and audit. Production failures become permanent regression cases, so operations feed the next evaluation and release cycle.

## Common questions

**Does every AI feature need an agent?**

No. If fixed rules, search, a normal service or a workflow can complete the task with lower risk, use that. The skill is deliberately willing to recommend a non-agent design.

**When is a multi-agent design justified?**

When roles need independently enforceable boundaries, permissions, context or evaluation. A process having many steps is not enough. If the roles cannot be authorized and measured separately, keep one agent and use deterministic orchestration around it.

**Does this skill choose a framework or cloud product?**

No. It is framework-neutral. A product can appear as a replaceable implementation example, but the decision stays anchored to business constraints, contracts, risks and verification.

**Will it implement the agent?**

Not by itself. It produces implementation-ready decisions, contracts, controls, gates and a phased route. Use the normal build flow after the design is settled.

## It's working if

- The design says which decisions require model judgment and which remain deterministic.
- Every write-capable tool has an authorization subject, side-effect model, approval rule, error contract and audit trail.
- Success, partial success, failure and refusal are measurable against versioned evaluation data.
- A trace can reconstruct the model, tools, state and delegation path for a production run.
- The release plan has budgets, timeouts, termination conditions, graceful degradation, rollout and rollback.
- Missing production gates are labelled as blockers instead of being treated as future cleanup.

## Where it fits

`production-agent-design` is a **reach-for-it-anytime standalone** for AI system architecture and production readiness. Its closest neighbour is [codebase-design](https://aihero.dev/skills-codebase-design), which shapes software modules rather than the end-to-end agent system. [research](https://aihero.dev/skills-research) supplies current primary-source evidence when a framework, protocol or vendor capability affects the choice. When you are unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
