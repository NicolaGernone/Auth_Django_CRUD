from rest_framework import serializers
from .entities import Profile, User
from ..services import ProfileServices, UserServices  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        UserServices.create_user_profile(user)
        return user

    def update(self, instance, validated_data):
        UserServices.update_user(instance, **validated_data)
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'past_address', 'current_address']

    def update(self, instance, validated_data):
        profile = super().update(instance, validated_data)
        ProfileServices.save_user_profile(profile.user)
        return profile

    def delete(self, instance):
        ProfileServices.delete_user(instance.user)
        return instance
