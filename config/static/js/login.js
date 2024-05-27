console.log("LOGIN JS")

import HTTPService from './HttpService.js';

const BASE_URL = 'http://127.0.0.1:5000/api'

const LoginModule = (function() {
    const formData = {
        usuario: '',
        clave: '',
        rol: ''
    };

    const httpService = new HTTPService();

    async function handleFormSubmit(event) {
        event.preventDefault();

        formData.usuario = document.getElementById('username').value;
        formData.clave = document.getElementById('password').value;
        formData.rol = document.getElementById('rol-select').value;

        // Make POST request using HTTPService
        console.log('formData', formData);

        httpService.post('/login', formData, (error, data) => {
            if (error) {
                Swal.fire({
                    position: "top-end",
                    icon: "error",
                    title: "Error en el login: usuario, contraseña o rol incorrecto(s)",
                    showConfirmButton: false,
                    timer: 1500
                });
                return;
            }

            console.log('Login successful:', data);

            localStorage.setItem("id_usuario", data.id);
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
        });
    }

    function init() {
        document.getElementById('login-form').addEventListener('submit', handleFormSubmit);
    }

    return {
        init: init
    };
})();

// Inicializacion modulo de LOGIN
LoginModule.init();
