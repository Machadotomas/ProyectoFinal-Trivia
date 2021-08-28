from django.contrib import admin
from django.db import models
from .models import cuestionario, ElegirRespuesta, respondidas
from .forms import elegirInlineFormset

# Register your models here.

class respuestaInline(admin. TabularInline):
    model = ElegirRespuesta
    can_delete = False
    max_num = ElegirRespuesta.RESPUESTAS_MAXIMAS
    min_num = ElegirRespuesta.RESPUESTAS_MAXIMAS
    formset = elegirInlineFormset

class preguntaAdmin(admin.ModelAdmin):
    model = cuestionario
    inlines = (respuestaInline, )
    list_display = ["texto", ]
    search_fields = ["texto", "preguntas__texto"]


class respondidasAdmin(admin.ModelAdmin):
    list_display = ["pregunta", "respuesta", "correcta", "puntaje"]

    class meta_:
        models = respondidas

admin.site.register(respondidas)
admin.site.register(cuestionario, preguntaAdmin)
admin.site.register(ElegirRespuesta)