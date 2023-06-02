from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.infrastructure.views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'profile', ProfileViewSet, basename='profile')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
