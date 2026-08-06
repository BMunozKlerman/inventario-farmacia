'use strict';

const test = require('node:test');
const assert = require('node:assert/strict');
const { StockError, queryStock } = require('../src/stock-service');

test('calcula stock disponible y excluye existencias no aptas', () => {
  const result = queryStock('SKU-001', 'LOCAL-001');
  assert.equal(result.physicalStock, 140);
  assert.equal(result.unfitStock, 20);
  assert.equal(result.availableStock, 105);
  assert.equal(result.availabilityStatus, 'Disponible');
  assert.equal(result.lots.find((lot) => lot.lot === 'LOT-V').availableStock, 0);
});

test('rechaza parámetros obligatorios ausentes', () => {
  assert.throws(() => queryStock('', 'LOCAL-001'), (error) => error instanceof StockError && error.status === 400);
});

test('informa producto o local inexistente', () => {
  assert.throws(() => queryStock('SKU-404', 'LOCAL-001'), (error) => error instanceof StockError && error.status === 404);
});
