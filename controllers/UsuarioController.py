from flask import Blueprint, jsonify
from config.db import bd, ma, app

from models.UsuarioModel import Usuario, UsuarioSchema

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

ruta_usuario = Blueprint('ruta_usuario', __name__)

# Ruta para obtener todos los usuarios
@ruta_usuario.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    resultado = usuarios_schema.dump(usuarios)
    return jsonify(resultado)
