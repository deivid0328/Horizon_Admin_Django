# apps/pqr/api_views.py

from rest_framework import viewsets
from .models import PQR
from .serializers import PQRSerializer

class PQRViewSet(viewsets.ModelViewSet):
    queryset = PQR.objects.all().order_by('-created_at')
    serializer_class = PQRSerializer