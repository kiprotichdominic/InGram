from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('image','author', 'title', 'body', 'created_at','link',)
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)   
        