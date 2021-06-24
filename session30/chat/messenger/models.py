from django.db import models
from messenger.lib.db import db
from datetime import datetime

# Create your models here.

class ChatMessage():

    def create(self, data):
        timestamp = str(datetime.timestamp(datetime.now()))
        db.collection("messages").document(timestamp).create(data)

    def all(self):

        messages_list = []
        chatref = db.collection("messages")
        queryref = chatref.where("emitter", "==", "Jhon")
        messages = queryref.stream()
        for message in messages:
            messages_list.append(message.to_dict())

        return messages_list
