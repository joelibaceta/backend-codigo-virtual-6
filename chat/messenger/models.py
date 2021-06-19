from django.db import models
from messenger.lib.db import db

# Create your models here.

class ChatMessage():

    def create(self, data):
        db.collection("messages").document("03").create(data)

    def all(self):
        messages_list = []
        chatref = db.collection("messages")
        queryref = chatref.where("emitter", "==", "Jhon")
        messages = queryref.stream()
        for message in messages:
            messages_list.append(message.to_dict())

        return messages_list
