function mostrarDetallesEmpleado(empleadoId, detallesDivId) {
    fetch(`/appDeustomachGestion/api/empleados/${empleadoId}/`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const detallesDiv = document.getElementById(detallesDivId);
            detallesDiv.innerHTML = `
                <h3>Detalles del Empleado</h3>
                <p><strong>DNI:</strong> ${data.dni}</p>
                <p><strong>Nombre:</strong> ${data.nombre}</p>
                <p><strong>Apellidos:</strong> ${data.apellidos}</p>
                <p><strong>Email:</strong> ${data.email}</p>
                <p><strong>Teléfono:</strong> ${data.telefono}</p>

            `;
        })
        .catch(error => {
            console.error('Error al cargar los detalles del empleado:', error);
        });
}
