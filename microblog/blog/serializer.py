from rest_framework import serializers
from blog.models import HashTag, Post

class HashTagSerializer(serializers.Serializer):
    label = serializers.CharField()

class PostSerializer(serializers.Serializer):
    content = serializers.CharField()
    hashtags = HashTagSerializer(many=True, required=False)


    def validate_content(self, value):
        if len(value) > 144:
            raise serializers.ValidationError("Max 144 Characters")
        return value

    def create(self, validated_data):

        hashtags = []

        

        post = Post()
        post.content = validated_data["content"]
      
        post.save()

        for item in validated_data["hashtags"]:
            hashtag = HashTag.objects.filter(**item).last()
            if hashtag == None:
                hashtag = HashTag(**item)
                hashtag.save()
            post.hashtags.add(hashtag)
        
        post.save()

        return post