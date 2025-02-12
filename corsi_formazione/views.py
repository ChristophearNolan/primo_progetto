from django.shortcuts import render,get_object_or_404
import datetime
from corsi_formazione.models import corso

def index4(request):
    return render(request,"index4.html")
# Create your views here.


def view_a(request):
    elenco_corsi=corso.objects.filter(data_inizio__gt=datetime.date(1000,1,1))

    context={
        'elenco_corsi':elenco_corsi,
    }
    return render(request, "view_a.html",context)

def view_b(request, pk=None):
    #articolo= Articolo.objects.get(pk=pk)
    corsi = get_object_or_404(corso, pk=pk)
    context= {"corsi": corsi}
    return render(request, "view_b.html",context)



def view_c(request):
    elenco_data_dopo= corso.objects.filter(data_inizio__gt=datetime.date(2025,5,1))

    context={
        'elenco_data_dopo':elenco_data_dopo,
    }
    return render(request,"view_c.html",context) 


def view_d(request):
    corsi_posti=corso.objects.filter(posti_disponibili__lt=20)
    context={
        'corsi_posti':corsi_posti,
    }
    return render(request, "view_d.html",context)

def view_e(request):
    corsi_termine=corso.objects.filter(data_inizio__range=(datetime.date(2025,1,1),datetime.date(2025,4,30)))

    context={
        'corsi_termine':corsi_termine,
    }
    return render(request, "view_e.html",context)
