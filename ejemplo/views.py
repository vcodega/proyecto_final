from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar 
from django.views import View 
def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Valentin"})

def index_tres(request):
    return render(request, "ejemplo/saludar.html", 
    {"notas": [1,2,3,4,5,6]}
    )

def monstrar_familiares(request): 
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html",
                {"lista_familiares": lista_familiares}) #diccionario =
                                                        # contexto

class BuscarFamiliar(View):  #class-base views 

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid(): #chequea las condiciones y reglas
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})