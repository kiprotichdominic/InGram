from django.urls import path
from . import views
from .views import HomePageView, GetPosts

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home3/", GetPosts.as_view(), name="home3"),
    path('home/', views.home, name='home2'),
]
