from django.contrib.auth.models import User
from test_plus.test import APITestCase

from .factories import NotificationFactory


class NotificationViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create_user(
            username="user1", password="password", email="user1@example.com"
        )
        self.user2 = User.objects.create_user(
            username="user2", password="password", email="user2@example.com"
        )

    def test_notification(self):
        NotificationFactory.create_batch(5)
        self.login(username=self.user1.username, password="password")
        response = self.get("notification-list")
        print(response.data)
