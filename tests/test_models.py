from notifications_plus import get_notification_model

NotificationModel = get_notification_model()


class TestNotification:
    def test___str__(self, admin_user):
        notification = NotificationModel.objects.create(
            content="test content",
            actor=admin_user,
            recipient=admin_user,
        )
        assert str(notification) == "admin's notification: test content..."

        notification = NotificationModel(
            content="a" * 100,
            actor=admin_user,
            recipient=admin_user,
        )
        notification.save()
        truncated = "a" * 50
        assert str(notification) == f"admin's notification: {truncated}..."

    def test_save(self, admin_user):
        notification = NotificationModel.objects.create(
            content="test content",
            actor=admin_user,
            recipient=admin_user,
        )
        notification.save()
        assert notification.created_at is not None
        assert NotificationModel.objects.get(pk=notification.pk).created_at is not None
