    document.addEventListener('DOMContentLoaded', function() {
        let aumentarBtn = document.getElementById('aumentar-fuente');
        let disminuirBtn = document.getElementById('disminuir-fuente');

        aumentarBtn.addEventListener('click', function() {
            cambiarTamano('x-large');
        });

        disminuirBtn.addEventListener('click', function() {
            cambiarTamano('x-small');
        });

        function cambiarTamano(tamano) {
            let elementos = document.querySelectorAll('a, h2');
            elementos.forEach(function(elemento) {
                elemento.style.fontSize = tamano;
            });
        }
    });
