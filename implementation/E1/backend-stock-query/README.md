# Backend Stock Query

Bundle Node.js de una sola capacidad: `FNC-BCK-AO-01`, trazada a `FR-BCK-GENERAL-003`. Implementa la consulta de stock disponible por producto para POS.

## Ejecución

Con Docker: `.\run.cmd`. Solo construir y probar: `.\run.cmd --build-only`.

Con Node.js 20+: `npm test` y `npm start`.

```powershell
Invoke-RestMethod -Uri 'http://localhost:8080/api/v1/pos/stock/MED-001?idLocal=LOCAL-001&idUbicacion=VENTA' -Headers @{Authorization='Bearer local-demo-token'; 'x-demo-scopes'='stock.read stock.lot.read'; 'X-Correlation-ID'='demo-001'}
```

El adaptador local usa datos en memoria y `x-demo-scopes`, por lo que la demostración no exige PostgreSQL ni GCP. En producción, el stack declarado sigue siendo Node.js/PostgreSQL/GCP y el gateway OAuth 2.0 Client Credentials debe validar el JWT (máximo 60 minutos), ámbito y permisos.
