from appcoder.models import Curso
from appcoder.forms import CursoFormulario

from django.shortcuts import render

from django.http import HttpResponse

from.models import Curso 

# Create your views here.
def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):

    cursos= Curso.objects.all()

    return render(request, "appcoder/cursos.html", {"curso":cursos})

def estudiantes (request):
    return HttpResponse("vista de estudiantes")

def profesores(request):
    return HttpResponse("vista de profesores")

def entregables(request):
    return HttpResponse("vista entregables")



def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "appcoder/index.html")

    return render(request,"appcoder/curso_formulario.html")



def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "appcoder/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "appcoder/form_con_api.html", {"mi_formulario": mi_formulario})