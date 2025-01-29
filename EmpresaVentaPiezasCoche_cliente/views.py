from django.shortcuts import render,redirect
import requests
from django.core import serializers


# Create your views here.
def index(request):
    return render(request, 'index.html')



def empleados_lista_api(request):
    response= requests.get('http://127.0.0.1:8000/api/v1/usuarios')
    
    empleados= response.json()
    
    return render(request, 'empleado/lista.html', {'empleados': empleados})


