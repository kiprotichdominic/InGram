from django.contrib.auth import get_user_model 
from rest_framework import viewsets
from .models import Post, Profile
from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer, UserSerializer, ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer
    
class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer   

class ProfileViewSet(viewsets.ModelViewSet): 
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer