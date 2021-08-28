from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

user = settings.AUTH_USER_MODEL

# Create your models here.

#class Preguntas(models.Model):
   
    #pregunta=models.CharField(max_length=100)
    #respuestaCorrecta=models.CharField(max_length=40)
    #respuestaIncorrecta1=models.CharField(max_length=40)
    #respuestaIncorrecta2=models.CharField(max_length=40)

class cuestionario(models. Model):
    
    respuestas_correctas_permitidas = 1

    texto = models.TextField(verbose_name="ingresa la pregunta")

    def __str__(self):
        return self.texto


class ElegirRespuesta(models.Model):
    RESPUESTAS_MAXIMAS = 4
   
    pregunta = models.ForeignKey(cuestionario, related_name="preguntas", on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name="esta es la correcta?", default=False, null=False)
    texto = models.TextField(verbose_name="ingrese las respuestas aqui")

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name="puntaje total",default=0, decimal_places=2, max_digits=10)

class respondidas (models.Model):
    usuario = models.ForeignKey(Usuario , on_delete=models.CASCADE)
    pregunta = models.ForeignKey(cuestionario, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, related_name="intentos")
    correcta = models.BooleanField(verbose_name="es esta la respuesta correcta?", default=False, null=False)
    puntaje = models.DecimalField(verbose_name="puntaje obtenido", default=0, decimal_places=2 ,max_digits=6 )
