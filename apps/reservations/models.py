# apps/reservations/models.py

from django.db import models

class Reservation(models.Model):
    AREA_CHOICES = [
        ('salon', 'Salón comunal'),
        ('pool', 'Piscina'),
        ('court', 'Cancha'),
        ('bbq', 'Zona BBQ'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('approved', 'Aprobada'),
        ('rejected', 'Rechazada'),
    ]

    resident_name = models.CharField(max_length=150)
    area = models.CharField(max_length=30, choices=AREA_CHOICES)
    reservation_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.resident_name} - {self.area}"