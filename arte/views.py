from django.http.response import HttpResponse
from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
from arte.formulario import FormularioArte
from .models import Arte

# Create your views here.
# def inicio(request):
#     return HttpResponse("<a href='arte/add'>Agregar</a>")
#     return render(request,"arte.html")

def agregar(request):
    f = FormularioArte()
    if request.method == "POST":
        f = FormularioArte(request.POST)
        if f.is_valid():
            f.save()
            return redirect("/arte")

    return render(request,"arte.html",{"form":f})

class ListaActividades(generic.ListView):
    model = Arte
    context_object_name = "actividadesarte"
    template_name = "arte.html"