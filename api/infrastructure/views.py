from rest_framework import viewsets, permissions, authentication
from .models import CustomUser
from api.application.domain.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for the User model.

    In addition to the standard `list()`, `create()`, `retrieve()`, `update()`, and `destroy()` actions,
    this viewset also provides `get()` and `set()` for individual instances of the User model.

    Attributes
    ----------
    queryset : QuerySet
        The set of all CustomUser instances.
    serializer_class : Serializer
        The serializer class used for validating and deserializing input, and for serializing output.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
