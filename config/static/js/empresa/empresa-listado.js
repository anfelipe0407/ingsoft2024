console.log("EMPRESA-LISTADO JS")

const BASE_GENERAL_URL = 'http://127.0.0.1:5000/general'
const BASE_URL = 'http://127.0.0.1:5000/api'

async function getEmpresas(){
    const response = await axios.get(BASE_GENERAL_URL + "/empresas")
    return response?.data || [];
}

document.addEventListener("DOMContentLoaded", async function() {
    const empresas = await getEmpresas();
    console.log('Empresas', empresas);
    const tbody = document.getElementById('empresas-tbody');
    
    empresas.forEach(empresa => {
      const tr = document.createElement('tr');
      
      tr.innerHTML = `
        <td>${empresa.nombre}</td>
        <td>${empresa.nit}</td>
        <td>${empresa.correo}</td>
        <td>${empresa.porcentaje_ganancia}</td>
        <td>${empresa.iva_establecido}</td>
        <td>${empresa.descuento_general}</td>
        <td>${empresa.vigencia_licencia_fin}</td>
        <td>
          <a href="${empresa.url_asociada}" class="btn btn-warning" title="Editar">
            <i class="fas fa-pen"></i>
          </a>
        </td>
        <td>
          <a class="btn btn-danger" title="Eliminar producto">
            <i class="fas fa-trash"></i>
          </a>
        </td>
      `;
      
      tbody.appendChild(tr);
    });
  });