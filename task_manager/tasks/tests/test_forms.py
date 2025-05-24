from .test_base import BaseTaskTest
from task_manager.tasks.forms import TaskForm, TaskFilter


class TaskFormTest(BaseTaskTest):
    def test_form_fields_and_widgets(self):
        """Тестирование полей формы и виджетов"""
        form = TaskForm(user=self.user1)

        # Проверка полей
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('status', form.fields)
        self.assertIn('executor', form.fields)
        self.assertIn('labels', form.fields)

        # Проверка виджетов
        self.assertEqual(
            form.fields['name'].widget.attrs['class'],
            'form-control'
        )
        self.assertEqual(
            form.fields['description'].widget.attrs['class'],
            'form-control'
        )
        self.assertEqual(
            form.fields['status'].widget.attrs['class'],
            'form-select'
        )
        self.assertEqual(
            form.fields['executor'].widget.attrs['class'],
            'form-select'
        )

    def test_form_validation(self):
        """Тестирование валидации формы"""
        # Валидные данные
        form = TaskForm(data={
            'name': 'Новая задача',
            'description': 'Описание',
            'status': self.status1.pk,
            'executor': self.user2.pk,
            'labels': [self.label1.pk]
        }, user=self.user1)
        self.assertTrue(form.is_valid())

        # Пустое имя
        form = TaskForm(data={
            'name': '',
            'status': self.status1.pk
        }, user=self.user1)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_form_save(self):
        """Тестирование сохранения формы"""
        form = TaskForm(data={
            'name': 'Сохраненная задача',
            'description': 'Описание',
            'status': self.status1.pk,
            'executor': self.user2.pk,
            'labels': [self.label1.pk]
        }, user=self.user1)

        task = form.save()
        self.assertEqual(task.author, self.user1)
        self.assertEqual(task.executor, self.user2)
        self.assertEqual(list(task.labels.all()), [self.label1])


class TaskFilterTest(BaseTaskTest):
    def test_filter_fields(self):
        """Тестирование полей фильтра"""
        filter_fields = TaskFilter(data={}, request=self.request)
        self.assertIn('status', filter_fields.filters)
        self.assertIn('executor', filter_fields.filters)
        self.assertIn('labels', filter_fields.filters)
        self.assertIn('self_tasks', filter_fields.filters)

    def test_self_tasks_filter(self):
        """Тестирование фильтрации своих задач"""
        filter_my_task = TaskFilter(
            data={'self_tasks': True},
            request=self.request
        )

        queryset = filter_my_task.qs

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset.first().author, self.user1)