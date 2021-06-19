import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("chat-codigo6-firebase-adminsdk-ltbs8-92574d5099.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
