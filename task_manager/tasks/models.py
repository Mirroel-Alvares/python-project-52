from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=100,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    status = models.ForeignKey(
        Status,
        verbose_name='Статус',
        on_delete=models.PROTECT,
        related_name="tasks"
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.PROTECT,
        related_name="tasks_author"
    )
    executor = models.ForeignKey(
        User,
        verbose_name='Исполнитель',
        on_delete=models.PROTECT,
        related_name="task_executor",
        blank=True,
        null=True
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name='Метки',
        related_name="tasks",
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tasks"
        verbose_name = "задача"
        verbose_name_plural = "задачи"
