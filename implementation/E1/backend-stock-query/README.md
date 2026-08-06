# Backend Stock Query

Slice ejecutable del bundle backend Node.js para un único post-it:
`FNC-BCK-APO-01`, trazado a `FR-BCK-003`.

## Ejecutar con Docker

```powershell
.\run.cmd
```

Para construir y ejecutar las pruebas sin iniciar el servidor:

```powershell
.\run.cmd --build-only
```

Consultar desde otra consola:

```powershell
Invoke-RestMethod `
  -Uri 'http://localhost:8080/api/stock?productCode=SKU-001&locationId=LOCAL-001' `
  -Headers @{'x-api-key'='local-demo-key'}
```

## Ejecutar con Node.js 20+

```powershell
npm test
npm start
```

El repositorio en memoria es un adaptador de demostración. Puede reemplazarse por PostgreSQL sin cambiar el contrato HTTP ni la lógica de cálculo validada.
