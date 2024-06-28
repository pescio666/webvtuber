from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('ajax/cargar-provincias/', cargar_provincias, name='ajax_cargar_provincias'),
    path('tienda/', tienda, name="tienda"),
    path('tienda/<codigo>', addtocar, name="addtocar"),
    path('Carrito', Carrito, name="Carrito"),
    path('talentos', talentos, name="talentos"),
    path('limpiar', limpiar),
    path('comprar', comprar, name="comprar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
]