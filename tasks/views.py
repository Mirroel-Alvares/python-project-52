from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django_filters.views import FilterView

from tasks.forms import TaskForm, TaskFilter
from tasks.models import Task
from main.mixins import AuthRequiredMixin, OwnerRequiredMixin


class TasksIndexView(AuthRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/tasks_index.html'
    context_object_name = "tasks"
    filterset_class = TaskFilter

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if not self.request.user.is_superuser:
    #         queryset = queryset.filter(author=self.request.user)
    #     return queryset.select_related(
    #         'status', 'performer', 'author'
    #     ).prefetch_related('labels_name')


class TaskCreate(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "main/form.html"
    success_url = reverse_lazy("tasks:tasks_index")
    extra_context = dict(
        page_title='Create task',
        title="Создать задачу",
        button="Создать"
    )
    success_message = "Задача успешно создана"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TaskUpdate(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "main/form.html"
    success_url = reverse_lazy("tasks:tasks_index")
    extra_context = dict(
        page_title='Update task',
        title="Изменение задачи",
        button="Изменить"
    )
    success_message = "Статус успешно изменен"


class TaskDelete(AuthRequiredMixin, OwnerRequiredMixin,
                 SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("tasks:tasks_index")
    extra_context = dict(
        page_title='Delete task',
        title="Удаление задачи"
    )
    success_message = 'Задача успешно удалена'
    permission_message = 'Задачу может удалить только ее автор'
    permission_url = reverse_lazy("tasks:tasks_index")


class TaskDetails(DetailView):
    model = Task
    template_name = "tasks/task_details.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('labels')
