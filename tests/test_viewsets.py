import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from notifications_plus.models import Notification


@pytest.mark.django_db
class TestNotificationViewSet:
    def setup(self):
        self.api_client = APIClient()
        self.user = User.objects.create_user(
            username="user", password="password", email="user@example.com"
        )
        self.list_url = reverse("notifications-list")

    def create_notifications(self):
        instance = Notification.objects.create(
            content="111", unread=False, recipient=self.user, actor=self.user
        )
        instance.save()

    def test_list_permission(self):
        response = self.api_client.post(self.list_url)
        assert response.status_code == 401

    def test_list_notifications(self):
        self.create_notifications()
        self.api_client.force_authenticate(user=self.user)
        response = self.api_client.get(self.list_url, data={"page": 1})
        assert len(response.data) == 1
