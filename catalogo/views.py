from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
<<<<<<< HEAD
from django.urls import reverse  # IMPORTANTE: Necesario para generar los links
from .models import Novela

def inicio(request):
    novelas_lista = Novela.objects.all().order_by('-id')

=======
from .models import Novela

def inicio(request):
    # 1. Traemos todas las novelas (ordenadas por ID)
    novelas_lista = Novela.objects.all().order_by('-id')

    # 2. Lógica del Buscador
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
    busqueda = request.GET.get('q')
    if busqueda:
        novelas_lista = novelas_lista.filter(
            Q(titulo__icontains=busqueda) | 
            Q(genero__icontains=busqueda)
        )

<<<<<<< HEAD
=======
    # 3. Filtros por Tipo
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
    tipo_filtrado = request.GET.get('tipo')
    if tipo_filtrado:
        novelas_lista = novelas_lista.filter(tipo=tipo_filtrado)

<<<<<<< HEAD
=======
    # 4. Paginación (8 por página)
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
    paginator = Paginator(novelas_lista, 8) 
    page_number = request.GET.get('page')
    novelas_paginadas = paginator.get_page(page_number)

    return render(request, 'inicio.html', {'novelas': novelas_paginadas})

def detalle(request, id):
    novela = get_object_or_404(Novela, pk=id)
    
<<<<<<< HEAD
    # Contador de visitas
    novela.vistas += 1
    novela.save() 
    
    # Novelas relacionadas
=======
    # --- NUEVO: CONTADOR DE VISITAS ---
    novela.vistas += 1
    novela.save() # Guardamos el nuevo número en la base de datos
    
    # --- NUEVO: NOVELAS RELACIONADAS ---
    # Busca novelas del mismo tipo, excluye la que estamos viendo, y toma 3 al azar
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
    relacionadas = Novela.objects.filter(tipo=novela.tipo).exclude(id=id).order_by('?')[:3]
    
    return render(request, 'detalle.html', {
        'novela': novela,
        'relacionadas': relacionadas
    })

def buscar_novelas(request):
    query = request.GET.get('q', '')
    resultados = []
    
    if query:
<<<<<<< HEAD
        # Buscamos las novelas que coincidan con el texto
=======
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
        novelas = Novela.objects.filter(
            Q(titulo__icontains=query) | 
            Q(genero__icontains=query)
        )[:5]
        
        for n in novelas:
<<<<<<< HEAD
            # CORRECCIÓN: Generamos la URL usando el name='detalle' definido en urls.py
            # Esto evita el error 404 al hacer clic en la sugerencia
            url_detalle = reverse('detalle', kwargs={'id': n.id})
            
=======
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
            resultados.append({
                'id': n.id,
                'titulo': n.titulo,
                'imagen': n.imagen.url if n.imagen else '',
<<<<<<< HEAD
                'tipo': n.get_tipo_display() if hasattr(n, 'get_tipo_display') else n.tipo,
                'url': url_detalle  # Enviamos la URL correcta al JavaScript
=======
                'tipo': n.tipo
>>>>>>> f51a23c8f863c29fc6b809e44dbbd6ed5cc9e10c
            })
    
    return JsonResponse({'resultados': resultados})