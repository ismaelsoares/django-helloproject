from django.urls import path
# aqui importaria todos os pacotes dentro de views
# from .views import *
# aqui importa pacotes específicos do arquivos views
from .views import homePageView, returnMyName
urlpatterns = [
    path("", homePageView, name="home"),
    path("myname/", returnMyName, name="myname"),
]
