from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from .formulario import FormularioDeporte
from .models import Deporte

# Create your views here.
def guardar(request):
    deporte = FormularioDeporte()
    if request.method == "POST":
        deporte = FormularioDeporte(request.POST)
        if deporte.is_valid():
            deporte.save()
            return redirect("/deportes")

    return render(request,"deportes.html",{"form":deporte})

class ListaDeportes(generic.ListView):
    model = Deporte
    context_object_name = "deportes"
    template_name = "deportes.html"