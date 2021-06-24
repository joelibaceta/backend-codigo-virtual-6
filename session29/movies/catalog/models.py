from django.db import models
from catalog.lib.db import connect

# Create your models here.
class Movie():

    def __init__(self):
        self.db_handle, self.db_client = connect()

    def insert(self, data):
        movie_collection = self.db_handle["movie_collection"]
        movie_collection.insert(data)

    def get_by_title(title):
        db_handle, db_client = connect()
        movie_collection = db_handle["movie_collection"]
        movies = list(movie_collection.find( { "title": title }, {"_id": 0} ))
        return movies

    def all():
        db_handle, db_client = connect()
        movie_collection = db_handle["movie_collection"]
        movies = list(movie_collection.find({}, {"_id": 0}))
        return movies

    def search(query):
        db_handle, db_client = connect()
        movie_collection = db_handle["movie_collection"]
        movies = list(movie_collection.find(query, {"_id": 0}))
        return movies

    
   