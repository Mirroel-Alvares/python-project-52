from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class AuthRequiredMixin(LoginRequiredMixin):
    auth_message = "Вы не авторизованы! Пожалуйста, выполните вход."

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_message)
            return redirect(reverse_lazy('main:login'))

        return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin(UserPassesTestMixin):
    permission_message = None
    permission_url = None

    def test_func(self):
        obj = self.get_object()
        if hasattr(obj, 'author'):
            return obj.author == self.request.user
        elif hasattr(obj, 'user'):
            return obj.user == self.request.user
        return obj == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_message)
        return redirect(self.permission_url)
