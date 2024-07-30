
from django.contrib import admin
from django.urls import path, include

from appcoder.views import inicio, estudiantes, profesores, entregables, cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include ("appcoder.urls"))
]
