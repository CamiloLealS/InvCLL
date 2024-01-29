from django.urls import path
from .views import importarExcel, formEq


urlpatterns = [
    path('equipos/imp', importarExcel , name='import'),
    path('equipos/form',formEq.as_view(),name='regEq'),
]
