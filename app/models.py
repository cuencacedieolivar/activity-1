from django.db import models
from django.contrib.auth.models import User
from datetime import date

# User Profile Model to extend user information
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    favorite_plant = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Plant Model
class Plant(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_planted = models.DateField()
    growth_stage = models.CharField(max_length=100, choices=[
        ('Seedling', 'Seedling'),
        ('Young Plant', 'Young Plant'),
        ('Mature Plant', 'Mature Plant'),
        ('Flowering', 'Flowering'),
        ('Dormant', 'Dormant'),
    ])
    image = models.ImageField(upload_to='plants/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.user.username})'

    def days_since_planted(self):
        return (date.today() - self.date_planted).days

# Watering Log Model
class WateringLog(models.Model):
    plant = models.ForeignKey(Plant, related_name='waterings', on_delete=models.CASCADE)
    date_watered = models.DateField()
    amount = models.FloatField(help_text="Amount of water in liters")

    def __str__(self):
        return f'Watered {self.plant.name} on {self.date_watered}'

# Fertilizing Log Model
class FertilizingLog(models.Model):
    plant = models.ForeignKey(Plant, related_name='fertilizations', on_delete=models.CASCADE)
    date_fertilized = models.DateField()
    fertilizer_type = models.CharField(max_length=100)
    amount = models.FloatField(help_text="Amount of fertilizer used in grams")

    def __str__(self):
        return f'Fertilized {self.plant.name} on {self.date_fertilized}'

# Growth Log Model
class GrowthLog(models.Model):
    plant = models.ForeignKey(Plant, related_name='growth_logs', on_delete=models.CASCADE)
    date_logged = models.DateField()
    previous_growth_stage = models.CharField(max_length=100, choices=Plant._meta.get_field('growth_stage').choices)
    new_growth_stage = models.CharField(max_length=100, choices=Plant._meta.get_field('growth_stage').choices)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.plant.name} growth update on {self.date_logged}'
