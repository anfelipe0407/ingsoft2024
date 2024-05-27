# app/models/producto.py
from config.db import bd, ma, app

class Producto(bd.Model):
    __tablename__ = "productos"
    id = bd.Column(bd.Integer, primary_key=True)
    nombre = bd.Column(bd.String(50))
    categoria = bd.Column(bd.String(50))
    precio_unitario_actual = bd.Column(bd.Float)
    stock_actual = bd.Column(bd.Integer)

    def __init__(self, nombre, categoria, precio_unitario_actual, stock_actual):
        self.nombre = nombre
        self.categoria = categoria
        self.precio_unitario_actual = precio_unitario_actual
        self.stock_actual = stock_actual

with app.app_context():
    bd.create_all()

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'categoria', 'precio_unitario_actual', 'stock_actual')
