
  //tabla stock
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
//buscar 
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

//paginacion de productos
document.addEventListener("DOMContentLoaded", function() {
  const productosContainer = document.querySelector("#productos-container .productos");
  const modal = document.querySelector("#modal");
const botonespaginacion=document.querySelector('#pagination-buttons')
  // Función para abrir la modal con los detalles del producto
  function abrirModal(productoId) {
      const producto = document.querySelector("#" + productoId);
      const nombre = producto.querySelector("h3").textContent;
      const precio = producto.querySelector("p").textContent;
      
      // Mostrar los detalles del producto en la modal
      document.getElementById("nombre").value = nombre;
      document.getElementById("codigo").value = productoId;
      document.getElementById("precio_unidad").value = precio;

      modal.style.display = "block";
  }

  // Mostrar productos en la página actual
  function mostrarProductosEnPagina(pagina) {
      const productos = document.querySelectorAll(".producto");
      const productosPorPagina = 6;
      const inicio = (pagina - 1) * productosPorPagina;
      const fin = inicio + productosPorPagina;

      productos.forEach((producto, index) => {
          if (index >= inicio && index < fin) {
              producto.style.display = "block";
          } else {
              producto.style.display = "none";
          }
      });
  }

  // Manejar evento de clic en un producto para abrir la modal
  productosContainer.addEventListener("click", function(event) {
      const productoId = event.target.closest(".producto").id;
      abrirModal(productoId);
  });

  // Mostrar la primera página al cargar la página
  mostrarProductosEnPagina(1);

  // Generar botones de paginación
  function generarBotonesPaginacion() {
      const totalProductos = document.querySelectorAll(".producto").length;
      const totalPaginas = Math.ceil(totalProductos / 6); // Considerando 10 productos por página

      
      for (let i = 1; i <= totalPaginas; i++) {
          const boton = document.createElement("button");
          boton.textContent = i;
          boton.addEventListener("click", function() {
              mostrarProductosEnPagina(i);
          });
          botonespaginacion.appendChild(boton);
      }

  }

  generarBotonesPaginacion();
});


// generar codigo de barras
document.getElementById('generarcod').addEventListener('click', function() {
    const codigo = document.getElementById('codigoInput').value;
    generarCodigoDeBarras(codigo);
});
function generarCodigoDeBarras(codigo) {
    JsBarcode("#codigoDeBarras")
        .options({font: "OCR-B"}) // Aplicar la fuente OCR-B
        .EAN13(codigo, {fontSize: 18, textMargin: 0})
        .blank(20) // Crear espacio entre los códigos de barras
        .render();
}



// obetener los nombres de los proveedores y ponerlos en el select
document.addEventListener('DOMContentLoaded', function () {
    let proveedorSelect = document.getElementById('proveedor');
    let endpoint ="/api/nombres-proveedores";
    axios.get(endpoint)
        .then(function (response) {
            const proveedores = response.data;
            proveedores.forEach(proveedor => {
                const option = document.createElement('option');
                option.value = proveedor.id;
                option.textContent = proveedor.nombre;
                proveedorSelect.appendChild(option);
            });
        })
        .catch(function (error) {
            console.error("Hubo un error al obtener los proveedores:", error);
        });
});

//guardar informacion devproductos  en bddd
document.getElementById('btnguardar-producto').addEventListener('click', function() {
    
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); 
     var nombre = document.querySelector('input[name="Nombre"]').value;
     var codigo = document.querySelector('input[name="Codigo"]').value;
     var precio_unitario = document.querySelector('input[name="precio_unitario"]').value;
     var iva = document.querySelector('input[name="Iva"]:checked') ? 19 : 0;
     var stock_actual = document.querySelector('input[name="stock_actual"]').value;
     var stock_minimo = document.querySelector('input[name="stock_minimo"]').value;
     
     var precioVenta= precio_unitario;
        
        endpoint = "/api/productos/guardar"; 
        axios.post(endpoint, {
            nombre,
            codigo,
            precio_unitario,
            iva,
            stock_actual,
            stock_minimo
        })
        .then(function (response) {
            alert("Producto guardado exitosamente");
           console.log("si sirve yuju");
        })
        .catch(function (error) {
            alert("hubo un error en guardar el producto");
        });
        
        form.reset();
    });
});







// //sacar los productos de la base de datos y mostrarlos
// document.addEventListener('DOMContentLoaded', function() {
//     endpoint="/api/productos-listado";
//     axios.get(endpoint)
//         .then(function (response) {
//             const productos = response.data;
//             const container = document.getElementById('productos-container');
//             productos.forEach(function(producto) {
//                 const card = document.createElement('div');
//                 card.classList.add('col-md-4');
//                 card.innerHTML = `
//                     <div class="card">
//                         <img src="${producto.imagen_url}" class="card-img-top" alt="${producto.nombre}">
//                         <div class="card-body">
//                             <h5 class="card-title">${producto.nombre}</h5>
//                             <p class="card-text">${producto.precio_ubitario} €</p>
//                             <a onclick="showModal('${producto.id}')" class="btn btn-primary">
//                                 <i class="fas fa-eye"></i>
//                                 Ver
//                             </a>
//                         </div>
//                     </div>
//                 `;
//                 container.appendChild(card);
//             });
//         })
//         .catch(function (error) {
//             console.error('Error al obtener los productos:', error);
//         });
// });







// //ver stock
// document.addEventListener('DOMContentLoaded', function() {
//     // Obtener el contenedor de la tabla
//     const tableBody = document.getElementById('tableBody');
    
//     // Hacer una solicitud a la API para obtener los datos de los productos desde la base de datos
//     axios.get('/api/productos-listado')
//         .then(function(response) {
//             const productos = response.data;
            
//             // Función para determinar el color del stock según la cantidad disponible
//             function getColor(cantidad, stock_minimo) {
//                 if (cantidad <= 0) {
//                     return 'rojo';
//                 } else if (cantidad <= stock_minimo) {
//                     return 'amarillo';
//                 } else {
//                     return 'verde';
//                 }
//             }
            
//             // Generar filas de la tabla para cada producto
//             productos.forEach(function(producto, index) {
//                 const row = document.createElement('tr');
//                 row.innerHTML = `
//                     <td>${index + 1}</td>
//                     <td>${producto.nombre}</td>
//                     <td>
//                         <span class="stock ${getColor(producto.cantidad, producto.stock_minimo)}"></span>
//                         ${producto.cantidad}
//                     </td>
//                     <td>${producto.proveedor}</td>
//                     <td>${producto.descripcion}</td>
//                     <td><button class="orden"> <i class="fas fa-truck"></i></button></td>
//                 `;
//                 tableBody.appendChild(row);
//             });
//         })
//         .catch(function(error) {
//             console.error('Error al obtener los productos:', error);
//         });
// });

