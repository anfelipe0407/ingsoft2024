# app/controllers/factura_controller.py
from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.FacturaModel import Factura, FacturaSchema
from models.ProductoModel import Producto
from models.UsuarioModel import Usuario
from models.PedidoModel import Pedido
from models.ServicioMantenimientoModel import ServicioMantenimiento

factura_schema = FacturaSchema()
facturas_schema = FacturaSchema(many=True)

ruta_factura = Blueprint('ruta_factura', __name__)

@ruta_factura.route('/facturas', methods=['POST'])

@ruta_factura.route('/facturas', methods=['GET'])
def get_facturas():
    try:
        # Obtener todas las facturas
        facturas = Factura.query.all()

        if not facturas:
            return jsonify({"message": "No se encontraron facturas."}), 404

        # Preparar la lista de resultados con el esquema de facturas
        result = []
        for factura in facturas:
            factura_data = factura_schema.dump(factura)

            # Obtener la información del pedido si existe
            if factura.id_pedido:
                pedido = Pedido.query.get(factura.id_pedido)
                pedido_data = {
                    'id': pedido.id,
                    'id_cliente': pedido.id_cliente,
                    'id_vendedor': pedido.id_vendedor,
                    'fecha_emision': pedido.fecha_emision,
                    'fecha_completo': pedido.fecha_completo,
                    'estado': pedido.estado,
                    # Puedes agregar más campos según sea necesario
                }

                # Obtener la información del vendedor del pedido
                vendedor_pedido = Usuario.query.get(pedido.id_vendedor)
                pedido_data['vendedor'] = {
                    'id': vendedor_pedido.id,
                    'nombre': vendedor_pedido.nombre,
                    'apellidos': vendedor_pedido.apellidos,
                    'num_telefono': vendedor_pedido.num_telefono,
                    'usuario': vendedor_pedido.usuario,
                    'rol': vendedor_pedido.rol
                }
                
                cliente_pedido = Usuario.query.get(pedido.id_cliente)
                pedido_data['cliente'] = {
                    'id': cliente_pedido.id,
                    'nombre': cliente_pedido.nombre,
                    'apellidos': cliente_pedido.apellidos,
                    'num_telefono': cliente_pedido.num_telefono,
                    'usuario': cliente_pedido.usuario,
                    'rol': cliente_pedido.rol
                }

                factura_data['pedido'] = pedido_data

            # Obtener la información del servicio de mantenimiento si existe
            if factura.id_servicio:
                servicio = ServicioMantenimiento.query.get(factura.id_servicio)
                servicio_data = {
                    'id': servicio.id,
                    'id_empleado': servicio.id_empleado,
                    'id_producto': servicio.id_producto,
                    'id_cliente': servicio.id_cliente,
                    'estado': servicio.estado,
                    # Puedes agregar más campos según sea necesario
                }

                # Obtener la información del vendedor del servicio de mantenimiento
                cliente_servicio = Usuario.query.get(servicio.id_empleado)
                servicio_data['vendedor'] = {
                    'id': cliente_servicio.id,
                    'nombre': cliente_servicio.nombre,
                    'apellidos': cliente_servicio.apellidos,
                    'num_telefono': cliente_servicio.num_telefono,
                    'usuario': cliente_servicio.usuario,
                    'rol': cliente_servicio.rol
                }
                
                cliente_servicio = Usuario.query.get(servicio.id_cliente)
                servicio_data['cliente'] = {
                    'id': cliente_servicio.id,
                    'nombre': cliente_servicio.nombre,
                    'apellidos': cliente_servicio.apellidos,
                    'num_telefono': cliente_servicio.num_telefono,
                    'usuario': cliente_servicio.usuario,
                    'rol': cliente_servicio.rol
                }

                # Obtener la información del producto del servicio de mantenimiento
                producto_servicio = Producto.query.get(servicio.id_producto)
                servicio_data['producto'] = {
                    'id': producto_servicio.id,
                    'nombre': producto_servicio.nombre,
                    'categoria': producto_servicio.categoria,
                    # Puedes agregar más campos según sea necesario
                }

                factura_data['servicio_mantenimiento'] = servicio_data

            result.append(factura_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500

def create_factura():
    try:
        data = request.json 
        nueva_factura = Factura(
            id_pedido=data.get('id_pedido'),
            id_servicio=data.get('id_servicio'),
            costo_total=data['costo_total'],
            estado=data['estado']
        )
        bd.session.add(nueva_factura)
        bd.session.commit()
        return factura_schema.jsonify(nueva_factura)
    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400
