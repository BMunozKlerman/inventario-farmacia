# Reglas de reescritura R1–R7 (post-it → artefacto)

Se aplican **en orden**. La primera regla que coincide decide el destino del post-it.
Ninguna regla puede agregar información que no esté en el canvas.

| Regla | Patrón detectado | Ejemplo del corpus | Texto emitido |
|---|---|---|---|
| **R1** | Sustantivo de dominio | "Publicaciones científicas (Papers)" | Entidad **Publicación** en §Key Entities; **atributos abiertos** (nunca inventados) |
| **R2** | Verbo de acción + objeto | "Redactar entradas de blog" | FR: "El sistema DEBE permitir a {rol} redactar una entrada de blog" + escenario feliz y de error |
| **R3** | Nombre de interfaz o endpoint | "Auth Callback Endpoint (Redireccionamiento u-pasaporte)" | FR de integración con dirección y contraparte; el nombre del producto se traslada a `plan.md` |
| **R4** | Tarea programada | "Consulta automatizada a API u-noticias" | FR con disparador temporal + `[NEEDS CLARIFICATION: periodicidad]` |
| **R5** | Verbo de mejora sin métrica ("reducir", "mejorar", "facilitar") | "Reducir duplicidad", "Mejorar la visibilidad" | Criterio de éxito + duda de métrica. **Nunca un FR** |
| **R6** | Tecnología nombrada | "BD relacionales PostgreSQL", "Proxy Nginx", "Docker" | Contexto técnico dado en `plan.md` + límite en `constitution.md`. **Fuera de `spec.md`** |
| **R7** | Imposibilidad o límite externo | "Sistema u-papers no expone API" | Restricción + FR compensatorio explícitamente derivado (p.ej. carga manual), con la causa citada |

## Prohibiciones de la reescritura

- **No fusionar** post-it de secciones distintas, salvo relación de calidad declarada
  (un post-it es condición de calidad del otro; ambas trazas quedan citadas).
- **No traducir un post-it a dos FR**: si se necesita, el post-it es ambiguo → emitir duda.
- **No completar sujetos**: si el canvas no dice qué rol ejecuta la acción, el requisito
  usa el placeholder `{rol}` y abre una duda.

## Forma canónica del requisito

```
FR-nnn El sistema DEBE {verbo observable} {objeto} {condición}.
  ← {canvas} / {sección} "{texto literal del post-it}"
  Escenario: Dado {precondición}, cuando {evento}, entonces {resultado observable}.
```

- Sujeto siempre "el sistema" (o "{rol}" cuando la acción es humana y el rol está declarado).
- **Prohibidos** los verbos "gestionar", "manejar" y "soportar" sin objeto: no son verificables.
- La flecha `←` (canvas / sección / texto literal entre comillas) es **obligatoria**:
  es la traza que permite calcular cobertura sin abrir el PDF.

## Por qué esto es una función y no un estilo

Las siete reglas son **funciones totales sobre el conjunto de post-it**: todo post-it cae en
exactamente una. Eso permite (a) predecir la salida antes de ejecutar, (b) auditar
discrepancias como error de regla y no de criterio, y (c) medir cobertura como una
igualdad, no como una impresión.

## Reglas de prefijo de bundle (asociadas a R2/R3/R4/R7)

- Cada FR lleva el `bundle.code` del censo del Structural como prefijo: `FR-ETL-001`, `FR-CMS-001`, `FR-INT-001`.
- Sin prefijo, dos bundles que tocan la misma entidad producen requisitos indistinguibles y `/speckit.tasks` genera trabajo duplicado.
- Formato: `FR-{bundle.code}-{NNN}` con `NNN` zero-padded a 3 dígitos.
- Si el post-it no permite identificar el bundle (p.ej. dice "el worker" sin nombre), el prefijo se obtiene de la sección `Bundles & components` del propio canvas; si también ahí falta, se emite duda.
- Los `Helpers` y otras reglas de soporte pueden usar el prefijo `HE-{bundle.code}-{NNN}` para traceability, pero no se emiten como requisitos visibles para el usuario.
