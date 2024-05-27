# app/models/pedido.py
from config.db import bd, ma, app

class Pedido(bd.Model):
    __tablename__ = "pedidos"
    id = bd.Column(bd.Integer, primary_key=True)
    id_cliente = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'))
    id_vendedor = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'))
    fecha_emision = bd.Column(bd.String(50))
    fecha_completo = bd.Column(bd.String(50))
    estado = bd.Column(bd.Integer)

    def __init__(self, id_cliente, id_vendedor, estado):
        self.id_cliente = id_cliente
        self.id_vendedor = id_vendedor
        self.estado = estado

with app.app_context():
    bd.create_all()

class PedidoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_cliente', 'id_vendedor', 'estado')
