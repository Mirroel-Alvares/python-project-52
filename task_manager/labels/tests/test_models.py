from .test_base import BaseLabelTest
from task_manager.labels.models import Label


class LabelModelTest(BaseLabelTest):
    def test_label_creation(self):
        """Тестирование создания метки"""
        label = Label.objects.create(name="новая метка")
        self.assertEqual(label.name, "новая метка")
        self.assertIsNotNone(label.created_at)

    def test_label_str_method(self):
        """Тестирование строкового представления"""
        self.assertEqual(str(self.label1), "local bug")
        self.assertEqual(str(self.label2), "database optimization")

    def test_label_meta_options(self):
        """Тестирование мета-опций модели"""
        meta = Label._meta
        self.assertEqual(meta.verbose_name, "метка")
        self.assertEqual(meta.verbose_name_plural, "метки")
        self.assertEqual(meta.db_table, "labels")
        self.assertEqual(meta.get_field('name').max_length, 100)
        self.assertTrue(meta.get_field('name').unique)

    def test_name_uniqueness(self):
        """Тестирование уникальности имени метки"""
        with self.assertRaises(Exception):
            Label.objects.create(name="local bug")