from django.test import TestCase
from tests.application.domain.factories import ProfileFactory, UserFactory


class ProfileModelTest(TestCase):

    def test_profile_creation(self):
        user = UserFactory.build()  # build, not create, for no DB interaction

        profile = ProfileFactory(
            user=user,
            name="Test User",
            phone_number="1234567890",
            past_address="123 Past St, Pastville",
            current_address="123 Current St, Currentville"
        )

        # These tests check the object in memory, not saved to the DB
        self.assertEqual(profile.user, user)
        self.assertEqual(profile.name, "Test User")
        self.assertEqual(profile.phone_number, "1234567890")
        self.assertEqual(profile.past_address, "123 Past St, Pastville")
        self.assertEqual(profile.current_address, "123 Current St, Currentville")

    def test_profile_str(self):
        user = UserFactory.build(username='testuser')
        profile = ProfileFactory(user=user)
        self.assertEqual(str(profile), 'testuser')

