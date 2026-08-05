# Rewriting Rules — System Context Canvas → Spec Kit

Reference material for the **downstream mapping skill** that consumes the
COM produced by `7cs-system-context`. The ingestion skill does not apply
any of this itself — it only reads the COM shape. This file exists so
both skills stay consistent when the mapping skill is built.

## Section → destination mapping table

One row per canvas section. The mapping skill cannot write to a
destination absent from this table, nor leave a section without a
destination.

| Canvas section | What the mapping skill produces |
|---|---|
| Source users | `spec.md` § Actors — who initiates interaction with the system |
| User data input interfaces | `plan.md` § Given technical context — user-facing input channel; anonymized version (rule R-T) in `spec.md` |
| User data output interfaces | `plan.md` § Given technical context — user-facing output channel; anonymized version (rule R-T) in `spec.md` |
| Target users | `spec.md` § Actors — who receives output from the system |
| Source systems | `spec.md` § External systems — upstream integration the system consumes |
| System data input interfaces | `plan.md` § Given technical context — system-to-system input contract; anonymized version (rule R-T) in `spec.md` |
| System data output interfaces | `plan.md` § Given technical context — system-to-system output contract; anonymized version (rule R-T) in `spec.md` |
| Target systems | `spec.md` § External systems — downstream integration the system feeds |
| Source repositories | `spec.md` § External systems — data source / record of truth the system reads |
| Repository data input interfaces | `plan.md` § Given technical context — repository write path; anonymized version (rule R-T) in `spec.md` |
| Repository data output interfaces | `plan.md` § Given technical context — repository read path; anonymized version (rule R-T) in `spec.md` |
| Target repositories | `spec.md` § External systems — archival / record-keeping destination the system writes to |
| Source devices | `spec.md` § External systems — physical input device |
| Device data input interfaces | `plan.md` § Given technical context — device input channel; anonymized version (rule R-T) in `spec.md` |
| Device data output interfaces | `plan.md` § Given technical context — device output channel; anonymized version (rule R-T) in `spec.md` |
| Target devices | `spec.md` § External systems — physical output device |

## Rewriting rules

### R-T — Technology anonymization

Any concrete product or technology name ("SPA", "PostgreSQL", "Nginx")
carried by an interface post-it goes to `plan.md` as given technical
context and, if it's a non-negotiable limit, also to `constitution.md`.
`spec.md` **never** names the product: it describes its function ("web
interface for pharmacy staff" instead of "UI WEB (SPA) responsiva").
Generic architectural roles (e.g. "POS", "API") are not products and
don't require anonymization.

### R-A — Actor/system identity

A Source and a Target post-it that repeat the same literal text in the
same row (e.g. "POS" as both a source and a target system) name the same
actor or system, referenced twice for its two roles — emit it once in
`spec.md`'s actor/external-system list, annotated with both directions,
never as two separate entries.

R-Q (quantification) and R-C (root cause), used by the Architectural
Context Canvas mapping, do not apply here: the System Context Canvas
carries no goals or constraints, only actors, systems, and interfaces.

## Writing forms

- Actor / external system: `A<n> <name>: <role, and which columns it appears in>. [SCC/<origin section(s)>]`
- Interface: `I<n> <interface purpose>, direction: <source → target>. [SCC/<origin section>]` — apply rule R-T before writing to `spec.md`.

Never merge two post-its into a single actor or interface entry, unless
they come from paired Source/Target columns of the same row and clearly
name the same actor or system (rule R-A).

## Worked example

Input: a System Context Canvas (16 sections, 4×4 grid).
Output: 3 actors/external systems, 6 interfaces, 0 clarifications.

```
/speckit.specify · Actors & external systems
A1 QF DT, QF Complementario, Bodeguero: pharmacy staff, source and
   target of the user-facing interfaces. [SCC/Source users + Target users]
A2 POS: point-of-sale system, source and target of the system
   integration interfaces. [SCC/Source systems + Target systems]
A3 ISP: recipient of the physical controlled-products record book.
   [SCC/Target repositories]

/speckit.plan · Given technical context
I1 Web interface for pharmacy staff, responsive SPA.
   [SCC/User data input interfaces + User data output interfaces]
I2 API for the POS to register transactions.
   [SCC/System data input interfaces]
I3 API for the POS to query available stock.
   [SCC/System data output interfaces]
I4 Barcode reader as an input device.
   [SCC/Source devices + Device data input interfaces]
I5 Monthly printout on foliated/stamped sheets.
   [SCC/Device data output interfaces]
I6 Purchase order generation, PDF/Excel.
   [SCC/Device data output interfaces]
```
