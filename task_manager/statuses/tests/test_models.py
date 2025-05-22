from .test_base import BaseStatusTest
from task_manager.statuses.models import Status


class StatusModelTest(BaseStatusTest):
    def test_status_creation(self):
        """Тестирование создания статуса"""
        status = Status.objects.create(name='тестовый статус')
        self.assertEqual(status.name, 'тестовый статус')
        self.assertIsNotNone(status.created_at)

    def test_status_str_method(self):
        """Тестирование строкового представления"""
        self.assertEqual(str(self.status), 'в космосе')

    def test_status_ordering(self):
        """Тестирование сортировки по умолчанию"""
        statuses = Status.objects.all()
        self.assertEqual(statuses[0].name, 'в космосе')
        self.assertEqual(statuses[1].name, 'на дне')

    def test_name_max_length(self):
        """Тестирование максимальной длины имени"""
        max_length = Status._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_meta_options(self):
        """Тестирование мета-опций модели"""
        self.assertEqual(Status._meta.verbose_name, 'статус')
        self.assertEqual(Status._meta.verbose_name_plural, 'статусы')