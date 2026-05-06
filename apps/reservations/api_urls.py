# apps/reservations/api_urls.py

from rest_framework.routers import DefaultRouter
from .api_views import ReservationViewSet

router = DefaultRouter()
router.register(r'reservations', ReservationViewSet, basename='reservations')

urlpatterns = router.urls