from flask import Blueprint, jsonify
from models.ProductoModel import Producto, ProductoSchema
from models.UsuarioModel import Usuario, UsuarioSchema

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

ruta_producto = Blueprint('ruta_producto', __name__)

# Ruta para obtener todos los productos
@ruta_producto.route('/productos', methods=['GET'])
def obtener_productos():
    todos_los_productos = Producto.query.all()
    resultado = productos_schema.dump(todos_los_productos)
    return jsonify(resultado)