# from django.contrib.auth import get_user_model
# from .test_base import BaseUserTest
# from ..forms import CustomUserCreationForm, CustomUserUpdateForm
#
# User = get_user_model()
#
#
# class CustomUserCreationFormTest(BaseUserTest):
#     def test_form_has_correct_fields(self):
#         """Проверка наличия всех ожидаемых полей в форме"""
#         form = CustomUserCreationForm()
#         expected_fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'password1',
#             'password2'
#         ]
#         self.assertSequenceEqual(expected_fields, list(form.fields.keys()))
#
#     def test_form_field_classes_and_attributes(self):
#         """Проверка атрибутов и классов полей формы"""
#         form = CustomUserCreationForm()
#
#         self.assertEqual(
#             form.fields['first_name'].widget.attrs['class'],
#             'form-control'
#         )
#         self.assertEqual(
#             form.fields['first_name'].widget.attrs['placeholder'],
#             'Имя'
#         )
#
#         self.assertIn(
#             'Ваш пароль должен содержать как минимум 3 символа',
#             form.fields['password1'].help_text
#         )
#
#         self.assertEqual(
#             form.fields['password2'].help_text,
#             'Для подтверждения введите, пожалуйста, пароль ещё раз.'
#         )
#
#     def test_valid_form_with_fixture_data(self):
#         """Проверка валидности формы с данными из фикстур"""
#         form = CustomUserCreationForm(data={
#             'first_name': 'New',
#             'last_name': 'User',
#             'username': 'newuser',
#             'password1': 'Testpass123',
#             'password2': 'Testpass123'
#         })
#         self.assertTrue(form.is_valid())
#
#     def test_password_mismatch(self):
#         """Проверка несоответствия паролей"""
#         form = CustomUserCreationForm(data={
#             'first_name': 'New',
#             'last_name': 'User',
#             'username': 'newuser',
#             'password1': 'Testpass123',
#             'password2': 'Wrongpass123'
#         })
#         self.assertFalse(form.is_valid())
#         self.assertIn('password2', form.errors)
#
#     def test_username_uniqueness(self):
#         """Проверка уникальности имени пользователя"""
#         form = CustomUserCreationForm(data={
#             'first_name': 'Ivan',
#             'last_name': 'Ivanov',
#             'username': 'Ivashka',
#             'password1': 'Newpass123',
#             'password2': 'Newpass123'
#         })
#         self.assertFalse(form.is_valid())
#         self.assertIn('username', form.errors)
#
#     def test_username_validation(self):
#         """Проверка валидации имени пользователя"""
#         form = CustomUserCreationForm(data={
#             'first_name': 'Test',
#             'last_name': 'User',
#             'username': 'invalid username',
#             'password1': 'Testpass123',
#             'password2': 'Testpass123'
#         })
#         self.assertFalse(form.is_valid())
#         self.assertIn('username', form.errors)
#
#
# class CustomUserUpdateFormTest(BaseUserTest):
#     def test_form_inheritance(self):
#         """Проверка что форма обновления наследует все поля от формы создания"""
#         self.assertEqual(
#             set(CustomUserUpdateForm.Meta.fields),
#             set(CustomUserCreationForm.Meta.fields)
#         )
#
#     def test_update_existing_user(self):
#         """Проверка обновления существующего пользователя"""
#         form = CustomUserUpdateForm(data={
#             'first_name': 'Updated',
#             'last_name': 'Name',
#             'username': 'updated_username',
#             'password1': 'Newpass123',
#             'password2': 'Newpass123'
#         }, instance=self.user1)
#         self.assertTrue(form.is_valid())
#
#     def test_username_uniqueness_on_update(self):
#         """Проверка уникальности имени при обновлении"""
#         form = CustomUserUpdateForm(data={
#             'first_name': 'Ivan',
#             'last_name': 'Ivanov',
#             'username': 'Gray',
#             'password1': 'Newpass123',
#             'password2': 'Newpass123'
#         }, instance=self.user1)
#         self.assertFalse(form.is_valid())
#         self.assertEqual(
#             form.errors['username'],
#             ['Пользователь с таким именем уже существует']
#         )
#
#     def test_update_with_same_username(self):
#         """Проверка что пользователь может сохранить свой текущий username"""
#         form = CustomUserUpdateForm(data={
#             'first_name': 'Ivan',
#             'last_name': 'Ivanov',
#             'username': 'Ivashka',
#             'password1': 'Newpass123',
#             'password2': 'Newpass123'
#         }, instance=self.user1)
#         self.assertTrue(form.is_valid())