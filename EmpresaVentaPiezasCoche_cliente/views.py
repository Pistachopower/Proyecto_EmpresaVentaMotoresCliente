from django.shortcuts import render,redirect
import requests
from django.core import serializers


# Create your views here.
def index(request):
    return render(request, 'index.html')

def empleados_lista_api(request):
    headers= {'Authorization': 'Bearer GjhyLVBACKhAxmh2pmcjQDASr4ZYa8'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/empleados_mejorado', headers=headers)
    empleados= response.json()
    return render(request, 'empleado/lista.html', {'empleados': empleados})

def empleados_lista_api_mejorado(request):
    headers= {'Authorization': 'Bearer GjhyLVBACKhAxmh2pmcjQDASr4ZYa8'} 
    response= requests.get('http://127.0.0.1:8080/api/v1/empleados_mejorado', headers=headers)
    empleados= response.json()
    return render(request, 'empleado/lista.html', {'empleados': empleados})


#def empleados_lista_api(request):
#    # obtenemos todos los libros
#    headers = {'Authorization': 'Bearer '+ env('token')} 
#    headers = {'Authorization': 'Bearer '+request.session["token"]} 
#    print(headers)
#    response = requests.get('http://127.0.0.1:8000/api/v1/libros',headers=headers)
#   # Transformamos la respuesta en json
#    libros = response.json()
#    #return render(request, 'libro/lista.html',{"libros_mostrar":libros})
#    return render(request, 'libro/lista_mejorada.html',{"libros_mostrar":libros})