
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

ruta_vendedor = Blueprint("ruta_vendedor", __name__)

@app.route('/vendedor', methods=['GET'])
def vendedor():
    return render_template("vendedor/vendedor-home.html")

@app.route('/vendedor/ventas', methods=['GET'])
def vendedor_ventas():
    return render_template("vendedor/vendedor-pedidos.html")

@app.route('/vendedor/productos', methods=['GET'])
def vendedor_productos():
    return render_template("vendedor/vendedor-productos.html")

