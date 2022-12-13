from django.shortcuts import render
from ejemplo.models import Mascotas


# Create your views here.

def mostrar_mascotas(request):
  lista_mascotas = Mascotas.objects.all()
  return render(request, "ejemplo/Mascotas.html", {"lista_mascotas": lista_mascotas})