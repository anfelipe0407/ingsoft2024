console.log("VENDEDOR PEDIDOS/VENTAS JS");

const BASE_URL = "http://127.0.0.1:5000/api";
const id_cliente = localStorage.getItem("id_usuario");

window.onload = function () {
  getProductos();
};

let productos = [];
let carrito = [];

function getProductos() {
  const url = BASE_URL + "/productos";
  console.log(url);

  axios
    .get(url)
    .then((response) => {
      console.log(response.data);
      productos = response.data; // Guardar los productos en una variable global
      // Actualizar la tabla de productos
      const productosTbody = document.getElementById("productos-tbody");
      productosTbody.innerHTML = ""; // Limpiar la tabla antes de añadir nuevos datos
      productos.forEach((producto) => {
        const row = `<tr>
                              <td>${producto.id}</td>
                              <td>${producto.nombre}</td>
                              <td>${producto.categoria}</td>
                              <td>${producto.precio_unitario_actual}</td>
                              <td>${producto.stock_actual}</td>
                              <td>
                                  <input type="number" id="cantidad-${producto.id}" 
                                      min="0" max="${producto.stock_actual}" 
                                      step="1" value="0" 
                                      onchange="updateCantidad(${producto.id}, ${producto.stock_actual})">
                              </td>
                              <td><button class="btn btn-warning" onclick="addToCart(${producto.id}, '${producto.nombre}', ${producto.precio_unitario_actual})">Añadir</button></td>
                          </tr>`;
        productosTbody.insertAdjacentHTML("beforeend", row);
      });
    })
    .catch((error) => {
      console.error("Hubo un error!", error);
    });
}

function updateCantidad(productId, maxCantidad) {
  const cantidadInput = document.getElementById(`cantidad-${productId}`);
  let cantidad = parseInt(cantidadInput.value);

  if (cantidad > maxCantidad) {
    cantidad = maxCantidad;
    cantidadInput.value = maxCantidad;
  } else if (cantidad < 0) {
    cantidad = 0;
    cantidadInput.value = 0;
  }
}

function addToCart(productId, nombre, precioUnitario) {
  const cantidadInput = document.getElementById(`cantidad-${productId}`);
  const cantidad = parseInt(cantidadInput.value);

  if (cantidad > 0) {
    const productoExistente = carrito.find((item) => item.id === productId);

    if (productoExistente) {
      productoExistente.cantidad += cantidad;
    } else {
      carrito.push({
        id: productId,
        cantidad: cantidad,
        precio_unitario: precioUnitario,
      });
    }

    renderCarrito();
  }
}

function renderCarrito() {
  const carritoDiv = document.getElementById("carrito-list");
  carritoDiv.innerHTML = ""; // Limpiar el carrito antes de añadir nuevos datos

  let total = 0;
  carrito.forEach((item) => {
    console.log(item);
    const producto = productos.find((p) => p.id === item.id);
    const subtotal = item.cantidad * item.precio_unitario;

    total += subtotal;

    const row = `<div class="carrito-item">
                      <span>${producto.nombre}</span>
                      <span>Cantidad: ${item.cantidad}</span>
                      <span>Precio unidad: ${item.precio_unitario}</span>
                  </div>`;
    carritoDiv.insertAdjacentHTML("beforeend", row);
  });

  carritoDiv.insertAdjacentHTML("beforeend", `<div>Total: $${total}</div>`);

  if (carrito.length > 0) {
    carritoDiv.insertAdjacentHTML(
      "beforeend",
      `<button class="btn btn-primary" onclick="hacerPedido()">Hacer Pedido</button>`
    );
  }
}

function actualizarCarrito() {
  const carritoList = document.getElementById("carrito-list");
  carritoList.innerHTML = ""; // Limpiar la lista antes de añadir nuevos datos
  let total = 0;

  carrito.forEach((producto) => {
    const item = `<li>
                    ${producto.nombre} - ${producto.cantidad} unidades - $${(
      producto.precio * producto.cantidad
    ).toFixed(2)}
                 </li>`;
    carritoList.insertAdjacentHTML("beforeend", item);
    total += producto.precio * producto.cantidad;
  });

  const carritoTotal = document.getElementById("carrito-total");
  carritoTotal.innerHTML = `Total: $${total.toFixed(2)}`;

  const hacerPedidoBtn = document.getElementById("hacer-pedido");
  if (carrito.length > 0) {
    hacerPedidoBtn.style.display = "block";
  } else {
    hacerPedidoBtn.style.display = "none";
  }
}

function hacerPedido() {
  const url = BASE_URL + "/pedidos/cliente/create";
  const pedidoData = {
    id_cliente: id_cliente,
    id_vendedor: id_cliente,
    productos: carrito,
  };

  axios
    .post(url, pedidoData)
    .then((response) => {
      console.log(response.data);

      setTimeout(function () {
        window.location.href =
          "http://127.0.0.1:5000/cliente/pedidos";
      }, 500);

      Swal.fire({
        position: "top-end",
        icon: "success",
        title: "Pedido hecho correctamente",
        showConfirmButton: false,
        timer: 1500,
      });
    })
    .catch((error) => {
      console.error("Hubo un error!", error);

      Swal.fire({
        position: "top-end",
        icon: "error",
        title: "Error al hacer el pedido",
        showConfirmButton: false,
        timer: 1500
    });
    });
}
