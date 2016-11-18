from django.db import models
from django.utils import timezone
from django.contrib import admin

class Libro(models.Model):
    ISBN = models.IntegerField()
    title = models.CharField(max_length=25)
    "portada = models.FileField()"
    author = models.CharField(max_length=30)
    editorial = models.CharField(max_length=25)
    pais = models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return self.title
