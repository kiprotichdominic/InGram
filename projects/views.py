from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer