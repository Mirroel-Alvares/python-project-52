from django import forms
from django_filters import (
    FilterSet,
    ModelChoiceFilter,
    BooleanFilter
)

from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['status'].queryset = Status.objects.all()
        self.fields['performer'].queryset = User.objects.filter(is_active=True)
        self.fields['labels'].queryset = Label.objects.all()

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.author = self.user
        instance.save()
        if 'labels' in self.cleaned_data:
            instance.labels.set(self.cleaned_data['labels'])
        return instance

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Имя"
        }),
        label="Имя"
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Описание",
        }),
        label="Описание"
    )
    status = forms.ModelChoiceField(
        queryset=Status.objects.none(),
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
        label="Статус"
    )
    performer = forms.ModelChoiceField(
        queryset=User.objects.none(),
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
        label="Исполнитель"
    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.none(),
        widget=forms.SelectMultiple(attrs={
            "class": "form-control",
        }),
        label="Метки",
        required=False,
    )

    class Meta:
        model = Task
        fields = [
            "name",
            "description",
            "status",
            "performer",
            "labels"
        ]


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    performer = ModelChoiceFilter(
        queryset=User.objects.filter(is_active=True),
        label='Исполнитель',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метка',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    self_tasks = BooleanFilter(
        method="filter_my_tasks",
        label="Только свои задачи",
        widget=forms.CheckboxInput(attrs={
        "class": "form-check-input",
        "style": "float: left; margin-right: 10px;"
        }),
    )

    def filter_my_tasks(self, queryset, name, value):
        if value and self.request:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'performer', 'labels']
