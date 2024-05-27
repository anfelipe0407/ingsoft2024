# app/models/servicio_mantenimiento.py
from config.db import bd, ma, app

class ServicioMantenimiento(bd.Model):
    __tablename__ = "servicios_mantenimiento"
    id = bd.Column(bd.Integer, primary_key=True)
    id_empleado = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'))
    id_producto = bd.Column(bd.Integer, bd.ForeignKey('productos.id'))
    id_cliente = bd.Column(bd.Integer, bd.ForeignKey('usuarios.id'))
    estado = bd.Column(bd.Integer)

    def __init__(self, id_empleado, id_producto, id_cliente, estado):
        self.id_empleado = id_empleado
        self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.estado = estado

with app.app_context():
    bd.create_all()

class ServicioMantenimientoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_empleado', 'id_producto', 'id_cliente', 'estado')
