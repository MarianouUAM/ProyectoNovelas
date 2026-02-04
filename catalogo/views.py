from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Novela

def inicio(request):
    # 1. Traemos todas las novelas (ordenadas por ID)
    novelas_lista = Novela.objects.all().order_by('-id')

    # 2. Lógica del Buscador
    busqueda = request.GET.get('q')
    if busqueda:
        novelas_lista = novelas_lista.filter(
            Q(titulo__icontains=busqueda) | 
            Q(genero__icontains=busqueda)
        )

    # 3. Filtros por Tipo
    tipo_filtrado = request.GET.get('tipo')
    if tipo_filtrado:
        novelas_lista = novelas_lista.filter(tipo=tipo_filtrado)

    # 4. Paginación (8 por página)
    paginator = Paginator(novelas_lista, 8) 
    page_number = request.GET.get('page')
    novelas_paginadas = paginator.get_page(page_number)

    return render(request, 'inicio.html', {'novelas': novelas_paginadas})

def detalle(request, id):
    novela = get_object_or_404(Novela, pk=id)
    
    # --- NUEVO: CONTADOR DE VISITAS ---
    novela.vistas += 1
    novela.save() # Guardamos el nuevo número en la base de datos
    
    # --- NUEVO: NOVELAS RELACIONADAS ---
    # Busca novelas del mismo tipo, excluye la que estamos viendo, y toma 3 al azar
    relacionadas = Novela.objects.filter(tipo=novela.tipo).exclude(id=id).order_by('?')[:3]
    
    return render(request, 'detalle.html', {
        'novela': novela,
        'relacionadas': relacionadas
    })

def buscar_novelas(request):
    query = request.GET.get('q', '')
    resultados = []
    
    if query:
        novelas = Novela.objects.filter(
            Q(titulo__icontains=query) | 
            Q(genero__icontains=query)
        )[:5]
        
        for n in novelas:
            resultados.append({
                'id': n.id,
                'titulo': n.titulo,
                'imagen': n.imagen.url if n.imagen else '',
                'tipo': n.tipo
            })
    
    return JsonResponse({'resultados': resultados})