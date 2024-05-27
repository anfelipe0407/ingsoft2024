from flask import Flask, render_template, request, json, jsonify, redirect
from config.db import app

# ! PLANTILLAS
from controllers.PlantillaLoginController import ruta_login
from controllers.PlantillaAdminController import ruta_admin
from controllers.PlantillaVendedorController import ruta_vendedor
from controllers.PlantillaTecnicoController import ruta_tecnico
from controllers.PlantillaClienteController import ruta_cliente

app.register_blueprint(ruta_login, url_prefix="/")
app.register_blueprint(ruta_admin, url_prefix="/")
app.register_blueprint(ruta_vendedor, url_prefix="/")
app.register_blueprint(ruta_tecnico, url_prefix="/")
app.register_blueprint(ruta_cliente, url_prefix="/")

# ! API
from controllers.UsuarioController import ruta_usuario  
from controllers.ProductoController import ruta_producto  
from controllers.PedidoController import ruta_pedido
from controllers.DetallePedidoController import ruta_detalle_pedido
from controllers.ServicioMantenimientoController import ruta_servicio_mantenimiento
from controllers.FacturaController import ruta_factura

app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_producto, url_prefix="/api")
app.register_blueprint(ruta_pedido, url_prefix="/api")
app.register_blueprint(ruta_detalle_pedido, url_prefix="/api")
app.register_blueprint(ruta_servicio_mantenimiento, url_prefix="/api")
app.register_blueprint(ruta_factura, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)