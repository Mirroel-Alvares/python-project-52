from .test_base import BaseUserTest
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(BaseUserTest):
    def test_fixture_users_loaded(self):
        """Проверка, что пользователи из фикстур загружены корректно"""
        self.assertEqual(self.user1.get_full_name(), 'Ivan Ivanov')
        self.assertEqual(self.user2.get_full_name(), '')
        self.assertEqual(self.user3.get_full_name(), 'Anonim nim')

        self.assertEqual(str(self.user1), 'Ivan Ivanov')
        self.assertTrue(str(self.user2) in ['Gray', ''])
        self.assertEqual(str(self.user3), 'Anonim nim')

    def test_user_creation(self):
        """Тестирование создания новых пользователей"""
        # Создаем нового пользователя
        new_user = User.objects.create_user(
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"],
            username=self.user_data["username"],
            password=self.user_data["password1"],
        )

        # Проверяем, что пользователь создан
        self.assertEqual(User.objects.count(), 4)  # 3 из фикстур + 1 новый
        self.assertEqual(new_user.get_full_name(), 'New User')
        self.assertEqual(str(new_user), 'New User')

        # Проверяем, что пароль хешируется
        self.assertNotEqual(new_user.password, 'testpass123')
        self.assertTrue(new_user.check_password('testpass123'))

        # Проверяем создание пользователя без имени
        user_no_name = User.objects.create_user(
            username='noname',
            password='testpass123'
        )
        self.assertEqual(user_no_name.get_full_name(), '')
        self.assertEqual(str(user_no_name), 'noname')

    def test_meta_options(self):
        """Тестирование мета-опций модели"""
        self.assertEqual(User._meta.db_table, 'users')
        self.assertEqual(User._meta.verbose_name, 'пользователь')
        self.assertEqual(User._meta.verbose_name_plural, 'пользователи')

    def test_empty_username_handling(self):
        """Тестирование обработки пустого username"""
        # Проверка что пользователь с пустым username был создан
        self.assertEqual(self.user3.username, '')

        # Проверка что нельзя создать нового пользователя с пустым username
        with self.assertRaises(ValueError):
            User.objects.create_user(
                username='',
                password='testpass'
            )

    def test_password_handling(self):
        """Тестирование работы с паролями"""
        self.assertFalse(self.user1.check_password('wrong_password'))
        self.assertFalse(self.user2.check_password(''))

    def test_superuser_creation(self):
        """Тестирование создания суперпользователя"""
        superuser = User.objects.create_superuser(
            username='admin',
            password='adminpass',
            first_name='Admin',
            last_name='User'
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)