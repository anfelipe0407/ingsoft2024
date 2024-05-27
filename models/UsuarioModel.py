# app/models/usuario.py
from config.db import bd, ma, app

class Usuario(bd.Model):
    __tablename__ = "usuarios"
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    apellidos = bd.Column(bd.String(50))
    num_telefono = bd.Column(bd.Integer)
    usuario = bd.Column(bd.String(50))
    clave = bd.Column(bd.String(50))
    rol = bd.Column(bd.Enum('administrador', 'vendedor', 'tecnico', 'cliente'))

    def __init__(self, nombre, apellidos, num_telefono, usuario, clave, rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.num_telefono = num_telefono
        self.usuario = usuario
        self.clave = clave
        self.rol = rol

with app.app_context():
    bd.create_all()

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellidos', 'num_telefono', 'usuario', 'clave', 'rol')
