from django import forms
from datetime import datetime, date
from .helper import helper


class BusquedaEmpleadoForm(forms.Form):
    textoBusqueda = forms.CharField(required=False, label="Buscar Empleado")

    def clean(self):
        cleaned_data = super().clean()

        textoBusqueda = cleaned_data.get("textoBusqueda")

        if not textoBusqueda:
            raise forms.ValidationError("Debe introducir un texto de búsqueda")

        return cleaned_data


class BusquedaAvanzadaEmpleadoForm(forms.Form):
    empleado = forms.CharField(required=False, label="Nombre del empleado")
    apellido = forms.CharField(required=False, label="Apellido del empleado")
    cargo = forms.CharField(required=False, label="Cargo del empleado")
    fecha_contratacion = forms.DateField(required=False, label="Fecha de contratacion")


# ES SOLO UN APAÑO, DEBES OBTENERLO DE LA API
TIPO_CLIENTES = [("P", "Particular"), ("E", "Empresa"), ("-", "------")]


class BusquedaAvanzadaClientesForm(forms.Form):
    cliente = forms.CharField(required=False, label="Nombre del cliente")
    apellido = forms.CharField(required=False, label="Apellido del cliente")
    tipo_clientes = forms.CharField(
        required=False,
        label="Tipo de cliente",
        widget=forms.Select(choices=TIPO_CLIENTES),
    )


class BusquedaAvanzadaPedidoForm(forms.Form):
    pedido = forms.CharField(required=False, label="Nombre del pedido")
    fecha_pedido = forms.CharField(required=False, label="Fecha del pedido")
    metodo_pago = forms.CharField(required=False, label="Método de pago")


class BusquedaAvanzadaProveedorForm(forms.Form):
    proveedor = forms.CharField(required=False, label="Nombre del proveedor")
    telefono = forms.CharField(required=False, label="telefono del proveedor")
    correo = forms.CharField(required=False, label="correo del proveedor")


# Formulario post, patch,
class ProveedoresForm(forms.Form):
    proveedor = forms.CharField(
        label="Nombre del proveedor",
        required=True,
        max_length=200,
        help_text="200 caracteres como máximo",
    )

    telefono = forms.CharField(
        label="telefono del proveedor",
        required=True,
        max_length=12,
        help_text="12 caracteres como máximo",
    )

    correo = forms.CharField(
        label="correo del proveedor",
        required=True,
        max_length=20,
        help_text="20 caracteres como máximo",
    )

    direccion = forms.CharField(
        label="direccion del proveedor",
        required=True,
        max_length=200,
        help_text="20 caracteres como máximo",
    )


class ProveedorActualizarNombreForm(forms.Form):
    proveedor = forms.CharField(
        label="Nombre del proveedor",
        required=True,
        max_length=200,
        help_text="200 caracteres como máximo",
    )


class PedidosForm(forms.Form):
    pedido = forms.CharField(
        label="Nombre del pedido",
        required=True,
        max_length=200,
        help_text="200 caracteres como máximo",
    )

    fecha_pedido = forms.DateField(
        label="Fecha fecha_pedido",
        initial=datetime.today,
        widget=forms.SelectDateWidget(years=range(2900)),
    )

    ESTADO = [("P", "Pendiente"), ("ENV", "Enviado"), ("ENTR", "Entregado")]

    estado = forms.CharField(
        required=False, label="Estado", widget=forms.Select(choices=ESTADO)
    )

    total_importe = forms.IntegerField(
        label="importe total", required=True, help_text="200 caracteres como máximo"
    )

    def __init__(self, *args, **kwargs):

        super(PedidosForm, self).__init__(*args, **kwargs)

        metodoPagoDisponibles = helper.obtener_metodos_pago_select()
        self.fields["metodo_pago"] = forms.ChoiceField(
            choices=metodoPagoDisponibles,
            widget=forms.Select,
            required=True,
            help_text="Despliega y selecciona un elemento",
        )

        UsuarioDisponiblesUsuario = helper.obtener_usuario_select()
        self.fields["usuario_Pedido"] = forms.ChoiceField(
            choices=UsuarioDisponiblesUsuario,
            widget=forms.Select,
            required=True,
            help_text="Despliega y selecciona un elemento",
        )

        clientesDisponibles = helper.obtener_cliente_select()
        self.fields["cliente"] = forms.ChoiceField(
            choices=clientesDisponibles,
            widget=forms.Select,
            required=True,
            help_text="Despliega y selecciona un elemento",
        )


class PedidoActualizarNombreForm(forms.Form):
    pedido = forms.CharField(
        label="Nombre del pedido",
        required=True,
        max_length=200,
        help_text="200 caracteres como máximo",
    )
