from rest_framework.routers import SimpleRouter

from notifications_plus.viewsets import NotificationViewSet

router = SimpleRouter()
router.register("notifications", NotificationViewSet, basename="notifications")


urlpatterns = router.urls
