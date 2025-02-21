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

# aqui lo que hacemos es que accedemos a .env para poder acceder a la api
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"), True)
env = environ.Env()


#definimos la url para la configuracion de la api
BASE_URL = "http://127.0.0.1:8080/api/v1/"

# Create your views here.
def index(request):
    return render(request, "index.html")


def empleados_lista_api(request):
    # header=  se refiere para acceder a la api y al servidor
    headers = {"Authorization": "Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8"}


# JWT: JSON WEB TOKEN


def empleados_lista_api(request):
    # header=  se refiere para acceder a la api y al servidor
    headers = {"Authorization": "Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8"}
    # http://127.0.0.1:8080/api/v1/empleados: esto hace referencia a la url de la api
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/empleados", headers=headers
    )  # aqui llamas a la url de la api
    empleados_normal = response.json()
    return render(request, "empleado/lista.html", {"empleados": empleados_normal})


def empleados_lista_api_mejorado(request):
    headers = {"Authorization": "Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8"}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/empleados_mejorado", headers=headers
    )
    empleados = response.json()
    return render(request, "empleado/lista_Mejorado.html", {"empleados": empleados})


def listar_clientes_mejorado(request):
    headers = {"Authorization": "Bearer 8qmTvt9IQ3h3tuDjPBjQbyMNEfRvk7"}
    response = requests.get(
        "http://127.0.0.1:8080/api/v1/clientes_mejorado", headers=headers
    )
    cliente = response.json()
    return render(request, "cliente/lista_Mejorado.html", {"cliente_mejorado": cliente})


def listar_pedido_mejorado(request):
    headers = {"Authorization": "Bearer 8qmTvt9IQ3h3tuDjPBjQbyMNEfRvk7"}
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

#tengo que buscar apellido o cargo
def busquedaSimpleEmpleado(request):

    if len(request.GET) > 0:
        # obtenemos el formulario
        formulario = BusquedaEmpleadoForm(request.GET)

        if formulario.is_valid():
            # objeto que contiene el token
            headers = crear_cabecera()
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
                # objeto que contiene el token
            headers = crear_cabecera()

            response = requests.get(
                    f"{BASE_URL}busqueda-avanzada-empleados",
                    headers=headers,
                    params=formulario.data,  # Pasar los datos del formulario validados
                )

            if response.status_code == requests.codes.ok:
                empleados = response.json()  # Obtenemos los datos en formato json
                return render(request,"empleado/busqueda_avanzada.html",{"formulario": formulario, "empleados": empleados})
            else:
                response.raise_for_status()

        except HTTPError as http_err:
            print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                errores = response.json()
                print(errores)
                for error in errores:
                    formulario.add_error(error, errores[error])  # Agregar los errores del formulario
                    return render(request,"empleado/busqueda_avanzada.html",{"formulario": formulario})
            else:
                return error_500(request)  # Retornar una página de error 500
        except Exception as err:
            print(f"Ocurrió un error: {err}")
            return error_500(request)

    else:
        formulario = BusquedaAvanzadaEmpleadoForm(None)
    return render(
        request, "empleado/busqueda_avanzada.html", {"formulario": formulario})
    
    
def busquedaAvanzadaClientes(request):

    if len(request.GET) > 0:

        formulario = BusquedaAvanzadaClientesForm(request.GET)

        
        try:
                # objeto que contiene el token
            headers = crear_cabecera()

            response = requests.get(
                    f"{BASE_URL}busqueda-avanzada-clientes",
                    headers=headers,
                    params=formulario.data,  # Pasar los datos del formulario validados
                )

            if response.status_code == requests.codes.ok:
                    clientes = response.json()  # Obtenemos los datos en formato json
                    return render(
                        request,
                        "cliente/busqueda_avanzada_cliente.html",
                        {"formulario": formulario, "clientes": clientes},
                    )
            else:
                    
                response.raise_for_status()

        except HTTPError as http_err:
                #print(f"Hubo un error en la petición: {http_err}")
                if response.status_code == 400:
                    errores = response.json()
                    
                    for error in errores:
                        formulario.add_error(
                            error, errores[error]
                        )  # Agrega los errores del formulario
                    return render(
                        request,"cliente/busqueda_avanzada_cliente.html",{"formulario": formulario},
                    )
                else:
                    return error_500(request)  # Retornar una página de error 500
        except Exception as err:
                print(f"Ocurrió un error: {err}")
                return error_500(request)

    else:
        formulario = BusquedaAvanzadaClientesForm(None)
    return render(
        request, "cliente/busqueda_avanzada_cliente.html", {"formulario": formulario}
    )

#busquedaAvanzadaPedidos
def busquedaAvanzadaPedidos(request):

    if len(request.GET) > 0:

        formulario = BusquedaAvanzadaPedidoForm(request.GET)


        try:
                # objeto que contiene el token
            headers = crear_cabecera()
            response = requests.get(
                    f"{BASE_URL}busqueda-avanzada-pedidos",
                    headers=headers,
                    params=formulario.data,  # Pasar los datos del formulario validados
                )
                

            if response.status_code == requests.codes.ok:
                    pedidos = response.json()  # Obtenemos los datos en formato json
                    return render(
                        request,
                        "pedido/busqueda_avanzada_pedidos.html",
                        {"formulario": formulario, "pedidos": pedidos},
                    )
            else:
                    print(response.status_code)
                    response.raise_for_status()

        except HTTPError as http_err:
                #print(f"Hubo un error en la petición: {http_err}")
                if response.status_code == 400:
                    errores = response.json()
                    
                    for error in errores:
                        formulario.add_error(
                            error, errores[error]
                        )  # Agrega los errores del formulario
                    return render(
                        request,"pedido/busqueda_avanzada_pedidos.html",{"formulario": formulario},
                    )
                else:
                    return error_500(request)  # Retornar una página de error 500
        except Exception as err:
                print(f"Ocurrió un error: {err}")
                return error_500(request)

    else:
        formulario = BusquedaAvanzadaPedidoForm(None)
    return render(
        request, "pedido/busqueda_avanzada_pedidos.html", {"formulario": formulario})


def busquedaAvanzadaProveedor(request):

    if len(request.GET) > 0:

        formulario = BusquedaAvanzadaProveedorForm(request.GET)
        


        try:
                # objeto que contiene el token
            headers = crear_cabecera()
            response = requests.get(
                    f"{BASE_URL}busqueda-avanzada-proveedor",
                    headers=headers,
                    params=formulario.data,  # Pasar los datos del formulario validados
                )
                
                

            if response.status_code == requests.codes.ok:
                proveedor = response.json()  # Obtenemos los datos en formato json
                return render(
                        request,
                        "proveedor/busqueda_avanzada_proveedor.html",
                        {"formulario": formulario, "proveedor": proveedor},
                    )
            else:
                print(response.status_code)
                response.raise_for_status()

        except HTTPError as http_err:
                #print(f"Hubo un error en la petición: {http_err}")
            if response.status_code == 400:
                    errores = response.json()
                    
                    for error in errores:
                        formulario.add_error(
                            error, errores[error]
                        )  # Agrega los errores del formulario
                    return render(
                        request,"proveedor/busqueda_avanzada_proveedor.html",{"formulario": formulario},
                    )
            else:
                return error_500(request)  # Retornar una página de error 500
        except Exception as err:
                print(f"Ocurrió un error: {err}")
                return error_500(request)

    else:
        formulario = BusquedaAvanzadaProveedorForm(None)
    return render(
        request, "proveedor/busqueda_avanzada_proveedor.html", {"formulario": formulario})


#post, patch, delete proveedores
def proveedor_lista(request):
    # obtenemos todos los libros
    headers =  {
                        'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN"),
                        "Content-Type": "application/json" 
                    } 
    print(headers)
    response = requests.get('http://127.0.0.1:8080/api/v1/proveedores/proveedores_listar/',headers=headers)
   # Transformamos la respuesta en json
    proveedores = response.json()
    return render(request, 'proveedor/lista_proveedor.html',{"proveedores":proveedores})


def proveedor_crear(request):
    if (request.method == "POST"):
        try:
            formulario = ProveedoresForm(request.POST)
            headers =  {
                        'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN"),
                        "Content-Type": "application/json" 
                    } 
            datos = formulario.data.copy()
            datos["proveedor"] = request.POST.get("proveedor")
            datos["telefono"] = request.POST.get("telefono")
            datos["correo"] = request.POST.get("correo") 
            datos["direccion"] = request.POST.get("direccion")                       
    
            response = requests.post(
                'http://127.0.0.1:8080/api/v1/proveedores/crear/',
                headers=headers,
                data=json.dumps(datos)
            )
            if(response.status_code == requests.codes.ok):
                return redirect("proveedor_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, 
                            'proveedor/crear.html',
                            {"formulario":formulario})
            else:
                return error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return error_500(request)
        
    else:
         formulario = ProveedoresForm(None)
    return render(request, 'proveedor/crear.html',{"formulario":formulario})


def proveedores_editar_put(request,proveedor_id):
    
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
        
    proveedor = helper.obtener_proveedor(proveedor_id)
    formulario = ProveedoresForm(datosFormulario,
            initial={
                'proveedor': proveedor['proveedor'],
                'telefono': proveedor["telefono"],
                'correo': proveedor['correo'],
                'direccion': proveedor['direccion'], 
            }
    )
    if (request.method == "POST"):
        formulario = ProveedoresForm(request.POST)
        datos = request.POST.copy()
        datos["proveedor"] = request.POST.get("proveedor")
        datos["telefono"] = request.POST.get("telefono")
        datos["correo"] = request.POST.get("correo") 
        datos["direccion"] = request.POST.get("direccion")  
        cliente = cliente_api(env('OAUTH2_ACCESS_TOKEN'),"PUT",'proveedores/editar/'+str(proveedor_id) + str('/'),datos)
        cliente.realizar_peticion_api()
        if(cliente.es_respuesta_correcta()):
            return redirect("proveedor_lista")
        else:
            if(cliente.es_error_validacion_datos()):
                cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request,cliente.codigoRespuesta)
    
    return render(request, 'proveedor/actualizar.html',{"formulario":formulario,"proveedor":proveedor})



def proveedores_editar_patch(request,proveedor_id):
   
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    proveedor = helper.obtener_proveedor(proveedor_id) #se hace la consulta a la bd
    formulario = ProveedorActualizarNombreForm(datosFormulario,
            initial={
                'proveedor': proveedor['proveedor'],
            }
    )
    if (request.method == "POST"):
        try:
            formulario = ProveedorActualizarNombreForm(request.POST)
            headers = crear_cabecera()
            datos = request.POST.copy()
            response= requests.patch(
                f"{BASE_URL}proveedores/editar/nombre/{proveedor_id}/",
                headers=headers,
                data=json.dumps(datos)
            )
            
            if(response.status_code == requests.codes.ok):
                return redirect("proveedor_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if(response.status_code == 400):
                errores = response.json()
                for error in errores:
                    formulario.add_error(error,errores[error])
                return render(request, "proveedor/actualizarNombreProveedor.html",{"formulario":formulario,"proveedor":proveedor})
            else:
                return error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return error_500(request)
            

        
    return render(request, 'proveedor/actualizarNombreProveedor.html',{"formulario":formulario,"proveedor":proveedor})



def proveedores_eliminar(request,proveedor_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
                f'http://127.0.0.1:8080/api/v1/proveedores/eliminar/{proveedor_id}/',
                headers=headers
            )
        if(response.status_code == requests.codes.ok):
            return redirect("proveedor_lista")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return error_500(request)
    return redirect('proveedor_lista')

#post, patch, delete pedido metodopago
def pedido_metodopago_lista(request):
    headers =  {
                        'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN"),
                        "Content-Type": "application/json" 
                    } 
    response = requests.get('http://127.0.0.1:8080/api/v1/pedido-metodopago_listar/',headers=headers)
   # Transformamos la respuesta en json
    pedidosMetPag = response.json()
    return render(request, 'pedidoMetodoPago/lista_pedidoMetodoPago.html',{"pedidosMetPag":pedidosMetPag})

#POR CORREGIR. HAY ERRORES
def pedido_metodopago_crear(request):
    if request.method == "POST":
        try:
            formulario = PedidoMetodoPagoForm(request.POST)
            headers = {
                'Authorization': 'Bearer ' + env("OAUTH2_ACCESS_TOKEN"),
                "Content-Type": "application/json"
            }
            datos = formulario.data.copy()
            datos["pedido"] = request.POST.get("pedido")
            datos["fecha_pedido"] = str(
                                            datetime.date(year=int(datos['fecha_publicacion_year']),
                                                        month=int(datos['fecha_pedido_month']),
                                                        day=int(datos['fecha_pedido_day']))
                                             )
            datos["metodo_pago"] = request.POST.get("metodo_pago")

            response = requests.post(
                'http://127.0.0.1:8080/api/v1/pedido-metodopago/crear/',
                headers=headers,
                data=json.dumps(datos)
            )
            if response.status_code == requests.codes.ok:
                return redirect("proveedor_lista")
            else:
                print(response.status_code)
                response.raise_for_status()
        except HTTPError as http_err:
            print(f'Hubo un error en la petición: {http_err}')
            if response.status_code == 400:
                errores = response.json()
                for error in errores:
                    formulario.add_error(error, errores[error])
                return render(request, 'pedidoMetodoPago/crear.html', {"formulario": formulario})
            else:
                return error_500(request)
        except Exception as err:
            print(f'Ocurrió un error: {err}')
            return error_500(request)
    else:
        formulario = PedidoMetodoPagoForm(None)
    return render(request, 'pedidoMetodoPago/crear.html', {"formulario": formulario})


def pedido_metodopago_editar_put(request, pedido_id):
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST

    pedido = helper.obtener_pedido(pedido_id)
    formulario = PedidoMetodoPagoForm(datosFormulario,
            initial={
                'pedido': pedido['pedido'],
                'fecha_pedido': pedido["fecha_pedido"],
                'metodo_pago': pedido['metodo_pago'],
            }
    )
    if request.method == "POST":
        formulario = PedidoMetodoPagoForm(request.POST)
        datos = request.POST.copy()
        datos["pedido"] = request.POST.get("pedido")
        datos["fecha_pedido"] = request.POST.get("fecha_pedido")
        datos["metodo_pago"] = request.POST.get("metodo_pago")
        cliente = cliente_api(env('OAUTH2_ACCESS_TOKEN'), "PUT", 'pedido-metodopago/editar/' + str(pedido_id) + str('/'), datos)
        cliente.realizar_peticion_api()
        if cliente.es_respuesta_correcta():
            return redirect("pedido_metodopago_editar_put", pedido_id=pedido_id)
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request, cliente.codigoRespuesta)

    return render(request, 'pedidoMetodoPago/actualizar.html', {"formulario": formulario, "pedido": pedido})

def pedido_metodopago_editar_patch(request, pedido_id):
    datosFormulario = None
    
    if request.method == "POST":
        datosFormulario = request.POST
    
    pedido = helper.obtener_pedido(pedido_id)  # se hace la consulta a la bd
    formulario = PedidoActualizarMetodoPagoForm(datosFormulario,
            initial={
                'metodo_pago': pedido['metodo_pago'],
            }
    )
    if request.method == "POST":
        formulario = PedidoActualizarMetodoPagoForm(request.POST)
        datos = request.POST.copy()
        datos["metodo_pago"] = request.POST.get("metodo_pago")
    
        cliente = cliente_api(env('OAUTH2_ACCESS_TOKEN'), "PUT", 'pedido-metodopago/editar/nombre/' + str(pedido_id) + str('/'), datos)
        cliente.realizar_peticion_api()
        if cliente.es_respuesta_correcta():
            return redirect("pedido_metodopago_editar_patch", pedido_id=pedido_id)
        else:
            if cliente.es_error_validacion_datos():
                cliente.incluir_errores_formulario(formulario)
            else:
                return tratar_errores(request, cliente.codigoRespuesta)
        
    return render(request, 'pedidoMetodoPago/actualizarMetodoPago.html', {"formulario": formulario, "pedido": pedido})


def pedido_metodopago_eliminar(request, pedido_id):
    try:
        headers = crear_cabecera()
        response = requests.delete(
                f'http://127.0.0.1:8080/api/v1/pedido-metodopago/eliminar/{pedido_id}/',
                headers=headers
            )
        if response.status_code == requests.codes.ok:
            return redirect("pedido_metodopago_lista")
        else:
            print(response.status_code)
            response.raise_for_status()
    except Exception as err:
        print(f'Ocurrió un error: {err}')
        return error_500(request)
    return redirect('pedido_metodopago_lista')


def tratar_errores(request,codigo):
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
