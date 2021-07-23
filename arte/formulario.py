from django import forms
from .models import Arte

class FormularioArte(forms.ModelForm):
    class Meta:
        model= Arte
        fields= ["nombre","descripcion"]
