from os import path
from django.urls import path
from news.views import  visualizza,index3, articoloDetailView,ListaArticoli,queryBase,giornalistaDetailView



app_name = 'news'

urlpatterns = [
    
    path('index3',index3,name="index3"),
    path('visualizza', visualizza, name= "visualizza"),
    path('articoli', articoloDetailView, name="art"),
    path('giornalisti/<int:pk>',giornalistaDetailView, name="giornalista_detail"),
    path('articoli/<int:pk>', articoloDetailView, name="articoli"),
   # path('lista_articoli',ListaArticoli,name="lista_articoli"),
    #path('lista_articoli/<int:pk>',ListaArticoli,name="lista_articoli"),
    path('query',queryBase,name="query"),


]