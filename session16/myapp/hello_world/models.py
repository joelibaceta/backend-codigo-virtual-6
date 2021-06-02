from django.db import models

# Create your models here.

class Gretting(models.Model):
    heading = models.CharField(max_length=30)
