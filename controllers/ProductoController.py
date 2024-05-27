# app/controllers/producto_controller.py
from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.ProductoModel import Producto, ProductoSchema

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

ruta_producto = Blueprint('ruta_producto', __name__)

@ruta_producto.route('/productos', methods=['GET'])
def get_productos():
    # try:
        usuarios = Producto.query.all()
        if not usuarios:
            return jsonify({"message": "No se encontraron usuarios."}), 404
        result = productos_schema.dump(usuarios)
        return jsonify(result)
    # except Exception as e:
    #     error_message = "Error al procesar la solicitud: {}".format(str(e))

@ruta_producto.route('/productos/crear', methods=['POST'])
def create_producto():
    try:
        data = request.json 
        nuevo_producto = Producto(
            nombre=data['nombre'],
            categoria=data['categoria'],
            precio_unitario_actual=data['precio_unitario_actual'],
            stock_actual=data['stock_actual']
        )
        bd.session.add(nuevo_producto)
        bd.session.commit()
        return producto_schema.jsonify(nuevo_producto)
    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400

@ruta_producto.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    try:
        producto = Producto.query.get(id)
        if not producto:
            return jsonify({"message": "Producto no encontrado"}), 404

        # Obtener los datos del formulario enviado en la solicitud PUT
        data = request.get_json()
        producto.nombre = data['nombre']
        producto.categoria = data['categoria']
        producto.precio_unitario_actual = data['precio_unitario_actual']
        producto.stock_actual = data['stock_actual']

        # Guardar los cambios en la base de datos
        bd.session.commit()

        return jsonify({"message": "Producto actualizado exitosamente"}), 200

    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500
