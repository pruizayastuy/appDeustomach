function mostrarDetalles(ticketId) {
    fetch(`/api/tickets/${ticketId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const detallesDiv = document.getElementById('ticket-detalles');
            detallesDiv.innerHTML = `
                <h3>Detalles del Ticket</h3>
                <p><strong>Referencia:</strong> ${data.numero_referencia}</p>
                <p><strong>Título:</strong> ${data.titulo}</p>
                <p><strong>Descripción:</strong> ${data.descripcion_detallada}</p>
                <p><strong>Estado:</strong> ${data.estado_ticket}</p>
                <p><strong>Fecha de apertura:</strong> ${data.fecha_apertura}</p>
                <p><strong>Nivel de urgencia:</strong> ${data.nivel_urgencia}</p>
            `;
        })
        .catch(error => {
            console.error('Error al cargar los detalles del ticket:', error);
        });
}