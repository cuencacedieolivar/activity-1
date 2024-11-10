from django.contrib import admin
from .models import Plant, PlantCategory, PlantCareLog, UserProfile, PlantObservation
class PlantCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the list view
    search_fields = ('name',)  # Allow search by name

# Plant model admin customization
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'category', 'description', 'care_instructions', 'image')
    search_fields = ('name', 'species', 'category__name')  # Allow search by name, species, and category name
    list_filter = ('category',)  # Filter by category
    prepopulated_fields = {'slug': ('name',)}  # Optional: Create slugs from names for URLs (if slug field exists)

# PlantCareLog model admin customization
class PlantCareLogAdmin(admin.ModelAdmin):
    list_display = ('plant', 'action', 'date', 'details')  # Display these fields in the list view
    list_filter = ('plant', 'action')  # Filter by plant and action (watering, fertilizing, etc.)
    search_fields = ('plant__name', 'action')  # Allow search by plant name and action

# UserProfile model admin customization
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture')  # Display user and their profile picture if available
    search_fields = ('user__username',)  # Allow search by username

# PlantObservation model admin customization
class PlantObservationAdmin(admin.ModelAdmin):
    list_display = ('plant', 'date', 'observation')  # Display plant, date, and observation
    search_fields = ('plant__name', 'observation')  # Allow search by plant name and observation details
    list_filter = ('date',)  # Filter by date of observation

# Register all models with the admin site
admin.site.register(PlantCategory, PlantCategoryAdmin)
admin.site.register(Plant, PlantAdmin)
admin.site.register(PlantCareLog, PlantCareLogAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(PlantObservation, PlantObservationAdmin)
