from django.urls import path
from . import views

urlpatterns = [
    # List of all plants
    path('plants/', views.PlantListView.as_view(), name='plant_list'),

    # Detailed view of a single plant
    path('plants/<int:pk>/', views.PlantDetailView.as_view(), name='plant_detail'),

    # Log care activities for a specific plant
    path('plants/<int:pk>/care_log/', views.PlantCareLogCreateView.as_view(), name='care_log_create'),

    # Admin Plant List
    path('admin/plants/', views.PlantListView.as_view(), name='admin_plant_list'),

    # Create a new plant
    path('admin/plants/new/', views.CreateView.as_view(), name='plant_create'),

    # Update an existing plant
    path('admin/plants/<int:pk>/edit/', views.PlantUpdateView.as_view(), name='plant_update'),

    # Delete a plant
    path('admin/plants/<int:pk>/delete/', views.PlantDeleteView.as_view(), name='plant_delete'),

]
