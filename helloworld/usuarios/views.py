from django.shortcuts import render
from .models import Usuario

# Create your views here.


def usuarios_app(request):
    usuarios = Usuario.objects.all()

    return render (request, 'usuarios/usuarios_app.html', {'usuarios': usuarios})
