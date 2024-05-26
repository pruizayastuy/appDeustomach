function mostrarDetallesEquipo(equipoId, detallesDivId) {
    fetch(`/appDeustomachGestion/api/equipos/${equipoId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const detallesDiv = document.getElementById(detallesDivId);
            detallesDiv.innerHTML = `
                <h3>Detalles del Equipo</h3>
                <p><strong>Número de serie:</strong> ${data.numero_serie}</p>
                <p><strong>Modelo:</strong> ${data.modelo}</p>
                <p><strong>Marca:</strong> ${data.marca}</p>
                <p><strong>Tipo de equipo:</strong> ${data.tipo_equipo}</p>
                <p><strong>Fecha de adquisición:</strong> ${data.fecha_adquisicion}</p>
                <p><strong>Fecha de puesta en marcha:</strong> ${data.fecha_puesta_marcha}</p>
                <p><strong>Información del proveedor:</strong> ${data.informacion_proveedor.nombre} - ${data.informacion_proveedor.telefono}</p>
                <p><strong>Planta:</strong> ${data.planta}</p>
            `;
        })
        .catch(error => {
            console.error('Error al cargar los detalles del equipo:', error);
        });
}
