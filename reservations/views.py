from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservationForm
from .models import Reservation

def home(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    else:
        form = ReservationForm()
    return render(request, 'home.html', {'form': form})

def admin_dashboard(request):
    reservations = Reservation.objects.all()
    return render(request, 'admin_dashboard.html', {'reservations': reservations})

def cancel_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.status = 'cancelled'
    reservation.save()
    return redirect('admin_dashboard')
