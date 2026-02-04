from django.shortcuts import render, get_object_or_404
from .models import Novela

def inicio(request):
    novelas = Novela.objects.all()
    return render(request, 'inicio.html', {'novelas': novelas})

def detalle(request, id):
    # Esto busca una novela específica por su ID único
    novela = get_object_or_404(Novela, pk=id)
    return render(request, 'detalle.html', {'novela': novela})
# Create your views here.
