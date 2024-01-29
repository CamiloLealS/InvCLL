from django.shortcuts import render, redirect
from django.views.generic import ListView
from equipos.models import equipo
from equipos.forms import equipoForm
from .serializers import json_serial
import json

# Create your views here.

class Home(ListView):
    model = equipo
    template_name = 'inventario/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(equipo.objects.values()), default=json_serial)
        return context

    

def deleteEquipo(request, id_equipo):
    try:
        eq = equipo.objects.get(pk = id_equipo)
    except eq.DoesNotExist:
        return redirect(to='index')
    
    eq.delete()

    return redirect(to='index')

#def updateEquipo(request, id_equipo):
    