from django_filters import rest_framework as filters

from notifications_plus import get_notification_model

NotificationModel = get_notification_model()


class NotificationFilter(filters.FilterSet):
    flag = filters.CharFilter(field_name="flag")

    class Meta:
        model = NotificationModel
        fields = ["flag"]
