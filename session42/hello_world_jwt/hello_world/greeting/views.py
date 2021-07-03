from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

# Create your views here.
class HelloView(APIView):

    def get(self,request):
        print(request.user)
        return HttpResponse('Welcome!')

def hello_world(request):
    print(request.user)
    return HttpResponse('Welcome!')