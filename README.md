
# Aplicación de Venta de Piezas de Coche

## Introducción
Esta aplicación permite gestionar la venta de piezas de coche, incluyendo la gestión de usuarios, empleados, clientes y pedidos.

## Requisitos
- Python 3.x
- Django 5.1.1
- Otras dependencias listadas en `requirements.txt`


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


Cuentas de usuarios:
Administrador:
nelson | 123456

Empleado 
fabian | sscqd88877e

Cliente
sara | Django.123

Tutorial para usar la aplicación
1- Clonar en tu ordenador los siguientes repositorios:

Cliente
https://github.com/Pistachopower/Proyecto_EmpresaVentaMotoresCliente.git

Api Rest 
https://github.com/Pistachopower/Proyecto_EmpresaVentaMotores.git


2- Creamos el entorno virtual dentro del proyecto del cliente y la Api con el siguiente comando:
python3 -m venv myvenv 

3- Activamos entorno virtual dentro de los proyectos de las aplicaciones:
source myvenv/bin/activate 

4- Instalamos los requerimientos en la Api:
pip install -r requirements.txt

5- Hacemos la migración en la api para trabajar con los datos de la bd ejecutando el siguiente comando:
python manage.py migrate

6- En la Api para trabajar con los datos y sesiones debemos aplicar el siguiente comando:
python manage.py loaddata EmpresaVentaPiezasCoche/fixtures/datos.json

7- Nos situamos dentro del directorio donde se encuentra el fichero manage.py y aplicamos el siguiente comando: 
python manage.py runserver 

Autenticación
Antes de usar la aplicación, es necesario tener la aplicacion Api activa y entrar en:
http://127.0.0.1:8081/oauth2/applications/register/

Foto de api registrar nueva aplicacion

Desmarcar Hash client secret:
Foto de Hash client secret

Foto de la api


Luego en tu aplicacion Api colocar en la terminal el siguiente comando:
Importante: client_id y client_secret lo sacas de la página de la Api. 
curl -X POST "http://127.0.0.1:8080/oauth2/token/" -d "grant_type=password&username=USUARIO&password=CONTRASENA&client_id=EmpresaVentaPiezasCoche&client_secret=EmpresaVentaPiezasCoche"







