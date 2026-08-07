'use strict';
const http = require('node:http');
const { randomUUID } = require('node:crypto');
const { StockError, queryStock } = require('./stock-service');
const port = Number(process.env.PORT || 8080);
const demoToken = process.env.POS_BEARER_TOKEN || 'local-demo-token';
function json(res, status, body, id) { res.writeHead(status, {'content-type':'application/json; charset=utf-8','x-correlation-id':id}); res.end(JSON.stringify(body)); }
const server = http.createServer((req, res) => {
  const id = req.headers['x-correlation-id'] || randomUUID();
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  if (req.method === 'GET' && url.pathname === '/health') return json(res, 200, {status:'ok'}, id);
  const match = url.pathname.match(/^\/api\/v1\/pos\/stock\/([^/]+)$/);
  if (req.method !== 'GET' || !match) return json(res, 404, {codigoError:'RUTA_NO_ENCONTRADA',mensaje:'Ruta inexistente','X-Correlation-ID':id,fechaHora:new Date().toISOString()}, id);
  if (req.headers.authorization !== `Bearer ${demoToken}`) return json(res, 401, {codigoError:'TOKEN_INVALIDO',mensaje:'Token ausente, vencido, revocado o inválido','X-Correlation-ID':id,fechaHora:new Date().toISOString()}, id);
  const scopes = new Set(String(req.headers['x-demo-scopes'] || '').split(' ').filter(Boolean));
  if (!scopes.has('stock.read')) return json(res, 403, {codigoError:'PERMISO_INSUFICIENTE',mensaje:'Se requiere stock.read',campoAfectado:'scope','X-Correlation-ID':id,fechaHora:new Date().toISOString()}, id);
  try {
    const stock = queryStock(decodeURIComponent(match[1]), url.searchParams.get('idLocal'), url.searchParams.get('idUbicacion'), scopes.has('stock.lot.read'));
    console.log(JSON.stringify({evento:'consulta-stock',codigoProducto:match[1],idLocal:url.searchParams.get('idLocal'),idUbicacion:url.searchParams.get('idUbicacion'),resultado:'exitoso',fechaHora:new Date().toISOString()}));
    return json(res, 200, {...stock,'X-Correlation-ID':id}, id);
  } catch (error) {
    const known = error instanceof StockError;
    return json(res, known?error.status:500, {codigoError:known?error.code:'ERROR_INTERNO',mensaje:known?error.message:'Error interno',campoAfectado:known?error.field:undefined,'X-Correlation-ID':id,fechaHora:new Date().toISOString()}, id);
  }
});
server.listen(port, '0.0.0.0', () => console.log(`Stock POS disponible en http://localhost:${port}`));
