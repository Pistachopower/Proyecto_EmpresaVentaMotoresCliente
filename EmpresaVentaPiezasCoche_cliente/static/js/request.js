document.addEventListener("DOMContentLoaded", function () {
    const token = "8qmTvt9IQ3h3tuDjPBjQbyMNEfRvk7";  // Reemplaza con el token real
    const dataList = document.getElementById("data-list");

    fetch("http://127.0.0.1:8080/api/v1/empleados", {  // Reemplaza con la URL de tu API DRF
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        dataList.innerHTML = "";  // Limpiar lista antes de agregar nuevos datos
        data.forEach(item => {
            const li = document.createElement("li");
            li.textContent = `ID: ${item.id}, Nombre: ${item.empleado}`;  
            dataList.appendChild(li);
        });
    })
    .catch(error => console.error("Error en la petición:", error));
});
