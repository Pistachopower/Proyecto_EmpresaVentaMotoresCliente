from django.shortcuts import render,redirect
import requests
from django.core import serializers
from pathlib import Path
import environ
import os
from .forms import *

#aqui lo que hacemos es que accedemos a .env para poder acceder a la api
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'),True)
env = environ.Env()

# Create your views here.
def index(request):
    return render(request, 'index.html')


def empleados_lista_api(request):
    #header=  se refiere para acceder a la api y al servidor
    headers= {'Authorization': 'Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8'} 
    

#JWT: JSON WEB TOKEN

def empleados_lista_api(request):
    #header=  se refiere para acceder a la api y al servidor
    headers= {'Authorization': 'Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8'} 
    #http://127.0.0.1:8080/api/v1/empleados: esto hace referencia a la url de la api 
    response= requests.get('http://127.0.0.1:8080/api/v1/empleados', headers=headers) #aqui llamas a la url de la api
    empleados_normal= response.json()
    return render(request, 'empleado/lista.html', {'empleados': empleados_normal})



def empleados_lista_api_mejorado(request):
    headers= {'Authorization': 'Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/empleados_mejorado', headers=headers)
    empleados= response.json()
    return render(request, 'empleado/lista_Mejorado.html', {'empleados': empleados})

def listar_clientes_mejorado(request):
    headers= {'Authorization': 'Bearer 8qmTvt9IQ3h3tuDjPBjQbyMNEfRvk7'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/clientes_mejorado', headers=headers)
    cliente= response.json()
    return render(request, 'cliente/lista_Mejorado.html', {'cliente_mejorado': cliente})


def listar_pedido_mejorado(request):
    headers= {'Authorization': 'Bearer 8qmTvt9IQ3h3tuDjPBjQbyMNEfRvk7'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/pedido_mejorado', headers=headers)
    pedido= response.json()
    return render(request, 'pedido/lista_Mejorado.html', {'pedido_mejorado': pedido})


def crear_cabecera():
    return {
        'Authorization': 'Bearer ' + env("OAUTH2_ACCESS_TOKEN"),
        "Content-Type": "application/json"
    }


#busqueda simple empleados
# def busquedaSimpleEmpleado(request):
#     #obtenemos el formulario
#     formulario = BusquedaEmpleadoForm(request.GET)
     

#     if formulario.is_valid():
#         #objeto que contiene el token
#         headers= crear_cabecera()
#         response = requests.get(
#             'http://127.0.0.1:8080/api/v1/busquedasimpleempleados',
#             headers=headers,
#             params={'textoBusqueda': formulario.data.get("textoBusqueda")}
#         )
    
#         empleados= response.json()
#         return render(request, 'empleado/lista.html', {'empleados': empleados})
    
#      # Redirigir si el formulario no es válido
#     if "HTTP_REFERER" in request.META:
#         return redirect(request.META["HTTP_REFERER"])
#     else:
#         return redirect("principal")


def busquedaSimpleEmpleado(request):
    print(request.GET)
    
    if(len(request.GET) > 0):
        #obtenemos el formulario
        formulario = BusquedaEmpleadoForm(request.GET)
        
        if formulario.is_valid():
        #objeto que contiene el token
            headers= crear_cabecera()
            response = requests.get(
            'http://127.0.0.1:8080/api/v1/busquedasimpleempleados',
            headers=headers,
            params={'textoBusqueda': formulario.data.get("textoBusqueda")}
        )
    
        empleados= response.json()
        return render(request, 'empleado/lista.html', {'empleados': empleados})
        
    else:
        empleados = None
    return render(request, 'empleado/lista.html', {'empleados': empleados})