document.addEventListener('DOMContentLoaded', function() {
    // Obtener la modal y el botón de cierre
    var modal = document.getElementById('modal');
    var botonCerrar = document.getElementsByClassName('cerrar')[0];
  
    // Función para mostrar la modal
    function mostrarModal() {
      modal.style.display = 'block';
    }
  
    // Función para ocultar la modal
    function cerrarModal() {
      modal.style.display = 'none';
    }
  
    // Evento de clic en el botón de cierre
    botonCerrar.addEventListener('click', cerrarModal);
  
    // Evento de clic fuera de la modal para cerrarla
    window.addEventListener('click', function(event) {
      if (event.target == modal) {
        cerrarModal();
      }
    });
  
    // Evento de clic en un producto para mostrar la modal con sus detalles
    var productos = document.getElementsByClassName('producto');
    for (var i = 0; i < productos.length; i++) {
      productos[i].addEventListener('click', mostrarModal);
    }
  });
  