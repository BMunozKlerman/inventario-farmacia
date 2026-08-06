'use strict';

const http = require('node:http');
const { randomUUID } = require('node:crypto');
const { StockError, queryStock } = require('./stock-service');

const port = Number(process.env.PORT || 8080);
const apiKey = process.env.POS_API_KEY || 'local-demo-key';

function json(response, status, body, correlationId) {
  response.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'x-correlation-id': correlationId
  });
  response.end(JSON.stringify(body));
}

const server = http.createServer((request, response) => {
  const correlationId = request.headers['x-correlation-id'] || randomUUID();
  const url = new URL(request.url, `http://${request.headers.host || 'localhost'}`);

  if (request.method !== 'GET' || url.pathname !== '/api/stock') {
    return json(response, 404, { code: 'ROUTE_NOT_FOUND', message: 'Ruta inexistente', correlationId, timestamp: new Date().toISOString() }, correlationId);
  }
  if (request.headers['x-api-key'] !== apiKey) {
    return json(response, 401, { code: 'UNAUTHORIZED', message: 'Autenticación ausente o inválida', correlationId, timestamp: new Date().toISOString() }, correlationId);
  }

  try {
    const stock = queryStock(url.searchParams.get('productCode'), url.searchParams.get('locationId'));
    return json(response, 200, stock, correlationId);
  } catch (error) {
    const known = error instanceof StockError;
    return json(response, known ? error.status : 500, {
      code: known ? error.code : 'INTERNAL_ERROR',
      message: known ? error.message : 'Error interno',
      field: known ? error.field : undefined,
      correlationId,
      timestamp: new Date().toISOString()
    }, correlationId);
  }
});

server.listen(port, '0.0.0.0', () => {
  console.log(`Backend stock query disponible en http://localhost:${port}`);
});
