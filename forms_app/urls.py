
from django.urls import path # type: ignore
from forms_app.views import contatti, lista_contatti

app_name="forms_app"
urlpatterns=[
    path('contatti/', contatti, name='contatti'),
    path('lista_contatti/', lista_contatti, name='lista_contatti'),
]