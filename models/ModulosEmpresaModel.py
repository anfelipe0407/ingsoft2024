# app/models/usuario.py
from config.db import bd, ma, app

class ModulosEmpresa(bd.Model):
    __tablename__ = "modulosempresas"
    id = bd.Column(bd.Integer, primary_key=True)
    id_modulo = bd.Column(bd.Integer, bd.ForeignKey('modulos.id'))
    id_empresa = bd.Column(bd.Integer, bd.ForeignKey('empresas.id'))

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

with app.app_context():
    bd.create_all()

class ModulosEmpresaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_modulo', 'id_empresa')
