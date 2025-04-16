import requests
from django.shortcuts import render

def todos_view(request):
    try:
        response = request.get('http://jsonplaceholder.typicode.com/todos/')
        if response.status_code == 200:
            lista_todos = response.json()

# Create your views here.
