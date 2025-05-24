from django.urls import reverse
from django.contrib.messages import get_messages
from .test_base import BaseTaskTest
from task_manager.tasks.models import Task


class TaskViewsTest(BaseTaskTest):
    def setUp(self):
        self.list_url = reverse('tasks:tasks_index')
        self.create_url = reverse('tasks:task_create')
        self.update_url = reverse(
            'tasks:task_update',
            kwargs={'pk': self.task1.pk}
        )
        self.delete_url = reverse(
            'tasks:task_delete',
            kwargs={'pk': self.task1.pk}
        )
        self.details_url = reverse(
            'tasks:task_details',
            kwargs={'pk': self.task1.pk}
        )

    def test_tasks_index_view(self):
        """Тестирование списка задач"""
        self.client.force_login(self.user1)
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks_index.html')
        self.assertContains(response, 'Test task')
        self.assertContains(response, 'Test task 2')
        self.assertEqual(len(response.context['tasks']), 2)

    def test_task_create_view(self):
        """Тестирование создания задачи"""
        self.client.force_login(self.user1)
        response = self.client.post(
            self.create_url,
            {
                'name': 'Новая задача',
                'description': 'Описание',
                'status': self.status1.pk,
                'executor': self.user2.pk,
                'labels': [self.label1.pk]
            },
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.assertTrue(
            Task.objects.filter(name='Новая задача').exists()
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Задача успешно создана')

    def test_task_update_view(self):
        """Тестирование обновления задачи"""
        self.client.force_login(self.user1)
        response = self.client.post(
            self.update_url,
            {
                'name': 'Обновленная задача',
                'description': 'Новое описание',
                'status': self.status1.pk,
                'executor': self.user2.pk,
                'labels': [self.label2.pk]
            },
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.name, 'Обновленная задача')
        self.assertEqual(list(self.task1.labels.all()), [self.label2])

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Задача успешно изменена')

    def test_task_delete_view(self):
        """Тестирование удаления задачи"""
        self.client.force_login(self.user1)
        response = self.client.post(
            self.delete_url,
            follow=True
        )

        self.assertRedirects(response, self.list_url)
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Задача успешно удалена')

    def test_task_details_view(self):
        """Тестирование просмотра задачи"""
        self.client.force_login(self.user1)
        response = self.client.get(self.details_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_details.html')
        self.assertEqual(response.context['task'], self.task1)
        self.assertContains(response, 'Test task')

    def test_views_protection(self):
        """
        Тестирование защиты представлений
        от неавторизованных пользователей
        """
        urls = [
            self.list_url,
            self.create_url,
            self.update_url,
            self.delete_url,
            self.details_url
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertTrue(response.url.startswith('/login/'))

    def test_templates_used(self):
        """Тестирование используемых шаблонов"""
        self.client.force_login(self.user1)

        templates = {
            self.list_url: 'tasks/tasks_index.html',
            self.create_url: 'main/form.html',
            self.update_url: 'main/form.html',
            self.delete_url: 'tasks/delete_task.html',
            self.details_url: 'tasks/task_details.html',
        }

        for url, template in templates.items():
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    def test_extra_context(self):
        """Тестирование дополнительного контекста"""
        self.client.force_login(self.user1)

        # Создание
        response = self.client.get(self.create_url)
        self.assertEqual(response.context['page_title'], 'Create task')
        self.assertEqual(response.context['title'], 'Создать задачу')
        self.assertEqual(response.context['button'], 'Создать')

        # Обновление
        response = self.client.get(self.update_url)
        self.assertEqual(response.context['page_title'], 'Update task')
        self.assertEqual(response.context['title'], 'Изменение задачи')
        self.assertEqual(response.context['button'], 'Изменить')

        # Удаление
        response = self.client.get(self.delete_url)
        self.assertEqual(response.context['page_title'], 'Delete task')
        self.assertEqual(response.context['title'], 'Удаление задачи')