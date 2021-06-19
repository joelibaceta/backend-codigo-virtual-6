from django.shortcuts import render
from messenger.models import ChatMessage
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class MessageAPI(APIView):

    def post(self, request):
        data = request.data
        message = ChatMessage()
        message.create(data)
        return Response("ok")
    
    def get(self, request):
        print(request.META.get('REMOTE_ADDR'))
        message = ChatMessage()
        messages = message.all()
        return Response(messages)

    

