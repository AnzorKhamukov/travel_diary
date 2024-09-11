from django import forms
from .models import TravelEntry
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']


class TravelEntryForm(forms.ModelForm):
    class Meta:
        model = TravelEntry
        fields = ['location', 'image', 'cost', 'heritage_sites', 'places_to_visit', 'rating']
