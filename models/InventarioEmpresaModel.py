# app/models/inventario_empresa.py
from config.db import bd, ma, app

class InventarioEmpresa(bd.Model):
    __tablename__ = "inventario_empresa"
    id = bd.Column(bd.Integer, primary_key=True)
    id_producto = bd.Column(bd.Integer, bd.ForeignKey('productos.id'))
    cantidad = bd.Column(bd.Integer)
    id_orden_compra = bd.Column(bd.Integer, bd.ForeignKey('orden_compra.id'))

    def __init__(self, id_producto, cantidad, id_orden_compra):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.id_orden_compra = id_orden_compra

with app.app_context():
    bd.create_all()

class InventarioEmpresaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_producto', 'cantidad', 'id_orden_compra')
