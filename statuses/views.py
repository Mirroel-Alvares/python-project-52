from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from statuses.forms import StatusForm
from statuses.models import Status
from main.mixins import AuthRequiredMixin


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


class StatusDelete(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = "main/delete_form.html"
    success_url = reverse_lazy("users:users_index")
    extra_context = dict(
        page_title='Delete status',
        title="Удаление статуса"
    )
    success_message = 'Статус успешно удален'

    # def delete(self, request, *args, **kwargs):
    #     status = self.get_object()
    #     if Task.objects.filter(status=status).exists():
    #         messages.error(request, 'Невозможно удалить статус, так как он связан с одной или несколькими задачами.')
    #         return redirect(self.success_url)
    #     return super().delete(request, *args, **kwargs)
