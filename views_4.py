from django.http import HttpResponse
from django.shortcuts import render

def paginaweb(request):
    return render(request, "index.html")

def macargafron(request):
    return render(request, "cargadorafron.html")

def mavolqueta(request):
    return render(request, "volqueta.html")

def maexcavado(request):
    return render(request, "excavadora.html")

def mamotonive(request):
    return render(request, "motoniveladora.html")

def marodillo(request):
    return render(request, "rodillocompac.html")
