from django.core import serializers
from django.core.serializers.base import Serializer
from rest_framework import viewsets
from blog.models import Post
from blog.serializer import PostRegexSerializer, PostSaveSerializer, PostSerializer, PostUpdateSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import io
from  django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TokenViewSet(viewsets.ViewSet):

    def get_token(self, request):
        data = request.data
        #try:
        user = User.objects.get(username=data["user"])
        if user.check_password(data["password"]):
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

            return Response({
                "token": token.key
            })
        else:
            return Response({
                "status": "unauthorized 1"
            })
        # except:
        #     return Response({
        #         "status": "unauthorized 2"
        #     })

class PostViewset(viewsets.ViewSet):
    #authentication_classes = [BasicAuthentication,]
    #permission_classes = [IsAuthenticated,]

    def update(self, request, id):
        queryset = Post.objects.get(pk=id)
        data = request.data
        serializer = PostUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.update(queryset, serializer.validated_data)
            return Response({"status": "ok"})
        else:
            return(Response({
                "errors": serializer.errors
            }))

    def retrieve(self, request, id):
        queryset = Post.objects.get(pk=id)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

    def list(self, request):
        user = request.user
        #if user = AnonymousUser: 

        queryset = Post.objects.filter(owner=user)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = PostRegexSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            reponse = {
                "status": serializer.is_valid()
            }
            return Response(reponse)
        else:
            return(Response({
                "errors": serializer.errors
            }))

    """ def list(self, request):

        status = False
        posts = []

        queryset = Post.objects.all()

        for item in queryset:
            serialized = PostSerializer(item)
            posts.append(serialized.data)

        if queryset != None:
            status = True

        response = {
            "ok": status,
            "Content": posts
        }

        return Response(response) """

    """  def create(self, request):

        binary_payload = request.data
        #print(binary_payload)
        #stream = io.BytesIO(binary_payload)
        #data = JSONParser().parse(stream)
        
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data)
        else:
            return Response({"errors": serializer.errors}) """