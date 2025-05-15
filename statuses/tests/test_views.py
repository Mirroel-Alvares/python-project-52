from django.urls import reverse
from django.contrib.messages import get_messages
from django.test import TestCase, Client
from .test_base import BaseStatusTest
from statuses.models import Status


class StatusViewsTest(BaseStatusTest):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('statuses:statuses_index')
        self.create_url = reverse('statuses:status_create')
        self.update_url = reverse('statuses:status_update', kwargs={'pk': self.status.pk})
        self.delete_url = reverse('statuses:status_delete', kwargs={'pk': self.status.pk})

    def test_status_index_view(self):
        """Тестирование списка статусов"""
        self.client.force_login(self.user)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses_index.html')
        self.assertContains(response, 'в космосе')
        self.assertContains(response, 'на дне')
        self.assertEqual(len(response.context['statuses']), 2)

    def test_status_create_view(self):
        """Тестирование создания статуса"""
        self.client.force_login(self.user)
        response = self.client.post(
            self.create_url,
            {'name': 'новый статус'},
            follow=True
        )

        # Проверка редиректа
        self.assertRedirects(response, self.list_url)
        # Проверка создания статуса
        self.assertTrue(Status.objects.filter(name='новый статус').exists())
        # Проверка сообщения об успехе
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Статус успешно создан')

    def test_status_update_view(self):
        """Тестирование обновления статуса"""
        self.client.force_login(self.user)
        response = self.client.post(
            self.update_url,
            {'name': 'обновленный статус'},
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'обновленный статус')

        # Проверка сообщения об успехе
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Статус успешно изменен')

    def test_status_delete_view(self):
        """Тестирование удаления статуса"""
        self.client.force_login(self.user)
        response = self.client.post(
            self.delete_url,
            follow=True
        )

        self.assertRedirects(response, reverse('users:users_index'))
        self.assertFalse(Status.objects.filter(pk=self.status.pk).exists())

        # Проверка сообщения об успехе
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Статус успешно удален')

    def test_views_protection(self):
        """Тестирование защиты представлений от неавторизованных пользователей"""
        urls = [
            self.list_url,
            self.create_url,
            self.update_url,
            self.delete_url,
        ]

        for url in urls:
            response = self.client.get(url)

            # Проверяем что это редирект на login
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith('/login/'))

    def test_templates_used(self):
        """Тестирование используемых шаблонов"""
        self.client.force_login(self.user)

        # Проверка шаблонов для каждого представления
        templates = {
            self.list_url: 'statuses/statuses_index.html',
            self.create_url: 'main/form.html',
            self.update_url: 'main/form.html',
            self.delete_url: 'main/delete_form.html',
        }

        for url, template in templates.items():
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    def test_extra_context(self):
        """Тестирование дополнительного контекста"""
        self.client.force_login(self.user)

        # Проверка для создания статуса
        response = self.client.get(self.create_url)
        self.assertEqual(response.context['page_title'], 'Create status')
        self.assertEqual(response.context['title'], 'Создать статус')
        self.assertEqual(response.context['button'], 'Создать')

        # Проверка для обновления статуса
        response = self.client.get(self.update_url)
        self.assertEqual(response.context['page_title'], 'Update status')
        self.assertEqual(response.context['title'], 'Изменение статуса')
        self.assertEqual(response.context['button'], 'Изменить')

        # Проверка для удаления статуса
        response = self.client.get(self.delete_url)
        self.assertEqual(response.context['page_title'], 'Delete status')
        self.assertEqual(response.context['title'], 'Удаление статуса')