from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog.models import Movie
import json

class MovieSearch(APIView):

    def get(self, request):
        query=request.GET.dict()
        print(query)
        movies = Movie.search(query)
        return Response(movies)

# Create your views here.
class MovieList(APIView):

    def get(self, request):
        title = request.GET.get("title")
        if title != None:
            movies = Movie.get_by_title(title)
        else:
            movies = Movie.all()
        return Response(movies)

    
    def post(self, request):
        data = request.data
        movie = Movie()
        movie.insert(data)
        return Response(data)