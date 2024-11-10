from django import forms
from .models import PlantCareLog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlantCareLogForm(forms.ModelForm):
    class Meta:
        model = PlantCareLog
        fields = ['action', 'details']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
