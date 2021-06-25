from django.db.models import query, query_utils
from rest_framework import serializers

class OptionSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=255)

class QuestionSerializer(serializers.Serializer):
    sentence = serializers.CharField(max_length=255)
    options = OptionSerializer(many=True)
    picture = serializers.ImageField()