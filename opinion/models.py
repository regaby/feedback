from django.db import models

# Create your models here.

class Opinion(models.Model):
    nombre = models.CharField(max_length=100)
    opinion = models.TextField()
    puntaje = models.IntegerField()

