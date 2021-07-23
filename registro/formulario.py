from django import forms
from registro.models import Persona

class FormularioPersona(forms.ModelForm):
    class Meta:
        model= Persona
        fields= ["nombre","apellidos","sexo","correo"]
# fields son las variables-atributos de la clase persona