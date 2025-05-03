from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    # DetailView,
    TemplateView,
    ListView,
    UpdateView,
)

from users.forms import CustomUserCreationForm, CustomUserUpdateForm
from users.models import User


class UsersIndexView(ListView):
    model = User
    template_name = 'users/users_index.html'
    context_object_name = "users"


class UserCreate(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "main/form.html"
    success_url = reverse_lazy("login")
    extra_context = dict(page_title='Create user', title="Регистрация", button="Зарегистрировать")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


class UserDelete(TemplateView):
    template_name = 'users/user_delete.html'


class UserUpdate(UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = "main/form.html"
    success_url = reverse_lazy("users:users_index")
    extra_context = dict(page_title='Update user', title="Изменение пользователя", button="Изменить")


class UserDelete(DeleteView):
    model = User
    template_name = "users/user_delete.html"
    success_url = reverse_lazy("users:users_index")


#
#
# class ArticleDetail(DetailView):
#     model = Article
#     template_name = "articles/detail.html"