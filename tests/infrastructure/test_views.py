from unittest.mock import patch
from django.test import RequestFactory, TestCase
from django.urls import reverse
from faker import Faker
from rest_framework.test import APIClient
from api.application.domain.serializers import UserSerializer
from tests.application.domain.factories import UserFactory
from rest_framework import status
from django.contrib.auth import get_user_model


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.faker = Faker()

    @patch("allauth.account.auth_backends.AuthenticationBackend.authenticate")
    def test_retrieve_user(self, mock_authenticate):
        user = UserFactory()
        self.client.force_authenticate(user=user)
        response = self.client.get(
            reverse("api:usersprofiles-detail", kwargs={"pk": self.user.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, UserSerializer(self.user).data)

    @patch("allauth.account.auth_backends.AuthenticationBackend.authenticate")
    def test_retrieve_user_not_found(self, mock_authenticate):
        user = UserFactory()
        non_existing_user_id = 99999  # This ID should not exist
        self.client.force_authenticate(user=user)
        response = self.client.get(
            reverse("api:usersprofiles-detail", kwargs={"pk": non_existing_user_id})
        )
        self.assertEqual(response.status_code, 404)

    @patch("allauth.account.auth_backends.AuthenticationBackend.authenticate")
    def test_list_users(self, mock_authenticate):
        # Mock the authentication
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.get(reverse("api:usersprofiles-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    @patch("allauth.account.auth_backends.AuthenticationBackend.authenticate")
    def test_create_user(self, mock_authenticate):
        # Mock the authentication
        user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=user)

        new_user_data = {
            "username": self.faker.user_name(),
            "email": self.faker.email(),
            "password": self.faker.password(),
            "is_staff": True,
            "is_superuser": False,
            "is_active": True,
        }

        response = self.client.post(reverse("api:usersprofiles-list"), new_user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 3)
        self.assertEqual(
            get_user_model().objects.latest("id").username, new_user_data["username"]
        )

    @patch("allauth.account.auth_backends.AuthenticationBackend.authenticate")
    def test_update_user(self, mock_authenticate):
        # Mock the authentication
        user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=user)
        user_to_update = UserFactory(is_staff=False)

        updated_user_data = {
            "is_staff": True,
        }

        response = self.client.patch(
            reverse("api:usersprofiles-detail", kwargs={"pk": user_to_update.pk}),
            updated_user_data,
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.is_staff, updated_user_data["is_staff"])

    @patch("allauth.account.auth_backends.AuthenticationBackend.authenticate")
    def test_destroy_user(self, mock_authenticate):
        # Mock the authentication
        user = UserFactory(is_staff=True)
        user_to_delete = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.delete(
            reverse("api:usersprofiles-detail", kwargs={"pk": user_to_delete.pk})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(get_user_model().objects.count(), 2)
