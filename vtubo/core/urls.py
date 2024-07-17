from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('actualizar_usuario/', actualizar_usuario, name='actualizar_usuario'),
    path('tienda/', tienda, name="tienda"),
    path('tiendaVista/<codigo>', tiendaVista, name="tiendaVista"),
    path('tienda/<codigo>', addtocar, name="addtocar"),
    path('Carrito', Carrito, name="Carrito"),
    path('historial_vista_admin/', historial_vista_admin, name="historial_vista_admin"),
    path('historial', historial, name="historial"),
    path('talentos/', talentos, name="talentos"),
    path('talentoVista/<id>', talentoVista, name="talentoVista"),
    path('limpiar', limpiar),
    path('comprar', comprar, name="comprar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
]