#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from news.models import Articolo, Giornalista
#from datetime import datetime
import datetime
  

def visualizza(request):
    articoli= Articolo.objects.all()
    giornalisti= Giornalista.objects.all()
    context= {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "visualizza.html", context)

def articoloDetailView(request, pk=None):
    #articolo= Articolo.objects.get(pk=pk)
    articoli = get_object_or_404(Articolo, pk=pk)
    context= {"articoli": articoli}
    return render(request, "art.html",context)

def giornalistaDetailView(request, pk=None):
    giornalista= get_object_or_404(Giornalista,pk=pk)
    context= {"giornalista":giornalista}
    return render(request, "giornalista_detail.html",context)

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
     articoli_cognome =Articolo.objects.filter(giornalista__cognome='Bianchi') 
     #2. totale
     numero_totale_articoli =Articolo.objects.count()

     #3. contare il numero di articoli scritti da un giornalista specifico
     giornalista_1= Giornalista.objects.get(id=3)
     numero_articoli_giornalista_1= Articolo.objects.filter(giornalista=giornalista_1).count()

     #4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente
     articoli_ordinati= Articolo.objects.order_by('-visualizzazione')

    #5. tutti gli articoli che non hanno visualizzazioni
     articoli_senza_visualizzazioni= Articolo.objects.filter(visualizzazione=0)
     
     #6. articolo più visualizzato
     articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazione').first()

     #7. tutti i giornalisti nati dopo una certa data
     giornalisti_data= Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990,1,1))

     #8. tutti gli articoli pubblicati in una data specifica
     articolo_del_giorno = Articolo.objects.filter(data=datetime.date(2023,1,1))

     #9. tutti gli articoli pubblicati in un intervallo di date
     articoli_periodo= Articolo.objects.filter(data__range=(datetime.date(2023,1,1),datetime.date(2023,12,31)))

     #10. gli articoli scritti da giornalisti nati prima del 1980
     giornalista_nati= Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980,1,1))
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
     articoli_parola= Articolo.objects.filter(titolo__icontains='importante')
     #crea dizionario context

     #16 Articoli pubblicati in un certo mese di un anno specifico
     #nota per poter modificare la data di un articolo togliere la proprietà auto_now=True al field data nel model
     #poi dare i comandi makemigrations e migrate per applicare le modifiche al database
     articoli_mese_anno= Articolo.objects.filter(data__month=1, data__year=2023)

     #17 Giornalista con almeno un articolo con più di 100 visualizzazioni
     giornalisti_con_articoli_particolari= Giornalista.objects.filter(articoli__visualizzazione__gte=100).distinct()

     #UTILIZZO DI PIU' CONDIZIONI DI SELEZIONE
     data=datetime.date(1990,1,1)
     visualizzazioni=50
     #per mettere in AND le condizioni separarle con la virgola
     #18 ...scrivi quali artic.oli vengono selezionati
     articoli_con_and= Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazione__gte=visualizzazioni)

     #per mettere in OR le condizioni utilizzare l'eporatore Q
     from django.db.models import Q
     #19 ...scrivi quali articoli vengono selezionati
     articoli_con_or=Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data) | Q(visualizzazione__lte=visualizzazioni))

     # per il NOT (~) uitilizzare l'operatore Q
     #20 ...scrivi quali articoli vengono selezionati
     articoli_con_not= Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=data))
     #oppure il metodo exclude
     # ... spiegala
     articoli_con_not=Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)
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
         'articoli_mese_anno': articoli_mese_anno,
         'giornalisti_con_articoli_particolari':giornalisti_con_articoli_particolari,
         'articoli_con_and':articoli_con_and,
         'articoli_con_or':articoli_con_or,
         'articoli_con_not':articoli_con_not,









          

     }
     return render(request, 'query.html',context)


