from django.contrib.auth import get_user_model 
from rest_framework import viewsets
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .permissions import IsAuthorOrReadOnly
from .serializers import ProjectSerializer, UserSerializer


class ProjectViewSet(viewsets.ModelViewSet): 
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = ProjectSerializer
    
class UserViewSet(viewsets.ModelViewSet): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer   

class ProjectCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home/post.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)