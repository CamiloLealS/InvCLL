"""
URL configuration for InvCLL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from usuario.views import loginUsuario, logoutUsuario
from django.contrib.auth.decorators import login_required
from inventario.views import Home, deleteEquipo,delAll, editAll
from equipos.views import importarExcel, formEq, editEq, verEquipo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventario/',include(('inventario.urls','inventario'))),
    path('equipos/',include(('equipos.urls','equipos'))),
    path('',login_required(Home.as_view()), name='index'),
    path('equipos/imp/',importarExcel, name='import'),
    path('del/<int:id_equipo>',deleteEquipo,name='delete'),
    path('dellAll/',delAll, name = 'delAll'),
    path('editAll/',editAll,name = 'editAll'),
    path('equipos/edit/<int:id_equipo>',editEq,name = 'update'),
    path('equipos/reg/',formEq.as_view(),name='regEq'),
    path('equipos/ver/<int:id_equipo>',verEquipo, name = 'ver'),
    path('accounts/login/',loginUsuario.as_view(),name = "login"),
    path('logout/',login_required(logoutUsuario), name= 'logout')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)