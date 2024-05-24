from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.UsuarioModel import Usuario, UsuarioSchema
from models.RolModel import Rol, RolSchema

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

ruta_usuario = Blueprint('ruta_usuario', __name__)

# ! LOGIN
@ruta_usuario.route('/login', methods=['POST'])
def login():
    try:
        data = request.json 
        
        if not data["clave"] or not data["usuario"]:
            raise ValueError("Uno o más campos están vacíos")
        
        if not data["rol"]["id"] or not data["rol"]["nombre"]:
            raise ValueError("Uno o más campos en 'rol' están vacíos")
        
        usuario = Usuario.query.filter_by(
            usuario=data["usuario"],
            contraseña=data["clave"],
        ).first() 

        if usuario is None:
            return jsonify({"error": "Usuario no encontrado"}), 404

        rol_usuario = Rol.query.get(usuario.rol_id)
        
        if rol_usuario.rol != data["rol"]["nombre"]:
            return jsonify({"error": "El rol proporcionado no coincide con el rol del usuario"}), 400
        
        return jsonify({
            "message": "Login correcto"
        })
    
    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400 