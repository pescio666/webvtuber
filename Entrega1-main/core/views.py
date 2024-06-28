from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
import requests
from django.http import JsonResponse
from django.views import View


def home(request):
    productos = Producto.objects.all()
    return render(request, "core/index.html", {"productos": productos})


def talentos(request):
    productos = Producto.objects.all()
    return render(request, "core/talentos.html", {"productos": productos})


def tienda(request):
    productos = Producto.objects.all()
    return render(
        request,
        "core/tienda.html",
        {"productos": productos, "carro": request.session.get("carro", [])},
    )


def addtocar(request, codigo):
    if not request.user.is_authenticated:
        return redirect(to="login")
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = float(item[3]) * item[4]
            break
    else:
        carro.append(
            [
                codigo,
                producto.detalle,
                producto.imagen.url,
                float(producto.precio),  # Convertir precio a float si es decimal
                1,
                float(producto.precio),  # Convertir precio a float si es decimal
            ]
        )
    request.session["carro"] = carro
    return redirect(to="tienda")


def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="Carrito")


def Carrito(request):
    carro = request.session.get("carro", [])
    return render(request, "core/Carrito.html", {"carro": carro})


def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo=item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()
        detalle.producto.stock -= detalle.cantidad
        detalle.producto.save()
    request.session["carro"] = []
    return redirect(to="carrito")


def limpiar(request):
    request.session.flush()
    productos = Producto.objects.all()
    return render(request, "core/index.html", {"productos": productos})


def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, "core/registro.html", {"form": registro})


def logout(request):
    return logout_then_login(request, login_url="login")


class RegistroView(View):
    form_class = Registro
    template_name = "registro.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
        return render(request, self.template_name, {"form": form})


def cargar_provincias(request):
    pais_id = request.GET.get("pais_id")
    if pais_id == "AR":
        provincias = [
            ("BA", "Buenos Aires"),
            ("CABA", "Ciudad Autónoma de Buenos Aires"),
            ...,
        ]
    elif pais_id == "BR":
        provincias = [("SP", "São Paulo"), ("RJ", "Rio de Janeiro"), ...]
    elif pais_id == "CL":
        provincias = [("ST", "Santiago"), ("MP", "Maipo"), ...]
    elif pais_id == "CO":
        provincias = [("BL", "Bolivar"), ("CD", "Caldas"), ...]
    elif pais_id == "MX":
        provincias = [("ZT", "Zacatecas"), ("VC", "Veracruz"), ...]
    elif pais_id == "PE":
        provincias = [("AQ", "Arequipa"), ("CC", "Cusco"), ...]
    # Agrega más opciones para otros países
    else:
        provincias = []
    return JsonResponse({"provincias": provincias})
