from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task

User = get_user_model()


class BaseTaskTest(TestCase):
    fixtures = [
        "task_manager/fixtures/users_td.json",
        "task_manager/fixtures/labels_td.json",
        "task_manager/fixtures/statuses_td.json",
        "task_manager/fixtures/tasks_td.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.task1 = Task.objects.get(pk=1)
        cls.task2 = Task.objects.get(pk=2)
        cls.label1 = Label.objects.get(pk=1)
        cls.label2 = Label.objects.get(pk=2)
        cls.status1 = Status.objects.get(pk=1)
        cls.status2 = Status.objects.get(pk=2)
        cls.user1 = User.objects.get(pk=1)
        cls.user2 = User.objects.get(pk=2)

        cls.task_data = {
            "name": "New task",
            "description": "пу-пу-пу",
            "status": cls.status1.pk,
            "labels": [cls.label2.pk],
            "executor": cls.user1.pk,
        }

    def setUp(self):
        """Имитация request для тестов фильтра"""
        self.request = type('Request', (), {'user': self.user1, 'GET': {}})()