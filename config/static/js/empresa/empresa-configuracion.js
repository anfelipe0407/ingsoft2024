console.log("EMPRESA-CONFIGURACION JS");

async function getEmpresaById(id) {
    const response = await axios.get(`${BASE_GENERAL_URL}/empresas/${id}`);
    return response?.data;
}