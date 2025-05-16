from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from users.forms import CustomUserCreationForm, CustomUserUpdateForm
from users.models import User
from tasks.models import Task
from main.mixins import AuthRequiredMixin, OwnerRequiredMixin


class UsersIndexView(ListView):
    model = User
    template_name = 'users/users_index.html'
    context_object_name = "users"


class UserCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "main/form.html"
    success_url = reverse_lazy("main:login")
    extra_context = dict(
        page_title='Create user',
        title="Регистрация",
        button="Зарегистрировать"
    )
    success_message = "Пользователь успешно зарегистрирован"


class UserUpdate(AuthRequiredMixin, OwnerRequiredMixin,
                 SuccessMessageMixin, UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = "main/form.html"
    success_url = reverse_lazy("users:users_index")
    extra_context = dict(
        page_title='Update user',
        title="Изменение пользователя",
        button="Изменить"
    )
    success_message = "Пользователь успешно изменен"
    permission_message = 'У вас нет прав для изменения другого пользователя.'
    permission_url = reverse_lazy('users:users_index')


class UserDelete(AuthRequiredMixin, OwnerRequiredMixin,
                 SuccessMessageMixin, DeleteView):
    model = User
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("users:users_index")
    success_message = 'Пользователь успешно удален'
    permission_message = 'У вас нет прав для изменения другого пользователя.'
    permission_url = reverse_lazy("users:users_index")

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        if Task.objects.filter(user=user).exists():
            messages.error(
            request,
            """
            Невозможно удалить пользователя,
            потому что он используется
            """
            )
            return redirect(self.success_url)
        return super().delete(request, *args, **kwargs)