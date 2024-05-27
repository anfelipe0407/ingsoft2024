# app/models/detalle_pedido.py
from config.db import bd, ma, app

class DetallePedido(bd.Model):
    __tablename__ = "detalles_pedido"
    id = bd.Column(bd.Integer, primary_key=True)
    id_pedido = bd.Column(bd.Integer, bd.ForeignKey('pedidos.id'))
    id_producto = bd.Column(bd.Integer, bd.ForeignKey('productos.id'))
    cantidad = bd.Column(bd.Integer)
    precio_unitario = bd.Column(bd.Float)

    def __init__(self, id_pedido, id_producto, cantidad, precio_unitario):
        self.id_pedido = id_pedido
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

with app.app_context():
    bd.create_all()

class DetallePedidoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_pedido', 'id_producto', 'cantidad', 'precio_unitario')
