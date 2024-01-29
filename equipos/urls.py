from django.urls import path
from .views import importarExcel, formEq, editEq


urlpatterns = [
    path('equipos/imp', importarExcel , name='import'),
    path('equipos/form',formEq.as_view(),name='regEq'),
    path('equipos/edit/<int:id_equipo>',editEq, name='update')
]
