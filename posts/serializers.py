from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk', 
            'title', 
            'slug', 
            'body', 
            'date_created', 
            'last_updated'
        ]
        
class PostSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk', 
            'title', 
            'body', 
            'date_created', 
            'last_updated'
        ]
