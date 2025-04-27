from django.views.generic import TemplateView


class TasksIndexView(TemplateView):
    template_name = 'tasks/tasks_index.html'
