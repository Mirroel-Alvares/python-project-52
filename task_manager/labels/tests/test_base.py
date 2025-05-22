from django.test import TestCase, Client

from task_manager.labels.models import Label
from task_manager.users.models import User


class BaseLabelTest(TestCase):
    fixtures = [
        "task_manager/fixtures/users_td.json",
        "task_manager/fixtures/labels_td.json"
    ]

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.label1 = Label.objects.get(pk=1)
        cls.label2 = Label.objects.get(pk=2)
        cls.user = User.objects.get(pk=1)

        cls.label_data = {"name": "охота на куропаток"}
