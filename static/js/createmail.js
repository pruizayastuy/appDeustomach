    document.addEventListener('DOMContentLoaded', function() {
        let nombreInput = document.querySelector('#id_nombre');
        let apellidoInput = document.querySelector('#id_apellidos');
        let emailInput = document.querySelector('#id_email');

        nombreInput.addEventListener('input', actualizarEmail);
        apellidoInput.addEventListener('input', actualizarEmail);

        function actualizarEmail() {
            let nombre = nombreInput.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            let apellido = apellidoInput.value.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/\s+/g, "");
            emailInput.value = nombre + '.' + apellido + '@gmail.com';
        }
    });