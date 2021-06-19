from django.http.response import HttpResponse
from django.shortcuts import render
from messenger.models import ChatMessage
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def chat_view(request):
    return render(request, 'chat.html')

def send_message(request):
    data = request.data
    message = ChatMessage()
    message.create(data)
    return HttpResponse("OK")

class MessageAPI(APIView):

    def post(self, request):
        data = request.data
        print(data)
        message = ChatMessage()
        message.create(data)
        return Response("ok")
    
    def get(self, request):
        message = ChatMessage()
        messages = message.all()
        return Response(messages)

    

