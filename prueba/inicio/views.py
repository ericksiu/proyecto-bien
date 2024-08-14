from django.shortcuts import render, HttpResponse
menu="""
<a href="{%url 'Principal'%}">Home</a>
<a href="{%url 'Formulario'%}">Cursos</a>
<a href="{%url 'Contacto'%}">Contactanos</a>
"""
# Create your views here.
def principal(request):
    return render(request, "inicio/principal.html")
def contacto(request):
    return render(request, "inicio/contacto.html")
def formulario(request):
    return render(request, "inicio/formulario.html")
def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, "inicio/seguridad.html",
                  {'nombre':nombre})
def comentarios(request):
    return render(request, "inicio/comentarios.html")