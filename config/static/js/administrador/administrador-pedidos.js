console.log("ADMINISTRADOR USUARIOS JS");

const BASE_URL = "http://127.0.0.1:5000/api";

let pedidos = [];

// Definir la clase Subject
class Subject {
  constructor() {
    this.observers = [];
  }

  addObserver(observer) {
    this.observers.push(observer);
  }

  removeObserver(observer) {
    this.observers = this.observers.filter(obs => obs !== observer);
  }

  notifyObservers() {
    this.observers.forEach(observer => observer.update());
  }
}

// Definir la interfaz Observer
class Observer {
  update() {
    // A implementar por los observadores concretos
  }
}

// Definir la clase Pedidos como sujeto observable
class Pedidos extends Subject {
  constructor() {
    super();
  }

  setPedidos(newPedidos) {
    pedidos = newPedidos;
    this.notifyObservers();
  }

  getPedidos() {
    const url = BASE_URL + "/pedidos";
    axios
      .get(url)
      .then(response => {
        this.setPedidos(response.data);
      })
      .catch(error => {
        console.error("Hubo un error!", error);
      });
  }
}

// Crear una instancia de Pedidos
const pedidosSubject = new Pedidos();

// Definir la función que actualiza la tabla de pedidos
function updatePedidosTable() {
  const productosTbody = document.getElementById("productos-tbody");
  productosTbody.innerHTML = "";
  pedidos.forEach(pedido => {
    const estado = pedido.estado === 1 ? "Completado" : "Pendiente";
    const estadoCss = pedido.estado === 1 ? "bg-green" : "bg-red";

    const row = `<tr>
                        <td>${pedido.id}</td>
                        <td>${pedido.cliente.nombre}</td>
                        <td>${pedido.vendedor.nombre}</td>
                        <td><div class="circulo-estado ${estadoCss}"></div> ${estado}</td>
                        <td><button class="btn btn-warning" onclick="editProducto(${pedido.id})">Editar</button></td>
                      </tr>`;
    productosTbody.insertAdjacentHTML("beforeend", row);
  });
}

// Agregar la función update a la lista de observadores de pedidosSubject
pedidosSubject.addObserver({
  update: updatePedidosTable
});

window.onload = function() {
  pedidosSubject.getPedidos();
};

function editProducto(id) {
  const pedido = pedidos.find(p => p.id === id);
  const modal = document.getElementById("myModal");
  const form = document.getElementById("editPedidoForm");

  // Llenar el formulario con los datos del pedido
  document.getElementById("nombre_cliente").value = pedido.cliente.nombre;
  document.getElementById("nombre_vendedor").value = pedido.vendedor.nombre;
  document.getElementById("estado").value = pedido.estado;

  modal.style.display = "block";

  // Cuando el usuario haga clic en <span> (x), cerrar la modal
  const span = document.getElementsByClassName("close")[0];
  span.onclick = function() {
    modal.style.display = "none";
  };

  // Cuando el usuario haga clic fuera de la modal, cerrarla
  window.onclick = function(event) {
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

    // Actualizar el estado del pedido en la lista
    pedido.estado = estado;
    const url = `${BASE_URL}/pedidos/${pedido.id}`;
    console.log("url: " + url);

    axios
      .put(url, pedido)
      .then(response => {
        console.log(response.data);

        Swal.fire({
          position: "top-end",
          icon: "success",
          title: "Cambios guardados",
          showConfirmButton: false,
          timer: 1500
        });

        pedidosSubject.getPedidos();

        modal.style.display = "none";
      })
      .catch(error => {
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
