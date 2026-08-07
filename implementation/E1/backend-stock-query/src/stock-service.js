'use strict';

class StockError extends Error {
  constructor(status, code, message, field) { super(message); this.status = status; this.code = code; this.field = field; }
}

const inventory = [
  { codigoProducto: 'MED-001', descripcion: 'Paracetamol 500 mg', idEstablecimiento: 'EST-001', idLocal: 'LOCAL-001', idUbicacion: 'VENTA', unidadMedida: 'unidad', enabled: true, fechaHoraActualizacion: '2026-08-05T00:00:00.000Z', lots: [
    { numeroLote: 'LOT-B', fechaVencimiento: '2027-12-31', fisico: 40, reservado: 0, comprometido: 5, bloqueado: 0, noApto: 0 },
    { numeroLote: 'LOT-A', fechaVencimiento: '2027-06-30', fisico: 120, reservado: 10, comprometido: 5, bloqueado: 0, noApto: 0 }
  ] },
  { codigoProducto: 'MED-001', descripcion: 'Paracetamol 500 mg', idEstablecimiento: 'EST-001', idLocal: 'LOCAL-001', idUbicacion: 'Vencidos', unidadMedida: 'unidad', enabled: true, fechaHoraActualizacion: '2026-08-05T00:00:00.000Z', lots: [
    { numeroLote: 'LOT-V', fechaVencimiento: '2026-01-31', fisico: 20, reservado: 0, comprometido: 0, bloqueado: 0, noApto: 20 }
  ] }
];

const available = (lot) => Math.max(0, lot.fisico - lot.reservado - lot.comprometido - lot.bloqueado - lot.noApto);

function queryStock(codigoProducto, idLocal, idUbicacion, includeLots = true) {
  if (!codigoProducto) throw new StockError(400, 'PARAMETRO_OBLIGATORIO', 'codigoProducto es obligatorio', 'codigoProducto');
  if (!idLocal) throw new StockError(400, 'PARAMETRO_OBLIGATORIO', 'idLocal es obligatorio', 'idLocal');
  if (!idUbicacion) throw new StockError(400, 'PARAMETRO_OBLIGATORIO', 'idUbicacion es obligatorio', 'idUbicacion');
  const product = inventory.find((item) => item.codigoProducto === codigoProducto && item.idLocal === idLocal && item.idUbicacion === idUbicacion);
  if (!product) throw new StockError(404, 'RECURSO_NO_ENCONTRADO', 'Producto, local o ubicación inexistente');
  if (!product.enabled) throw new StockError(409, 'PRODUCTO_NO_HABILITADO', 'El producto no está habilitado para la ubicación');
  const t = product.lots.reduce((s, x) => ({ fisico:s.fisico+x.fisico, reservado:s.reservado+x.reservado, comprometido:s.comprometido+x.comprometido, bloqueado:s.bloqueado+x.bloqueado, noApto:s.noApto+x.noApto, disponible:s.disponible+available(x) }), { fisico:0, reservado:0, comprometido:0, bloqueado:0, noApto:0, disponible:0 });
  const vencidos = product.idUbicacion === 'Vencidos';
  const result = { codigoProducto:product.codigoProducto, descripcion:product.descripcion, idEstablecimiento:product.idEstablecimiento, idLocal:product.idLocal, idUbicacion:product.idUbicacion, stockFisico:t.fisico, stockReservado:t.reservado, stockComprometido:t.comprometido, stockBloqueado:t.bloqueado, stockNoAptoVenta:t.noApto, stockDisponible:vencidos?0:t.disponible, unidadMedida:product.unidadMedida, estadoDisponibilidad:vencidos?'No disponible para venta':(t.disponible?'Disponible':'Sin stock'), fechaHoraActualizacion:product.fechaHoraActualizacion };
  if (includeLots) result.lotes = product.lots.map((x) => ({ numeroLote:x.numeroLote, fechaVencimiento:x.fechaVencimiento, stockDisponibleLote:vencidos?0:available(x) })).sort((a,b) => a.fechaVencimiento.localeCompare(b.fechaVencimiento));
  return result;
}

module.exports = { StockError, queryStock };
