from rest_framework_extensions.routers import ExtendedSimpleRouter

from notifications_plus.viewsets import NotificationViewSet

router = ExtendedSimpleRouter()
router.register("notification", NotificationViewSet, basename="notification")


urlpatterns = router.urls + []
