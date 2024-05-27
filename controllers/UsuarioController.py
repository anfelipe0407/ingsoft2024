# app/controllers/usuario_controller.py
from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.UsuarioModel import Usuario, UsuarioSchema

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

ruta_usuario = Blueprint('ruta_usuario', __name__)

@ruta_usuario.route('/login', methods=['POST'])
def login():
    try:
        data = request.json 
        
        if not data["clave"] or not data["usuario"] or not data["rol"]:
            raise ValueError("Uno o más campos están vacíos")
        
        usuario = Usuario.query.filter_by(
            usuario=data["usuario"],
            clave=data["clave"],
            rol=data["rol"]
        ).first()
        
        if usuario is None:
            raise ValueError("Usuario o clave incorrectos")

        result = usuario_schema.dump(usuario)
        return jsonify(result)

    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400
    
@ruta_usuario.route('/usuarios', methods=['GET'])
def get_usuarios():
    try:
        usuarios = Usuario.query.all()
        if not usuarios:
            return jsonify({"message": "No se encontraron usuarios."}), 404
        result = usuarios_schema.dump(usuarios)
        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    
@ruta_usuario.route('/usuarios/<string:rol>', methods=['GET'])
def get_usuarios_por_rol(rol):
    try:
        usuarios = Usuario.query.filter_by(rol=rol).all()
        if not usuarios:
            return jsonify({"message": "No se encontraron usuarios con el rol especificado."}), 404
        result = usuarios_schema.dump(usuarios)
        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    
@ruta_usuario.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    # try:
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"message": "Usuario no encontrado"}), 404

    # Obtener los datos del formulario enviado en la solicitud PUT
    data = request.get_json()
    usuario.nombre = data['nombre']
    usuario.apellidos = data['apellidos']
    usuario.num_telefono = data['num_telefono']
    usuario.usuario = data['usuario']
    usuario.rol = data['rol']
    usuario.clave = data['clave']

    # Guardar los cambios en la base de datos
    bd.session.commit()

    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

    # except Exception as e:
    #     error_message = "Error al procesar la solicitud: {}".format(str(e))
    #     return jsonify({"error": error_message}), 500