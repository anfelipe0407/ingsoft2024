document.addEventListener("DOMContentLoaded", function() {
    const tableBody = document.getElementById("tableBody");
    const numElementos = document.getElementById("numElementos");
    const pagination = document.getElementById("pagination");

    numElementos.addEventListener("change", function() {
        showPage(1); // Mostrar la primera página al cambiar el número de elementos
    });

    function showPage(pageNumber) {
        const elementosPorPagina = parseInt(numElementos.value);
        const rows = tableBody.querySelectorAll("tr");

        const startIndex = (pageNumber - 1) * elementosPorPagina;
        const endIndex = pageNumber * elementosPorPagina;

        rows.forEach((row, index) => {
            if (index >= startIndex && index < endIndex) {
                row.style.display = "table-row";
            } else {
                row.style.display = "none";
            }
        });

        renderPagination(rows.length, pageNumber, elementosPorPagina);
    }

    function renderPagination(totalItems, currentPage, itemsPerPage) {
        pagination.innerHTML = "";

        const totalPages = Math.ceil(totalItems / itemsPerPage);

        for (let i = 1; i <= totalPages; i++) {
            const button = document.createElement("button");
            button.innerText = i;

            if (i === currentPage) {
                button.classList.add("active");
            }

            button.addEventListener("click", function() {
                showPage(i);
            });

            pagination.appendChild(button);
        }
    }
});

function buscar() {
  const input = document.getElementById('search');
  const filter = input.value.toUpperCase();
  const table = document.getElementById('myTable');
  const rows = table.getElementsByTagName('tr');

  for (let i = 0; i < rows.length; i++) {
      let firstCol = rows[i].getElementsByTagName('td')[0];
      if (firstCol) {
          let idValue = firstCol.textContent || firstCol.innerText;
          if (idValue.trim().toUpperCase() === filter) {
            rows[i].style.display = '';
        } else {
            rows[i].style.display = 'none';
        }
      }
  }
}

//guardar cliente en la bdd

document.addEventListener('DOMContentLoaded', function() {
    // Obtener el cuerpo de la tabla
    const tableBody = document.getElementById('tableBody');

    // Hacer una solicitud para obtener los datos de los clientes desde el servidor
    axios.get('/obtener_clientes')
        .then(function(response) {
            const clientes = response.data;

            // Iterar sobre la lista de clientes y agregar cada cliente como una fila en la tabla
            clientes.forEach(function(cliente) {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${cliente.id}</td>
                    <td>${cliente.nombre}</td>
                    <td>${cliente.cantidad}</td>
                    <td>
                        <button class="editar" onclick="editarCliente(${cliente.id})">
                            <i class="fas fa-pencil-alt"></i>
                        </button>
                        <button class="eliminar" onclick="eliminarCliente(${cliente.id})">
                            <i class="fas fa-trash-alt"></i>
                        </button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(function(error) {
            console.error('Error al obtener los datos de los clientes:', error);
        });
});

function editarCliente(id) {
    // Lógica para editar el cliente con el ID dado
    
}

function eliminarCliente(id) {
    // Lógica para eliminar el cliente con el ID dado
   
}