from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView, GetPosts

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("home3/", GetPosts.as_view(), name="home3"),
    path('home/', views.home, name='home2'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)