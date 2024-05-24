from flask import Blueprint, jsonify, request
from models.EmpresaModel import Empresa, EmpresaSchema
from config.db import bd, ma

empresa_schema = EmpresaSchema()
empresas_schema = EmpresaSchema(many=True)

ruta_empresa = Blueprint('ruta_empresa', __name__)

# ! GET ALL
@ruta_empresa.route('/empresas', methods=['GET'])
def obtener_empresas():
    todas_las_empresas = Empresa.query.all()
    resultado = empresas_schema.dump(todas_las_empresas)
    return jsonify(resultado)

# ! GET BY ID
@ruta_empresa.route('/empresas/<int:id>', methods=['GET'])
def obtener_empresa_por_id(id):
    empresa = Empresa.query.get(id)
    if empresa is None:
        return jsonify({'message': 'Empresa no encontrada'}), 404
    return empresa_schema.jsonify(empresa)

# ! CREATE
@ruta_empresa.route('/empresas/create', methods=['POST'])
def crear_empresa():
    nombre = request.json.get('nombre')
    nit = request.json.get('nit')
    correo = request.json.get('correo')
    url_asociada = request.json.get('url_asociada', '')  # Campo opcional, por defecto vacío
    porcentaje_ganancia = request.json.get('porcentaje_ganancia', 0)  # Valor por defecto
    iva_establecido = request.json.get('iva_establecido', 0)  # Valor por defecto
    descuento_general = request.json.get('descuento_general', 0)  # Valor por defecto
    vigencia_licencia_fin = request.json.get('vigencia_licencia_fin', '')  # Campo opcional, por defecto vacío

    nueva_empresa = Empresa(
        nombre=nombre,
        nit=nit,
        correo=correo,
        url_asociada=url_asociada,
        porcentaje_ganancia=porcentaje_ganancia,
        iva_establecido=iva_establecido,
        descuento_general=descuento_general,
        vigencia_licencia_fin=vigencia_licencia_fin
    )
    
    print(nueva_empresa)

    bd.session.add(nueva_empresa)
    bd.session.commit()

    return empresa_schema.jsonify(nueva_empresa)

# ! UPDATE
@ruta_empresa.route('/empresas/<int:id>', methods=['PUT'])
def actualizar_empresa(id):
    empresa = Empresa.query.get(id)
    
    if not empresa:
        return jsonify({"error": "Empresa no encontrada"}), 404

    # Actualizar los campos de la empresa con los datos del request
    empresa.nombre = request.json.get('nombre', empresa.nombre)
    empresa.nit = request.json.get('nit', empresa.nit)
    empresa.correo = request.json.get('correo', empresa.correo)
    empresa.url_asociada = request.json.get('url_asociada', empresa.url_asociada)
    empresa.porcentaje_ganancia = request.json.get('porcentaje_ganancia', empresa.porcentaje_ganancia)
    empresa.iva_establecido = request.json.get('iva_establecido', empresa.iva_establecido)
    empresa.descuento_general = request.json.get('descuento_general', empresa.descuento_general)
    empresa.vigencia_licencia_fin = request.json.get('vigencia_licencia_fin', empresa.vigencia_licencia_fin)
    
    bd.session.commit()

    return empresa_schema.jsonify(empresa)
