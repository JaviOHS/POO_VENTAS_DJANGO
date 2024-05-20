function mostrarEsperaAutomatica() {
    document.addEventListener('DOMContentLoaded', function () {
        Swal.fire({
            title: 'Espera un momento...',
            text: 'Realizando la operación...',
            icon: 'info',
            showConfirmButton: false,
            timer: 1000 // tiempo en milisegundos (1 segundo)
        });
    });
}

function mostrarError(mensaje) {
    Swal.fire({
        icon: 'error',
        title: 'Error',
        text: mensaje,
        confirmButtonText: 'Aceptar'
    });
}

async function validarFormulario(event) {
    event.preventDefault(); // Detiene el envío del formulario
    const ruc = document.getElementById('id_ruc').value;
    const name = document.getElementById('id_name').value;
    const phone = document.getElementById('id_phone').value;
    try {
        if (!Validaciones.esCedulaValida(ruc)) {
            mostrarError('El formato del DNI es inválido. Por favor, inténtelo de nuevo.');
          } else if (!Validaciones.soloLetras(name)) {
            mostrarError('Formato de nombre incorrecto. Por favor, inténtelo de nuevo.');
          } else if (!Validaciones.soloNumeros(phone) || phone.length !== 10) {
            mostrarError('Celular incorrecto. Por favor, inténtelo de nuevo.');
          } else {
            Swal.fire({
                title: 'Proveedor agregado!',
                text: 'El proveedor se ha agregado correctamente.',
                icon: 'success',
                confirmButtonText: 'Aceptar'
            }).then(() => {
                event.target.submit();
            });
        }
    } catch (error) {
        console.error('Error al validar el formulario:', error);
        mostrarError('Hubo un error al validar el formulario. Por favor, inténtelo de nuevo.');
    }
}

async function validarFormularioProductos(event) {
    event.preventDefault(); 
    const name = document.getElementById('id_description').value;
    const price= document.getElementById('id_price').value;
    const stock = document.getElementById('id_stock').value;
    try {
        if (!Validaciones.soloLetras(name)) {
            mostrarError('El nombre del producto es inválido. Por favor, inténtelo de nuevo.');
          } else if (!Validaciones.soloDecimales(price)) {
            mostrarError('El precio debe ser un número decimal positivo. Por favor, inténtelo de nuevo.');
          } else if (!Validaciones.soloNumeros(stock)) {
            mostrarError('El stock debe ser un número entero. Por favor, inténtelo de nuevo.');
          } else {
            Swal.fire({
                title: '¡Producto agregado!',
                text: 'El producto se ha agregado correctamente.',
                icon: 'success',
                confirmButtonText: 'Aceptar'
            }).then(() => {
                event.target.submit(); // Envía el formulario si todas las validaciones pasan
            });
        }
    } catch (error) {
        console.error('Error al validar el formulario:', error);
        mostrarError('Hubo un error al validar el formulario. Por favor, inténtelo de nuevo.');
    }
}