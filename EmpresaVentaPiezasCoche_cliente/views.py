import json
from django.shortcuts import render, redirect
import requests
from django.core import serializers
from pathlib import Path
import environ
import os

from EmpresaVentaPiezasCoche_cliente.cliente_api import cliente_api
from .forms import *
from requests.exceptions import HTTPError
from datetime import date

# aqui lo que hacemos es que accedemos a .env para poder acceder a la api
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"), True)
env = environ.Env()

# definimos la url para la configuracion de la api
BASE_URL = "http://127.0.0.1:8080/api/v1/"


# Create your views here.
def index(request):
    token = request.session.get("token")
    isLogin = False
    if token:
        isLogin = True
    return render(request, "index.html", {"isLogin": isLogin})


def empleados_lista_api(request):
    token = request.session.get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get("http://127.0.0.1:8080/api/v1/empleados", headers=headers)
    empleados_normal = response.json()
    return render(request, "empleado/lista.html", {"empleados": empleados_normal})


def empleados_lista_api_mejorado(request):
    token = request.session.get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/empleados_mejorado", headers=headers
    )
    empleados = response.json()
    return render(request, "empleado/lista_Mejorado.html", {"empleados": empleados})


def listar_clientes_mejorado(request):
    token = request.session.get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/clientes_mejorado", headers=headers
    )
    cliente = response.json()
    return render(request, "cliente/lista_Mejorado.html", {"cliente_mejorado": cliente})


def listar_pedido_mejorado(request):
    token = request.session.get("token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        "http://127.0.0.1:8081/api/v1/pedido_mejorado", headers=headers
    )
    pedido = response.json()
    return render(request, "pedido/lista_Mejorado.html", {"pedido_mejorado": pedido})


def crear_cabecera():
    return {
        "Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN"),
        "Content-Type": "application/json",
    }


def busquedaSimpleEmpleado(request):
    if len(request.GET) > 0:
        formulario = BusquedaEmpleadoForm(request.GET)
        if formulario.is_valid():
            token = request.session.get("token")
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"{BASE_URL}busquedasimpleempleados/",
                headers=headers,
                params={"textoBusqueda": formulario.data.get("textoBusqueda")},
            )
            empleados = response.json()
            return render(request, "empleado/lista.html", {"empleados": empleados})
        else:
            empleados = {}
            return render(request, "empleado/lista.html", {"empleados": empleados})
    else:
        empleados = {}
        return render(request, "empleado/lista.html", {"empleados": empleados})


def busquedaAvanzadaEmpleado(request):
    if len(request.GET) > 0:
        formulario = BusquedaAvanzadaEmpleadoForm(request.GET)
        try:
            token = request.session.get("token")
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"{BASE_URL}busqueda-avanzada-empleados",
                headers=headers,
                params=formulario.data,
            )
            if response.status_code == requests.codes.ok:
                empleados = response.json()
                return render(
                    request,
                    "empleado/busqueda_avanzada.html",
                    {"formulario": formulario, "empleados": empleados},
                )
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "empleado/busqueda_avanzada.html",
                    {"formulario": formulario},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)
    else:
        formulario = BusquedaAvanzadaEmpleadoForm(None)
    return render(
        request, "empleado/busqueda_avanzada.html", {"formulario": formulario}
    )


def busquedaAvanzadaClientes(request):
    if len(request.GET) > 0:
        formulario = BusquedaAvanzadaClientesForm(request.GET)
        try:
            token = request.session.get("token")
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"{BASE_URL}busqueda-avanzada-clientes",
                headers=headers,
                params=formulario.data,
            )
            if response.status_code == requests.codes.ok:
                clientes = response.json()
                return render(
                    request,
                    "cliente/busqueda_avanzada_cliente.html",
                    {"formulario": formulario, "clientes": clientes},
                )
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "cliente/busqueda_avanzada_cliente.html",
                    {"formulario": formulario},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)
    else:
        formulario = BusquedaAvanzadaClientesForm(None)
    return render(
        request, "cliente/busqueda_avanzada_cliente.html", {"formulario": formulario}
    )


def busquedaAvanzadaPedidos(request):
    if len(request.GET) > 0:
        formulario = BusquedaAvanzadaPedidoForm(request.GET)
        try:
            token = request.session.get("token")
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"{BASE_URL}busqueda-avanzada-pedidos",
                headers=headers,
                params=formulario.data,
            )
            if response.status_code == requests.codes.ok:
                pedidos = response.json()
                return render(
                    request,
                    "pedido/busqueda_avanzada_pedidos.html",
                    {"formulario": formulario, "pedidos": pedidos},
                )
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "pedido/busqueda_avanzada_pedidos.html",
                    {"formulario": formulario},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)
    else:
        formulario = BusquedaAvanzadaPedidoForm(None)
    return render(
        request, "pedido/busqueda_avanzada_pedidos.html", {"formulario": formulario}
    )


def busquedaAvanzadaProveedor(request):
    if len(request.GET) > 0:
        formulario = BusquedaAvanzadaProveedorForm(request.GET)
        try:
            token = request.session.get("token")
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(
                f"{BASE_URL}busqueda-avanzada-proveedor",
                headers=headers,
                params=formulario.data,
            )
            if response.status_code == requests.codes.ok:
                proveedor = response.json()
                return render(
                    request,
                    "proveedor/busqueda_avanzada_proveedor.html",
                    {"formulario": formulario, "proveedor": proveedor},
                )
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "proveedor/busqueda_avanzada_proveedor.html",
                    {"formulario": formulario},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)
    else:
        formulario = BusquedaAvanzadaProveedorForm(None)
    return render(
        request,
        "proveedor/busqueda_avanzada_proveedor.html",
        {"formulario": formulario},
    )


def proveedor_lista(request):
    try:
        token = request.session.get("token")
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/proveedores/proveedores_listar/", headers=headers
        )
    
        if response.status_code == requests.codes.ok:
            proveedores = response.json()
            return render(
            request, "proveedor/lista_proveedor.html", {"proveedores": proveedores}
            )
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f"Ocurrió un error: {err}")
        return error_500(request)
    
    proveedores = response.json()
    
    return render(
        request, "proveedor/lista_proveedor.html", {"proveedores": proveedores}
    )


def proveedor_crear(request):
    if request.method == "POST":
        try:
            formulario = ProveedoresForm(request.POST)
            token = request.session.get("token")
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }
            datos = formulario.data.copy()
            datos["proveedor"] = request.POST.get("proveedor")
            datos["telefono"] = request.POST.get("telefono")
            datos["correo"] = request.POST.get("correo")
            datos["direccion"] = request.POST.get("direccion")

            response = requests.post(
                "http://127.0.0.1:8080/api/v1/proveedores/crear/",
                headers=headers,
                data=json.dumps(datos),
            )
            if response.status_code == requests.codes.ok:
                return redirect("proveedor_lista")
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request, "proveedor/crear.html", {"formulario": formulario}
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)
    else:
        formulario = ProveedoresForm(None)
    return render(request, "proveedor/crear.html", {"formulario": formulario})


def proveedores_editar_put(request, proveedor_id):
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST

    proveedor = helper.obtener_proveedor_select(proveedor_id)
    formulario = ProveedoresForm(
        datosFormulario,
        initial={
            "proveedor": proveedor["proveedor"],
            "telefono": proveedor["telefono"],
            "correo": proveedor["correo"],
            "direccion": proveedor["direccion"],
        },
    )
    if request.method == "POST":
        formulario = ProveedoresForm(request.POST)
        datos = request.POST.copy()
        datos["proveedor"] = request.POST.get("proveedor")
        datos["telefono"] = request.POST.get("telefono")
        datos["correo"] = request.POST.get("correo")
        datos["direccion"] = request.POST.get("direccion")
        token = request.session.get("token")
        cliente = cliente_api(
            token ,
            "PUT",
            "proveedores/editar/" + str(proveedor_id) + str("/"),
            datos,
        )
        cliente.realizar_peticion_api()
        if cliente.es_respuesta_correcta():
            return redirect("proveedor_lista")
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request, cliente.codigoRespuesta)

    return render(
        request,
        "proveedor/actualizar.html",
        {"formulario": formulario, "proveedor": proveedor},
    )


def proveedores_editar_patch(request, proveedor_id):
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST

    proveedor = helper.obtener_proveedor_select(proveedor_id)
    formulario = ProveedorActualizarNombreForm(
        datosFormulario,
        initial={
            "proveedor": proveedor["proveedor"],
        },
    )
    if request.method == "POST":
        try:
            formulario = ProveedorActualizarNombreForm(request.POST)
            token = request.session.get("token")
            headers = {"Authorization": f"Bearer {token}"}
            datos = request.POST.copy()
            response = requests.patch(
                f"{BASE_URL}proveedores/editar/nombre/{proveedor_id}/",
                headers=headers,
                data=json.dumps(datos),
            )

            if response.status_code == requests.codes.ok:
                return redirect("proveedor_lista")
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "proveedor/actualizarNombreProveedor.html",
                    {"formulario": formulario, "proveedor": proveedor},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    return render(
        request,
        "proveedor/actualizarNombreProveedor.html",
        {"formulario": formulario, "proveedor": proveedor},
    )



def proveedor_crear(request):
    if request.method == "POST":
        try:
            formulario = ProveedoresForm(request.POST)
            headers = {
                "Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN"),
                "Content-Type": "application/json",
            }
            datos = formulario.data.copy()
            datos["proveedor"] = request.POST.get("proveedor")
            datos["telefono"] = request.POST.get("telefono")
            datos["correo"] = request.POST.get("correo")
            datos["direccion"] = request.POST.get("direccion")

            response = requests.post(
                "http://127.0.0.1:8080/api/v1/proveedores/crear/",
                headers=headers,
                data=json.dumps(datos),
            )
            if response.status_code == requests.codes.ok:
                return redirect("proveedor_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request, "proveedor/crear.html", {"formulario": formulario}
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    else:
        formulario = ProveedoresForm(None)
    return render(request, "proveedor/crear.html", {"formulario": formulario})


def proveedores_editar_put(request, proveedor_id):

    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST

    proveedor = helper.obtener_proveedor_select(proveedor_id)
    formulario = ProveedoresForm(
        datosFormulario,
        initial={
            "proveedor": proveedor["proveedor"],
            "telefono": proveedor["telefono"],
            "correo": proveedor["correo"],
            "direccion": proveedor["direccion"],
        },
    )
    if request.method == "POST":
        formulario = ProveedoresForm(request.POST)
        datos = request.POST.copy()
        datos["proveedor"] = request.POST.get("proveedor")
        datos["telefono"] = request.POST.get("telefono")
        datos["correo"] = request.POST.get("correo")
        datos["direccion"] = request.POST.get("direccion")
        token = request.session.get("token")
        cliente = cliente_api(
            token,
            "PUT",
            "proveedores/editar/" + str(proveedor_id) + str("/"),
            datos,
        )
        cliente.realizar_peticion_api()
        if cliente.es_respuesta_correcta():
            return redirect("proveedor_lista")
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request, cliente.codigoRespuesta)

    return render(
        request,
        "proveedor/actualizar.html",
        {"formulario": formulario, "proveedor": proveedor},
    )


def proveedores_editar_patch(request, proveedor_id):

    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    proveedor = helper.obtener_proveedor_select(
        proveedor_id
    )  # se hace la consulta a la bd

    formulario = ProveedorActualizarNombreForm(
        datosFormulario,
        initial={
            "proveedor": proveedor["proveedor"],
        },
    )
    if request.method == "POST":
        try:
            formulario = ProveedorActualizarNombreForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()
            response = requests.patch(
                f"{BASE_URL}proveedores/editar/nombre/{proveedor_id}/",
                headers=headers,
                data=json.dumps(datos),
            )

            if response.status_code == requests.codes.ok:
                return redirect("proveedor_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "proveedor/actualizarNombreProveedor.html",
                    {"formulario": formulario, "proveedor": proveedor},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    return render(
        request,
        "proveedor/actualizarNombreProveedor.html",
        {"formulario": formulario, "proveedor": proveedor},
    )


def proveedores_eliminar(request, proveedor_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
            f"http://127.0.0.1:8080/api/v1/proveedores/eliminar/{proveedor_id}/",
            headers=headers,
        )
        if response.status_code == requests.codes.ok:
            return redirect("proveedor_lista")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f"Ocurrió un error: {err}")
        return error_500(request)
    return redirect("proveedor_lista")


# post, patch, delete pedido metodopago
def pedido_metodopago_lista(request):
    try:
        #obtenemos la session del usuario y con ello manejamos los permisos
        token = request.session.get("token")
        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
        }
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/pedidos-lista/", headers=headers
        )

        if response.status_code == requests.codes.ok:
            pedidosMetPag = response.json()
            return render(
                request,
                "pedidoMetodoPago/lista_pedidoMetodoPago.html",
                {"pedidosMetPag": pedidosMetPag},
            )
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f"Ocurrió un error: {err}")
        return error_500(request)

    # Transformamos la respuesta en json
    pedidosMetPag = response.json()
    return render(
        request,
        "pedidoMetodoPago/lista_pedidoMetodoPago.html",
        {"pedidosMetPag": pedidosMetPag},
    )


def pedido_metodopago_crear(request):
    if request.method == "POST":
        try:
            formulario = PedidosForm(request.POST)
            headers = {
                "Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN"),
                "Content-Type": "application/json",
            }
            datos = formulario.data.copy()
            print(datos)
            datos["pedido"] = request.POST.get("pedido")
            datos["fecha_pedido"] = str(
                date(
                    year=int(datos["fecha_pedido_year"]),
                    month=int(datos["fecha_pedido_month"]),
                    day=int(datos["fecha_pedido_day"]),
                )
            )

            datos["metodo_pago"] = request.POST.get("metodo_pago")

            datos["usuario"] = request.POST.get("usuario")

            response = requests.post(
                "http://127.0.0.1:8080/api/v1/pedido-metodopago/crear/",
                headers=headers,
                data=json.dumps(datos),
            )
            if response.status_code == requests.codes.ok:
                return redirect("pedido_metodopago_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request, "pedidoMetodoPago/crear.html", {"formulario": formulario}
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    else:
        formulario = PedidosForm(None)
    return render(request, "pedidoMetodoPago/crear.html", {"formulario": formulario})


def pedido_eliminar(request, pedido_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
            f"http://127.0.0.1:8080/api/v1/pedido/eliminar/{pedido_id}/",
            headers=headers,
        )
        if response.status_code == requests.codes.ok:
            return redirect("pedido_metodopago_lista")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f"Ocurrió un error: {err}")
        return error_500(request)
    return redirect("pedido_metodopago_lista")


def pedido_editar_patch(request, pedido_id):

    datosFormulario = None

    if request.method == "POST":
        datosFormulario = request.POST

    pedido = helper.obtener_pedido_select(pedido_id)  # se hace la consulta a la bd
    formulario = PedidoActualizarNombreForm(
        datosFormulario,
        initial={
            "pedido": pedido["pedido"],
        },
    )
    if request.method == "POST":
        try:
            formulario = PedidoActualizarNombreForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()
            response = requests.patch(
                f"{BASE_URL}pedido-metodopago/editar/nombre/{pedido_id}/",
                headers=headers,
                data=json.dumps(datos),
            )

            if response.status_code == requests.codes.ok:
                return redirect("pedido_metodopago_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request,
                    "pedidoMetodoPago/actualizarNombrePedido.html",
                    {"formulario": formulario, "pedido_id": pedido_id},
                )
            else:
                return error_500(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    return render(
        request,
        "pedidoMetodoPago/actualizarNombrePedido.html",
        {"formulario": formulario, "pedido": pedido},
    )


def pedido_editar_put(request, pedido_id):

    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST

    pedido = helper.obtener_pedido_select(pedido_id)
    fecha_obj = datetime.strptime(pedido["fecha_pedido"], "%d-%m-%Y").date()
    formulario = PedidosForm(
        datosFormulario,
        initial={
            "pedido": pedido["pedido"],
            "fecha_pedido": str(
                date(year=fecha_obj.year, month=fecha_obj.month, day=fecha_obj.day)
            ),
            "estado": pedido["estado"],
            "metodo_pago": pedido["metodo_pago"],
            "total_importe": pedido["total_importe"],
            "usuario_Pedido": pedido["usuario_Pedido"],
            "cliente": pedido["cliente"],
        },
    )
    if request.method == "POST":
        formulario = PedidosForm(request.POST)
        datos = request.POST.copy()
        datos["pedido"] = request.POST.get("pedido")

        # conversion de fechas
        datos["fecha_pedido"] = str(
            date(
                year=int(datos["fecha_pedido_year"]),
                month=int(datos["fecha_pedido_month"]),
                day=int(datos["fecha_pedido_day"]),
            )
        )
        datos["estado"] = request.POST.get("estado")
        datos["total_importe"] = request.POST.get("total_importe")
        datos["usuario"] = request.POST.get("usuario")
        datos["cliente"] = request.POST.get("cliente")

        token = request.session.get("token")
        cliente = cliente_api(
            # env("OAUTH2_ACCESS_TOKEN"),
            token,
            "PUT",
            "pedido-metodopago/editar/" + str(pedido_id) + str("/"),
            datos,
        )
        cliente.realizar_peticion_api()
        if cliente.es_respuesta_correcta():
            return redirect("pedido_metodopago_lista")
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request, cliente.codigoRespuesta)

    return render(request,"pedidoMetodoPago/actualizar.html", {"formulario": formulario, "pedido": pedido},
)


def registrar_usuario(request):
    if request.method == "POST":
        try:
            formulario = RegistroForm(request.POST)
            if formulario.is_valid():

                # se prepara el formulario para enviarlo a la API
                headers = {"Content-Type": "application/json"}
                response = requests.post(
                    BASE_URL + "registrar/usuario",
                 
                    headers=headers,
                    data=json.dumps(formulario.cleaned_data),
                )

                if response.status_code == requests.codes.ok:
                    usuario = response.json()
                    token_acceso = helper.obtener_token_session(
                        formulario.cleaned_data.get("username"),
                        formulario.cleaned_data.get("password1"),
                    )
                    request.session["usuario"] = usuario
                    request.session["token"] = token_acceso
                    return redirect("index")
                else:
                    print(response.status_code)
                    response.raise_for_status()
                print(formulario.errors)
        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(
                    request, "registration/signup.html", {"formulario": formulario}
                )
            else:
                return error_404(request)
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    else:
        formulario = RegistroForm()
    return render(request, "registration/signup.html", {"formulario": formulario})


def login(request):
    if request.method == "POST":
        formulario = LoginForm(request.POST)
        try:
            # enviamos los datos al servidor para tener el token
            token_acceso = helper.obtener_token_session(
                formulario.data.get("username"), formulario.data.get("password")
            )
            request.session["token"] = token_acceso

            headers = {"Authorization": "Bearer " + token_acceso}

            # obtenemos los datos del usuario
            response = requests.get(
                BASE_URL + "usuario/token/" + token_acceso,
                headers=headers,
            )
            usuario = response.json()

            # guardamos los datos en la sesion del usuario
            request.session["usuario"] = usuario

            return redirect("index")
        except Exception as excepcion:
            print(f"Hubo un error en la petición: {excepcion}")
            formulario.add_error("username", excepcion)
            formulario.add_error("password", excepcion)
            return render(request, "registration/login.html", {"form": formulario})
    else:
        formulario = LoginForm()
    return render(request, "registration/login.html", {"form": formulario})


def logout(request):
    del request.session["token"]
    return redirect("index")


def prueba_cors(request):
    return render(request, "empleado/empleado_js.html")


def tratar_errores(request, codigo):
    if codigo == 404:
        return error_404(request)
    else:
        return error_500(request)


# Páginas de Error
def error_404(request, exception=None):
    return render(request, "errores/404.html", None, None, 404)


# Páginas de Error
def error_500(request, exception=None):
    return render(request, "errores/500.html", None, None, 500)
