
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

ruta_cliente = Blueprint("ruta_cliente", __name__)

@app.route('/cliente', methods=['GET'])
def cliente():
    return render_template("cliente/cliente-home.html")

@app.route('/cliente/pedidos', methods=['GET'])
def cliente_pedidos():
    return render_template("cliente/cliente-pedidos.html")

@app.route('/cliente/mantenimientos', methods=['GET'])
def cliente_mantenimientos():
    return render_template("cliente/cliente-mantenimientos.html")

