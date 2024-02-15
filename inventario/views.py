from django.shortcuts import render, redirect
from django.views.generic import ListView
from equipos.models import equipo
from equipos.forms import equipoForm
from .serializers import json_serial
import json
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime, timedelta

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


def delAll(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')

        for i in ids:
            eq = equipo.objects.get(pk = i)
            eq.delete()
        
        return HttpResponse('OK')
    return redirect(to='index')

def editAll(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids[]')

        for i in ids:
            eq = equipo.objects.get(pk = i)
            hoy = datetime.now()
            hoy = hoy.date()
            hoy_str = hoy.strftime('%d/%m/%Y')
            eq.mantencion = hoy_str
            eq.required = False
            eq.save()
        return HttpResponse('OK')
    return redirect(to='index')

def reqMant(request):
    for i in equipo.objects.all():
        if i.mantencion != '-':
            hoy = datetime.now()
            mant = datetime.strptime(i.mantencion, '%d/%m/%Y')
            dif = hoy - mant
            meses_dif = dif.days // 30
            if meses_dif >= 8:
                i.required = True
                i.save()
    return redirect(to='index')
