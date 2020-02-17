from django.contrib.auth import get_user_model 
from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer, UserSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer
    
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer
    
class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer