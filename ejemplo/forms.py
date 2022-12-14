from django import forms 
from ejemplo.models import Mascotas


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100, 
                            widget = forms.TextInput(attrs={'placeholder':'busque algo...'} ) )

##creamos el formulario

class MascotasForm(forms.ModelForm):
  class Meta:
    model = Mascotas
    fields = ['nombre', 'tipo', 'direccion', 'numero_registro']