from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from task_manager.users.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Имя"
        }),
        label="Имя"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Фамилия"
        }),
        label="Фамилия"
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Имя пользователя"
        }),
        label="Имя пользователя",
        help_text="Обязательное поле. Не более 150 символов. \
            Только буквы, цифры и символы @/./+/-/_."
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Пароль"
        }),
        label="Пароль",
        help_text=mark_safe("""
            <span style='margin-left: 10px;'><strong>•</strong> 
            Ваш пароль должен содержать как минимум 3 символа.
            """
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Подтверждение пароля"
        }),
        label="Подтверждение пароля",
        help_text="Для подтверждения введите, пожалуйста, пароль ещё раз."
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2"
            ]


class CustomUserUpdateForm(CustomUserCreationForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(
                username=username
        ).exclude(id=self.instance.id).exists():
            raise ValidationError(
                "Пользователь с таким именем уже существует"
            )
        return username
