console.log("ADMINISTRADOR USUARIOS JS");

const BASE_URL = "http://127.0.0.1:5000/api";

let facturas = [];

window.onload = function () {
  getFacturas();
};

function getFacturas() {
  const url = BASE_URL + "/facturas";
  console.log(url);

  axios
    .get(url)
    .then((response) => {
      console.log(response.data);
      facturas = response.data; // Guardar las facturas en una variable global
      // Actualizar la tabla de facturas
      const productosTbody = document.getElementById("productos-tbody");
      productosTbody.innerHTML = ""; // Limpiar la tabla antes de añadir nuevos datos
      facturas.forEach((factura) => {
        const iconoPedido =
          factura.id_pedido !== null
            ? '<i class="fa fa-check-circle"></i>'
            : "";
        const iconoServicio =
          factura.id_servicio !== null
            ? '<i class="fa fa-check-circle"></i>'
            : "";

        const row = `<tr>
                              <td>${factura.id}</td>
                              <td>${iconoPedido}</td>
                              <td>${iconoServicio}</td>
                              <td>${factura.costo_total}</td>
                              <td>
                                <button class="btn btn-warning" onclick="verDetalle(${factura.id})">Ver Detalle</button>
                              </td>
                          </tr>`;
        productosTbody.insertAdjacentHTML("beforeend", row);
      });
    })
    .catch((error) => {
      console.error("Hubo un error!", error);
    });
}

function verDetalle(facturaId) {
  const factura = facturas.find((factura) => facturaId === factura.id);

  // Verificar si la factura es de un pedido o de un servicio de mantenimiento
  if (factura.id_pedido) {
    console.log("ES FACTURA PEDIDO");
    // Factura de pedido
    const pedido = factura.pedido;
    document.getElementById("pedido_nombre_cliente").value =
      pedido.cliente.nombre;
    document.getElementById("pedido_nombre_empleado").value =
      pedido.vendedor.nombre;
    document.getElementById("pedido_fecha_emision").value =
      pedido.fecha_emision;
    document.getElementById("pedido_fecha_completo").value =
      pedido.fecha_completo || '<< Sin completar >>';

    document.querySelector("#detallePedido").style.display = "block";
  } else if (factura.id_servicio) {
    console.log("ES FACTURA SERVICIO");
    // Factura de servicio de mantenimiento
    const servicio = factura.servicio_mantenimiento;
    document.getElementById("servicio_nombre_cliente").value =
      servicio.cliente.nombre;
    document.getElementById("servicio_nombre_empleado").value =
      servicio.vendedor.nombre;
    document.getElementById("servicio_nombre_producto").value =
      servicio.producto.nombre;
    document.getElementById("servicio_categoria_producto").value =
      servicio.producto.categoria;

    document.querySelector("#detalleServicio").style.display = "block";

  }
  // Configurar el estado
  document.getElementById("estado_factura").value =
    factura.estado === 1 ? "1" : "0"; // Convertir el estado a cadena
  // Mostrar la modal
  document.getElementById("myModal").style.display = "block";
}

// Añadir evento de clic al botón de cierre de la modal
document.querySelector(".close").addEventListener("click", () => {
  document.getElementById("myModal").style.display = "none";
  document.querySelector("#detallePedido").style.display = "none";
  document.querySelector("#detalleServicio").style.display = "none";
});

// Añadir evento de clic al área fuera de la modal para cerrarla
window.addEventListener("click", (event) => {
  if (event.target === document.getElementById("myModal")) {
    document.getElementById("myModal").style.display = "none";
  }
});

function editServicio(id) {
  const servicio = facturas.find((s) => s.id === id);
  const modal = document.getElementById("myModal");
  const form = document.getElementById("editServicioForm");

  console.log("id", id);
  console.log(facturas);
  console.log("servicio EDIT: ", servicio);

  // Llenar el formulario con los datos del servicio
  document.getElementById("nombre_cliente").value = servicio.cliente.nombre;
  document.getElementById("nombre_empleado").value = servicio.empleado.nombre;
  document.getElementById("nombre_producto").value = servicio.producto.nombre;
  document.getElementById("categoria_producto").value =
    servicio.producto.nombre;
  document.getElementById("estado").value = servicio.estado;

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

  // Eliminar cualquier listener de evento submit existente
  const newForm = form.cloneNode(true);
  form.parentNode.replaceChild(newForm, form);

  // Añadir un nuevo listener de evento submit
  newForm.addEventListener("submit", function (event) {
    console.log("SUBMIT EDIT FORM");
    event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario

    // Obtener los datos del formulario
    const estado = document.getElementById("estado").value;

    // Actualizar el estado del servicio en la lista
    servicio.estado = estado;
    const url = `${BASE_URL}/servicios_mantenimiento/${servicio.id}`;
    console.log("url: " + url);

    axios
      .put(url, servicio)
      .then((response) => {
        console.log(response.data);

        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "Cambios guardados",
          showConfirmButton: false,
          timer: 1500,
        });

        getFacturas();

        modal.style.display = "none";
      })
      .catch((error) => {
        console.error("Hubo un error!", error);

        Swal.fire({
          position: "top-end",
          icon: "error",
          title: "Error al guardar cambios",
          showConfirmButton: false,
          timer: 1500,
        });
      });
  });
}
