#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from news.models import Articolo, Giornalista
  

def home(request):
    articoli= Articolo.objects.all()
    giornalisti= Giornalista.objects.all()
    context= {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homep.html", context)

def articoloDetailView(request, pk):
    #articolo= Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context= {"articolo": articolo}
    return render(request, "art.html",context)


def index3(request):
    return render(request,"index3.html")