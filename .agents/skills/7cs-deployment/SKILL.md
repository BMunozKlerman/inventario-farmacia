---
name: 7cs-deployment
description: Reads a Deployment Canvas (7Cs) from a PDF or image, converts it into a structured Canvas Object Model (COM), and then maps that COM to Spec Kit artifacts — operation NFRs (NFR-OP-n) for /speckit.specify, plus technical context, packaging and topology for /speckit.plan, and non-negotiable limits for constitution.md. Use this skill whenever the user uploads, attaches, or references a PDF or image of a Deployment Canvas, or asks to derive infrastructure, operation, deployment, or operation NFRs from one already ingested. This skill does NOT produce functional FRs, entities, or Dado/Cuando/Entonces scenarios — that is 7cs-functional-B's job.
---

# 7cs-deployment

A single-canvas skill with two internal phases: **ingestion** (pixels →
COM) and **mapping** (COM → Spec Kit fragments). One Deployment Canvas per
delivery, one COM, one split.

**This canvas barely reaches the specification.** Spec Kit asks for *what*
and *why* without fixing the stack. The Deployment Canvas talks about
technology, so its natural destination is `plan.md`. Only what the
organization can **observe** rises to `spec.md`: installing, operating,
supporting. Everything else — proxy, containers, runtimes, hardware — is
solution.

**The split is the skill's metric.** Every run declares how many post-its
went to `plan.md`, how many rose as `NFR-OP-n`, and how many
clarifications stayed open. A post-it with no destination is a defect, not
an acceptable omission.

> Before emitting output, read:
> - `references/com-schema.md` — full COM schema, field-by-field notes, the fifteen-section code table, and a real worked example.
> - `references/rewriting-rules.md` — R6, R7, R-OP, R-B, the promotion criterion, the prohibitions, the canonical form of an operation NFR, and a corpus example.

---

## Contract

```yaml
name: 7cs-deployment
when_to_use: >
  The user provides a PDF or image whose title (top-left corner) reads
  "Deployment Canvas", or a COM with canvas == "deployment" exists that
  has not been mapped yet. Run once per Deployment Canvas of the delivery.
inputs:
  input: pdf_path | image_path   # a page containing exactly one Deployment Canvas
  delivery_id: string            # e.g. "E1"; if omitted, derive it from the filename
  bundle_census: [ string ]?     # from the (planned) 7cs-structural skill, for R-B
  acc_com: CanvasObjectModel?    # optional; only to corroborate a citation about operation governance
outputs:
  com: CanvasObjectModel         # phase 1 — full schema in references/com-schema.md
  com_path: string               # e.g. "com/E1-deployment-p6.json"
  spec_fragment: markdown        # phase 2 — the NFR-OP-n block for /speckit.specify
  plan_context: markdown         # phase 2 — §Technical context, §Packaging and orchestration, §Topology
  constitution_limits: markdown  # phase 2 — non-negotiable limits derived from Constraints
  traces: [ {sticky_id, section, target_id} ]
  clarifications: [ string ]
  balance: {stickies, to_plan, to_spec, clarifications}
acceptance:
  - com.sections covers all fifteen printed sections, empty ones included (stickies: [])
  - traces.length == total_stickies
  - balance.to_plan + balance.to_spec == total_stickies
  - every NFR-OP-n cites at least one post-it from a promotable section
```

---

## Phase 1 · Ingestion (pixels → COM)

**Golden rule: the COM does not interpret.** It copies literal text and
coordinates. All interpretation happens in phase 2, where it is recorded
and auditable.

1. **Isolate the page.** If the input is a multi-page PDF, treat each page
   as one image with no text layer. If it's already a single image, treat
   it as one page.
2. **Classify the page.** Read the title in the top-left corner: it must
   read "Deployment Canvas". If it doesn't match — a different canvas
   type, a payroll table, a C4 diagram, a blank page — mark the page
   `out_of_scope`, emit a single clarification, and **stop**. Do not
   produce a COM for the wrong canvas. In the 7Cs corpus the Deployment
   Canvas is the last canvas of the delivery, but position is a hint,
   never a classifier: only the printed title decides.
3. **Read the header verbatim.** Capture System, Organization, Canvas,
   Version and Date exactly as written. Empty fields are valid data, not
   an error — record them as `null` and add a provenance clarification.
4. **Segment sections.** The Deployment Canvas is a fixed fifteen-section
   template in three columns: a left column (Environments, Constraints), a
   tall middle column (Bundles, Middleware, Runtime, Orchestration &
   scheduling, Container runtimes, Operating systems, Virtualization
   engines, Cloud abstractions, Hardware, Locations) and a right column
   (Networks, Installation, Operation). Detect each section by its outline
   and label it with the text actually printed on it, not by fixed
   position. All fifteen boxes belong to the template and normally appear
   even when they hold no post-its: a present-but-empty section goes into
   `sections[]` with `stickies: []`, **not** into `empty_sections`. Only a
   box missing from the printed template itself goes into
   `empty_sections`.
5. **Read post-its literally.** Each yellow rectangle produces a record
   with its literal text, its bounding box, and the section that contains
   it. Font size varies a lot on this canvas — "Docker" may be printed
   three times larger than a four-line operation note — and never encodes
   importance, priority, or category. Copy the text exactly as printed: do
   not correct spelling, expand acronyms ("GCP", "SPA", "DBMS"), or
   paraphrase. Ids follow the `DPC-<section-code>-<NN>` format (see
   `references/com-schema.md`).
6. **Resolve groupers and connectors.** A bordered rectangle enclosing
   post-its and carrying a loose label is a grouper: represent it as a
   `parent`/child hierarchy, never flattened. Arrows between post-its
   (common between Hardware, Locations, Runtime and Virtualization
   engines) are **not** groupers: if legible, record them in `notes[]` as
   literal evidence; never merge the two post-its they join.
7. **Persist the COM.** Write the COM as JSON to a flat file directly
   under `com/` — no per-delivery subfolder — named
   `com/<delivery_id>-deployment-p<n>.json`, where `<n>` is the page
   number from the `source` field (`p1` if the input is a single image).
   Report that path as `com_path`.

### Phase 1 guardrails

- Never infer or invent header fields, section names, or post-it text that
  isn't legible in the image.
- An illegible post-it → `[NEEDS CLARIFICATION: illegible post-it in
  <section>]`, never a guessed transcription.
- Never decide in this phase whether an empty section is *coherent* or an
  *inconsistency*: record the emptiness as data and leave the judgement to
  phase 2.
- Never cross-check `Bundles` against the Structural census here: that
  reconciliation belongs to phase 2.
- Never persist the COM anywhere other than
  `com/<delivery_id>-deployment-p<n>.json`.
- Never generate an ingest report or a page index
  (`<delivery_id>-ingest-report.md`, `<delivery_id>-page-index.json`):
  those are produced by a separate orchestration skill that aggregates all
  canvases in a delivery.

---

## Phase 2 · Mapping (COM → Spec Kit)

Runs **on the COM only**. Going back to the PDF is prohibited: if a datum
isn't in the COM, emit a clarification.

1. Verify `canvas == "deployment"` and that all fifteen sections are
   present.
2. Classify every empty section as coherent or inconsistent (table below),
   **citing** the evidence that supports the judgement.
3. Reconcile `Bundles` against `bundle_census` (R-B) and report
   differences in both directions.
4. Apply each section's single destination from the mapping table.
5. Apply the promotion criterion: only `Installation`, `Operation`,
   `Environments` and the OS-variants post-it of `Operating systems` may
   produce an `NFR-OP-n`.
6. Emit one trace per post-it and close with the balance of the split.

### Mapping table (one row per section; single destination)

| Section | What the skill produces |
|---|---|
| Environments | **Operation NFR** in `spec.md`: which environments must exist and what is promoted between them |
| Bundles | Deployable units; reconciled against the Structural census (they must match) |
| Middleware · Runtime | `plan.md` § Technical context: proxy, database, runtimes per bundle |
| Orchestration & scheduling · Container runtimes | `plan.md` § Packaging and orchestration |
| Operating systems · Virtualization engines | `plan.md`; a post-it naming OS variants is preserved as a **test criterion** |
| Cloud abstractions | **Judged**, never assumed: empty is coherent when a Constraint declares on-premise; empty is an inconsistency when the canvas names cloud managed services in another section |
| Hardware · Locations · Networks | `plan.md` § Topology: servers, physical dependencies, internal network and public access |
| Installation · Operation | **Operation NFR**: automated installation, who operates the system, supported platforms |
| Constraints | Limits in `constitution.md` + constraints in `plan.md`: licensing, platform reuse, operation governance, non-negotiable exclusions |

### Empty-section classification (quick reference)

| Section | Empty is coherent when… | Empty is an inconsistency when… |
|---|---|---|
| `Cloud abstractions` | a Constraint declares on-premise / "sin cloud" | the canvas names cloud managed services (Cloud Run, Cloud SQL…) in another section |
| `Operating systems` | the whole deployment runs on managed services with no exposed OS | the canvas declares own hardware, VMs, or virtualization |
| `Virtualization engines` | the deployment is serverless or on managed containers | `Hardware` or `Locations` declare own servers |
| `Hardware` / `Locations` | the deployment is 100% managed cloud | a Constraint declares on-premise or existing servers |
| `Networks` | (rare) no external access is declared | the system exposes a UI or an API to external users or systems |
| `Environments` | (never) — with no environments there is no describable deployment | always |
| `Installation` / `Operation` | (never) — without them no operation NFR is possible | always |
| `Bundles` | (never) — the deployable unit is the object of this canvas | always |
| `Middleware` / `Runtime` | the single bundle is self-contained and says so | persistence or a proxy are declared in another section |
| `Constraints` | (acceptable) the limits come from the Architectural Context | the canvas fixes technology that no other source justifies |

An empty section is **always** reported; the classification decides whether
the resulting clarification blocks the run or is merely recorded for
`/speckit.clarify`.

### Mapping-specific rules

- **Promotion criterion.** Only a post-it describing something observable
  by the organization rises to `spec.md`: installing, operating,
  supporting, running on its own platforms. A post-it naming a product
  describes *how*, not *what*: it stays in `plan.md`. When in doubt, it
  does not rise.
- **Who operates matters.** "Área de Sistemas" or "personal de soporte del
  cliente" in `Operation` is an **operation requirement**, not an
  administrative detail: it fixes who must be able to run the system
  without depending on the development team.
- **Cross-check with the Structural.** The deployable units in `Bundles`
  must match the bundle census. Any bundle appearing here and not there
  (or the reverse) is a reportable inconsistency, never a silent
  reconciliation.
- **Absence is reported, not filled in.** If the canvas declares no
  backup, monitoring, or availability, record it as an **expected gap** so
  it gets asked, instead of inventing an availability target. This is the
  costliest failure mode of this canvas: a number invented here becomes an
  SLA in `/speckit.plan`.
- **A scheduler is not a job.** `Cloud Scheduler (Jobs)`, `cron`,
  `Cloud Run` are infrastructure (R6). The *functional* job that runs on
  them comes from the Functional Canvas and is emitted by
  `7cs-functional-B`. Merging them is prohibited.
- **Declared environments vs. needed environments.** If the canvas
  declares fewer environments than the promotion flow requires (e.g. only
  Desarrollo and Producción, with no staging/UAT), emit a test-environment
  clarification — never invent the missing environment.

The rewriting rules (R6, R7, R-OP, R-B), their prohibitions, the canonical
form of the NFR, and why R1–R4 never fire on this canvas are in
`references/rewriting-rules.md`.

---

## Output format (phase 2)

```markdown
## /speckit.specify · NFR de operación

NFR-OP-1 {subject} DEBE {observable verb} {condition}.
  ← Deployment / {section} "{literal text}"
  [+ {other canvas} "{literal text}" if the promotion leans on it]
  [NEEDS CLARIFICATION: ...]
...

## /speckit.plan · Technical context given by the organization
{destination} · {literal technology}. [DPC/{section}]
...

## /speckit.plan · Packaging and orchestration
...

## /speckit.plan · Topology
...

## constitution.md · Non-negotiable limits
C{n} {limit}. [DPC/Constraints]

## Findings
- Empty sections: {section} → {coherent | inconsistency}, because {cited reason}
- Bundle reconciliation: {matches} / {discrepancies}
- Expected gaps: {backup | monitoring | availability | …}

## Balance
{n} post-its · {n} to plan.md · {n} NFRs in spec.md · {n} clarifications
```

Requirement text is emitted in the canvas's own language (Spanish in the
current corpus), because it quotes and rewrites literal post-it content.
The skill's documentation is English; the artifacts it produces are not
translated.

A corpus example with the three `NFR-OP-n` and its balance is at the end
of `references/rewriting-rules.md`.

---

## Guardrails (numbered, auditable)

- **G0 — Ingestion before mapping, never blended.** Phase 2 reads only the
  persisted COM. No judgement, NFR, empty-section classification, or plan
  line may appear inside the COM.
- **G1 — Complete split.** Every post-it in the COM has exactly one
  destination: `balance.to_plan + balance.to_spec == total_stickies`, or
  the skill fails.
- **G2 — Zero technical contamination.** No technology name from the
  corpus (Node.js, PostgreSQL, Docker, Nginx, Cloud Run, Cloud SQL, GCP,
  Linux, SPA…) may appear in the **requirement text** of `spec_fragment`.
  The `←` trace lines are exempt: they quote the literal post-it and are
  the evidence. The skill greps its own output — ignoring trace lines —
  before emitting.
- **G3 — Justified promotion.** An `NFR-OP-n` whose trace does not come
  from `Installation`, `Operation`, `Environments`, or the OS-variants
  post-it of `Operating systems` is a defect: the skill rejects it before
  emitting.
- **G4 — No invented targets.** Emitting availability figures, RPO/RTO,
  backup frequency, or monitoring thresholds the canvas does not declare
  is prohibited. The absence is reported as a finding.
- **G5 — Empty sections classified.** Every section with `stickies: []` is
  classified as `coherent` or `inconsistency`, **citing** the evidence
  that supports the judgement (usually a `Constraints` post-it). Without a
  citation the classification is void and degrades to a clarification.
- **G6 — Fail on census mismatch.** If `Bundles` and `bundle_census` don't
  match, the skill emits a single grouped clarification listing the
  differences in both directions and does not reconcile on its own; the
  orchestrator decides whether to continue. If the census doesn't exist
  yet, reconciliation is **pending**, not failed.
- **G7 — No cross-section merging.** A runtime and the bundle that uses it
  are two traces. The only joint citation allowed is an `NFR-OP-n` that
  leans on an Architectural Context post-it to justify operation
  governance, and both traces are cited.
- **G8 — Literal text quoted.** Every trace quotes the post-it text in
  double quotes, **exactly** as it appears in the COM. No paraphrase, no
  expanded acronyms.
- **G9 — No functional FRs.** This skill emits no `FR-nnn`, no
  `§Key Entities`, and no `Dado/Cuando/Entonces` scenarios: that is
  `7cs-functional-B`.

---

## Acceptance (checks run by the audit skill)

The run is declared valid by `7cs-spec-audit` if and only if:

- [ ] `com.sections` covers the fifteen printed sections, including
      present-but-empty ones (`stickies: []`).
- [ ] Every sticky has `text`, `bbox`, a containing section, and an `id`
      matching `^DPC-[A-Z]+-[0-9]{2}$`.
- [ ] No sticky text differs from what is printed on the canvas.
- [ ] The COM is persisted at `com/<delivery_id>-deployment-p<n>.json` and
      `com_path` matches that path.
- [ ] `traces.length == total_stickies`.
- [ ] `balance.to_plan + balance.to_spec == total_stickies`.
- [ ] Every NFR id matches `^NFR-OP-[0-9]+$` and its trace comes from a
      promotable section.
- [ ] No denylisted technology name appears in the requirement text of
      `spec_fragment`.
- [ ] Every section with `stickies: []` appears in `clarifications` with
      its classification and its cited evidence.
- [ ] If the canvas declares no backup, monitoring, or availability, there
      is exactly one expected-gap clarification for each.
- [ ] `Bundles` and `bundle_census` match, or there is exactly one grouped
      reconciliation clarification.

If any check fails, the audit blocks the run and the orchestrator requests
a rerun with a corrected COM or a clarified census.

---

## Fit in the pipeline

One canvas → one COM → one split. This skill covers both **Stage A ·
Ingestion** and **Stage B · Mapping** for the Deployment Canvas — the
delivery carries exactly one, so splitting it into two skills would buy
nothing. It feeds `/speckit.plan` together with the (planned)
`7cs-structural`; its `NFR-OP-n` enter through `/speckit.specify`. Three
pipeline rules govern it:

- **Isolation.** It sees only its own canvas and, optionally, the
  Structural bundle census and one Architectural Context citation to
  justify operation governance. If it needs a datum it doesn't have, it
  emits `[NEEDS CLARIFICATION]`.
- **Idempotence.** Given the same canvas and the same census, it emits the
  same COM, the same `NFR-OP-n`, and the same traces; post-it ids
  (`DPC-IN-01`, etc.) are stable across runs.
- **Explicit failure.** Facing ambiguity or a missing datum it **does not
  choose**: it emits `[NEEDS CLARIFICATION: ...]` and leaves the decision
  to `/speckit.clarify`. It invents no environments, availability targets,
  backup windows, or operation owners.

Delivery-level artifacts (an ingest report, a page index) are produced by
a separate orchestration skill. Cross-canvas composition and deduplication
belong to `7cs-spec-compose`; the coverage (C), ambiguity (A), technical
contamination (T) and verifiability (V) metrics belong to
`7cs-spec-audit`. This canvas is the one that stresses metric T the most:
its natural split is ~90% to `plan.md`.

**Strict Spec Kit ordering:** never run `/speckit.plan` before closing the
clarifications from `/speckit.clarify`.
