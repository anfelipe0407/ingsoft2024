console.log("MODULOS-EMPRESA JS");

const BASE_GENERAL_URL = "http://127.0.0.1:5000/general";
const BASE_URL = "http://127.0.0.1:5000/api";

// ! HTTP
async function getEmpresas() {
  const response = await axios.get(BASE_GENERAL_URL + "/empresas");
  return response?.data || [];
}

async function getModulosEmpresa(id_empresa) {
  const response = await axios.get(BASE_GENERAL_URL + "/empresas/" + id_empresa + "/modulos");
  return response?.data || [];
}

async function getEmpresaById(id) {
  const response = await axios.get(`${BASE_GENERAL_URL}/empresas/${id}`);
  return response?.data;
}

// ! LISTADO DE EMPRESAS
document.addEventListener("DOMContentLoaded", async function () {
  const empresas = await getEmpresas();
  console.log("Empresas", empresas);
  const tbody = document.getElementById("empresas-tbody");

  if (tbody) {
    empresas.forEach((empresa) => {
      const tr = document.createElement("tr");

      tr.innerHTML = `
            <td>${empresa.nombre}</td>
            <td>${empresa.nit}</td>
            <td>${empresa.correo}</td>
            <td>${empresa.porcentaje_ganancia}</td>
            <td>${empresa.iva_establecido}</td>
            <td>${empresa.descuento_general}</td>
            <td>${empresa.vigencia_licencia_fin}</td>
            <td>
                <a class="btn btn-primary" data-id="${empresa.id}" title="Ver modulos">
                <i class="fas fa-eye"></i>
                </a>
            </td>
            `;

      tbody.appendChild(tr);
    });

    document.querySelectorAll(".btn-primary").forEach((button) => {
      button.addEventListener("click", function () {
        const empresaId = this.getAttribute("data-id");
        // Redirige al usuario a la página de módulos con el ID de la empresa
        window.location.href = `/administrador/modulos/${empresaId}`;
      });
    });
  }
});

// ! MODULOS
document.addEventListener("DOMContentLoaded", async function () {
    const currentUrl = window.location.href;
    const lastSlashIndex = currentUrl.lastIndexOf("/");
    const empresaId = +currentUrl.substring(lastSlashIndex + 1);
  
    if (typeof empresaId === "number" && !isNaN(empresaId)) {
      console.log("ID de la empresa:", empresaId);
      const empresa = await getEmpresaById(empresaId);
      const modulosEmpresa = await getModulosEmpresa(empresaId);

      console.log(modulosEmpresa);
  
      // Seleccionar el contenedor de los módulos
      const modulosContainer = document.getElementById("modulos-container");
  
      // Verificar si hay módulos asociados
      if (modulosEmpresa.length > 0) {
        // Iterar sobre los módulos y agregar botones para cada uno
        modulosEmpresa.forEach((moduloEmpresa, index) => {
          const modulo = moduloEmpresa.modulo;
          const boton = document.createElement("button");
          boton.className = "boton boton-activo";
          boton.textContent = modulo.nombre;
          const div = document.createElement("div");
          div.className = "btn btn-warning";
          div.textContent = "Extender";
          div.onclick = function() {
            showModal(index);
          };
          boton.appendChild(div);
          modulosContainer.appendChild(boton);
        });
      } else {
        // Si no hay módulos asociados, mostrar un mensaje
        const mensaje = document.createElement("p");
        mensaje.textContent = "No hay módulos asociados a esta empresa.";
        modulosContainer.appendChild(mensaje);
      }
    }
  });
  
