from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('user', 'user@localhost')

    def test_user_exists(self):
        email = User.objects.get(username='user').email
        self.assertEqual(email, 'user@localhost')