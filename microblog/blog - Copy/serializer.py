from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    content = serializers.CharField()