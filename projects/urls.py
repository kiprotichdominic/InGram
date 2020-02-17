from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ProjectViewSet, ProfileViewSet


router = SimpleRouter()
router.register('users', UserViewSet, )
router.register('', ProjectViewSet,)
router.register('profile/', ProfileViewSet,)

urlpatterns = router.urls