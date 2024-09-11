from .models import TravelEntry
from .forms import TravelEntryForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def add_travel_entry(request):
    if request.method == 'POST':
        form = TravelEntryForm(request.POST, request.FILES)
        if form.is_valid():
            travel_entry = form.save(commit=False)
            travel_entry.user = request.user
            travel_entry.save()
    else:
        form = TravelEntryForm()

    return render(request, 'add_travel_entry.html', {'form': form})


def view_travel_entries(request):
    travel_entries = TravelEntry.objects.all()
    return render(request, 'view_travel_entries.html', {'travel_entries': travel_entries})
