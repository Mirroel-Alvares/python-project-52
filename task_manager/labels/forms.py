from django import forms
from task_manager.labels.models import Label


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Имя'
        }),
        label="Имя"
        )

    class Meta:
        model = Label
        fields = ['name']
