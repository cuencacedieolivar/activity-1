from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin page URL
    path('admin/', admin.site.urls),

    # Include URLs from your app (assuming your app is named 'plants')
    path('', include('app.urls')),  # Root URL includes the app's URLs (plants.urls)
]