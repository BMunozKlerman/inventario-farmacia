# Repository Guidelines

## Pipeline

- Mantener las fuentes PDF únicamente en `resources/` y tratarlas como inmutables.
- Usar `7cs-canvas-ingest` sólo para separar y enrutar; nunca para escribir COM.
- Entregar cada candidato a todas las skills lectoras.
- Hacer que cada lectora acepte sólo su canvas, devuelva `ignored` para el resto y genere un COM literal.
- Tratar Functional A como Front y Functional B como Back.
- Usar `7cs-com-transform` como primera etapa autorizada para interpretar los COM.
- No volver al PDF después de generar los COM: éstos son la única fuente de verdad.
- Componer y auditar antes de generar plan, tareas o código.

## Evidencia e identificadores

Conservar texto literal, errores ortográficos, sección, `bbox`, `parent`, secciones vacías e identificadores estables. No inventar métricas, atributos, periodicidades, contratos, permisos ni topología. Usar `[NEEDS CLARIFICATION: ...]` cuando corresponda.

## Validación

```bash
python3 -m unittest discover -s tests
```

Exigir cobertura de trazas igual a 1,00 y que la prueba de falsabilidad rechace la eliminación de una traza.
