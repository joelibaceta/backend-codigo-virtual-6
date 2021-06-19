import rest_framework
from blog.serializer import PostSerializer
import io, json, time
from blog.models import Post
from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.views.decorators.cache import cache_page
from ratelimit.decorators import ratelimit


def login(request):
    if request.method == "GET":
        return render(request, "login.html", {"flag": False})
    else:
        data = request.POST

        try:
            user = User.objects.get(username=data["user"])
            if user.check_password(data["password"]):
                return HttpResponse("ok")
            else:
                return render(request, "login.html", {"flag": True})
        except:
            return render(request, "login.html", {"flag": True})

            
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

@cache_page(1000)
def slow_api(request):
    time.sleep(4)
    return HttpResponse(str(datetime.now()))

#@ratelimit(key='ip', rate="10/h")
def whatimeisit(request):
    return HttpResponse(str(datetime.now()))

def whoiam(request):
    return HttpResponse(str(request.headers['User-Agent']))

def hello_world(request):

    posts = Post.objects.all()
    data = serializers.serialize("json", posts)

    items = serializers.deserialize("json", data)

    for item in items:
        print(item.__dict__)
 
    return HttpResponse("OK")
