from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)
from labels.forms import LabelForm
from labels.models import Label
from main.mixins import AuthRequiredMixin, DeleteProtectionMixin


class LabelsIndexView(AuthRequiredMixin, ListView):
    model = Label
    template_name = 'labels/labels_index.html'
    context_object_name = "labels"


class LabelCreate(AuthRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = "main/form.html"
    success_url = reverse_lazy("labels:labels_index")
    extra_context = dict(
        page_title='Create label',
        title="Создать метку",
        button="Создать"
    )
    success_message = "Метка успешно создана"


class LabelUpdate(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "main/form.html"
    success_url = reverse_lazy("labels:labels_index")
    extra_context = dict(
        page_title='Update label',
        title="Изменение метки",
        button="Изменить"
    )
    success_message = "Метка успешно изменена"


class LabelDelete(AuthRequiredMixin, DeleteProtectionMixin,
                  SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "main/delete_form.html"
    success_url = reverse_lazy("labels:labels_index")
    extra_context = dict(
        page_title='Delete label',
        title="Удаление метки"
    )
    success_message = 'Метка успешно удалена'
    protected_message = 'Невозможно удалить метку, потому что она используется'
    protected_url = reverse_lazy("labels:labels_index")
