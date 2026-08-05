# Trazas — bundle Front (E1, p. 5)

> Tabla de correspondencia 1-a-1 entre cada post-it del COM
> `com/E1-functional-p5.json` y el FR (o Key Entity / plan_context) emitido.
> Acceptance check: `traces.length == total_stickies` → debe ser 26.

| post-it id   | sección                       | texto literal (cita exacta)                                  | regla | destino                          | id_req        |
|--------------|-------------------------------|---------------------------------------------------------------|-------|----------------------------------|---------------|
| FNC-BC-01    | Bundles & components          | "Compras"                                                     | —     | registro de bundles              | —             |
| FNC-BC-02    | Bundles & components          | "Recepción de Mercadería"                                     | —     | registro de bundles              | —             |
| FNC-BC-03    | Bundles & components          | "Reposición"                                                  | —     | registro de bundles              | —             |
| FNC-BC-04    | Bundles & components          | "Inventario (stock, lotes, ubicaciones)"                      | —     | registro de bundles              | —             |
| FNC-BC-05    | Bundles & components          | "Control Regulatorio (libro de productos controlados)"        | —     | registro de bundles              | —             |
| FNC-BC-06    | Bundles & components          | "Reportes"                                                    | —     | registro de bundles              | —             |
| FNC-BC-07    | Bundles & components          | "Vencimientos (canje/destrucción)"                            | —     | registro de bundles              | —             |
| FNC-UI-01    | User inputs                   | "Registro de recepción de mercadería"                         | R2    | spec.md#FR-001                   | FR-FRO-001    |
| FNC-UI-02    | User inputs                   | "Autorización y firma de guía de recepción"                   | R2    | spec.md#FR-002                   | FR-FRO-002    |
| FNC-UI-03    | User inputs                   | "Registro de reposición"                                      | R2    | spec.md#FR-003                   | FR-FRO-003    |
| FNC-UI-04    | User inputs                   | "Generación de OC"                                            | R2    | spec.md#FR-004                   | FR-FRO-004    |
| FNC-UI-05    | User inputs                   | "Registro de canje"                                           | R2    | spec.md#FR-005                   | FR-FRO-005    |
| FNC-UI-06    | User inputs                   | "Registro de destrucción"                                     | R2    | spec.md#FR-006                   | FR-FRO-006    |
| FNC-UPI-01   | UI-processing inputs          | "Dashboard de stock (fila roja para stock crítico)"           | R2    | spec.md#FR-007                   | FR-FRO-007    |
| FNC-UPI-02   | UI-processing inputs          | "Reporte semanal de próximos a vencer"                        | R4    | spec.md#FR-008                   | FR-FRO-008    |
| FNC-UPI-03   | UI-processing inputs          | "Historial de movimientos"                                    | R2    | spec.md#FR-009                   | FR-FRO-009    |
| FNC-UV-01    | User visualizations / reports | "Reporte mensual de compras"                                  | R4    | spec.md#FR-010                   | FR-FRO-010    |
| FNC-UV-02    | User visualizations / reports | "Alerta urgente en dashboard"                                 | R2    | spec.md#FR-011                   | FR-FRO-011    |
| FNC-UV-03    | User visualizations / reports | "PDF/Excel de orden de compra"                                | R2    | spec.md#FR-012                   | FR-FRO-012    |
| FNC-UV-04    | User visualizations / reports | "Guía de despacho impresa"                                    | R2    | spec.md#FR-013                   | FR-FRO-013    |
| FNC-UV-05    | User visualizations / reports | "Informe de productos controlados"                            | R2    | spec.md#FR-014                   | FR-FRO-014    |
| FNC-UV-06    | User visualizations / reports | "Libro de control de productos controlados"                   | R2    | spec.md#FR-015                   | FR-FRO-015    |
| FNC-CT-01    | Constraints                   | "Frontend SPA responsiva"                                     | R6+R7 | plan.md + spec.md#FR-016         | FR-FRO-016    |
| FNC-CT-02    | Constraints                   | "Sin soporte offline"                                         | R7    | spec.md#FR-017 (compensatorio)   | FR-FRO-017    |
| FNC-CT-03    | Constraints                   | "Stock Crítico para Dashboard"                                | R7    | spec.md#FR-018 (umbral)          | FR-FRO-018    |
| FNC-API-01   | API inputs                    | "Peticiones hacia el Backend Bundle vía API REST"             | R3    | spec.md#FR-019 + plan.md         | FR-FRO-019    |

## Secciones vacías (registradas por el COM)

- `Data objects`, `Data imports`, `Data exports`, `Jobs`, `Event handlers`,
  `Event triggers`, `Helpers`, `Technology stack` — todas en `empty_sections[]`.

Clasificación (per SKILL.md §"Clasificación de secciones vacías"):

| Sección                          | Vacía coherente porque…                                              | Clasificación    |
|----------------------------------|----------------------------------------------------------------------|------------------|
| `Data objects`                   | El bundle Front no declara entidades; están en el Back canvas.       | coherente        |
| `Data imports`                   | El bundle Front no importa datos; consume vía API del Back.          | coherente        |
| `Data exports`                   | El bundle Front no exporta datos; genera visualizaciones en pantalla. | coherente        |
| `Jobs`                           | El bundle Front no ejecuta jobs; los jobs viven en el Back.          | coherente        |
| `Event handlers`                 | El bundle Front reacciona vía polling/consulta, no por evento.      | coherente        |
| `Event triggers`                 | El bundle Front no emite eventos; los emite el Back.                | coherente        |
| `Helpers`                        | El bundle Front no transforma datos; los recibe ya procesados.      | coherente        |
| `Technology stack`               | (Aceptable) el stack se decide en `plan.md`; solo "SPA" en CT-01.    | coherente        |

Total stickies trazados: **26 / 26** ✓

## Balance del bundle Front

- post-it: 26
- FR con prefijo (`FR-FRO-`): 19
- entidades (Key Entities): 0 (todas en el Back)
- dudas: 6 (ver `evidence/E1-functional-bundle-delivery-clarifications.md`)
- secciones vacías clasificadas: 8 (todas coherentes)