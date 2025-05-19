from django.urls import reverse
from django.contrib.messages import get_messages
from .test_base import BaseLabelTest
from labels.models import Label


class LabelViewsTest(BaseLabelTest):
    def setUp(self):
        self.list_url = reverse('labels:labels_index')
        self.create_url = reverse('labels:label_create')
        self.update_url = reverse(
            'labels:label_update',
            kwargs={'pk': self.label1.pk}
        )
        self.delete_url = reverse(
            'labels:label_delete',
            kwargs={'pk': self.label1.pk}
        )

    def test_labels_index_view(self):
        """Тестирование списка меток"""
        self.client.force_login(self.user)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/labels_index.html')
        self.assertContains(response, 'local bug')
        self.assertContains(response, 'database optimization')
        self.assertEqual(len(response.context['labels']), 2)

    def test_label_create_view(self):
        """Тестирование создания метки"""
        self.client.force_login(self.user)
        response = self.client.post(
            self.create_url,
            {'name': 'новая метка'},
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.assertTrue(Label.objects.filter(name='новая метка').exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Метка успешно создана')

    def test_label_update_view(self):
        """Тестирование обновления метки"""
        self.client.force_login(self.user)
        response = self.client.post(
            self.update_url,
            {'name': 'обновленная метка'},
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.label1.refresh_from_db()
        self.assertEqual(self.label1.name, 'обновленная метка')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Метка успешно изменена')

    def test_label_delete_view(self):
        """Тестирование удаления метки"""
        self.client.force_login(self.user)
        response = self.client.post(
            self.delete_url,
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.assertFalse(Label.objects.filter(pk=self.label1.pk).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Метка успешно удалена')

    def test_views_protection(self):
        """
        Тестирование защиты представлений
        от неавторизованных пользователей
        """
        urls = [
            self.list_url,
            self.create_url,
            self.update_url,
            self.delete_url
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith('/login/'))

    def test_templates_used(self):
        """Тестирование используемых шаблонов"""
        self.client.force_login(self.user)

        templates = {
            self.list_url: 'labels/labels_index.html',
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

        response = self.client.get(self.create_url)
        self.assertEqual(response.context['page_title'], 'Create label')
        self.assertEqual(response.context['title'], 'Создать метку')
        self.assertEqual(response.context['button'], 'Создать')

        response = self.client.get(self.update_url)
        self.assertEqual(response.context['page_title'], 'Update label')
        self.assertEqual(response.context['title'], 'Изменение метки')
        self.assertEqual(response.context['button'], 'Изменить')

        response = self.client.get(self.delete_url)
        self.assertEqual(response.context['page_title'], 'Delete label')
        self.assertEqual(response.context['title'], 'Удаление метки')
