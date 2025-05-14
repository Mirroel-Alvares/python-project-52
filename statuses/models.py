from django.db import models


class Status(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        db_table = "statuses"
        verbose_name = "статус"
        verbose_name_plural = "статусы"

    def __str__(self):
        return self.name
