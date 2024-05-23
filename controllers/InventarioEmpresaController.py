from flask import Blueprint, jsonify
from models.InventarioEmpresaModel import InventarioEmpresa, InventarioEmpresaSchema

inventario_empresa_schema = InventarioEmpresaSchema()
inventarios_empresa_schema = InventarioEmpresaSchema(many=True)

ruta_inventario_empresa = Blueprint('ruta_inventario_empresa', __name__)

# Ruta para obtener el inventario de la empresa
@ruta_inventario_empresa.route('/inventario_empresa', methods=['GET'])
def obtener_inventario_empresa():
    inventario_empresa = InventarioEmpresa.query.all()
    resultado = inventarios_empresa_schema.dump(inventario_empresa)
    return jsonify(resultado)
