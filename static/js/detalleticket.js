function mostrarDetallesTicket(ticketId, detallesDivId) {
    fetch(`/appDeustomachGestion/api/tickets/${ticketId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const detallesDiv = document.getElementById(detallesDivId);
            detallesDiv.innerHTML = `
                <h3>Detalles del Ticket</h3>
                <p><strong>Referencia :</strong> ${data.numero_referencia}</p>
                <p><strong>Título :</strong> ${data.titulo}</p>
                <p><strong>Descripción :</strong> ${data.descripcion_detallada}</p>
                <p><strong>Fecha de apertura :</strong> ${data.fecha_apertura}</p>
                <p><strong>Fecha de resolucion :</strong> ${data.fecha_resolucion}</p>
                <p><strong>Nivel de urgencia :</strong> ${data.nivel_urgencia}</p>
                <p><strong>Tipo de ticket:</strong> ${data.tipo_ticket}</p>
                <p><strong>Estado :</strong> ${data.estado_ticket}</p>
                <p><strong>Empleado asignado :</strong> ${data.empleado_asignado}</p>
                <p><strong>Equipo asignado :</strong> ${data.equipo_asignado}</p>
                <p><strong>Comentarios :</strong>${data.comentarios}</p>
            `;
        })
        .catch(error => {
            console.error('Error al cargar los detalles del ticket:', error);
        });
}
