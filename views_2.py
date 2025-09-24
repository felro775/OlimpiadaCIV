import subprocess
from django.http import HttpResponse
from django.shortcuts import render
from .suma import sumare

def paginaweb(request):
    resultado = None

    if request.method == "POST":
        try:
            a = float(request.POST.get("a"))
            b = float(request.POST.get("b"))
            resultado = sumare(a, b)
            subprocess.run(["sudo python3 demo/nomo1.py %d" %(a)], shell=True)
        except (TypeError, ValueError):
            resultado = "Error: ingresa números válidos."

    return render(request, "index.html", {"resultado": resultado})

