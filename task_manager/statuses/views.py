from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.main.mixins import AuthRequiredMixin, DeleteProtectionMixin


class StatusesIndexView(AuthRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses_index.html'
    context_object_name = "statuses"


class StatusCreate(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = "main/form.html"
    success_url = reverse_lazy("statuses:statuses_index")
    extra_context = dict(
        page_title='Create status',
        title="Создать статус",
        button="Создать"
    )
    success_message = "Статус успешно создан"


class StatusUpdate(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "main/form.html"
    success_url = reverse_lazy("statuses:statuses_index")
    extra_context = dict(
        page_title='Update status',
        title="Изменение статуса",
        button="Изменить"
    )
    success_message = "Статус успешно изменен"


class StatusDelete(AuthRequiredMixin, DeleteProtectionMixin,
                   SuccessMessageMixin, DeleteView):
    model = Status
    template_name = "main/delete_form.html"
    success_url = reverse_lazy("statuses:statuses_index")
    extra_context = dict(
        page_title='Delete status',
        title="Удаление статуса"
    )
    success_message = 'Статус успешно удален'
    protected_message = 'Невозможно удалить статус, потому что он используется'
    protected_url = reverse_lazy("statuses:statuses_index")
