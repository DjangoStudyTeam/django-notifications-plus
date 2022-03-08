from rest_framework.routers import SimpleRouter

from notifications_plus.viewsets import NotificationViewSet

router = SimpleRouter()
router.register("notifications", NotificationViewSet, basename="notification")


urlpatterns = router.urls
