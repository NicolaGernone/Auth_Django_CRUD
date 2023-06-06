from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from tests.application.domain.factories import UserFactory


class UserTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_user_creation(self):
        """
        Positive test case: A user should be successfully created by the UserFactory with default values.
        """
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, True)
        self.assertEqual(self.user.is_superuser, False)

    def test_user_creation_with_custom_values(self):
        """
        Positive test case: A user should be successfully created by the UserFactory with custom values.
        """
        custom_user = UserFactory(is_staff=False, is_superuser=True)
        self.assertEqual(get_user_model().objects.count(), 2)
        self.assertEqual(custom_user.is_staff, False)
        self.assertEqual(custom_user.is_superuser, True)

    def test_user_creation_with_invalid_email(self):
        """
        Negative test case: A user should not be created if an invalid email is provided.
        """
        with self.assertRaises(IntegrityError):
            UserFactory(email=None)

    def test_user_creation_with_duplicate_username(self):
        """
        Negative test case: A user should not be created if a duplicate username is provided.
        """
        with self.assertRaises(IntegrityError):
            UserFactory(username=self.user.username)
