from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, "core/index.html")


def talentos(request):
    talentos = Talento.objects.all()
    return render(request, "core/Talentos.html", {"talentos": talentos})


def talentoVista(request, id):
    talento = get_object_or_404(Talento, id=id)
    return render(request, 'core/talentosVistas.html', {'talento': talento})


def tienda(request):
    productos = Producto.objects.all()
    return render(
        request,
        "core/tienda.html",
        {"productos": productos, "carro": request.session.get("carro", [])},
    )

def tiendaVista(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    return render(
        request,
        "core/tiendaVista.html",
        {"producto": producto, "carro": request.session.get("carro", [])},
    )

def addtocar(request, codigo):
    if not request.user.is_authenticated:
        return redirect(to="login")
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    total = request.session.get("total",0)
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append(
            [
                codigo,
                producto.detalle,
                producto.imagen.url,
                producto.precio,
                1,
                producto.precio,
            ]
        )

    #calcular el nuevo total
    total = sum(item[5] for item in carro)

    request.session["carro"] = carro
    request.session["total"] = total
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

    total = sum(item[5] for item in carro)
    
    request.session["carro"] = carro
    request.session["total"] = total
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
    return redirect(to="Carrito")


def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, "core/historial.html", {"compras": compras})


def historial_vista_admin(request):
    ventas = Venta.objects.all()
    context = {
        "ventas": ventas,
    }
    return render(request, "core/historial_de_ventas.html", context)


def limpiar(request):
    request.session.flush()
    productos = Producto.objects.all()
    return render(request, "core/tienda.html", {"productos": productos})


def logout(request):
    return logout_then_login(request, login_url="login")


def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, "core/registro.html", {"form": registro})


@login_required
def actualizar_usuario(request):
    if request.method == "POST":
        form = ActualizarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Tus datos han sido actualizados correctamente.")
            return redirect("home")

    else:
        form = ActualizarUsuarioForm(instance=request.user)

    return render(request, "core/actualizar_usuario.html", {"form": form})


# Usuarios creados para prueba de formulario registro
# -admin
# -123456

# -Shouko
# -1234567

# -pedrito
# -pico.verde233

# -NiñoMigraña
# -j.potrillo@23

# juanito566
# Alpi.nini900

# Zucarita.899
# zumar.yico@
