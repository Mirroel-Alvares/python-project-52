from django import forms
from django_filters import (
    FilterSet,
    ModelChoiceFilter,
    BooleanFilter
)

from tasks.models import Task
from labels.models import Label
from statuses.models import Status
from users.models import User


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['status'].queryset = Status.objects.all()
        self.fields['performer'].queryset = User.objects.filter(is_active=True)
        self.fields['labels'].queryset = Label.objects.all()

        if user:
            self.instance.author = user

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
            #"rows": 3 проверить с ним и без него. и с вариациями
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
        widget=forms.CheckboxSelectMultiple(attrs={   #widget=forms.SelectMultiple(attrs={ проверить варианты.
            "class": "form-select",
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
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mr-3"}),
    )

    def filter_my_tasks(self, queryset, name, value):
        if value and self.request:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'performer', 'labels']
