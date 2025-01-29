from os import path
from django.urls import path
from news.views import  visualizza,index3, articoloDetailView,ListaArticoli



app_name = 'news'

urlpatterns = [
    
    path('index3',index3,name="index3"),
    path('visualizza', visualizza, name= "visualizza"),
    path("articoli", articoloDetailView, name="art"),
    path("articoli/<int:pk>", articoloDetailView, name="art"),
    path('lista_articoli',ListaArticoli,name="lista_articoli"),
    path('lista_articoli/<int:pk>',ListaArticoli,name="lista_articoli"),

]