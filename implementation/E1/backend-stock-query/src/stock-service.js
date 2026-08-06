'use strict';

class StockError extends Error {
  constructor(status, code, message, field) {
    super(message);
    this.status = status;
    this.code = code;
    this.field = field;
  }
}

const inventory = [
  {
    productCode: 'SKU-001',
    description: 'Paracetamol 500 mg',
    locationId: 'LOCAL-001',
    unit: 'unidad',
    enabled: true,
    updatedAt: '2026-08-05T00:00:00.000Z',
    lots: [
      { lot: 'LOT-A', expiresAt: '2027-06-30', physical: 120, reserved: 10, committed: 5, blocked: 0, unfit: 0 },
      { lot: 'LOT-V', expiresAt: '2026-01-31', physical: 20, reserved: 0, committed: 0, blocked: 0, unfit: 20 }
    ]
  }
];

function available(value) {
  return Math.max(0, value.physical - value.reserved - value.committed - value.blocked - value.unfit);
}

function queryStock(productCode, locationId) {
  if (!productCode) throw new StockError(400, 'MISSING_PRODUCT_CODE', 'productCode es obligatorio', 'productCode');
  if (!locationId) throw new StockError(400, 'MISSING_LOCATION_ID', 'locationId es obligatorio', 'locationId');

  const product = inventory.find((item) => item.productCode === productCode && item.locationId === locationId);
  if (!product) throw new StockError(404, 'STOCK_NOT_FOUND', 'Producto o local inexistente');
  if (!product.enabled) throw new StockError(409, 'PRODUCT_DISABLED', 'El producto no está habilitado para el local');

  const totals = product.lots.reduce((sum, lot) => ({
    physical: sum.physical + lot.physical,
    reserved: sum.reserved + lot.reserved,
    committed: sum.committed + lot.committed,
    blocked: sum.blocked + lot.blocked,
    unfit: sum.unfit + lot.unfit,
    available: sum.available + available(lot)
  }), { physical: 0, reserved: 0, committed: 0, blocked: 0, unfit: 0, available: 0 });

  return {
    productCode: product.productCode,
    description: product.description,
    locationId: product.locationId,
    physicalStock: totals.physical,
    reservedStock: totals.reserved,
    committedStock: totals.committed,
    blockedStock: totals.blocked,
    unfitStock: totals.unfit,
    availableStock: Math.max(0, totals.available),
    unit: product.unit,
    availabilityStatus: totals.available > 0 ? 'Disponible' : 'Sin stock',
    updatedAt: product.updatedAt,
    lots: product.lots.map((lot) => ({ lot: lot.lot, expiresAt: lot.expiresAt, availableStock: available(lot) }))
  };
}

module.exports = { StockError, queryStock };
