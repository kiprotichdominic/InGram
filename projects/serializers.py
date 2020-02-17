from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Profile

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'image','author', 'title', 'body', 'created_at',)
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)   
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username','image')   