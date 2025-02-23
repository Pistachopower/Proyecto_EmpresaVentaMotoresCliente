import requests
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(
    os.path.join(BASE_DIR, ".env"), True
)  # configura todo lo referente a las variables de entorno
env = environ.Env()


class helper:
    # def obtener_proveedores_select():
    # # obtenemos todos los proveedores
    #     headers = {'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN")}
    #     response = requests.get('http://127.0.0.1:8080/api/v1/proveedores/proveedores_listar/',headers=headers)
    #     proveedores = response.json()

    #     lista_proveedores = [("","Ninguna")]
    #     for proveedor in proveedores:
    #         lista_proveedores.append((proveedor["id"],proveedor["proveedor"]))
    #     return lista_proveedores

    def obtener_proveedor_select(proveedor_id):
        # obtenemos todos los proveedores
        headers = {"Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN")}
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/proveedores/" + str(proveedor_id),
            headers=headers,
        )
        proveedores = response.json()
        return proveedores

    # def obtener_pedido(pedido_id):
    #     headers = {'Authorization': 'Bearer '+env("OAUTH2_ACCESS_TOKEN")}
    #     response = requests.get('http://127.0.0.1:8080/api/v1/pedido-metodopago/' + str(pedido_id), headers=headers)
    #     pedido = response.json()
    #     return pedido

    def obtener_metodos_pago_select():
        headers = {"Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN")}
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/metodos-pago-lista/", headers=headers
        )
        metodospago = response.json()

        lista_metodospago = [("", "Ninguna")]
        for metodoP in metodospago:
            lista_metodospago.append((metodoP["id"], metodoP["metodo_pago"]))
        return lista_metodospago

    def obtener_usuario_select():
        headers = {"Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN")}
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/usuario-lista/", headers=headers
        )
        usuario = response.json()

        lista_usuario = [("", "Ninguna")]
        for user in usuario:
            lista_usuario.append((user["id"], user["nombre"]))
        return lista_usuario

    def obtener_cliente_select():
        headers = {"Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN")}
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/clientes-lista/", headers=headers
        )
        clientes = response.json()

        lista_clientes = [("", "Ninguna")]
        for cliente in clientes:
            lista_clientes.append((cliente["id"], cliente["cliente"]))
        return lista_clientes

    def obtener_pedido_select(pedido_id):
        headers = {"Authorization": "Bearer " + env("OAUTH2_ACCESS_TOKEN")}
        response = requests.get(
            "http://127.0.0.1:8080/api/v1/pedido-metodopago/" + str(pedido_id),
            headers=headers,
        )
        pedido = response.json()
        return pedido
    