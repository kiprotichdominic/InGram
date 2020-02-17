from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    

class ProfileView(generic.TemplateView):
    template_name = 'users/profile.html'