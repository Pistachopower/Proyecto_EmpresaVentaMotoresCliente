from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#recuperacion passw
from django.urls import path 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados/',views.empleados_lista_api,name='empleados'),
    path('empleados_mejorado/',views.empleados_lista_api_mejorado,name='empleados_mejorado'),
    path('clientes_mejorado/',views.listar_clientes_mejorado,name='cliente_mejorado'),
    path('pedido_mejorado/',views.listar_pedido_mejorado,name='pedido_mejorado'),
    
    #busqueda
    path('busquedasimpleempleados/',views.busquedaSimpleEmpleado,name='busquedaSimpleEmpleado'),
    
    path('busqueda-avanzada-empleados/',views.busquedaAvanzadaEmpleado,name='busquedaAvanzadaEmpleado'),
    path('busqueda-avanzada-clientes/',views.busquedaAvanzadaClientes,name='busquedaAvanzadaClientes'),
    path('busqueda-avanzada-pedidos/',views.busquedaAvanzadaPedidos,name='busquedaAvanzadaPedidos'),
    path('busqueda-avanzada-proveedor/',views.busquedaAvanzadaProveedor,name='busquedaAvanzadaProveedor'),
    
    #post, patch, put, delete
    path('proveedores/crear/',views.proveedor_crear,name='proveedor_crear'),
    path('proveedores/editar/<int:proveedor_id>/',views.proveedores_editar_put,name='proveedores_editar_put'),
    path('proveedores/eliminar/<int:proveedor_id>/',views.proveedores_eliminar,name='proveedores_eliminar'),

]