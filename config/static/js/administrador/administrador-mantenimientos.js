console.log("ADMINISTRADOR USUARIOS JS");

const BASE_URL = "http://127.0.0.1:5000/api";

let servicios = [];

window.onload = function () {
  getServicios();
};

function getServicios() {
  const url = BASE_URL + "/servicios_mantenimiento";
  console.log(url);
  
  axios
    .get(url)
    .then((response) => {
      console.log(response.data);
      servicios = response.data; // Guardar los servicios en una variable global
      // Actualizar la tabla de servicios
      const productosTbody = document.getElementById("productos-tbody");
      productosTbody.innerHTML = ""; // Limpiar la tabla antes de añadir nuevos datos
      servicios.forEach((servicio) => {

        const estado = servicio.estado === 1 ? 'Completado' : 'Pendiente';
        const estadoCss = servicio.estado === 1 ? 'bg-green' : 'bg-red';

        const row = `<tr>
                        <td>${servicio.id}</td>
                        <td>${servicio.cliente.nombre}</td>
                        <td>${servicio.empleado.nombre}</td>
                        <td>${servicio.producto.nombre}</td>
                        <td>${servicio.producto.categoria}</td>
                        <td><div class="circulo-estado ${estadoCss}"></div> ${estado}</td>
                        <td><button class="btn btn-warning" onclick="editServicio(${servicio.id})">Editar</button></td>
                      </tr>`;
        productosTbody.insertAdjacentHTML("beforeend", row);
      });
    })
    .catch((error) => {
      console.error("Hubo un error!", error);
    });
}

function editServicio(id) {
  const servicio = servicios.find((s) => s.id === id);
  const modal = document.getElementById("myModal");
  const form = document.getElementById("editServicioForm");

  console.log('id', id);
  console.log(servicios);
  console.log('servicio EDIT: ', servicio);

  // Llenar el formulario con los datos del servicio
  document.getElementById("nombre_cliente").value = servicio.cliente.nombre;
  document.getElementById("nombre_empleado").value = servicio.empleado.nombre;
  document.getElementById("nombre_producto").value = servicio.producto.nombre;
  document.getElementById("categoria_producto").value = servicio.producto.nombre;
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
  newForm.addEventListener("submit", function(event) {
    console.log("SUBMIT EDIT FORM");
    event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario
    
    // Obtener los datos del formulario
    const estado = document.getElementById("estado").value;

    // Actualizar el estado del servicio en la lista
    servicio.estado = estado;
    const url = `${BASE_URL}/servicios_mantenimiento/${servicio.id}`
    console.log('url: ' + url);

    axios
      .put(url, servicio)
      .then((response) => {
        console.log(response.data);

        Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Cambios guardados",
            showConfirmButton: false,
            timer: 1500
        });

        getServicios();

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
  });
}