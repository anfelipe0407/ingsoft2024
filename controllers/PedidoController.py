# app/controllers/pedido_controller.py
from flask import Blueprint, jsonify, request
from config.db import bd, ma, app

from models.PedidoModel import Pedido, PedidoSchema
from models.UsuarioModel import Usuario, UsuarioSchema
from models.PedidoModel import Pedido, PedidoSchema
from models.ProductoModel import Producto, ProductoSchema
from models.DetallePedido import DetallePedido, DetallePedidoSchema

pedido_schema = PedidoSchema()
pedidos_schema = PedidoSchema(many=True)

ruta_pedido = Blueprint('ruta_pedido', __name__)

@ruta_pedido.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        # Obtener todos los pedidos
        pedidos = Pedido.query.all()

        if not pedidos:
            return jsonify({"message": "No se encontraron pedidos."}), 404

        # Preparar la lista de resultados con el esquema de pedidos
        result = []
        for pedido in pedidos:
            pedido_data = pedido_schema.dump(pedido)

            # Obtener la información del cliente
            cliente = Usuario.query.get(pedido.id_cliente)
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellidos': cliente.apellidos,
                'num_telefono': cliente.num_telefono,
                'usuario': cliente.usuario,
                'rol': cliente.rol
            }

            # Obtener la información del vendedor
            vendedor = Usuario.query.get(pedido.id_vendedor)
            vendedor_data = {
                'id': vendedor.id,
                'nombre': vendedor.nombre,
                'apellidos': vendedor.apellidos,
                'num_telefono': vendedor.num_telefono,
                'usuario': vendedor.usuario,
                'rol': vendedor.rol
            }

            # Anidar la información del cliente y del vendedor en el pedido
            pedido_data['cliente'] = cliente_data
            pedido_data['vendedor'] = vendedor_data

            result.append(pedido_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500

@ruta_pedido.route('/pedidos', methods=['POST'])
def create_pedido():
    try:
        data = request.json 
        nuevo_pedido = Pedido(
            id_cliente=data['id_cliente'],
            id_vendedor=data['id_vendedor'],
            estado=data['estado']
        )
        bd.session.add(nuevo_pedido)
        bd.session.commit()
        return pedido_schema.jsonify(nuevo_pedido)
    except (KeyError, TypeError, ValueError) as e:
        error_message = "Error en los datos recibidos: {}".format(str(e))
        return jsonify({"error": error_message}), 400
    
@ruta_pedido.route('/pedidos/<int:id>', methods=['PUT'])
def editar_pedido(id):
    try:
        pedido = Pedido.query.get(id)
        if not pedido:
            return jsonify({"message": "Pedido no encontrado"}), 404

        # Obtener los datos del formulario enviado en la solicitud PUT
        data = request.get_json()
        pedido.estado = data['estado']

        # Guardar los cambios en la base de datos
        bd.session.commit()

        return jsonify({"message": "Pedido actualizado exitosamente"}), 200

    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500

# ! VENDEDOR -----------------------
@ruta_pedido.route('/pedidos/vendedor/<int:id_vendedor>', methods=['GET'])
def get_pedidos_vendedor(id_vendedor):
    try:
        # Obtener todos los pedidos del vendedor especificado por su ID
        pedidos = Pedido.query.filter_by(id_vendedor=id_vendedor).all()

        if not pedidos:
            return jsonify({"message": "No se encontraron pedidos para este vendedor."}), 404

        # Preparar la lista de resultados con el esquema de pedidos
        result = []
        for pedido in pedidos:
            pedido_data = pedido_schema.dump(pedido)

            # Obtener la información del cliente
            cliente = Usuario.query.get(pedido.id_cliente)
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellidos': cliente.apellidos,
                'num_telefono': cliente.num_telefono,
                'usuario': cliente.usuario,
                'rol': cliente.rol
            }

            # Obtener la información del vendedor
            vendedor = Usuario.query.get(pedido.id_vendedor)
            vendedor_data = {
                'id': vendedor.id,
                'nombre': vendedor.nombre,
                'apellidos': vendedor.apellidos,
                'num_telefono': vendedor.num_telefono,
                'usuario': vendedor.usuario,
                'rol': vendedor.rol
            }

            # Anidar la información del cliente y del vendedor en el pedido
            pedido_data['cliente'] = cliente_data
            pedido_data['vendedor'] = vendedor_data

            result.append(pedido_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500
    
    
# ! CLIENTE -----------------------
@ruta_pedido.route('/pedidos/cliente/<int:id_cliente>', methods=['GET'])
def get_pedidos_cliente(id_cliente):
    try:
        # Obtener todos los pedidos del vendedor especificado por su ID
        pedidos = Pedido.query.filter_by(id_cliente=id_cliente).all()

        if not pedidos:
            return jsonify({"message": "No se encontraron pedidos para este vendedor."}), 404

        # Preparar la lista de resultados con el esquema de pedidos
        result = []
        for pedido in pedidos:
            pedido_data = pedido_schema.dump(pedido)

            # Obtener la información del cliente
            cliente = Usuario.query.get(pedido.id_cliente)
            cliente_data = {
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellidos': cliente.apellidos,
                'num_telefono': cliente.num_telefono,
                'usuario': cliente.usuario,
                'rol': cliente.rol
            }

            # Obtener la información del vendedor
            vendedor = Usuario.query.get(pedido.id_vendedor)
            vendedor_data = {
                'id': vendedor.id,
                'nombre': vendedor.nombre,
                'apellidos': vendedor.apellidos,
                'num_telefono': vendedor.num_telefono,
                'usuario': vendedor.usuario,
                'rol': vendedor.rol
            }

            # Anidar la información del cliente y del vendedor en el pedido
            pedido_data['cliente'] = cliente_data
            pedido_data['vendedor'] = vendedor_data

            result.append(pedido_data)

        return jsonify(result)
    except Exception as e:
        error_message = "Error al procesar la solicitud: {}".format(str(e))
        return jsonify({"error": error_message}), 500

@ruta_pedido.route('/pedidos/cliente/create', methods=['POST'])
def create_pedido_cliente():
    try:
        data = request.get_json()
        id_cliente = data.get('id_cliente')
        id_vendedor = data.get('id_vendedor')
        productos = data.get('productos')
        
        # Crear el pedido
        nuevo_pedido = Pedido(id_cliente=id_cliente, id_vendedor=id_vendedor, estado=0)  # estado 0: pendiente
        bd.session.add(nuevo_pedido)
        bd.session.commit()

        # Crear los detalles del pedido y actualizar el stock de productos
        for producto in productos:
            id_producto = producto.get('id')
            cantidad = producto.get('cantidad')
            producto_db = Producto.query.get(id_producto)
            
            if producto_db and producto_db.stock_actual >= cantidad:
                precio_unitario = producto_db.precio_unitario_actual
                detalle_pedido = DetallePedido(id_pedido=nuevo_pedido.id, id_producto=id_producto, cantidad=cantidad, precio_unitario=precio_unitario)
                bd.session.add(detalle_pedido)

                # Actualizar el stock del producto
                producto_db.stock_actual -= cantidad
                bd.session.commit()
            else:
                return jsonify({"error": f"Stock insuficiente para el producto ID {id_producto}"}), 400

        return pedido_schema.jsonify(nuevo_pedido), 201
    except Exception as e:
        bd.session.rollback()
        return jsonify({"error": str(e)}), 500