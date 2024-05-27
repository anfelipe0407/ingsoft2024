console.log("ADMINISTRADOR USUARIOS JS");

const BASE_URL = "http://127.0.0.1:5000/api";

let productos = [];

window.onload = function () {
  getProductos();
};

function getProductos() {
  const url = BASE_URL + "/productos";
  console.log(url);
  
  axios
    .get(url)
    .then((response) => {
      console.log(response.data);
      productos = response.data; // Guardar los usuarios en una variable global
      // Actualizar la tabla de usuarios
      const productosTbody = document.getElementById("productos-tbody");
      productosTbody.innerHTML = ""; // Limpiar la tabla antes de añadir nuevos datos
      productos.forEach((producto) => {
        const row = `<tr>
                        <th scope="row">${producto.id}</th>
                        <td>${producto.nombre}</td>
                        <td>${producto.categoria}</td>
                        <td>${producto.precio_unitario_actual}</td>
                        <td>${producto.stock_actual}</td>
                        <td><button class="btn btn-warning" onclick="editProducto(${producto.id})">Editar</button></td>
                      </tr>`;
        productosTbody.insertAdjacentHTML("beforeend", row);
      });
    })
    .catch((error) => {
      console.error("Hubo un error!", error);
    });
}

function editProducto(id) {
  const producto = productos.find((p) => p.id === id);
  const modal = document.getElementById("myModal");
  const form = document.getElementById("editProductForm");

  // Llenar el formulario con los datos del producto
  document.getElementById("nombre").value = producto.nombre;
  document.getElementById("categoria").value = producto.categoria;
  document.getElementById("precio").value = producto.precio_unitario_actual;
  document.getElementById("stock").value = producto.stock_actual;

  modal.style.display = "block";

  // Cuando el usuario haga clic en <span> (x), cerrar la modal
  const span = document.getElementsByClassName("close")[0];
  span.onclick = function () {
    modal.style.display = "none";
  };

  // Cuando el usuario haga clic fuera de la modal, cerrarla
  window.onclick = function (event) {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  };

  // Evitar que el formulario se envíe
  form.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario
    
    // Obtener los datos del formulario
    const nombre = document.getElementById("nombre").value;
    const categoria = document.getElementById("categoria").value;
    const precio = document.getElementById("precio").value;
    const stock = document.getElementById("stock").value;

    // Actualizar los datos del producto en la lista
    producto.nombre = nombre;
    producto.categoria = categoria;
    producto.precio_unitario_actual = precio;
    producto.stock_actual = stock;

    axios
      .put(`${BASE_URL}/productos/${producto.id}`, producto)
      .then((response) => {
        console.log(response.data);

        Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Cambios guardados",
            showConfirmButton: false,
            timer: 1500
        });

        getProductos();

        modal.style.display = "none";
      })
      .catch((error) => {
        console.error("Hubo un error!", error);

        Swal.fire({
            position: "top-end",
            icon: "error",
            title: "Error al guardar cambios",
            showConfirmButton: false,
            timer: 1500
        });
      });

    modal.style.display = "none";

    // Actualizar la lista de productos
    getProductos();
  });
}
