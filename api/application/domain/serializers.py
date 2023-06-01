from rest_framework import serializers
from .entities import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'phone_number', 'past_address', 'current_address']
