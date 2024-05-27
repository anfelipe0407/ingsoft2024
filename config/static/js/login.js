console.log("LOGIN JS")

const BASE_URL = 'http://127.0.0.1:5000/api'

const formData = {
    usuario: '',
    clave: '',
    rol: ''
}

document.getElementById('login-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve values from form fields
    formData.usuario = document.getElementById('username').value;
    formData.clave = document.getElementById('password').value;
    formData.rol = document.getElementById('rol-select').value;

    // Make POST request using Axios
    console.log('formData', formData);

    try {
        const response = await axios.post(BASE_URL + '/login', formData);
        console.log('Login successful:', response.data);

        localStorage.setItem("id_usuario", response.data.id);
        localStorage.setItem("rol_name", formData.rol);

        setTimeout(function() {
            window.location.href = "http://127.0.0.1:5000/" + formData.rol.toLowerCase().trim();
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
            title: "Error en el login: usuario, contraseña o rol incorrecto(s)",
            showConfirmButton: false,
            timer: 1500
        });
    }
});