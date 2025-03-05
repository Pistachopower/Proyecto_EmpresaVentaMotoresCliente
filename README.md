# Aplicación de Venta de Piezas de Coche

## Introducción
Esta aplicación permite gestionar la venta de piezas de coche, incluyendo la gestión de usuarios, empleados, clientes y pedidos.

## Requisitos
- Python 3.x
- Django 5.1.1
- Otras dependencias listadas en `requirements.txt`

Paso 1: Clonar los Repositorios
Necesitarás clonar dos repositorios: el cliente y la API REST.
# Clonar el repositorio del cliente
git clone https://github.com/Pistachopower/Proyecto_EmpresaVentaMotoresCliente.git

# Clonar el repositorio de la API REST
git clone https://github.com/Pistachopower/Proyecto_EmpresaVentaMotores.git
Paso 2: Configurar el Entorno Virtual para Ambos Proyectos
Para el Cliente:
# Navegar al directorio del cliente
cd Proyecto_EmpresaVentaMotoresCliente

# Crear entorno virtual
python3 -m venv myvenv

# Activar entorno virtual
source myvenv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
Para la API:
# Navegar al directorio de la API
cd ../Proyecto_EmpresaVentaMotores

# Crear entorno virtual
python3 -m venv myvenv

# Activar entorno virtual
source myvenv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
Paso 3: Configurar y Ejecutar la API
La API debe estar en funcionamiento antes de usar el cliente:
# Asegúrate de estar en el directorio de la API con el entorno virtual activado
cd Proyecto_EmpresaVentaMotores

# Realizar migraciones
python manage.py migrate

# Cargar datos iniciales
python manage.py loaddata EmpresaVentaPiezasCoche/fixtures/datos.json

# Iniciar el servidor (por defecto en puerto 8080)
python manage.py runserver 8080
Paso 4: Registrar una Aplicación OAuth2 en la API
1.
Con la API en funcionamiento, visita: http://127.0.0.1:8080/oauth2/applications/register/
2.
Completa el formulario de registro:
Nombre: "Cliente MotorPartExpress"
Cliente Type: "Confidential"
Authorization Grant Type: "Authorization code"
Redirect URIs: http://127.0.0.1:8081/oauth/callback/
3.
Importante: Desmarca la opción "Hash client secret"
4.
Guarda la aplicación y anota el Client ID y Client Secret generados

Paso 5: Configurar Variables de Entorno en el Cliente
Crea un archivo .env en la raíz del proyecto cliente:
# En el directorio del cliente
cd ../Proyecto_EmpresaVentaMotoresCliente
touch .env
Edita el archivo .env con la siguiente información:
OAUTH2_CLIENT_ID=tu_client_id
OAUTH2_CLIENT_SECRET=tu_client_secret
OAUTH2_ACCESS_TOKEN=tu_access_token_inicial
Paso 6: Ejecutar el Cliente
# Asegúrate de estar en el directorio del cliente con el entorno virtual activado
cd Proyecto_EmpresaVentaMotoresCliente
source myvenv/bin/activate

# Iniciar el servidor en el puerto 8081
python manage.py runserver 8081
Paso 7: Usar la Aplicación
1.
Abre tu navegador y visita: http://127.0.0.1:8081/
2.
Inicia sesión con alguna de las siguientes cuentas:
Administrador:
Usuario: nelson
Contraseña: 123456
Empleado:
Usuario: fabian
Contraseña: sscqd88877e
Cliente:
Usuario: sara
Contraseña: Django.123

Tipos de usuarios:
Administrador (rol 1)
Este usuario puede: 
Modelo cliente, empleado, metodo pago, pedido, pieza motor, pieza motor pedido, proveedor: añadir, crear, actualizar, ver y borrar. 

Empleado (rol 2)
Este usuario puede:
Modelo cliente: ver. 

proveedor: crear, actualizar, ver y borrar.

pedido: ver.


Cliente (3)
Este usuario puede:
pedido: añadir, crear, actualizar, ver y borrar.

Operaciones Get, post, put, patch, delete pedidos
Para realizar las siguientes operaciones es necesario tener instalado Postman. 

Listar pedidos GET
Endpoint: GET https://pistacho.pythonanywhere.com/api/v1/pedidos-lista/
Authorization | Type: Bearer Token: Q6ScRQFZptyQHfV8MpKPywH0mbywfx
Respuesta: devuelve toda la lista de pedidos

Crear pedido POST
Endpoint: POST https://pistacho.pythonanywhere.com/api/v1/pedido-metodopago/crear/
Authorization | Type: Bearer Token: Q6ScRQFZptyQHfV8MpKPywH0mbywfx
Body:
{
    "pedido": "otro para probar",
    "fecha_pedido": "2025-03-05", 
    "total_importe": 24,
    "estado": "ENV",
    "metodo_pago": 2, 
    "cliente": 2 
}

Respuesta: pedido creado

Eliminar pedido Delete
Endpoint: POST https://pistacho.pythonanywhere.com/api/v1/pedido-metodopago/crear/
Authorization | Type: Bearer Token: Q6ScRQFZptyQHfV8MpKPywH0mbywfx

Body:
{
    "id": 1,
    "pedido": "otro para probar",
    "fecha_pedido": "2025-03-05",
    "total_importe": 241251232151231,
    "estado": "ENV",
    "estado_display": "Enviado"
}
Respuesta: pedido borrado


Editar pedido Put
Endpoint: PUT https://pistacho.pythonanywhere.com/api/v1/pedido-metodopago/editar/2/
Authorization | Type: Bearer Token: Q6ScRQFZptyQHfV8MpKPywH0mbywfx
Body:
{
    "id": 2,
    "pedido": "Actualización del pedido.",
    "fecha_pedido": "2025-02-01",
    "total_importe": 123456,
    "estado": "ENV",
    "estado_display": "En proceso",
    "metodo_pago": 1,
    "cliente": 1,
    "usuario_Pedido": 5
}

Respuesta: pedido actualizado


Editar pedido nombre Patch
Endpoint: PATCH https://pistacho.pythonanywhere.com/api/v1/pedido-metodopago/editar/nombre/2/
Authorization | Type: Bearer Token: Q6ScRQFZptyQHfV8MpKPywH0mbywfx
Body:
{
    "pedido": "Nuevo nombre del pedido actualizado"
}

Respuesta: nombre pedido actualizado






