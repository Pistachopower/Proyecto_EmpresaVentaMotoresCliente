import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent 
environ.Env.read_env(os.path.join(BASE_DIR, '.env'),True) #configura todo lo referente a las variables de entorno
env = environ.Env()

class helper: 
    def obtener_proveedores_select():
    # obtenemos todos los proveedores
        headers = {'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN")} 
        response = requests.get('http://127.0.0.1:8080/api/v1/proveedores',headers=headers)
        proveedores = response.json()

        lista_proveedores = [("","Ninguna")]
        for proveedor in proveedores:
            lista_proveedores.append((proveedor["proveedor"],proveedor["telefono"]))
        return lista_proveedores
    
    def obtener_proveedor(proveedor_id):
    # obtenemos todos los proveedores
        headers = {'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN")} 
        response = requests.get('http://127.0.0.1:8080/api/v1/proveedores/' +str(proveedor_id),headers=headers)
        proveedores = response.json()
        return proveedores

    
    