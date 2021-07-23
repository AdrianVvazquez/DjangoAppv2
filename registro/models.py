from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2, choices=[("H","Hombre"),("M","Mujer")])
    correo = models.CharField(max_length=100)