// static/js/validaciones.js

class Validaciones {
  // Método para validar si una cédula es válida
  static esCedulaValida(cedula) {
      try {
          if (cedula.length !== 10) {
              throw new Error('La cédula debe tener 10 dígitos.');
          }

          const multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2];
          const cedArray = Array.from(cedula).map(Number).slice(0, 9);
          const ultimoDigito = Number(cedula[9]);

          const resultado = cedArray.reduce((acc, val, index) => {
              let temp = val * multiplicador[index];
              if (temp >= 10) temp -= 9;
              return acc + temp;
          }, 0);

          const digitoVerificador = Math.ceil(resultado / 10) * 10 - resultado;

          if (digitoVerificador !== ultimoDigito) {
              throw new Error('La cédula ingresada no es válida.');
          }

          return true;
      } catch (error) {
          console.error('Error al validar la cédula:', error);
          return false;
      }
    }
  
    // Método para validar si un valor contiene solo números
    static soloNumeros(valor) {
      return !isNaN(valor) && parseInt(valor) > 0;
    }
  
    // Método para validar si un valor contiene solo letras, tildes y un espacio
    static soloLetras(valor) {
      return /^[A-Za-zÁÉÍÓÚáéíóúüÜñÑ\s]+$/.test(valor);
    }
  
    // Método para validar si un valor contiene solo números decimales
    static soloDecimales(valor) {
      return !isNaN(valor) && parseFloat(valor) > 0;
    }
  
    // Método para verificar si un RUC ya está registrado
    static async rucExistente(ruc) {
      try {
        const response = await fetch('/check_ruc?ruc=' + ruc);
        
        if (!response.ok) {
          throw new Error('No se pudo acceder al servidor.');
        }
  
        const data = await response.json();
        return data.exists;
      } catch (error) {
        console.error('Error al verificar el RUC:', error);
        return false;
      }
    }
  }
