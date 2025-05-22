from django.test import TestCase, Client

from task_manager.statuses.models import Status
from task_manager.users.models import User


class BaseStatusTest(TestCase):
    fixtures = ["task_manager/fixtures/users_td.json", "task_manager/fixtures/statuses_td.json"]

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.status = Status.objects.get(pk=1)
        cls.user = User.objects.get(pk=1)

        cls.status_data = {"name": "в пустоте"}
