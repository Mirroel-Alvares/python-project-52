from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from .test_base import BaseTaskTest

User = get_user_model()


class ConnectedDataDeletionTest(BaseTaskTest):
    """Тесты защиты связанных данных от удаления"""

    def test_protected_status_deletion(self):
        """Тестирование защиты используемого статуса от удаления"""
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse('statuses:status_delete', kwargs={'pk': self.status2.pk}),
            follow=True
        )
        self.assertTrue(Status.objects.filter(pk=self.status2.pk).exists())
        self.assertRedirects(response, reverse('statuses:statuses_index'))
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            'Невозможно удалить статус, потому что он используется',
            str(messages[0])
        )

    def test_protected_label_deletion(self):
        """Тестирование защиты используемой метки от удаления"""
        self.client.force_login(self.user1)
        response = self.client.post(
            reverse('labels:label_delete', kwargs={'pk': self.label1.pk}),
            follow=True
        )
        self.assertTrue(Label.objects.filter(pk=self.label1.pk).exists())
        self.assertRedirects(response, reverse('labels:labels_index'))
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            'Невозможно удалить метку, потому что она используется',
            str(messages[0])
        )

    def test_protected_user_deletion(self):
        """Тестирование защиты используемого пользователя от удаления"""
        self.client.force_login(self.user1)

        response = self.client.post(
            reverse('users:user_delete', kwargs={'pk': self.user1.pk}),
            follow=True
        )
        self.assertTrue(User.objects.filter(pk=self.user1.pk).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            'Невозможно удалить пользователя, потому что он используется',
            [str(m) for m in messages]
        )

        response = self.client.post(
            reverse('users:user_delete', kwargs={'pk': self.user2.pk}),
            follow=True
        )
        self.assertTrue(User.objects.filter(pk=self.user2.pk).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(
            'У вас нет прав для изменения другого пользователя.',
            [str(m) for m in messages]
        )
