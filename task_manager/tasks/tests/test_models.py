from .test_base import BaseTaskTest
from task_manager.tasks.models import Task


class TaskModelTest(BaseTaskTest):
    def test_task_creation(self):
        """Тестирование создания задачи"""
        task = Task.objects.create(
            name="Новая задача",
            description="Описание",
            status=self.status1,
            author=self.user1,
            performer=self.user2
        )
        task.labels.add(self.label1)

        self.assertEqual(task.name, "Новая задача")
        self.assertEqual(task.status, self.status1)
        self.assertEqual(task.author, self.user1)
        self.assertEqual(task.performer, self.user2)
        self.assertEqual(list(task.labels.all()), [self.label1])
        self.assertIsNotNone(task.created_at)

    def test_task_str_method(self):
        """Тестирование строкового представления"""
        self.assertEqual(str(self.task1), "Test task")
        self.assertEqual(str(self.task2), "Test task 2")

    def test_task_meta_options(self):
        """Тестирование мета-опций модели"""
        meta = Task._meta
        self.assertEqual(meta.verbose_name, "задача")
        self.assertEqual(meta.verbose_name_plural, "задачи")
        self.assertEqual(meta.db_table, "tasks")
        self.assertEqual(meta.get_field('name').max_length, 100)
        self.assertTrue(meta.get_field('name').unique)

    def test_foreign_keys(self):
        """Тестирование связей модели"""
        self.assertEqual(self.task1.status, self.status2)
        self.assertEqual(self.task1.author, self.user1)
        self.assertEqual(self.task1.performer, self.user2)
        self.assertEqual(
            list(self.task1.labels.all()),
            [self.label1, self.label2]
        )