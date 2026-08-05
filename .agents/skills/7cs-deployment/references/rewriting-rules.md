# Rewriting Rules — Deployment Canvas → Spec Kit

Rules for **phase 2 (mapping)** of `7cs-deployment`. They are applied **in
order**: the first matching rule decides the post-it's destination. No rule
may add information that isn't on the canvas, and none of them applies
during phase 1 (ingestion), where the COM only copies literal text.

## The methodological decision that governs this canvas

Spec Kit asks for **what** and **why** without fixing the stack in the
specification. The Deployment Canvas talks almost exclusively about
technology, so **the vast majority of its post-its go to `plan.md`, not to
`spec.md`**. Pouring them in earlier contaminates the specification and
forecloses design alternatives.

## Applicable rules

| Rule | Pattern detected | Corpus example | What is emitted |
|---|---|---|---|
| **R6** | Named technology | "Node.js", "Cloud SQL for PostgreSQL", "Docker", "Cloud Run (backend)" | Given technical context in `plan.md` + a limit in `constitution.md` when a Constraint imposes it. **Out of `spec.md`** |
| **R7** | Impossibility or external limit | "Sin soporte offline", "On-premise obligatorio" | Constraint + an explicitly derived compensating requirement, with the cause cited |
| **R-OP** | Observable installation, operation, or support action | "Despliegue automatizado mediante contenedores", "Area de Sistemas" | `NFR-OP-n` in `spec.md`, with its trace and, if detail is missing, a clarification |
| **R-B** | Deployable unit | "Backend: monolito (Node.js)" | Deployment-split entry + reconciliation against the Structural census. **Not a requirement** |

R6 is the dominant rule: it is the default destination for the entire
middle column of the canvas.

### Why R1–R4 don't fire here

| Rule | Why it doesn't apply to the Deployment Canvas |
|---|---|
| **R1** Domain noun → entity | The canvas declares no business objects; its nouns are products, not entities. `Key Entities` is Functional Canvas territory |
| **R2** Action verb + object → FR | The canvas's actions are performed by the operations team, not by the system in response to a user. A functional FR derived from here would be invented |
| **R3** Interface or endpoint name | Interfaces come from the System Context Canvas; `Networks` describes the medium, not the contract |
| **R4** Scheduled task → time-triggered FR | A scheduler ("Cloud Scheduler (Jobs)") is **infrastructure** (R6). The *functional* job that runs on it comes from the Functional Canvas. Merging them is prohibited |
| **R5** Improvement verb without a metric | Doesn't appear on this canvas; if it did, it would be a success criterion + a metric clarification, never an NFR |

## Promotion criterion for `spec.md`

A post-it rises to the specification **only if it describes something
observable by the organization**: installing, operating, supporting,
running on its platforms. Everything else — proxy, containers, hardware,
runtimes — is solution and stays in `plan.md`. **When in doubt, it does not
rise.**

Promotable sections (valid sources for an `NFR-OP-n`):

- `Installation`
- `Operation`
- `Environments`
- `Operating systems`, and only the post-it naming supported
  variants/platforms (preserved as a test criterion)

Any `NFR-OP-n` whose trace comes from another section is a defect.

## Canonical form of the operation NFR

```
NFR-OP-n {subject} DEBE {observable verb} {condition}.
  ← Deployment / {section} "{literal post-it text}"
  [+ {other canvas} "{literal text}"]
  [NEEDS CLARIFICATION: {missing datum}]
```

- The subject is what gets observed: "La instalación", "La operación",
  "El sistema".
- The verbs "gestionar", "manejar" and "soportar" without an object are
  **prohibited**: they are not verifiable.
- The `←` arrow (canvas / section / literal text in double quotes) is
  **mandatory**: it is the trace that makes coverage computable without
  reopening the PDF.

Requirement text is written in the canvas's own language (Spanish in the
current corpus), because it quotes and rewrites literal post-it content.
These rules are documented in English; the artifacts they produce are not
translated.

## Writing forms for `plan.md` and `constitution.md`

- Plan line: `{plan.md destination} · {literal technology}. [DPC/{section}]`
- Constitution limit: `C{n} {limit}. [DPC/Constraints]`
- Deployment-split entry: `{literal bundle} → {literal runtime/orchestrator}. [DPC/Bundles + DPC/{section}]`

## Prohibitions

- **Never invent availability, backup, RPO/RTO, or monitoring targets.**
  If the canvas doesn't declare them, the absence is reported as a finding
  so it gets asked. A number invented here becomes an SLA in
  `/speckit.plan`.
- **Never expand acronyms or product names** when citing them ("GCP" does
  not become "Google's public cloud"; in fact it never reaches `spec.md`).
- **Never merge post-its from different sections.** A runtime and the
  bundle that uses it are two traces. Sole exception: an `NFR-OP-n` that
  leans on an Architectural Context post-it to justify operation
  governance — both traces are cited.
- **Never turn one post-it into two requirements**: if that seems
  necessary, the post-it is ambiguous → emit a clarification.
- **Never classify an empty section without citing the evidence** that
  supports the judgement (usually a `Constraints` post-it). Without a
  citation the classification degrades to a clarification.
- **Never reconcile bundles silently**: a difference against the
  Structural census is a reportable inconsistency in both directions.

## Why this is a function and not a style

The rules are **total functions over the set of post-its**: every post-it
falls into exactly one and gets exactly one destination. That allows
(a) predicting the split before running, (b) auditing discrepancies as a
rule error rather than a matter of taste, and (c) measuring coverage as an
equality (`to_plan + to_spec == total_stickies`), not as an impression.

## Corpus example (reference canvas, 30 post-its)

```
/speckit.specify · NFR de operación

NFR-OP-1 La instalación DEBE ser reproducible y automatizada, sin
  pasos manuales no documentados.
  ← Deployment / Installation "Despliegue automatizado mediante
    contenedores"

NFR-OP-2 La operación DEBE poder ejecutarla el área de sistemas de la
  organización, sin dependencia del equipo de desarrollo.
  ← Deployment / Operation "Area de Sistemas"
    + ACC "control total de la operacion"

NFR-OP-3 El sistema DEBE funcionar en las variantes de sistema operativo
  usadas por la organización.
  ← Deployment / Installation "Verificación de ejecución en
    variantes de Linux"
  [NEEDS CLARIFICATION: lista de variantes y versiones soportadas]
```

Balance: 30 post-its · 27 to `plan.md` · 3 NFRs in `spec.md` · 2
clarifications (test environments and OS variants).

That ~90/10 split is what to expect from any Deployment Canvas: use it as
a sanity check on the run's balance. A split far from that proportion
means either technology post-its are being promoted to `spec.md`
(technical contamination) or installation and operation requirements that
were genuinely observable are being buried in `plan.md`.
