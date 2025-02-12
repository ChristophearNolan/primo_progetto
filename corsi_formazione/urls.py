from os import path
from django.urls import path
from corsi_formazione.views import index4,view_a,view_c,view_d,view_e,view_b



app_name = 'corsi_formazione'

urlpatterns = [
    path('index4',index4,name="index4"),
    path('view_a',view_a,name="view_a"),
    path('view_b',view_b,name="view_b"),
    path('view_c',view_c,name="view_c"),
    path('view_d',view_d,name="view_d"),
    path('view_e',view_e,name="view_e"),

]