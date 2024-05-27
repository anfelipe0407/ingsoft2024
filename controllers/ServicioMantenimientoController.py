# app/controllers/servicio_mantenimiento_controller.py
from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.ServicioMantenimientoModel import ServicioMantenimiento, ServicioMantenimientoSchema
from models.UsuarioModel import Usuario, UsuarioSchema
from models.ProductoModel import Producto, ProductoSchema

servicio_mantenimiento_schema = ServicioMantenimientoSchema()
servicios_mantenimiento_schema = ServicioMantenimientoSchema(many=True)

ruta_servicio_mantenimiento = Blueprint('ruta_servicio_mantenimiento', __name__)

@ruta_servicio_mantenimiento.route('/servicios_mantenimiento', methods=['GET'])
def get_servicios_mantenimiento():
    try:
        # Obtener todos los servicios de mantenimiento
        servicios = ServicioMantenimiento.query.all()

        if not servicios:
            return jsonify({"message": "No se encontraron servicios de mantenimiento."}), 404

        # Preparar la lista de resultados con el esquema de servicios de mantenimiento
        result = []
        for servicio in servicios:
            servicio_data = servicio_mantenimiento_schema.dump(servicio)

            # Obtener la información del empleado
            empleado = Usuario.query.get(servicio.id_empleado)
            empleado_data = {
                'id': empleado.id,
                'nombre': empleado.nombre,
                'apellidos': empleado.apellidos,
                'num_telefono': empleado.num_telefono,
                'usuario': empleado.usuario,
                'rol': empleado.rol
            }

            # Obtener la información del cliente
            cliente = Usuario.query.get(servicio.id_cliente)
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellidos': cliente.apellidos,
                'num_telefono': cliente.num_telefono,
                'usuario': cliente.usuario,
                'rol': cliente.rol
            }

            # Obtener la información del producto
            producto = Producto.query.get(servicio.id_producto)
            producto_data = {
                'id': producto.id,
                'nombre': producto.nombre,
                'categoria': producto.categoria  # Suponiendo que producto.categoria es un campo de tipo cadena
            }

            # Anidar la información del empleado, cliente, y producto en el servicio de mantenimiento
            servicio_data['empleado'] = empleado_data
            servicio_data['cliente'] = cliente_data
            servicio_data['producto'] = producto_data

            result.append(servicio_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    
    
    

@ruta_servicio_mantenimiento.route('/servicios_mantenimiento', methods=['POST'])
def create_servicio_mantenimiento():
    try:
        data = request.json 
        nuevo_servicio_mantenimiento = ServicioMantenimiento(
            id_empleado=data['id_empleado'],
            id_producto=data['id_producto'],
            id_cliente=data['id_cliente'],
            estado=data['estado']
        )
        bd.session.add(nuevo_servicio_mantenimiento)
        bd.session.commit()
        return servicio_mantenimiento_schema.jsonify(nuevo_servicio_mantenimiento)
    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400

@ruta_servicio_mantenimiento.route('/servicios_mantenimiento/<int:id>', methods=['PUT'])
def editar_servicio_mantenimiento(id):
    try:
        servicio = ServicioMantenimiento.query.get(id)
        if not servicio:
            return jsonify({"message": "Servicio de mantenimiento no encontrado"}), 404

        # Obtener los datos del formulario enviado en la solicitud PUT
        data = request.get_json()
        servicio.estado = data['estado']

        # Guardar los cambios en la base de datos
        bd.session.commit()

        return jsonify({"message": "Servicio de mantenimiento actualizado exitosamente"}), 200

    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    

# ! TECNICO
@ruta_servicio_mantenimiento.route('/servicios_mantenimiento/tecnico/<int:id_empleado>', methods=['GET'])
def get_servicios_mantenimiento_tecnico(id_empleado):
    try:
        # Obtener todos los servicios de mantenimiento
        servicios = ServicioMantenimiento.query.filter_by(id_empleado=id_empleado).all()
        
        if not servicios:
            return jsonify({"message": "No se encontraron servicios de mantenimiento."}), 404

        # Preparar la lista de resultados con el esquema de servicios de mantenimiento
        result = []
        for servicio in servicios:
            servicio_data = servicio_mantenimiento_schema.dump(servicio)

            # Obtener la información del empleado
            empleado = Usuario.query.get(servicio.id_empleado)
            empleado_data = {
                'id': empleado.id,
                'nombre': empleado.nombre,
                'apellidos': empleado.apellidos,
                'num_telefono': empleado.num_telefono,
                'usuario': empleado.usuario,
                'rol': empleado.rol
            }

            # Obtener la información del cliente
            cliente = Usuario.query.get(servicio.id_cliente)
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellidos': cliente.apellidos,
                'num_telefono': cliente.num_telefono,
                'usuario': cliente.usuario,
                'rol': cliente.rol
            }

            # Obtener la información del producto
            producto = Producto.query.get(servicio.id_producto)
            producto_data = {
                'id': producto.id,
                'nombre': producto.nombre,
                'categoria': producto.categoria  # Suponiendo que producto.categoria es un campo de tipo cadena
            }

            # Anidar la información del empleado, cliente, y producto en el servicio de mantenimiento
            servicio_data['empleado'] = empleado_data
            servicio_data['cliente'] = cliente_data
            servicio_data['producto'] = producto_data

            result.append(servicio_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500

# ! CLIENTE
@ruta_servicio_mantenimiento.route('/servicios_mantenimiento/cliente/<int:id_cliente>', methods=['GET'])
def get_servicios_mantenimiento_cliente(id_cliente):
    try:
        # Obtener todos los servicios de mantenimiento
        servicios = ServicioMantenimiento.query.filter_by(id_cliente=id_cliente).all()
        
        if not servicios:
            return jsonify({"message": "No se encontraron servicios de mantenimiento."}), 404

        # Preparar la lista de resultados con el esquema de servicios de mantenimiento
        result = []
        for servicio in servicios:
            servicio_data = servicio_mantenimiento_schema.dump(servicio)

            # Obtener la información del empleado
            empleado = Usuario.query.get(servicio.id_empleado)
            empleado_data = {
                'id': empleado.id,
                'nombre': empleado.nombre,
                'apellidos': empleado.apellidos,
                'num_telefono': empleado.num_telefono,
                'usuario': empleado.usuario,
                'rol': empleado.rol
            }

            # Obtener la información del cliente
            cliente = Usuario.query.get(servicio.id_cliente)
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellidos': cliente.apellidos,
                'num_telefono': cliente.num_telefono,
                'usuario': cliente.usuario,
                'rol': cliente.rol
            }

            # Obtener la información del producto
            producto = Producto.query.get(servicio.id_producto)
            producto_data = {
                'id': producto.id,
                'nombre': producto.nombre,
                'categoria': producto.categoria  # Suponiendo que producto.categoria es un campo de tipo cadena
            }

            # Anidar la información del empleado, cliente, y producto en el servicio de mantenimiento
            servicio_data['empleado'] = empleado_data
            servicio_data['cliente'] = cliente_data
            servicio_data['producto'] = producto_data

            result.append(servicio_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500