from django.db import models

# Create your models here.

class Preguntas(models.Model):
   
    pregunta=models.CharField(max_length=100)
    respuestaCorrecta=models.CharField(max_length=40)
    respuestaIncorrecta1=models.CharField(max_length=40)
    respuestaIncorrecta2=models.CharField(max_length=40)



