from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    #
    def test_create_user_with_email_successful(self):
        # test creating a new user with an email is successful
        email = 'test@test.com'
        password = '1'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test email for a new user is normalized
        email = 'test@RRest.com'
        user = get_user_model().objects.create_user(email, '1')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            '1@123.com',
            '1'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
