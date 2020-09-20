from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager

class ModelTests(TestCase,BaseUserManager):
    def test_create_user_with_email_successful(self):
        email="test@test.com"
        #password="Testpass123"
        password=self.make_random_password()
        print("password generated: "+password)
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email="test@TESTINGAPP.COM"
        user=get_user_model().objects.create_user(email,'testing123')
        self.assertEqual(user.email,email.lower())
