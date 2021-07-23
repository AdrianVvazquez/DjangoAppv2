from django import forms
from deportes.models import Deporte

class FormularioDeporte(forms.ModelForm):
    class Meta:
        model= Deporte
        fields= ["nombre","descripcion"]
