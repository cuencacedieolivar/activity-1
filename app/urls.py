from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('plant_dashboard/', views.plant_dashboard, name='plant_dashboard'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('add_watering_log/<int:plant_id>/', views.add_watering_log, name='add_watering_log'),
    path('add_fertilizing_log/<int:plant_id>/', views.add_fertilizing_log, name='add_fertilizing_log'),
    path('add_growth_log/<int:plant_id>/', views.add_growth_log, name='add_growth_log'),
    # Other URLs for authentication and other views
]
