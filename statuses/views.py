from django.views.generic import TemplateView


class StatusesIndexView(TemplateView):
    template_name = 'statuses/statuses_index.html'
