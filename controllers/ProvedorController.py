from flask import Blueprint, jsonify
from models.ProvedorModel import Proveedor, ProveedorSchema

proveedor_schema = ProveedorSchema()
proveedores_schema = ProveedorSchema(many=True)

ruta_proveedor = Blueprint('ruta_proveedor', __name__)

# Ruta para obtener todos los proveedores
@ruta_proveedor.route('/proveedores', methods=['GET'])
def obtener_proveedores():
    todos_los_proveedores = Proveedor.query.all()
    resultado = proveedores_schema.dump(todos_los_proveedores)
    return jsonify(resultado)
