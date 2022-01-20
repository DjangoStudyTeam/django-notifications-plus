from django_filters import rest_framework as filters
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet

from notifications_plus import get_notification_model, pagination
from notifications_plus.serializers import NotificationListSerializer

from .filters import NotificationFilter

NotificationModel = get_notification_model()


class NotificationViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.MyPageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = NotificationFilter
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        queryset = NotificationModel.objects.filter(recipient=user)
        return queryset

    def get_serializer_class(self):
        return NotificationListSerializer
