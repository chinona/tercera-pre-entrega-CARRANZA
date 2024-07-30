from django.contrib import admin

from.models import Curso, Estudiante, Profesor, Entregable

class CursoAdmin (admin.ModelAdmin):
    list_display= ("nombre", "comision")
    list_per_page= 1
    ordering= ("nombre",)

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)