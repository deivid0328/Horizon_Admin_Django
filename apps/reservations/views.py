# apps/reservations/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.all().order_by('-created_at')
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_create(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_create.html', {'form': form})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_delete.html', {'reservation': reservation})