from rest_framework.routers import DefaultRouter
from .views import PQRViewSet

router = DefaultRouter()

router.register(r'pqr', PQRViewSet)

urlpatterns = router.urls