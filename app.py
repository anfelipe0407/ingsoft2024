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
# ! RUTA GUSTAVO

# ! RUTA AGUILAR
@app.route('/empresa', methods=['GET'])
def home_empresa():
    return render_template("empresa/homeempresa.html")


if __name__ == '__main__':
    app.run(debug=True)