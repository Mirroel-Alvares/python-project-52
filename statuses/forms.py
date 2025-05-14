from django import forms
from .models import Status


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
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Имя"}
            )
        }
