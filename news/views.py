#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from news.models import Articolo, Giornalista
from datetime import datetime
  

def visualizza(request):
    articoli= Articolo.objects.all()
    giornalisti= Giornalista.objects.all()
    context= {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "visualizza.html", context)

def articoloDetailView(request, pk=None):
    #articolo= Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context= {"articolo": articolo}
    return render(request, "art.html",context)

def ListaArticoli(request, pk=None):
    if pk==None:
        articoli=Articolo.objects.all()
    else:
        articoli=Articolo.objects.filter(giornalista_id=pk)
    context={
        'articoli': articoli,    
        }
    return render(request, 'lista_articoli.html',context)


def index3(request):
    return render(request,"index3.html")


def queryBase(request):
    #1. Tutti gli articoli scritti da giornalisti di un certo cognome:
     articoli_cognome =Articolo.objects.filter(giornalista_cognome='Rossi') 
     #2. totale
     numero_totale_articoli =Articolo.objects.count()

     #3. contare il numero di articoli scritti da un giornalista specifico
     giornalista_1= Giornalista.objects.get(id=1)
     numero_articoli_giornalista_1= Articolo.objects.filter(giornalista=giornalista_1).count()

     #4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente
     articoli_ordinati= Articolo.objects.order_by('-visualizzazioni')

    #5. tutti gli articoli che non hanno visualizzazioni
     articoli_senza_visualizzazioni= Articolo.objects.filter(visualizzazioni=0)
     
     #6. articolo più visualizzato
     articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazione').first()

     #7. tutti i giornalisti nati dopo una certa data
     giornalisti_data= Giornalista.objects.filter(anno_di_nascita_gt=datetime.date(1990,1,1))

     #8. tutti gli articoli pubblicati in una data specifica
     articolo_del_giorno = Articolo.objects.filter(date=datetime.date(2023,1,1))

     #9. tutti gli articoli pubblicati in un intervallo di date
     articoli_periodo= Articolo.objects.filter(date__range=(datetime.date(2023,1,1),datetime.date(2023,12,31)))

     #10. gli articoli scritti da giornalisti nati prima del 1980
     giornalista_nati= Giornalista.objects.filter(anno_di_nascita__It=datetime.date(1980,1,1))
     articoli_giornalisti= Articolo.objects.filter(giornalista__in=giornalista_nati)

     #11. il giornalista piu giovane
     giornalista_giovane= Giornalista.objects.order_by('anno_di_nascita').first()

     #12. giornalista piu anziano
     giornalista_anziano = Giornalista.objects.order_by('-anno_di_nascita').first()

     #13.ultimi 5 articoli pubblicati
     ultimi= Articolo.objects.order_by('-data')[:5]

     #14. articoli con un certo minimo di visualizzazioni
     articolo_minime_visualizzazioni= Articolo.objects.filter(visualizzazione__gte=100)

     #15 articolii che contengono una certa parola nel titolo
     articoli_parola= Articolo.objects.filter(titolo_icontains='importante')
     #crea dizionario context

     context={
         'articolo_cognome': articoli_cognome,
         'numero_totale_articoli':numero_totale_articoli,
         'giornalista_1':giornalista_1,
         'numero_articoli_giornalista_1':numero_articoli_giornalista_1,
         'articoli_ordinati':articoli_ordinati,
         ' articoli_senza_visualizzazioni':articoli_senza_visualizzazioni,
         ' articolo_piu_visualizzato':articolo_piu_visualizzato,
         ' giornalisti_data':giornalisti_data,
         'articolo_del_giorno':articolo_del_giorno,
         ' articoli_periodo':articoli_periodo,
         'articoli_giornalisti':articoli_giornalisti,
         'giornalista_giovane':giornalista_giovane,
         'giornalista_anziano':giornalista_anziano,
         'ultimi':ultimi,
         'articolo_minime_visualizzazioni':articolo_minime_visualizzazioni,
         'articoli_parola':articoli_parola,









          

     }

