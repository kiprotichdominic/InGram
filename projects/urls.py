from django.urls import path

from .views import ProjectList, ProjectDetail, UserDetail, UserList

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()), 
    path('project/<int:pk>', ProjectDetail.as_view()),
    path('project/', ProjectList.as_view()),
]
