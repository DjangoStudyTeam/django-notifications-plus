import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from notifications_plus.models import Notification


@pytest.mark.django_db
class TestNotificationViewSet:
    def setup_method(self, method):
        self.api_client = APIClient()
        self.user = User.objects.create_user(
            username="user", password="password", email="user@example.com"
        )
        self.other_user = User.objects.create_user(
            username="other_user", password="password", email="user2@example.com"
        )
        self.actor_user = User.objects.create_user(
            username="actor_user", password="password", email="user3@example.com"
        )
        self.list_url = reverse("notifications-list")
        self.notification_1 = Notification.objects.create(
            content="111", unread=True, recipient=self.user, actor=self.actor_user
        )
        self.notification_2 = Notification.objects.create(
            content="222", unread=True, recipient=self.other_user, actor=self.actor_user
        )
        self.notification_3 = Notification.objects.create(
            content="333", unread=True, recipient=self.user, actor=self.other_user
        )
        self.notification_4 = Notification.objects.create(
            content="444", unread=False, recipient=self.user, actor=self.actor_user
        )

    def test_list_permission(self):
        response = self.api_client.get(self.list_url)
        assert response.status_code == 401

    def test_list(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(self.list_url, data={"page": 1})
        assert len(response.data) == 3

    def test_list_filter_by_unread(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(self.list_url, data={"page": 1, "unread": True})
        assert len(response.data) == 2

    def test_list_order_by_created_at(self):
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(
            self.list_url, data={"page": 1, "ordering": "created_at"}
        )
        assert response.data[0]["created_at"] < response.data[1]["created_at"]
