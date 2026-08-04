# Rewriting Rules — Architectural Context Canvas → Spec Kit

Reference material for the **downstream mapping skill** that consumes the
COM produced by `7cs-architectural-context`. The ingestion skill does not
apply any of this itself — it only reads the COM shape. This file exists
so both skills stay consistent when the mapping skill is built.

## Section → destination mapping table

One row per canvas section. The mapping skill cannot write to a
destination absent from this table, nor leave a section without a
destination.

| Canvas section | What the mapping skill produces |
|---|---|
| Stakeholders | List of who validates acceptance for each requirement |
| Business strategy | `constitution.md` § Organizational objectives |
| IT strategy | `constitution.md` § Platform principles (centralization, architecture control) |
| Business goals & drivers | `§Measurable success criteria` — rule R-Q: requires a metric, never becomes an FR |
| Technology goals & drivers | Integration/standardization NFRs |
| Business standards & policies | Project constraints (e.g. licensing) |
| Technology standards & policies | `plan.md` § Given technical context; in `spec.md` only the observable/anonymized version |
| Situational constraints | `§Constraints` — rule R-C: only if it implies observable behavior |
| Business principles | `constitution.md` § Business principles |
| Technical principles | `constitution.md` § Technical principles |

## Rewriting rules

### R-Q — Quantification

If a post-it's text starts with an improvement verb ("reduce", "improve",
"facilitate", "optimize"...) it is a **goal**, not a requirement or a
principle. Emit it as a success criterion (`CE-n`) and attach
`[NEEDS CLARIFICATION: metric and baseline]` if the post-it carries no
number. Never invent a percentage.

### R-C — Root cause

A post-it from *Situational constraints* becomes a constraint (`R-n`)
only if it implies observable system behavior. If it also generates a
compensating requirement in another canvas (e.g. Functional), cite the
cause (`cause: ACC/R-n`) instead of duplicating the requirement.

### R-T — Technology anonymization

Any concrete product or technology name ("PostgreSQL", "Nginx", "Docker")
goes to `plan.md` as given technical context and, if it's a
non-negotiable limit, also to `constitution.md`. `spec.md` **never**
names the product: it describes its function ("authentication via the
institutional identity system"). Generic architectural roles (e.g. "POS",
"API") are not products and don't require anonymization.

## Writing forms

- Principle: `P<n> <short statement>: <declaration>. [ACC/<origin section>]`
- Success criterion: `CE-<n> <goal, as an infinitive or measurable statement>.` + clarification if it lacks a metric.
- Constraint: `R-<n> <observable statement, without naming technology if R-T applies>.`

Never merge two post-its into a single principle or requirement, unless
they come from different sections and clearly restate the same
declaration — in that case cite both sections on one line (see `P4`
below).

## Worked example

Input: an Architectural Context Canvas (42 post-its, 10 sections).
Output: 5 principles, 3 success criteria, 4 constraints, 2 clarifications.

```
/speckit.constitution
P1 Centralized platform: all capability is provisioned from a single,
   centralized technology platform. [ACC/IT strategy]
P2 Free or academic software: introducing dependencies under a
   commercial license is prohibited. [ACC/Business standards & policies]
P3 Incremental, organization-wide development: deliverables must be
   verifiable per increment. [ACC/Technical principles]
P4 Centralized application governance, with operations controlled by the
   Systems Area. [ACC/IT strategy + Technical principles]
P5 Eventual consistency is acceptable for fast reads of aggregated
   content. [ACC/Technical principles]

/speckit.specify · Success criteria
CE-1 Reduce duplicate published content.
     [NEEDS CLARIFICATION: measured how? % of duplicate items?]
CE-2 Improve visibility of institutional content.
     [NEEDS CLARIFICATION: metric and baseline?]
CE-3 Centralize management: a single administration interface for news,
     multimedia, press, and blog.

/speckit.specify · Constraints
R-1 The solution runs on on-premise infrastructure.
R-2 The publications repository exposes no API: publication uploads must
    support manual file ingestion.
R-3 Authentication is delegated to the institutional identity system;
    the system does not manage its own credentials.
R-4 The composition of the development deliveries is fixed.
```
