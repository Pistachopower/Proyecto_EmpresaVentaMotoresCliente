from django import forms
from datetime import datetime, date

class BusquedaEmpleadoForm(forms.Form):
    textoBusqueda = forms.CharField(required=False, label="Buscar Empleado")
    
class BusquedaAvanzadaEmpleadoForm(forms.Form):
    empleado= forms.CharField(required=False, label="Nombre del empleado")
    apellido= forms.CharField(required=False, label="Apellido del empleado")
    cargo= forms.CharField(required=False, label="Cargo del empleado")
    fecha_contratacion= forms.DateField(required=False, label="Fecha de contratacion")
 
  
#ES SOLO UN APAÑO, DEBES OBTENERLO DE LA API
TIPO_CLIENTES = [('P', 'Particular'), ('E', 'Empresa'), ('-', '------')]
    
class BusquedaAvanzadaClientesForm(forms.Form):
    cliente = forms.CharField(required=False, label="Nombre del cliente")
    apellido = forms.CharField(required=False, label="Apellido del cliente")
    tipo_clientes = forms.CharField(required=False, label="Tipo de cliente"
                                    , widget=forms.Select(choices=TIPO_CLIENTES))
    
    
class BusquedaAvanzadaPedidoForm(forms.Form):
    pedido = forms.CharField(required=False, label="Nombre del pedido")
    fecha_pedido = forms.CharField(required=False, label="Fecha del pedido")
    metodo_pago = forms.CharField(required=False, label="Método de pago")
    
class BusquedaAvanzadaProveedorForm(forms.Form):
    proveedor = forms.CharField(required=False, label="Nombre del proveedor")
    telefono = forms.CharField(required=False, label="telefono del proveedor")
    correo = forms.CharField(required=False, label="correo del proveedor")