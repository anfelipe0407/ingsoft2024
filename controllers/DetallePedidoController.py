# app/controllers/detalle_pedido_controller.py
from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.DetallePedido import DetallePedido, DetallePedidoSchema

detalle_pedido_schema = DetallePedidoSchema()
detalles_pedido_schema = DetallePedidoSchema(many=True)

ruta_detalle_pedido = Blueprint('ruta_detalle_pedido', __name__)

@ruta_detalle_pedido.route('/detalles_pedido', methods=['POST'])
def create_detalle_pedido():
    try:
        data = request.json 
        nuevo_detalle_pedido = DetallePedido(
            id_pedido=data['id_pedido'],
            id_producto=data['id_producto'],
            cantidad=data['cantidad'],
            precio_unitario=data['precio_unitario']
        )
        bd.session.add(nuevo_detalle_pedido)
        bd.session.commit()
        return detalle_pedido_schema.jsonify(nuevo_detalle_pedido)
    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400
