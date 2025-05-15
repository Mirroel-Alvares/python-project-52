from django import forms
from .test_base import BaseStatusTest
from ..forms import StatusForm


class StatusFormTest(BaseStatusTest):
    def test_form_has_correct_fields_and_attrs(self):
        """Тестирование полей формы и их атрибутов"""
        form = StatusForm()

        # Проверка наличия поля
        self.assertIn('name', form.fields)

        # Проверка атрибутов поля
        field = form.fields['name']
        self.assertEqual(field.label, 'Имя')
        self.assertIsInstance(field.widget, forms.TextInput)
        self.assertEqual(field.widget.attrs['class'], 'form-control')
        self.assertEqual(field.widget.attrs['placeholder'], 'Имя')

    def test_form_validation(self):
        """Тестирование валидации формы"""
        # Валидные данные
        valid_data = {'name': 'Новый статус'}
        form = StatusForm(data=valid_data)
        self.assertTrue(form.is_valid())

        # Пустое имя
        invalid_data = {'name': ''}
        form = StatusForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

        # Слишком длинное имя
        long_name = {'name': 'а' * 101}
        form = StatusForm(data=long_name)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)

    def test_unique_name_validation(self):
        """Тестирование уникальности имени статуса"""
        form = StatusForm(data={'name': 'в космосе'})  # Используем существующее имя из фикстуры
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)