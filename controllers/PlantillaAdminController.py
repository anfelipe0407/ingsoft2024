
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

ruta_admin = Blueprint("route_admin", __name__)

@app.route('/administrador/', methods=['GET'])
def administrador():
    return render_template("administrador/administrador-home.html")

@app.route('/administrador/usuarios', methods=['GET'])
def administrador_usuarios():
    return render_template("administrador/administrador-usuarios.html")

@app.route('/administrador/productos', methods=['GET'])
def administrador_productos():
    return render_template("administrador/administrador-productos.html")

@app.route('/administrador/pedidos', methods=['GET'])
def administrador_pedidos():
    return render_template("administrador/administrador-pedidos.html")

@app.route('/administrador/mantenimientos', methods=['GET'])
def administrador_mantenimientos():
    return render_template("administrador/administrador-mantenimientos.html")

@app.route('/administrador/facturas', methods=['GET'])
def administrador_facturas():
    return render_template("administrador/administrador-facturas.html")

