from django.shortcuts import render
from ejemplo.models import Mascotas
from ejemplo.forms import Buscar, MascotasForm
from django.views import View
from django.shortcuts import render

# Create your views here.

def mostrar_mascotas(request):
  lista_mascotas = Mascotas.objects.all()
  return render(request, "ejemplo/Mascotas.html", {"lista_mascotas": lista_mascotas})


class Buscar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid(): 
            nombre = form.cleaned_data.get("nombre") 
            lista_mascotas = Mascotas.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})


class AltaMascotas(View):

    form_class = MascotasForm
    template_name = 'ejemplo/alta_mascotas.html'
    initial = {"nombre":"", "tipo": "", "direccion":"", "numero_registro":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})