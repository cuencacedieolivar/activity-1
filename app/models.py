from django.db import models
from django.contrib.auth.models import User


# Plant categories to classify plant types
class PlantCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Represents a plant with essential details
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    category = models.ForeignKey(PlantCategory, on_delete=models.CASCADE, related_name='plants')
    description = models.TextField()
    care_instructions = models.TextField()  # an  instruction and info like watering
    image = models.ImageField(upload_to='plants/')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


# plant care log, activities for a specific plant
class PlantCareLog(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='care_logs')
    date = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)  # Example: Watering, Fertilizing, etc.
    details = models.TextField()  # Additional notes or details

    def __str__(self):
        return f"{self.action} on {self.date.strftime('%Y-%m-%d')}"


# User profile to track personal plant collection (optional)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plants = models.ManyToManyField(Plant, related_name='owners')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


# Observations for plant progress like health condition)
class PlantObservation(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='observations')
    date = models.DateTimeField(auto_now_add=True)
    observation = models.TextField()  # Notes on the plant's condition or growth

    def __str__(self):
        return f"Observation on {self.plant.name} on {self.date.strftime('%Y-%m-%d')}"
