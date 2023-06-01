from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework.test import APIClient
from tests.application.domain.factories import UserFactory
from rest_framework import status

class UserViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.user2 = UserFactory(username='user2')
        self.user_url = reverse('user-detail', kwargs={'pk': self.user2.pk})

    def test_retrieve_user(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'user2')

    def test_update_user(self):
        data = {'username': 'new_username'}
        response = self.client.patch(self.user_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'new_username')

    def test_delete_user(self):
        response = self.client.delete(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ProfileViewSetTest(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile(self):
        url = reverse('profile-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        url = reverse('profile-list')
        data = {'name': 'new_name'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'new_name')

    def test_delete_profile(self):
        url = reverse('profile-detail', kwargs={'pk': self.user.profile.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

