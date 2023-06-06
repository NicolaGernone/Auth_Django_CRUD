from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    CustomUser extends the default AbstractUser model with custom settings.

    Attributes:
        is_superuser: A boolean that indicates if the user has all permissions without explicitly assigning them.
        is_staff: A boolean that indicates if the user is allowed to access the admin site.
        is_active: A boolean that indicates if the user account is currently active.
    """

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns a string representation of this `CustomUser`.

        This string is used when a `CustomUser` is referred to in a string format.

        Returns:
            A string representation of this `CustomUser` which is the username.
        """
        return self.username

    class Meta:
        """
        Meta class for CustomUser.

        Attributes:
            verbose_name: A human-readable name for the object, singular.
            verbose_name_plural: The plural name for the object.
        """
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
