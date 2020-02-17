from rest_framework import serializers
from .models import Post

class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'image','author', 'title', 'body', 'created_at',)
        model = Post