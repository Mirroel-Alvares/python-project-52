from django.db import models
from django.db.models import ProtectedError


class Label(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100, unique=True)
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def delete(self, *args, **kwargs):
        if self.tasks.exists():
            raise ProtectedError(
                "Невозможно удалить метку, потому что она используется",
                self.tasks.all()
            )
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "labels"
        verbose_name = "метка"
        verbose_name_plural = "метки"
