import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    """
    User factory.

    A factory for creating User model instances for testing. The factory_boy library allows for easy, flexible, and efficient creation of complex objects, avoiding the need for repeated setup code in your tests.

    Attributes
    ----------
    username : Sequence
        A sequence that generates a unique username for each user.
    email : Sequence
        A sequence that generates a unique email address for each user.
    is_active : Boolean
        A flag that is set to True by default, indicating that the user account is active.
    is_staff : Boolean
        A flag that is set to True by default, indicating that the user is a staff member.
    is_superuser : Boolean
        A flag that is set to False by default, indicating whether the user has all permissions without explicitly assigning them.
    """

    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    is_active = True
    is_staff = True
    is_superuser = False
