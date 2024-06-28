from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto


class Registro(UserCreationForm):
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "NOMBRE"}
        ),
    )

    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "APELLIDO"}
        ),
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "E-MAIL"}
        ),
    )

    telefono = forms.IntegerField(
        max_value=999999999,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "TELEFONO"}
        ),
    )

    PAISES_CHOICES = [
        ('AR', 'Argentina'),
        ('BR', 'Brasil'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('MX', 'México'),
        ('PE', 'Perú'),
    ]

    paises = forms.ChoiceField(
        choices=PAISES_CHOICES,
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "PAISES"}
        ),
    )

    provincia = forms.ChoiceField(
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "PROVINCIA"}
        ),
    )

    direccion = forms.CharField(
        max_length=200,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "TELEFONO"}
        ),
    )

    dpto_casa = forms.IntegerField(
        max_value=9999,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "NÚMERO DPTO / CASA"}
        ),
    )

    codigo_postal = forms.IntegerField(
        max_value=9999999,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "CÓDIGO POSTAL"}
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "telefono",
            "password1",
            "password2",
            "paises",
            "provincia",
            "direccion",
            "dpto_casa",
            "codigo_postal",
        )

    def __init__(self, *args, **kwargs):
        super(Registro, self).__init__(*args, **kwargs)
        self.fields['provincia'].choices = [('', 'Seleccione un país primero')]
