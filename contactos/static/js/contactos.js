function eliminarContacto(id) {
    if (confirm("¿Está seguro de que desea eliminar este registro?")) {
        try {
            fetch(`/borrar_contacto/${id}`, {
                method: 'GET'
            }).then(response => {
                if (!response.ok) {
                    throw new Error('La redirección falló');
                }                
            });
        } catch (error) {
            console.error('Ha ocurrido un error en la operacion de busqueda:', error);
            alert("Error al eliminar el registro.");
            return;
        }
        alert("Registro eliminado correctamente.");
    }
}


