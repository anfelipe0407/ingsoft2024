from flask import Blueprint, jsonify
from models.CotizacionModel import Cotizacion, CotizacionSchema

cotizacion_schema = CotizacionSchema()
cotizaciones_schema = CotizacionSchema(many=True)

ruta_cotizacion = Blueprint('ruta_cotizacion', __name__)

# Ruta para obtener todas las cotizaciones
@ruta_cotizacion.route('/cotizaciones', methods=['GET'])
def obtener_cotizaciones():
    todas_las_cotizaciones = Cotizacion.query.all()
    resultado = cotizaciones_schema.dump(todas_las_cotizaciones)
    return jsonify(resultado)
