from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormContatto

def contatti(request):
    if request.method == "POST":

        form=FormContatto(request.POST)

        if form.is_valid():
            print("il Form è valido!")
            print("NOME: ", form.cleaned_data["nome"])
            print("COGNOME: ", form.cleaned_data["cognome"])
            print("EMAIL: ", form.cleaned_data["email"])
            print("CONTENUTO: ", form.cleaned_data["contenuto"])

            return HttpResponse("<h1>Grazie per averci contatto</h1>")
    else:
        form = FormContatto()

    context = {"form" : form}

    return render(request, "contatti.html",context)

    