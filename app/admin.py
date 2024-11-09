from django.contrib import admin
from .models import UserProfile, Plant, WateringLog, FertilizingLog, GrowthLog

admin.site.register(UserProfile)
admin.site.register(Plant)
admin.site.register(WateringLog)
admin.site.register(FertilizingLog)
admin.site.register(GrowthLog)
