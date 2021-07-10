from rest_framework_simplejwt.exceptions import AuthenticationFailed
from core.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response

from core.users.serializers import CustomObtainPairSerializer

# Create your views here.

class LoginAPI(APIView):
    def post(self, request):
        login_data = request.data
        email = login_data["correo"]
        user = User.objects.filter(email__exact=email).first()
        password = login_data.get("password")
        user_authenticated = authenticate(username=user.username, password=password)
        if user_authenticated != None:
            
            #refresh_token = RefreshToken.for_user(user_authenticated)
            #token = refresh_token.access_token
            token = CustomObtainPairSerializer.get_token(user_authenticated)

            return Response({
                'ok': True,
                'token': str(token)
            })
            

        
        return HttpResponse("ok")