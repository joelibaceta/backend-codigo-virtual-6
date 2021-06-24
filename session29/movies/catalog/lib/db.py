from pymongo import MongoClient

def connect():
    client = MongoClient(
        host= "127.0.0.1",
        port= 27017
    )

    db_handle = client['movie_catalog']
    return db_handle, client