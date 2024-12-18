from os import path
from django.urls import path # type: ignore
from prima_app.views import homepage, welcome, lista,chiSiamo,variabili,index

app_name="prima_app"
urlpatterns=[
    path('homepage',homepage,name='homepage'),
    path('homepage',homepage,name='homepage'),
     path('welcome',welcome,name='welcome'),
     path('lista',lista,name='lista'),
     path('chiSiamo',chiSiamo,name='chiSiamo'),
     path('variabili',variabili,name='variabili'),
     path('',index,name='index')
]