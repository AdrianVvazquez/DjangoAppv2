"""ArteyCultura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib import auth
from django.urls import path
from django.conf.urls import url

from .views import inicio, enviarCorreo, ingresar, salir, registroUsuario
from registro.views import registro, ListaRegistro
from arte.views import agregar as addArte, ListaActividades
from deportes.views import guardar as addDeporte, ListaDeportes
# guardar
urlpatterns = [
    path('admin/', admin.site.urls),
    url("registro",ListaRegistro.as_view()),
    url("nuevo",registro),
    url(r"^$",inicio),
    # agrega a la url lo especificado
    # ^ que comienze con
    #   /url  -->  comienza/
    # $ que termine con
    #   /url  -->  url/termina
    url(r"arte$",ListaActividades.as_view()),
    url(r"deportes$",ListaDeportes.as_view()),
    url(r"^arte/add$",addArte),
    url(r"^deportes/add$",addDeporte),
    url(r"^correo$",enviarCorreo),
    url(r"^usuarios/agregar$",registroUsuario),
    url(r"^login",ingresar),
    url(r"^logout",salir),
]
