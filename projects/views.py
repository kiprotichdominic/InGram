from rest_framework import generics, permissions 
from .models import Post
from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,) 
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer