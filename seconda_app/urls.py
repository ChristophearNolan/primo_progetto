from os import path
from django.urls import path # type: ignore
from seconda_app.views import es_if,index2,if_else_elif


app_name="seconda app"
urlpatterns=[
    path('es_if',es_if,name='es_if'),
    path('if_else_elif',if_else_elif,name='if_else_elif'),
    path('index2',index2,name="index2"),
    
]

