console.log("ADMINISTRADOR USUARIOS JS");

const BASE_URL = "http://127.0.0.1:5000/api";

let usuarios = [];

window.onload = function () {
  handleCheckboxClick(document.querySelector("input[value='todos']"));
};

function handleCheckboxClick(clickedCheckbox) {
  const checkboxes = document.querySelectorAll('input[name="userType"]');
  checkboxes.forEach((checkbox) => {
    if (checkbox !== clickedCheckbox) {
      checkbox.checked = false;
    }
  });

  const selectedRole = clickedCheckbox.value;
  let url = BASE_URL + "/usuarios";
  if (selectedRole !== "todos") {
    url += `/${selectedRole}`;
  }

  // Realizar la solicitud GET con Axios
  axios
    .get(url)
    .then((response) => {
      console.log(response.data);
      usuarios = response.data; // Guardar los usuarios en una variable global
      // Actualizar la tabla de usuarios
      const usuariosTbody = document.getElementById("usuarios-tbody");
      usuariosTbody.innerHTML = ""; // Limpiar la tabla antes de añadir nuevos datos
      usuarios.forEach((usuario) => {
        const row = `<tr>
                        <th scope="row">${usuario.id}</th>
                        <td>${usuario.nombre}</td>
                        <td>${usuario.apellidos}</td>
                        <td>${usuario.num_telefono}</td>
                        <td>${usuario.usuario}</td>
                        <td>${usuario.rol}</td>
                        <td>${usuario.clave}</td>
                        <td><button class="btn btn-warning" onclick="editUser(${usuario.id})">Editar</button></td>
                      </tr>`;
        usuariosTbody.insertAdjacentHTML("beforeend", row);
      });
    })
    .catch((error) => {
      console.error("Hubo un error!", error);
      alert("Error al realizar la solicitud.");
    });
}

function editUser(id) {
  const user = usuarios.find((usuario) => usuario.id === id);
  const modal = document.getElementById("myModal");
  const form = document.getElementById("editUserForm");

  // Llenar el formulario con los datos del usuario
  document.getElementById("nombre").value = user.nombre;
  document.getElementById("apellidos").value = user.apellidos;
  document.getElementById("num_telefono").value = user.num_telefono;
  document.getElementById("usuario").value = user.usuario;
  document.getElementById("rol").value = user.rol;
  document.getElementById("clave").value = user.clave;
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
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevenir el comportamiento predeterminado del formulario

    // Obtener los datos del formulario
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });

    console.log(data);

    // // Realizar la solicitud PUT con Axios
    axios
      .put(`${BASE_URL}/usuarios/${user.id}`, data)
      .then((response) => {
        console.log(response.data);

        Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Cambios guardados",
            showConfirmButton: false,
            timer: 1500
        });

        const checkboxes = document.querySelectorAll('input[name="userType"]');
        checkboxes.forEach((checkbox) => {
          if (checkbox.checked) {
            handleCheckboxClick(checkbox);
          }
        });

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
