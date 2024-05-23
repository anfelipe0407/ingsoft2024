from flask import Blueprint, jsonify
from models.InventarioProvedorModel import InventarioProveedor, InventarioProveedorSchema

inventario_proveedor_schema = InventarioProveedorSchema()
inventarios_proveedor_schema = InventarioProveedorSchema(many=True)

ruta_inventario_proveedor = Blueprint('ruta_inventario_proveedor', __name__)

# Ruta para obtener el inventario de un proveedor por su ID de proveedor
@ruta_inventario_proveedor.route('/inventario_proveedor/<int:id_proveedor>', methods=['GET'])
def obtener_inventario_proveedor(id_proveedor):
    inventario_proveedor = InventarioProveedor.query.filter_by(id_proveedor=id_proveedor).all()
    resultado = inventarios_proveedor_schema.dump(inventario_proveedor)
    return jsonify(resultado)
