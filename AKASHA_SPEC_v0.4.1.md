AKASHA v0.4.1 — CANONICAL SPEC (DELTA)

FOCUS OF THIS BUILD
• Boundary enforcement against agency drift
• Explicit semantic atom definition
• Human intent preservation across translation layers

NON-GOALS
• No autonomy
• No goal optimization
• No execution capability

--------------------------------
1. MEMORY NODE (SEMANTIC ATOM)
--------------------------------

A memory node MUST:
• Encode a single proposition or relationship
• Include origin (human / model / system)
• Include epoch of introduction
• Include intent scope (descriptive only)

A node MUST NOT:
• Contain imperatives
• Encode goals
• Imply preference

--------------------------------
2. REINFORCEMENT (CLARIFIED)
--------------------------------

Reinforcement:
• Adjusts recall probability only
• Never implies preference, value, or choice
• Is reversible via attenuation

Language constraint:
Allowed: "likelihood", "weight", "path strength"
Disallowed: "decision", "selection", "optimization"

--------------------------------
3. IDENTITY (DERIVED ONLY)
--------------------------------

Identity is:
• A read-only projection
• Recomputed on demand
• Never cached as authority

Identity summaries are non-normative.
They describe history, not intent.

--------------------------------
4. WITNESS TRACE
--------------------------------

Trace is append-only.
Trace entries are immutable.
Trace describes WHAT occurred, never WHY it should occur.

--------------------------------
5. TRANSLATION SAFETY
--------------------------------

At every boundary:
• Clarification is allowed
• Amplification is forbidden
• Completion of intent is forbidden

If ambiguity exists:
→ Defer to human re-introduction

--------------------------------
6. AGENCY FIREWALL
--------------------------------

Akasha must never be described using verbs implying action.
Forbidden metaphors include:
• wants
• decides
• chooses
• optimizes

If such language is required, the design has failed.

END SPEC
