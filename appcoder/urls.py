from django.urls import path
from appcoder import views

from appcoder.views import inicio, estudiantes, profesores, entregables, cursos

urlpatterns = [
    path("", inicio, name="inicio"),
    path("in", inicio),
    path("est", estudiantes),
    path("prof", profesores),
    path("entr", entregables),
    path("cur", cursos, name="cursos"),
    
]

clase_21= [
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    path('form-con-api/', views.form_con_api, name="FormConApi")
]

urlpatterns += clase_21