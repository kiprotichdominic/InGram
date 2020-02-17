from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .services import get_posts
import requests

class HomePageView(TemplateView):
    template_name = "home/home.html"
    
    
def home(request):
    url = 'https://blogapi001.herokuapp.com/api/v1/?format=json'
    response = requests.get(url)
    data = response.json()
    print(data)
    context ={"data":data}
    return render(request, 'home/home.html', context)

class GetPosts(TemplateView):
    template_name = 'home/home3.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'posts' : get_posts
        }
        return context