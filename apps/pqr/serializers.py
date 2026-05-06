# apps/pqr/serializers.py

from rest_framework import serializers
from .models import PQR

class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR
        fields = '__all__'