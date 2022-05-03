from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Saul Ambrosio'
    })


def sobre(request):
    return HttpResponse("Página sobre")


def contato(request):
    return HttpResponse("Página contato")
