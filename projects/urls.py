from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, ProjectViewSet


router = SimpleRouter()
router.register('users', UserViewSet, )
router.register('', ProjectViewSet,)

urlpatterns = router.urls