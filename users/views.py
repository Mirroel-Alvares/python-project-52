from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    # DeleteView,
    # DetailView,
    TemplateView,
    ListView,
    # UpdateView,
)

from users.forms import CustomUserCreationForm
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
    extra_context = dict(title="Регистрация", button="Зарегистрировать")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


class UserDelete(TemplateView):
    template_name = 'users/user_delete.html'


class UserUpdate(TemplateView):
    template_name = 'users/user_update.html'





# from python_django_blog.articles.forms import ArticleForm
# from python_django_blog.articles.models import Article
#
#
# class IndexView(ListView):
#     model = Article
#     template_name = "articles/index.html"
#
#
# class ArticleCreate(CreateView):
#     model = Article
#     form_class = ArticleForm
#     template_name = "articles/create.html"
#
#
# class ArticleUpdate(UpdateView):
#     model = Article
#     form_class = ArticleForm
#     template_name = "articles/update.html"
#
#
# class ArticleDelete(DeleteView):
#     model = Article
#     success_url = reverse_lazy("articles:index")
#     template_name = "articles/delete.html"
#
#
# class ArticleDetail(DetailView):
#     model = Article
#     template_name = "articles/detail.html"