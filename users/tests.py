from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from .models import CustomUser

# Create your tests here.
class UserTests(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
        self.client = Client()

    def test_string_representation(self):
        user = CustomUser(
            username="test",
            email="testuser@email.com",
            password="secret"
        )
        self.assertEqual(str(user), user.username)

    def test_user_content(self):
        self.assertEqual(f"{self.user.username}", "testuser")
        self.assertEqual(f"{self.user.email}", "test@email.com")

    