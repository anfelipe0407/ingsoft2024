console.log("LOGIN JS")

const BASE_URL = 'http://127.0.0.1:5000/api'

const formData = {
    usuario: '',
    clave: '',
    rol: {
        id: 0,
        nombre: ''
    }
}

async function getRoles(){
    const response = await axios.get(BASE_URL + "/roles")
    return response?.data || [];
}

async function updateSelect(){
    const select = document.getElementById('rol-select');
    const roles = await getRoles();

    console.log('Roles', roles);

    formData.rol = {
        id: roles[0]?.id,
        nombre: roles[0]?.rol
    }

    select.innerHTML = '';

    roles.forEach(role => {
        const option = document.createElement('option');
        option.value = role.rol;
        option.text = role.rol.charAt(0).toUpperCase() + role.rol.slice(1);
        option.setAttribute('data-id', role.id); // Set custom attribute for id
        select.appendChild(option);
    });

    // Add change event listener
    select.addEventListener('change', (event) => {
        const selectedOption = event.target.options[event.target.selectedIndex];
        formData.rol.nombre = selectedOption.value;
        formData.rol.id = selectedOption.getAttribute('data-id');
        console.log('Selected Role:', formData.rol);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    updateSelect();
});

document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve values from form fields
    formData.usuario = document.getElementById('username').value;
    formData.clave = document.getElementById('password').value;

    // Make POST request using Axios
    console.log('formData', formData);
    try {
        const response = await axios.post(BASE_URL + '/login', formData);
        console.log('Login successful:', response.data);

        localStorage.setItem("rol_name", formData.rol.nombre);

        setTimeout(function() {
            window.location.href = "http://127.0.0.1:5000/" + formData.rol.nombre.toLowerCase().trim();
        }, 500);

        Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Login correcto",
            showConfirmButton: false,
            timer: 1500
        });
    } catch (error) {
        // console.error('Login failed:', error.response.data);
        Swal.fire({
            position: "top-end",
            icon: "error",
            title: "Error en el login",
            showConfirmButton: false,
            timer: 1500
        });
    }
});