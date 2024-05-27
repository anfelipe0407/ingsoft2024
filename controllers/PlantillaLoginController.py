
from flask import Blueprint, Flask, render_template, request
from config.db import bd, ma, app

ruta_login = Blueprint("ruta_login", __name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template("login/login.html")

