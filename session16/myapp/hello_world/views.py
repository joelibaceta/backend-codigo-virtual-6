from hello_world.models import Gretting
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):

    # Creando un saludo
    greeting = Gretting()
    greeting.heading = "hello world"
    greeting.save()

    # Obteniendo todos los saludos
    greetings = Gretting.objects.all

    return render(request, 'index.html', {"greetings": greetings})