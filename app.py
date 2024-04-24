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
# * home
@app.route('/empresa', methods=['GET'])
def empresa_home():
    return render_template("empresa/homeempresa.html")

# * Configuracion
@app.route('/empresa/configuracion', methods=['GET'])
def empresa_config():
    return render_template("empresa/empresa-configuracion.html")

# * Inventario
@app.route('/empresa/inventario', methods=['GET'])
def empresa_inventario():
    return render_template("empresa/empresa-inventario.html")

@app.route('/empresa/inventario/crear', methods=['GET'])
def empresa_inventario_crear():
    return render_template("empresa/empresa-inventario-crear.html")

# * Ordenes de compra
@app.route('/empresa/ordenes', methods=['GET'])
def empresa_ordenes():
    return render_template("empresa/empresa-ordenes.html")

@app.route('/empresa/ordenes/nueva', methods=['GET'])
def empresa_ordenes_nueva():
    return render_template("empresa/empresa-ordenes-nueva.html")

@app.route('/empresa/ordenes/ver', methods=['GET'])
def empresa_ordenes_ver():
    return render_template("empresa/empresa-ordenes-ver.html")

# * Provedores
@app.route('/empresa/provedores', methods=['GET'])
def empresa_provedores():
    return render_template("empresa/empresa-provedores.html")

if __name__ == '__main__':
    app.run(debug=True)