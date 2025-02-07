from django.shortcuts import render, redirect
import requests
from django.core import serializers
from pathlib import Path
import environ
import os
from .forms import *
from requests.exceptions import HTTPError

# aqui lo que hacemos es que accedemos a .env para poder acceder a la api
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"), True)
env = environ.Env()


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
        "http://127.0.0.1:8080/api/v1/pedido_mejorado", headers=headers
    )
    pedido = response.json()
    return render(request, "pedido/lista_Mejorado.html", {"pedido_mejorado": pedido})


def crear_cabecera():
    return {
        "Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN"),
        "Content-Type": "application/json",
    }




def busquedaSimpleEmpleado(request):
    print(request.GET)

    if len(request.GET) > 0:
        # obtenemos el formulario
        formulario = BusquedaEmpleadoForm(request.GET)

        if formulario.is_valid():
            # objeto que contiene el token
            headers = crear_cabecera()
            response = requests.get(
                "http://127.0.0.1:8080/api/v1/busquedasimpleempleados",
                headers=headers,
                params={"textoBusqueda": formulario.data.get("textoBusqueda")},
            )

        empleados = response.json()
        return render(request, "empleado/lista.html", {"empleados": empleados})

    else:
        empleados = None
    return render(request, "empleado/lista.html", {"empleados": empleados})


def busquedaAvanzadaEmpleado(request):
    
    print(request.GET)
    
    if len(request.GET) > 0:

        formulario = BusquedaAvanzadaEmpleadoForm(request.GET)
        
        if formulario.is_valid():
            try:
                # objeto que contiene el token
                headers = crear_cabecera()

                response = requests.get(
                    "http://127.0.0.1:8080/api/v1/busqueda-avanzada-empleados",
                    headers=headers,
                    params= formulario.cleaned_data  # Pasar los datos del formulario validados
                )
                
                print("🔍 Respuesta del servidor:", response.status_code, response.text)
                
                if response.status_code == requests.codes.ok:
                    empleados = response.json()  # Obtenemos los datos en formato json
                    print("🔍 Datos recibidos:", empleados)  # Verifica que los datos llegan correctamente
                    return render(request, 'empleado/busqueda_avanzada.html', {"formulario": formulario,"empleados": empleados})
                else:
                    print(response.status_code)
                    response.raise_for_status() 
                

            except HTTPError as http_err:
                print(f'Hubo un error en la petición: {http_err}')
                if response.status_code == 400:
                    errores = response.json()
                    for error in errores:
                        formulario.add_error(error, errores[error])  # Agregar los errores del formulario
                    return render(request, 'empleado/busqueda_avanzada.html', {"formulario": formulario, "errores": errores})
                else:
                    return error_500(request)  # Retornar una página de error 500
            except Exception as err:
                print(f'Ocurrió un error: {err}')
                return error_500(request)

    else:
        formulario = BusquedaAvanzadaEmpleadoForm(None)
    return render(request, "empleado/busqueda_avanzada.html", {"formulario": formulario})



#Páginas de Error
def error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

#Páginas de Error
def error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)