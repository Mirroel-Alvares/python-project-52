from django.views.generic import TemplateView


class UsersIndexView(TemplateView):
    template_name = 'users/users_index.html'