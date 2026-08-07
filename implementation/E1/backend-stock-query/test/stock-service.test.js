'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { StockError, queryStock } = require('../src/stock-service');
test('calcula saldo y ordena lotes por FEFO', () => { const r=queryStock('MED-001','LOCAL-001','VENTA'); assert.equal(r.stockFisico,160); assert.equal(r.stockDisponible,140); assert.deepEqual(r.lotes.map(x=>x.numeroLote),['LOT-A','LOT-B']); });
test('rechaza parámetros obligatorios ausentes', () => assert.throws(() => queryStock('','LOCAL-001','VENTA'), e => e instanceof StockError && e.status===400));
test('informa recurso inexistente', () => assert.throws(() => queryStock('MED-404','LOCAL-001','VENTA'), e => e instanceof StockError && e.status===404));
test('Vencidos cuenta físicamente pero no está disponible', () => { const r=queryStock('MED-001','LOCAL-001','Vencidos'); assert.equal(r.stockFisico,20); assert.equal(r.stockDisponible,0); assert.equal(r.estadoDisponibilidad,'No disponible para venta'); });
