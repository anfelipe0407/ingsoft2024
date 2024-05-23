from flask import Flask, render_template, request, json, jsonify, redirect
from config.db import app

# ! PLANTILLAS
from controllers.AuthController import ruta_auth
from controllers.EmpresaController import ruta_empresa
from controllers.ClienteController import ruta_cliente
from controllers.AdministradorController import ruta_admin
from controllers.VendedorController import ruta_vendedor

app.register_blueprint(ruta_auth, url_prefix="/")
app.register_blueprint(ruta_empresa, url_prefix="/")
app.register_blueprint(ruta_cliente, url_prefix="/")
app.register_blueprint(ruta_admin, url_prefix="/")
app.register_blueprint(ruta_vendedor, url_prefix="/")

# ! API
from controllers.RolController import ruta_roles  
from controllers.UsuarioController import ruta_usuario  
from controllers.ProvedorController import ruta_proveedor
from controllers.ProductoController import ruta_producto
from controllers.InventarioProvedorController import ruta_inventario_proveedor
from controllers.CotizacionController import ruta_cotizacion
from controllers.FacturaCotizacionController import ruta_factura_cotizacion
from controllers.CotizacionProductosController import ruta_cotizacion_productos
from controllers.OrdenCompraController import ruta_orden_compra
from controllers.InventarioEmpresaController import ruta_inventario_empresa
from controllers.OrdenCompraProductosController import ruta_orden_compra_productos
from controllers.FacturaOrdenCompraController import ruta_factura_orden_compra

app.register_blueprint(ruta_roles, url_prefix="/api")
app.register_blueprint(ruta_usuario, url_prefix="/api")
app.register_blueprint(ruta_proveedor, url_prefix="/api")
app.register_blueprint(ruta_producto, url_prefix="/api")
app.register_blueprint(ruta_inventario_proveedor, url_prefix="/api")
app.register_blueprint(ruta_cotizacion, url_prefix="/api")
app.register_blueprint(ruta_factura_cotizacion, url_prefix="/api")
app.register_blueprint(ruta_cotizacion_productos, url_prefix="/api")
app.register_blueprint(ruta_orden_compra, url_prefix="/api")
app.register_blueprint(ruta_inventario_empresa, url_prefix="/api")
app.register_blueprint(ruta_orden_compra_productos, url_prefix="/api")
app.register_blueprint(ruta_factura_orden_compra, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)