from django.http import HttpResponse
from django.shortcuts import render
# Para poder acceder al método para el envío de un correo
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def inicio(request):
    return render(request,"inicio.html")

def enviarCorreo(request):
    # correo = EmailMessage("Bienvenida","Saludos, Gracias por suscribirte ",to=["josea.vazquez@edu.uag.mx"])
    n = "Adrian"
    diccionario = {"x":"y","nombre":n}
    plantilla = get_template("correo.html")
    body = plantilla.render(diccionario)
    correo = EmailMultiAlternatives(
            "Prueba 2" # subject
            ,"Mensaje de prueba" # body
            ,"josea.vazquez@edu.uag.mx" # sender
            ,["josea.vazquez@edu.uag.mx"] # receiver
            ,["mavelar2001@gmail.com"] # cc
        )
    correo.attach_alternative(body,"text/html")
    correo.send()
    return HttpResponse("Hola")

def ingresar(request):
    f = AuthenticationForm()
    if request.method == "POST":
        f = AuthenticationForm(data = request.POST)
        if f.is_valid():
            u = request.POST["username"]
            p = request.POST["password"]
            usr = authenticate(username = u, password = p)
            if usr is not None:
                login(request, usr)
                # llave de usuario
                request.session["variableSesion"] = u
    return render(request,"login.html",{"formulario":f})

def registroUsuario(request):
    f = UserCreationForm()
    if request.method == "POST":
        f = UserCreationForm(data = request.POST)
        if f.is_valid():
            usr = f.save()

    # para eliminar las recomendaciones de inicio de sesión
    f.fields["username"].help_text = None
    f.fields["password1"].help_text = None
    f.fields["password2"].help_text = None
    return render(request,"agregaUsuario.html",{"formulario":f})

def salir(request):
    logout(request)
    # Se abre una sesión por navegador en la base de datos
    return HttpResponse("Saliendo ...")