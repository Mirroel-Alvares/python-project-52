from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from task_manager.main.forms import CustomAuthForm


class IndexView(TemplateView):
    template_name = 'main/index.html'


class LoginView(AuthLoginView):
    template_name = "main/form.html"
    form_class = CustomAuthForm
    success_url = reverse_lazy("main:index")
    extra_context = dict(page_title='Login', title="Вход", button="Войти")

    def get_success_url(self):
        return self.get_redirect_url() or self.success_url

    def form_valid(self, form):
        messages.success(self.request, "Вы залогинены")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            """Пожалуйста, введите правильные имя пользователя и пароль.
            Оба поля могут быть чувствительны к регистру.""",
        )
        return super().form_invalid(form)


@method_decorator(require_POST, name='dispatch')
class LogoutView(AuthLogoutView):
    next_page = reverse_lazy("main:index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)
