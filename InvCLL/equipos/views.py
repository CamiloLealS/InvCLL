from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import equipoForm
from .models import equipo
from django.http import HttpResponse
from django.contrib import messages
import pandas as pd
from tablib import Dataset
from .resources import EquipoResource

# Create your views here.

def importarExcel(request):
    if request.method == 'POST':
        equipo_resource = EquipoResource
        data = Dataset()

        new_equipo = request.FILES['excel_uploaded']

        if not '.xls' in new_equipo.name:
            messages.info(request, 'Por favor utilizar un archivo excel ".xls".')
            return render(request, 'inventario/index.html')
        else:
            messages.info(request, 'Archivo subido correctamente.')

        dataset = pd.read_excel(new_equipo, header=None)

        for row in range(len(dataset)):
            ubi_eq = dataset.iloc[row,0].upper()
            tipo_eq = dataset.iloc[row, 1].upper()
            ip_equipo = dataset.iloc[row,2]
            mac_eq = dataset.iloc[row, 3]
            mantencion_eq = (dataset.iloc[row, 4])
            if ip_equipo in equipo.objects.values_list('ip', flat=True).distinct():
                equipo.objects.filter(ip = ip_equipo).update(ubicacion = ubi_eq)
                equipo.objects.filter(ip = ip_equipo).update(mantencion = mantencion_eq)
                equipo.objects.filter(ip = ip_equipo).update(estadoMant = 'PENDIENTE')
            else:
                created = equipo.objects.update_or_create(
                    ubicacion = ubi_eq,
                    tipo = tipo_eq,
                    ip = ip_equipo,
                    mac = mac_eq,
                    mantencion = mantencion_eq
                    )

        return redirect( to='index')
    return render(request, 'equipos/import.html')

        
class formEq(CreateView):
    model = equipo
    form_class = equipoForm
    template_name = 'equipos/registroEquipo.html'
    success_url = reverse_lazy('index')