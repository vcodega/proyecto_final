from django.contrib import admin
from django.urls import path
from ejemplo.views import index, index_tres, monstrar_familiares, BuscarFamiliar
from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('saludar/', index),
    #path('mostrar-notas/',index_tres),
    path('mi-familia/', monstrar_familiares), 
    path('blog/',blog_index),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
]
