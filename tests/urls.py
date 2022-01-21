from notifications_plus.viewsets import NotificationViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register("notifications", NotificationViewSet, basename="notifications")


urlpatterns = router.urls
