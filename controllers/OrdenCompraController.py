from flask import Blueprint, jsonify
from models.OrdenCompraModel import OrdenCompra, OrdenCompraSchema

orden_compra_schema = OrdenCompraSchema()
ordenes_compra_schema = OrdenCompraSchema(many=True)

ruta_orden_compra = Blueprint('ruta_orden_compra', __name__)

# Ruta para obtener todas las órdenes de compra
@ruta_orden_compra.route('/ordenes_compra', methods=['GET'])
def obtener_ordenes_compra():
    todas_las_ordenes_compra = OrdenCompra.query.all()
    resultado = ordenes_compra_schema.dump(todas_las_ordenes_compra)
    return jsonify(resultado)
