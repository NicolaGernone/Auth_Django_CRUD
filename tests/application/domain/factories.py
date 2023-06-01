import factory
from django.contrib.auth import get_user_model

from api.application.domain.entities import Profile

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('name')
    phone_number = factory.Faker('phone_number')
    past_address = factory.Faker('address')
    current_address = factory.Faker('address')
