# Backend Stock Query

Bundle Node.js de una sola capacidad: `FNC-BCK-AO-01`, trazada a `FR-BCK-GENERAL-003`.
Implementa la consulta de stock disponible por producto para POS.

## Ejecutar con Docker

```bash
./run.sh
```

En Windows: `run.bat`.

Para construir y ejecutar las pruebas sin iniciar el servidor:

```bash
./run.sh --build-only
```

Consultar desde otra consola:

```bash
curl -H 'x-api-key: local-demo-key' 'http://localhost:8080/api/stock?productCode=SKU-001&locationId=LOCAL-001'
```

## Ejecutar con Node.js 20+

```bash
npm test
```

```bash
npm start
```

El repositorio en memoria es un adaptador de demostración. Puede reemplazarse por PostgreSQL sin cambiar el contrato HTTP ni la lógica de cálculo validada.
