from flask import Blueprint, jsonify
from models.EmpresaModel import Empresa, EmpresaSchema

empresa_schema = EmpresaSchema()
empresas_schema = EmpresaSchema(many=True)

ruta_empresa = Blueprint('ruta_empresa', __name__)

# Ruta para obtener todas las empresas
@ruta_empresa.route('/empresas', methods=['GET'])
def obtener_empresas():
    todas_las_empresas = Empresa.query.all()
    resultado = empresas_schema.dump(todas_las_empresas)
    return jsonify(resultado)
