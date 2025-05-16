from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        full_name = self.get_full_name().strip()
        return full_name if full_name else self.username

    class Meta:
        db_table = "users"
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"



    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
    # проверить работу первого варианта
