from django import forms
from datetime import datetime, date

class BusquedaEmpleadoForm(forms.Form):
    textoBusqueda = forms.CharField(required=False, label="Buscar Empleado")
    
class BusquedaAvanzadaEmpleadoForm(forms.Form):
    empleado= forms.CharField(required=False, label="Nombre del empleado")
    apellido= forms.CharField(required=False, label="Apellido del empleado")
    cargo= forms.CharField(required=False, label="Cargo del empleado")
    fecha_contratacion= forms.DateField(required=False, label="Fecha de contratacion")
    