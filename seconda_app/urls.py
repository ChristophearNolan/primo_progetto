from os import path
from django.urls import path # type: ignore
from seconda_app.views import es_if

app_name="seconda app"
urlpatterns=[
    path('es_if',es_if,name='homepage'),
    
]