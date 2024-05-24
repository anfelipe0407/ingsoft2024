from flask import Blueprint, jsonify, request
from models.ProductoModel import Producto, ProductoSchema
from models.UsuarioModel import Usuario, UsuarioSchema
from models.ProductoAlternoModel import ProductoAlterno, ProductoAlternoSchema
from models.InventarioProvedorModel import InventarioProveedor, InventarioProveedorSchema
from models.ProvedorModel import Proveedor, ProveedorSchema
from config.db import bd,ma


producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

ruta_producto = Blueprint('ruta_producto', __name__)

# Ruta para obtener todos los productos
@ruta_producto.route('/productos', methods=['GET'])
def obtener_productos():
    todos_los_productos = Producto.query.all()
    resultado = productos_schema.dump(todos_los_productos)
    return jsonify(resultado)


# @ruta_producto.route('/productos-listado', methods=['GET'])
# def productoslistado():
 
#     productos = Producto.query.all()
    
#     producto_schema = ProductoSchema(many=True)
#     output = producto_schema.dump(productos)
    
#     return jsonify(output)
#     return jsonify(resultado)




@ruta_producto.route('/productos/guardar', methods=['POST'])
def guardar_producto():
    data = request.json
    
   
    nuevo_producto = Producto(
        nombre=data.get('nombre'),
        codigo=data.get('codigo'),
        precio_unitario=data.get('precio_unitario'),
        stock_actual=data.get('stock_actual'),
        stock_minimo=data.get('stock_minimo'),
        iva=data.get('iva'),
        img="",
        descripcion="",
        descuento=0,
        estado=0  
    )
    bd.session.add(nuevo_producto)
    bd.session.commit()

    return jsonify({"message": "Producto guardado exitosamente"}), 201


@ruta_producto.route('/nombres-proveedores', methods=['GET'])
def obtener_proveedores():
    proveedores = Proveedor.query.all()
    proveedores_data = [{"id": proveedor.id, "nombre": proveedor.nombre} for proveedor in proveedores]
    return jsonify(proveedores_data)
