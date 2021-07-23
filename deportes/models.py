from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250,null=True)