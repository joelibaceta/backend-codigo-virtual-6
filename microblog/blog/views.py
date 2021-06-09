import rest_framework
from blog.serializer import PostSerializer
import io
from blog.models import Post
from datetime import date
import json
from django.http.response import HttpResponse
from django.shortcuts import render

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer

@csrf_exempt
def create_post(request):
    json_data = "{\"content\": \"mi tweet\"}"
    #stream = io.StringIO(json_data)
    #item = JSONParser.parse(stream)
    item = json.loads(json_data)
    print(item["content"])
    return HttpResponse("OK")

def serialize_demo(request):
    post = Post.objects.first()
    serializer = PostSerializer(post)
 
    return serializer.data
  
def hello_world(request):

    posts = Post.objects.all()
    data = serializers.serialize("json", posts)

    print(data)
    
    items = serializers.deserialize("json", data)

    for item in items:
        print(item.__dict__)
 
    return HttpResponse("OK")
