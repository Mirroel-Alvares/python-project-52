from django.urls import reverse
from django.contrib.messages import get_messages
from .test_base import BaseUserTest
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersViewsTest(BaseUserTest):
    def test_users_index_view(self):
        """Тестирование списка пользователей"""
        response = self.client.get(reverse('users:users_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users_index.html')
        self.assertContains(response, 'Ivan Ivanov')
        self.assertContains(response, 'Gray')

    def test_user_create_view_get(self):
        """Тестирование GET-запроса для создания пользователя"""
        response = self.client.get(reverse('users:user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/form.html')
        self.assertContains(response, 'Регистрация')
        self.assertContains(response, 'form-control')  # Проверка CSS класса

    def test_user_create_view_post_success(self):
        """Тестирование успешного создания пользователя"""
        data = {
            'first_name': 'New',
            'last_name': 'User',
            'username': 'newuser',
            'password1': 'Complexpass123',
            'password2': 'Complexpass123'
        }
        response = self.client.post(reverse('users:user_create'), data)

        # Проверка редиректа
        self.assertRedirects(response, reverse('main:login'))

        # Проверка создания пользователя
        self.assertTrue(User.objects.filter(username='newuser').exists())

        # Проверка сообщения об успехе
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(
            messages[0]),
            "Пользователь успешно зарегистрирован"
        )

    def test_user_create_view_post_invalid(self):
        """Тестирование создания пользователя с невалидными данными"""
        data = {
            'first_name': '',  # Пустое имя
            'last_name': 'User',
            'username': 'Ivashka',  # Существующий username
            'password1': 'short',
            'password2': 'shorts'
        }
        response = self.client.post(reverse('users:user_create'), data)

        # Проверяем что форма не валидна и осталась на той же странице
        self.assertEqual(response.status_code, 200)

        # Получаем форму из контекста
        form = response.context['form']

        # Проверяем ошибки
        self.assertIn('first_name', form.errors)
        self.assertEqual(
            form.errors['first_name'],
            ['Обязательное поле.']
        )
        self.assertIn('username', form.errors)
        self.assertEqual(
            form.errors['username'],
            ['Пользователь с таким именем уже существует.']
        )
        self.assertIn('password2', form.errors)

    def test_user_update_view_owner(self):
        """Тестирование обновления пользователя владельцем"""
        self.user1.set_password('IvIva27')
        self.user1.save()

        login_success = self.client.login(
            username='Ivashka', password='IvIva27'
        )
        self.assertTrue(login_success)

        response = self.client.get(
            reverse('users:user_update', kwargs={'pk': self.user1.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Изменение пользователя')

    def test_user_update_view_post(self):
        """Тестирование POST-запроса для обновления пользователя"""
        self.user1.set_password('IvIva27')
        self.user1.save()

        login_success = self.client.login(
            username='Ivashka', password='IvIva27'
        )
        self.assertTrue(
            login_success,
            "Не удалось войти как пользователь. Проверьте username и password"
        )

        update_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'username': 'updated_username',
            'password1': 'Newpass123',
            'password2': 'Newpass123'
        }

        response = self.client.post(
            reverse('users:user_update', kwargs={'pk': self.user1.pk}),
            data=update_data,
            follow=True
        )

        self.assertRedirects(
            response,
            reverse('users:users_index'),
            msg_prefix="Неправильный редирект после обновления"
        )

        updated_user = User.objects.get(pk=self.user1.pk)

        self.assertEqual(
            updated_user.first_name,
            'Updated',
            "Имя пользователя не обновилось"
        )
        self.assertEqual(
            updated_user.username,
            'updated_username',
            "Username не обновился"
        )
        self.assertTrue(
            updated_user.check_password('Newpass123'),
            "Пароль не изменился"
        )

    def test_user_update_view_not_owner(self):
        """Тестирование попытки обновления чужого пользователя"""
        self.user1.set_password('IvIva27')
        self.user1.save()
        self.client.login(username='Ivashka', password='IvIva27')
        response = self.client.get(
            reverse('users:user_update', kwargs={'pk': self.user2.pk})
        )
        self.assertRedirects(response, reverse('users:users_index'))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'У вас нет прав для изменения другого пользователя.'
        )
