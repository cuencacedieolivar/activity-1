from django.urls import path
from .views import HomePageView, AboutPageView, ProjectPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('project/', ProjectPageView.as_view(), name='project'),
    path('contact/', ContactPageView.as_view(), name='contact')
]