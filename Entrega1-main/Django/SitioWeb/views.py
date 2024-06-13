from django.shortcuts import render

# Create your views here.
def crud(request):
    Usuarios = Usuarios.objects.all()
    context = {'Usuarios': usuarios}
    return render(request, 'usuarios/usuarios_list.html', context)
