from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer for the User model.

    The serializer takes the User model instance and converts it into a format that's easy to render into JSON, XML, or other content types. The serializer also provides deserialization, validating incoming data.

    Attributes
    ----------
    id : IntegerField
        An auto-incrementing integer that serves as the unique identifier for each user.
    username : CharField
        The username of the user.
    email : EmailField
        The email address of the user.
    is_active : BooleanField
        A flag that indicates whether the user account is active.
    is_staff : BooleanField
        A flag that indicates whether the user is a staff member.
    is_superuser : BooleanField
        A flag that indicates whether the user has all permissions without explicitly assigning them.

    Methods
    -------
    create(validated_data: dict) -> User
        Create and return a new User instance, given the validated data.
    update(instance: User, validated_data: dict) -> User
        Update and return an existing User instance, given the validated data.
    """

    class Meta:
        model = User
        fields = ("id", "username", "email", "is_active", "is_staff", "is_superuser")
