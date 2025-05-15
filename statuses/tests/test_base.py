from django.test import TestCase, Client

from statuses.models import Status
from users.models import User


class BaseStatusTest(TestCase):
    fixtures = ["fixtures/users_td.json", "fixtures/statuses_td.json"]

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.status = Status.objects.get(pk=1)
        cls.user = User.objects.get(pk=1)

        cls.status_data = {"name": "в пустоте"}
