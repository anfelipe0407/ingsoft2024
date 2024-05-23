# app/models/producto.py
from config.db import bd, ma, app

class Producto(bd.Model):
    __tablename__ = "productos"
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    descripcion = bd.Column(bd.String(200))
    codigo = bd.Column(bd.Integer)
    precio_unitario = bd.Column(bd.Float)
    stock_minimo = bd.Column(bd.Integer)
    img = bd.Column(bd.String(200))
    descuento = bd.Column(bd.Float)
    iva = bd.Column(bd.Float)
    estado = bd.Column(bd.String(50))

    def __init__(self, nombre, descripcion, codigo, precio_unitario, stock_minimo, img, descuento, iva, estado):
        self.nombre = nombre
        self.descripcion = descripcion
        self.codigo = codigo
        self.precio_unitario = precio_unitario
        self.stock_minimo = stock_minimo
        self.img = img
        self.descuento = descuento
        self.iva = iva
        self.estado = estado

with app.app_context():
    bd.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'descripcion', 'codigo', 'precio_unitario', 'stock_minimo', 'img', 'descuento', 'iva', 'estado')