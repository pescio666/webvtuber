from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


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

    telefono = forms.CharField(
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "TELEFONO",
                "maxlength": "9",
            }
        ),
    )

    PAISES_CHOICES = [
        ("SL", "Selecciona un pais"),
        ("AR", "Argentina"),
        ("BR", "Brasil"),
        ("CL", "Chile"),
        ("CO", "Colombia"),
        ("MX", "México"),
        ("PE", "Perú"),
    ]

    paises = forms.ChoiceField(
        choices=PAISES_CHOICES,
        widget=forms.Select(
            attrs={"class": "form-control", "id": "id_pais", "placeholder": "PAISES"}
        ),
    )

    direccion = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "DIRECCIÓN"}
        ),
    )

    dpto_casa = forms.CharField(
        max_length=5,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "NÚMERO DPTO / CASA",
                "maxlength": "9",
            }
        ),
    )

    codigo_postal = forms.CharField(
        max_length=9,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "CÓDIGO POSTAL",
                "maxlength": "9",
            }
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
            "direccion",
            "dpto_casa",
            "codigo_postal",
        )

    def __init__(self, *args, **kwargs):
        super(Registro, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "NOMBRE DE USUARIO"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "CONTRASEÑA"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "CONFIRMAR CONTRASEÑA"}
        )

class ActualizarUsuarioForm(UserChangeForm):
    password = None  # Excluye el campo de contraseña

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control-actualizar", "placeholder": "NOMBRE DE USUARIO"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control-actualizar", "placeholder": "NOMBRE"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control-actualizar", "placeholder": "APELLIDO"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control-actualizar", "placeholder": "E-MAIL"}
            ),
        }
