from rest_framework import serializers
from blog.models import HashTag, Post

import re

class HashTagSerializer(serializers.Serializer):
    label = serializers.CharField()

class PostRegexSerializer(serializers.Serializer):
    content = serializers.CharField()

    def create(self, validated_data):
        content = validated_data["content"]
        hashtags = re.findall(r'(\#[\w]+)', content)

        post = Post()
        post.content = content
        post.save()

        for item in hashtags:
            hashtag = HashTag.objects.filter(label=item).last()
            if hashtag == None:
                hashtag = HashTag()
                hashtag.label=item
                hashtag.save()

            post.hashtags.add(hashtag)
        
        post.save() 

        return post

class PostSaveSerializer(serializers.Serializer):
    content = serializers.CharField()
    hashtags = serializers.ListField()

    def validate_content(self, value):
        if len(value) > 144:
            raise serializers.ValidationError("Max 144 Characters")
        return value


    def create(self, validated_data):

        post = Post()
        post.content = validated_data["content"]
        post.save()

        for item in validated_data["hashtags"]:
            hashtag = HashTag.objects.filter(label=item).last()
            if hashtag == None:
                hashtag = HashTag()
                hashtag.label=item
                hashtag.save()

            post.hashtags.add(hashtag)
        
        post.save() 

        return post

class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    hashtags = HashTagSerializer(many=True)

class PostUpdateSerializer(serializers.Serializer):
    content = serializers.CharField()

    def update(self, queryset, validated_data):
        post = queryset
        post.content = validated_data["content"]
        post.save()

        return post