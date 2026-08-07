# Rewriting Rules — Structural Canvas → Spec Kit

Reference material for the **downstream mapping skill** that consumes the
COM produced by `7cs-structural`. The ingestion skill does not
apply any of this itself — it only reads the COM shape. This file exists
so both skills stay consistent when the mapping skill is built.

## Section → destination mapping table

One row per canvas section. The mapping skill cannot write to a
destination absent from this table, nor leave a section without a
destination.

| Canvas section | What the mapping skill produces |
|---|---|
| Frontend bundles | `plan.md` § Frontend Components (`COMP-FE-n`) |
| Data input interfaces to frontend bundles | `spec.md` § Frontend Input Interfaces (`INT-FEIN-n`) |
| Data output interfaces from frontend bundles | `spec.md` § Frontend Output Interfaces (`INT-FEOUT-n`) |
| Backend bundles | `plan.md` § Backend Components (`COMP-BE-n`) |
| Data input interfaces to backend bundles | `spec.md` § Backend Input Interfaces (`INT-BEIN-n`) |
| Data output interfaces from backend bundles | `spec.md` § Backend Output Interfaces (`INT-BEOUT-n`) |
| Repository bundles | `plan.md` § Repository & Data Persistence (`COMP-REPO-n`) |
| Data input interfaces to repository bundles | `spec.md` § Repository Input Interfaces (`INT-REPOIN-n`) |
| Data output interfaces from repository bundles | `spec.md` § Repository Output Interfaces (`INT-REPOOUT-n`) |
| Platform & Infrastructure bundles | `plan.md` § Platform & Infrastructure (`INFRA-n`) |
| Data input interfaces to platform & infrastructure bundles | `spec.md` § Infrastructure Input Interfaces (`INT-IPIN-n`) |
| Data output interfaces from platform & infrastructure bundles | `spec.md` § Infrastructure Output Interfaces (`INT-IPOUT-n`) |
| Device bundles | `plan.md` § Device Components (`DEV-n`) |
| Data input interfaces to device bundles | `spec.md` § Device Input Interfaces (`INT-DEVIN-n`) |
| Data output interfaces from device bundles | `spec.md` § Device Output Interfaces (`INT-DEVOUT-n`) |
| Constraints | `spec.md` § Structural Constraints (`R-STR-n` / `NFR-STR-n`) — rule R-C |

## Rewriting rules

### R-T — Technology anonymization & allocation

Any concrete product, framework, language, or vendor name ("Node.js", "PostgreSQL", "React", "AWS", "Docker") extracted from bundle sections must be routed to `plan.md` under its respective architectural component. `spec.md` **never** names the specific product: it describes only the observable functionality or contract (e.g., "Server-side REST application layer" instead of "Node.js Express API"). Generic architectural terms (e.g., "SPA", "Relational Database", "Broker") do not require anonymization.

### R-I — Interface boundary definition

Post-its in any *Data input/output interfaces* section define cross-boundary contracts. They must be rewritten into `spec.md` as observable protocol or data-exchange requirements (`INT-<boundary>-n`), focusing on inputs, outputs, and format guarantees without binding to specific implementation libraries.

### R-C — Structural constraints classification

A post-it from *Constraints* becomes a functional constraint (`R-STR-n`) or a non-functional quality requirement (`NFR-STR-n`) in `spec.md` if it describes an observable system boundary or operational rule (e.g., "Data immutability"). If it specifies an infrastructure or deployment limit (e.g., "Must run on Linux containers"), it is additionally recorded as an explicit architecture decision in `plan.md`.

## Writing forms

- Component / Infrastructure (`plan.md`): `COMP-<TYPE>-<n> <short description>: <assigned tech stack or structural boundary>. [STR/<origin section>]`
- Interface contract (`spec.md`): `INT-<BOUNDARY>-<n> <observable data contract or protocol statement>. [STR/<origin section>]`
- Structural Constraint (`spec.md`): `R-STR-<n>` or `NFR-STR-<n> <observable requirement, without naming specific commercial products if R-T applies>. [STR/Constraints]`

Never merge two post-its into a single component or interface requirement unless they come from complementary input/output sections and clearly describe the exact same interface boundary.

## Worked example

Input: a Structural Canvas (16 sections, COM JSON format).
Output: 3 components in `plan.md`, 2 interface contracts in `spec.md`, 1 non-functional constraint in `spec.md`.

```
/speckit.plan · Architecture & Components
COMP-FE-01 Web Client Interface: Single Page Application (SPA) responsive web frontend. [STR/Frontend bundles]
COMP-BE-01 Application Core: Server-side monolithic backend service implemented with Node.js runtime. [STR/Backend bundles]
INFRA-01 Hosting Platform: Containerized runtime environment running on Linux-based instances. [STR/Platform & Infrastructure bundles]

/speckit.specify · Interfaces
INT-FEIN-01 Web Access Contract: System shall accept incoming HTTP/HTTPS request streams for user interactions. [STR/Data input interfaces to frontend bundles]
INT-BEIN-01 Application API Contract: System shall process incoming application requests via standardized JSON endpoints. [STR/Data input interfaces to backend bundles]

/speckit.specify · Structural Constraints
NFR-STR-01 Immutable Audit Logging: All transaction records must remain immutable once written to persistent storage. [STR/Constraints]
```