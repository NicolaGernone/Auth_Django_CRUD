from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Define an inline admin descriptor for the Profile model
# This allows us to edit the Profile whenever we are editing the User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin which includes the Profile
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register ProfileAdmin separately
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'phone_number', 'past_address', 'current_address']

admin.site.register(Profile, ProfileAdmin)

