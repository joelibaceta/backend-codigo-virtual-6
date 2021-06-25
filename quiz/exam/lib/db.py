from pymongo import MongoClient

def connect():
    client = MongoClient("mongodb+srv://root:root@cluster0.zx1wu.mongodb.net/exam?retryWrites=true&w=majority")

    db_handle = client['exam']

    return db_handle, client