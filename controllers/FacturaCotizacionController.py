from flask import Blueprint, jsonify
from models.FacturaCotizacionModel import FacturaCotizacion, FacturaCotizacionSchema

factura_cotizacion_schema = FacturaCotizacionSchema()
facturas_cotizacion_schema = FacturaCotizacionSchema(many=True)

ruta_factura_cotizacion = Blueprint('ruta_factura_cotizacion', __name__)

# Ruta para obtener todas las facturas de cotización
@ruta_factura_cotizacion.route('/facturas_cotizacion', methods=['GET'])
def obtener_facturas_cotizacion():
    todas_las_facturas_cotizacion = FacturaCotizacion.query.all()
    resultado = facturas_cotizacion_schema.dump(todas_las_facturas_cotizacion)
    return jsonify(resultado)
