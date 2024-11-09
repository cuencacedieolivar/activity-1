from django import forms
from .models import WateringLog, FertilizingLog, GrowthLog, Plant

class WateringLogForm(forms.ModelForm):
    class Meta:
        model = WateringLog
        fields = ['plant', 'date_watered', 'amount']

class FertilizingLogForm(forms.ModelForm):
    class Meta:
        model = FertilizingLog
        fields = ['plant', 'date_fertilized', 'fertilizer_type', 'amount']

class GrowthLogForm(forms.ModelForm):
    class Meta:
        model = GrowthLog
        fields = ['plant', 'date_logged', 'previous_growth_stage', 'new_growth_stage', 'notes']
