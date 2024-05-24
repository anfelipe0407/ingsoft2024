from flask import Blueprint, jsonify
from models.ProductoModel import Producto, ProductoSchema


producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

ruta_producto = Blueprint('ruta_producto', __name__)

# Ruta para obtener todos los productos
@ruta_producto.route('/productos', methods=['GET'])
def obtener_productos():
    todos_los_productos = Producto.query.all()
    resultado = productos_schema.dump(todos_los_productos)
    return jsonify(resultado)


@ruta_producto.route('/productos-listado', methods=['GET'])
def productoslistado():
 
    productos = Producto.query.all()
    
    producto_schema = ProductoSchema(many=True)
    output = producto_schema.dump(productos)
    
    return jsonify(output)