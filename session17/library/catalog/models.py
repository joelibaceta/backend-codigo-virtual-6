from django.db import models
from django.db.models.base import Model

class Book(models.Model):

    title       = models.CharField(max_length=45)
    autor       = models.CharField(max_length=45)
    year        = models.IntegerField()
    editorial   = models.CharField(max_length=25)
    volume      = models.IntegerField()

    def __str__(self):
        return self.title