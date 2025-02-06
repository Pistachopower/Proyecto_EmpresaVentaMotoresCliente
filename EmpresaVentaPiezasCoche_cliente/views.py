from django.shortcuts import render,redirect
import requests
from django.core import serializers


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
    headers= {'Authorization': 'Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/clientes_mejorado', headers=headers)
    cliente= response.json()
    return render(request, 'cliente/lista_Mejorado.html', {'cliente_mejorado': cliente})


def listar_pedido_mejorado(request):
    headers= {'Authorization': 'Bearer 0eRLQm0yVN3346rkzVB01b4MX2tvC8'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/pedido_mejorado', headers=headers)
    pedido= response.json()
    return render(request, 'pedido/lista_Mejorado.html', {'pedido_mejorado': pedido})
