from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def doacoes(request):
    return render(request, 'doacoes.html')

def contato(request):
    return render(request, 'contato.html')

def transparencia(request):
    return render(request, 'transparencia.html')