
from django.urls import path # type: ignore
from forms_app.views import contatti

app_name="forms_app"
urlpatterns=[
    path('contatti/', contatti, name='contatti'),
]