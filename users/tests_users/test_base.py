from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseUserTest(TestCase):
    fixtures = ["fixtures/users_td.json"]

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user1 = User.objects.get(pk=1)
        cls.user2 = User.objects.get(pk=2)
        cls.user3 = User.objects.get(pk=3)

        cls.user_data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
