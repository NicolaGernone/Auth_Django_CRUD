from unittest.mock import patch
from django.test import TestCase
from api.application.services import ProfileServices, UserServices
from tests.application.domain.factories import UserFactory

class UserServiceTest(TestCase):
    @patch('django.contrib.auth.get_user_model().save')
    def test_update_user(self, mock_save):
        user = UserFactory.build()  # build doesn't save the object to DB
        ProfileServices.update_user(user, username='new_username')
        self.assertEqual(user.username, 'new_username')
        mock_save.assert_called_once()

    @patch('django.contrib.auth.get_user_model().delete')
    def test_delete_user(self, mock_delete):
        user = UserFactory.build()
        ProfileServices.delete_user(user)
        mock_delete.assert_called_once()

    @patch('api.models.Profile.objects.get_or_create')
    def test_create_user_profile(self, mock_get_or_create):
        user = UserFactory.build()
        UserServices.create_user_profile(user)
        mock_get_or_create.assert_called_once_with(user=user)

    @patch('django.contrib.auth.get_user_model().profile.save')
    def test_save_user_profile(self, mock_save):
        user = UserFactory.build()
        UserServices.save_user_profile(user)
        mock_save.assert_called_once()
