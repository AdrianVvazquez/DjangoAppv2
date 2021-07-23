from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render
from registro.formulario import FormularioPersona
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from django.views import generic
from .models import Persona

# Create your views here.
def registro (request):
    formulario = FormularioPersona()
    if request.method == "POST":
        # Crear variable del formulario con lo que haya recibido del método POST
        formulario = FormularioPersona(request.POST)
        if formulario.is_valid():
            formulario.save()
            # Datos para mandar correo
            nombre = request.POST["nombre"]
            apellidos = request.POST["apellidos"]
            correo = request.POST["correo"]
            # enviarCorreo(correo)
            correoBienvenida(nombre,apellidos,correo)
            return redirect("/")

    return render(request,"registro.html",{"form":formulario})

def enviarCorreo(correo):
    enviar = EmailMessage("Bienvenida","Saludos, Gracias por suscribirte ",to=[correo])
    enviar.send()
    return redirect("/")

def correoBienvenida(nombre,apellidos,correo):
    diccionario = {"nombre":nombre,"apellidos":apellidos}
    plantilla = get_template("bienvenida.html")
    body = plantilla.render(diccionario)
    enviar = EmailMultiAlternatives(
            "Prueba 2" # subject
            ,"Mensaje de prueba" # body
            ,"josea.vazquez@edu.uag.mx" # sender
            ,[correo] # receiver
            ,["jrendon@edu.uag.mx"] # cc
        )
    enviar.attach_alternative(body,"text/html")
    enviar.send()
    return HttpResponse("Hola")
    
class ListaRegistro(generic.ListView):
    model = Persona
    context_object_name = "registros" # este nombre se usa en el for de registro.htmls
    template_name = "registro.html"