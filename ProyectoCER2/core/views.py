from django.shortcuts import render
from django.shortcuts import render
from .models import Correspondencia

# Create your views here.

def home(request):
    filtro = request.POST.get("buscar")
    enco = Correspondencia.objects.all
    if filtro:
         enco = Correspondencia.objects.filter(id_residencia = filtro)
    
    return render(request, 'core/index.html', {'encomienda':enco})

