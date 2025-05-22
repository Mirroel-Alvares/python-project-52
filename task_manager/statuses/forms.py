from django import forms
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя'
        }),
        label="Имя"
        )

    class Meta:
        model = Status
        fields = ['name']
