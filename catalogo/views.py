from django.shortcuts import render
from .models import Novela

def inicio(request):
    # Esto busca TODAS las novelas que guardaste en la base de datos
    novelas = Novela.objects.all()
    # Y las envía a un archivo HTML que crearemos después
    return render(request, 'inicio.html', {'novelas': novelas})


# Create your views here.
