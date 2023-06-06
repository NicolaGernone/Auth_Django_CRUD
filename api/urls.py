from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.infrastructure.views import UserViewSet

router = DefaultRouter()
router.register(r"usersprofiles", UserViewSet, basename="usersprofiles")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
