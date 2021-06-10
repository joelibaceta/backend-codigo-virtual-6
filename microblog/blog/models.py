from django.db import models

class HashTag(models.Model):
    """Hashtags de un Post"""

    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label

class Post(models.Model):
    """Post de MicroBloging"""
    
    #TODO: Corregir nombre de cambio
    content = models.CharField(max_length=50)
    hashtags = models.ManyToManyField(HashTag, null=True)

    def __str__(self):
        return self.content