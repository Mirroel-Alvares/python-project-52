from django import forms
from .test_base import BaseLabelTest
from labels.forms import LabelForm


class LabelFormTest(BaseLabelTest):
    def test_form_fields_and_widgets(self):
        """Тестирование полей формы и виджетов"""
        form = LabelForm()
        self.assertIn('name', form.fields)
        field = form.fields['name']
        self.assertEqual(field.label, "Имя")
        self.assertIsInstance(field.widget, forms.TextInput)
        self.assertEqual(field.widget.attrs['class'], 'form-control')
        self.assertEqual(field.widget.attrs['placeholder'], 'Имя')

    def test_form_validation(self):
        """Тестирование валидации формы"""
        form = LabelForm(data={'name': 'новая метка'})
        self.assertTrue(form.is_valid())

        form = LabelForm(data={'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

        form = LabelForm(data={'name': 'a' * 101})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_unique_name_validation(self):
        """Тестирование уникальности имени в форме"""
        form = LabelForm(data={'name': 'local bug'})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)