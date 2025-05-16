from django.db import models


class Status(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, unique=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "statuses"
        verbose_name = "статус"
        verbose_name_plural = "статусы"
