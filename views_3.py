from django.http import HttpResponse
from django.shortcuts import render

def paginamenu(request):
    return render(request, "menu.html")

def maexcavadora(request):
    return render(request, "excavadora.html")
