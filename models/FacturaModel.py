# app/models/factura.py
from config.db import bd, ma, app

class Factura(bd.Model):
    __tablename__ = "facturas"
    id = bd.Column(bd.Integer, primary_key=True)
    id_pedido = bd.Column(bd.Integer, bd.ForeignKey('pedidos.id'), nullable=True)
    id_servicio = bd.Column(bd.Integer, bd.ForeignKey('servicios_mantenimiento.id'), nullable=True)
    costo_total = bd.Column(bd.Float)
    estado = bd.Column(bd.Integer)

    def __init__(self, id_pedido, id_servicio, costo_total, estado):
        self.id_pedido = id_pedido
        self.id_servicio = id_servicio
        self.costo_total = costo_total
        self.estado = estado

with app.app_context():
    bd.create_all()

class FacturaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_pedido', 'id_servicio', 'costo_total', 'estado')
