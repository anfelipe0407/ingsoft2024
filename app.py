from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)

# ! RUTA SHEYLA
@app.route('/vendedor', methods=['GET'])
def home_vendedor():
    return render_template("vendedor/homevendedor.html")
@app.route('/vendedor/productos', methods=['GET'])
def productos_vendedor():
    return render_template("vendedor/productosvendedor.html")
@app.route('/vendedor/cliente', methods=['GET'])
def clientes_vendedor():
    return render_template("vendedor/clientesvendedor.html")
@app.route('/vendedor/cotizaciones', methods=['GET'])
def cotizaciones_vendedor():
    return render_template("vendedor/cotizacionesvendedor.html")
@app.route('/vendedor/informes', methods=['GET'])
def informes_vendedor():
    return render_template("vendedor/informesvendedor.html")
@app.route('/vendedor/hacercotizaciones', methods=['GET'])
def hacercotizaciones_vendedor():
    return render_template("/vendedor/hacercotizacionesvendedor.html")


# ! RUTA GUSTAVO
@app.route('/administrador', methods=['GET'])
def administrador_home():
    return render_template("administrador/administradorhome.html")

@app.route('/administrador/empresas', methods=['GET'])
def Empresas():
    return render_template("administrador/empresas.html")

# ! RUTA AGUILAR
@app.route('/empresa', methods=['GET'])
def home_empresa():
    return render_template("empresa/homeempresa.html")

@app.route('/empresa/configuracion', methods=['GET'])
def config_empresa():
    return render_template("empresa/empresa-configuracion.html")

@app.route('/empresa/inventario', methods=['GET'])
def inventario_empresa():
    return render_template("empresa/empresa-inventario.html")

@app.route('/empresa/inventario/crear', methods=['GET'])
def inventario_empresa_crear():
    return render_template("empresa/empresa-inventario-crear.html")

if __name__ == '__main__':
    app.run(debug=True)