# Reglas de transformación desde COM

| canvas | destinos principales |
|---|---|
| business_context | propósito, actores, capacidades, entidades y criterios |
| architectural_context | principios, restricciones, objetivos, criterios y NFR |
| system_context | actores, sistemas externos e interfaces |
| structural | censo de bundles, capas, componentes y decisiones de plan |
| functional/front | FR de interacción y visualización, entidades y dudas |
| functional/back | FR de API, datos, jobs y eventos, entidades y dudas |
| deployment | contexto de despliegue y NFR observables |

Aplicar las reglas detalladas conservadas en las referencias de cada skill cuando correspondan. Esas referencias jamás se aplican durante la lectura COM.

Identificadores derivados: `FR-FRT-<BUNDLE>-NNN`, `FR-BCK-<BUNDLE>-NNN`, `NFR-<CANVAS>-NNN`, `ENT-<CANVAS>-NNN` y `Q-<CANVAS>-NNN`.

Cada traza contiene `{sticky_id, canvas, section, rule, target, target_id, literal_text}`. Un post-it puede compartir destino con otro sólo bajo una regla de deduplicación o calidad explícita; ambos conservan trazas independientes.

