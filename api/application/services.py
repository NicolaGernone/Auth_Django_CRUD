from .domain.entities import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileServices:
    
    @staticmethod
    def create_user_profile(user):
        Profile.objects.get_or_create(user=user)

    @staticmethod
    def save_user_profile(user):
        user.profile.save()

    @staticmethod
    def delete_user(user):
        user.delete()

    @staticmethod
    def update_user(user, **kwargs):
        for attr, value in kwargs.items():
            setattr(user, attr, value)
        user.save()
        
