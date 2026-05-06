# apps/reservations/forms.py

from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'resident_name': forms.TextInput(attrs={'class': 'input'}),
            'area': forms.Select(attrs={'class': 'input'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'input'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'input'}),
            'status': forms.Select(attrs={'class': 'input'}),
        }