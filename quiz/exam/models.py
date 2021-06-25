from exam.validators import validate_file_size
from django.db import models
from django.db.models.fields import CharField
from exam.lib.db import connect

# Create your models here.

class Question(models.Model):
    sentence = models.TextField()
    picture = models.ImageField(null=True, upload_to="questions")
    attachment = models.FileField(null=True, validators=[validate_file_size])

    def __str__(self):
        return self.sentence


class Option(models.Model):
    label = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    def __str__(self):
        return self.label

class Answer():

    def __init__(self):
        self.db_handle, self.db_client = connect()

    def create(self, data):
        answers_collection = self.db_handle["answers_collection"]
        answers_collection.insert(data)

    