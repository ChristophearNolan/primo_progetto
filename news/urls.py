from os import path
from django.urls import path
from news.views import home, index3, articoloDetailView



app_name = 'news'

urlpatterns = [
    path('index3',index3,name="index3"),
    path('', home, name= "homep"),
    path("articoli/<int:pk>", articoloDetailView, name="art"),

]