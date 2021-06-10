from django.core import serializers
from django.core.serializers.base import Serializer
from rest_framework import viewsets
from blog.models import Post
from blog.serializer import PostSaveSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

import io

class PostViewset(viewsets.ViewSet):

    def retrieve(self, request, id):
        queryset = Post.objects.get(pk=id)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = PostSaveSerializer(data=data)
        
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