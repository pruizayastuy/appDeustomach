document.addEventListener('DOMContentLoaded', function() {
    let aumentarBtn = document.getElementById('aumentar-fuente');
    let disminuirBtn = document.getElementById('disminuir-fuente');

    const tamanosTexto = ['x-small', 'medium', 'x-large'];
    let indiceTamano = 1; // Empezamos en el tamaño medio

    aumentarBtn.addEventListener('click', function() {
        indiceTamano = (indiceTamano + 1) % tamanosTexto.length;
        cambiarTamano(tamanosTexto[indiceTamano]);
    });

    disminuirBtn.addEventListener('click', function() {
        indiceTamano = (indiceTamano - 1 + tamanosTexto.length) % tamanosTexto.length;
        cambiarTamano(tamanosTexto[indiceTamano]);
    });

    function cambiarTamano(tamano) {
        let elementos = document.querySelectorAll('a, h2');
        elementos.forEach(function(elemento) {
            elemento.style.fontSize = tamano;
        });
    }
});
