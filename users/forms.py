from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Имя"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Фамилия"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name') + UserCreationForm.Meta.fields


# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.Select(attrs={'class': 'form-select'}),
#         }
#         labels = {
#             'title': 'Название книги',
#         }
#         help_texts = {
#             'author': 'Выберите автора из списка',
#         }