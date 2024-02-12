from django.urls import path
from .views import Home, deleteEquipo, delAll,editAll

urlpatterns = [
    path('', Home.as_view(), name = 'index'),
    path('del/<int:id_equipo>', deleteEquipo, name='delete'),
    path('delAll/',delAll, name='delAll'),
    path('editAll/',editAll, name='editAll')
]
