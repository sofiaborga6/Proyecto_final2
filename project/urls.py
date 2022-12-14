"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ejemplo.views import mostrar_mascotas, Buscar, BuscarMascotas, AltaMascotas, BorrarMascota

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascotas/', mostrar_mascotas),
    path('buscar/', Buscar),
    path('mascotas/buscar/', BuscarMascotas.as_view()),
    path('mascotas/alta', AltaMascotas.as_view()),
    path('mascotas/borrar/<int:pk>', BorrarMascota.as_view()),
 
]
