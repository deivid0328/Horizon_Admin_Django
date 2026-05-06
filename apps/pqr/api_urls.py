# apps/pqr/api_urls.py

from rest_framework.routers import DefaultRouter
from .api_views import PQRViewSet

router = DefaultRouter()
router.register(r'pqr', PQRViewSet, basename='pqr')

urlpatterns = router.urls