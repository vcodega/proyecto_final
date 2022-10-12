from django.shortcuts import render

def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Valentin"})

def index_tres(request):
    return render(request, "ejemplo/saludar.html", 
    {"notas": [1,2,3,4,5,6]}
    )