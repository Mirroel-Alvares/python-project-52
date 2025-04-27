from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'


class LoginView(TemplateView):
    template_name = 'main/index.html'


class LogoutView(TemplateView):
    template_name = 'main/index.html'
