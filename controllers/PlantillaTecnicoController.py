
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

ruta_tecnico = Blueprint("ruta_tecnico", __name__)

@app.route('/tecnico', methods=['GET'])
def tecnico():
    return render_template("tecnico/tecnico-home.html")

@app.route('/tecnico/mantenimientos', methods=['GET'])
def tecnico_mantenimientos():
    return render_template("tecnico/tecnico-mantenimientos.html")

