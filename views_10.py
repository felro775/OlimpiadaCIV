import subprocess
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

def resultado(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        subprocess.run(["sudo python3 nomo/Nomo_CargadorFrontal.py %d" %(num1)], shell=True)
        suma = num1 + num2
        return render(request, "resultado.html", {"suma": suma})
    return render(request, "index.html")
