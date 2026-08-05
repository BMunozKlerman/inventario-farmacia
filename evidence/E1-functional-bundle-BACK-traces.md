# Trazas — bundle Back (E1, p. 7)

> Tabla de correspondencia 1-a-1 entre cada post-it del COM
> `com/E1-functional-p7.json` y el FR (o Key Entity / plan_context) emitido.
> Acceptance check: `traces.length == total_stickies` → debe ser 32.

| post-it id   | sección                       | texto literal (cita exacta)                                                       | regla   | destino                          | id_req        |
|--------------|-------------------------------|----------------------------------------------------------------------------------|---------|----------------------------------|---------------|
| FNC-BC-01    | Bundles & components          | "Compras"                                                                        | —       | registro de bundles              | —             |
| FNC-BC-02    | Bundles & components          | "Recepción de Mercadería"                                                        | —       | registro de bundles              | —             |
| FNC-BC-03    | Bundles & components          | "Reposición"                                                                     | —       | registro de bundles              | —             |
| FNC-BC-04    | Bundles & components          | "Inventario (stock, lotes, ubicaciones)"                                         | —       | registro de bundles              | —             |
| FNC-BC-05    | Bundles & components          | "Control Regulatorio (libro de productos controlados)"                           | —       | registro de bundles              | —             |
| FNC-BC-06    | Bundles & components          | "Módulo de Alertas y Notificaciones"                                             | —       | registro de bundles              | —             |
| FNC-BC-07    | Bundles & components          | "Integración POS Venta"                                                          | —       | registro de bundles              | —             |
| FNC-BC-08    | Bundles & components          | "Vencimientos (canje/destrucción)"                                               | —       | registro de bundles              | —             |
| FNC-API-01   | API inputs                    | "Peticiones del Frontend Bundle"                                                 | R3      | spec.md#FR-001 + plan.md         | FR-BCK-001    |
| FNC-API-02   | API inputs                    | "Registro de transacciones desde el POS"                                          | R3      | spec.md#FR-002 + plan.md         | FR-BCK-002    |
| FNC-API-03   | API inputs                    | "Registros de transacciones inmutables una vez emitidos"                         | R7+R2   | spec.md#FR-003 (fusión c/ OB-03) | FR-BCK-003    |
| FNC-UPI-01   | UI-processing inputs          | "OC pendientes"                                                                  | R2      | spec.md#FR-004                   | FR-BCK-004    |
| FNC-UPI-02   | UI-processing inputs          | "Vencidos"                                                                       | R2      | spec.md#FR-005                   | FR-BCK-005    |
| FNC-OB-01    | Data objects                  | "Producto (categoría, controlado sí/no)"                                         | R1      | §Key Entities                    | —             |
| FNC-OB-02    | Data objects                  | "Lote (número, vencimiento, saldo)"                                              | R1      | §Key Entities                    | —             |
| FNC-OB-03    | Data objects                  | "Movimiento de inventario"                                                       | R1+R2   | §Key Entities + FR-BCK-003 (fusión calidad) | — / FR-BCK-003 |
| FNC-OB-04    | Data objects                  | "Orden de Compra (estados)"                                                      | R1      | §Key Entities                    | —             |
| FNC-OB-05    | Data objects                  | "Guía de despacho"                                                               | R1      | §Key Entities                    | —             |
| FNC-OB-06    | Data objects                  | "Informe de productos controlados"                                               | R1      | §Key Entities                    | —             |
| FNC-OB-07    | Data objects                  | "Tipo de Movimiento"                                                             | R1      | §Key Entities                    | —             |
| FNC-DE-01    | Data exports                  | "Consulta de stock (POS)"                                                        | R3      | spec.md#FR-006 + plan.md         | FR-BCK-006    |
| FNC-DE-02    | Data exports                  | "PDF/Excel"                                                                      | R2      | spec.md#FR-007                   | FR-BCK-007    |
| FNC-DE-03    | Data exports                  | "Guía despacho impresa"                                                          | R2      | spec.md#FR-008                   | FR-BCK-008    |
| FNC-DE-04    | Data exports                  | "Informe controlados"                                                            | R2      | spec.md#FR-009                   | FR-BCK-009    |
| FNC-DE-05    | Data exports                  | "Libro de control"                                                               | R2      | spec.md#FR-010                   | FR-BCK-010    |
| FNC-ET-01    | Event triggers                | "Cruce de umbral stock crítico → Event Handler"                                  | R2      | spec.md#FR-011                   | FR-BCK-011    |
| FNC-H-01     | Helpers                       | "Servicio envío correo (alertas)"                                                | R2      | spec.md#FR-012                   | FR-BCK-012    |
| FNC-H-02     | Helpers                       | "Servicio generación PDF"                                                        | R2      | spec.md#FR-013                   | FR-BCK-013    |
| FNC-J-01     | Jobs                          | "Job diario revisión stock"                                                      | R4      | spec.md#FR-014                   | FR-BCK-014    |
| FNC-J-02     | Jobs                          | "Job mensual libro controlados"                                                  | R4      | spec.md#FR-015                   | FR-BCK-015    |
| FNC-J-03     | Jobs                          | "Job vencimientos"                                                               | R4      | spec.md#FR-016                   | FR-BCK-016    |
| FNC-TS-01    | Technology stack              | "Backend: monolito Node.js / DB: PostgreSQL / Infra: GCP"                        | R6      | plan.md                          | —             |

## Fusión de calidad (1)

- **FR-BCK-003** combina `FNC-API-03` (inmutabilidad) + `FNC-OB-03` (entidad Movimiento de inventario). El primero es una restricción de calidad sobre el segundo. Ambas trazas citadas en el fragmento.

## Secciones vacías (registradas por el COM)

- `User inputs`, `Data imports`, `Event handlers`, `User visualizations / reports`,
  `Constraints` — todas en `empty_sections[]`.

Clasificación (per SKILL.md §"Clasificación de secciones vacías"):

| Sección                          | Vacía coherente porque…                                              | Clasificación    |
|----------------------------------|----------------------------------------------------------------------|------------------|
| `User inputs`                    | El bundle Back no expone UI; es servidor / worker.                   | coherente        |
| `Data imports`                   | El bundle Back no importa datos de archivos; recibe por API.          | coherente        |
| `Event handlers`                 | El bundle Back declara `Event triggers` (FNC-ET-01) pero no handlers. La sección está vacía; **inconsistencia** probable: el evento emitido por FNC-ET-01 debe tener un handler en algún lado — o está en el Front (FNC-UPI-01 "Dashboard de stock" lee del Back) o falta declarar el consumidor. | **inconsistencia** |
| `User visualizations / reports`  | El bundle Back no expone UI; el Front sí (`FNC-UV-*`).                | coherente        |
| `Constraints`                    | (Aceptable) las constraints están en el Front (CT-01..03) y en el Architectural Context (p2). | coherente        |

Total stickies trazados: **32 / 32** ✓

## Balance del bundle Back

- post-it: 32
- FR con prefijo (`FR-BCK-`): 16
- entidades (Key Entities): 7
- dudas: 7 (ver `evidence/E1-functional-bundle-delivery-clarifications.md`)
- secciones vacías clasificadas: 4 coherentes + 1 **inconsistencia** (`Event handlers`).