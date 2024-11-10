from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Plant, PlantCareLog
from .forms import PlantCareLogForm, CustomUserCreationForm  # Ensure your form is correctly imported
from django.contrib.auth.models import User

# Login view for custom user login
class CustomLoginView(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True

# Register view for new users
class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm  # Use your custom form
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

# Logout view for users
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout

# Home page view
class HomePageView(TemplateView):
    template_name = 'app/home.html'  # Create this template to display products

# Plant list view (for displaying all plants)
class PlantListView(ListView):
    model = Plant
    template_name = 'app/plant_list.html'
    context_object_name = 'plants'

# Plant detail view (for viewing a specific plant)
class PlantDetailView(DetailView):
    model = Plant
    template_name = 'app/plant_detail.html'
    context_object_name = 'plant'

# Create a new plant care log entry
class PlantCareLogCreateView(LoginRequiredMixin, CreateView):
    model = PlantCareLog
    form_class = PlantCareLogForm
    template_name = 'app/care_log_form.html'

    def form_valid(self, form):
        form.instance.plant = get_object_or_404(Plant, pk=self.kwargs['pk'])
        form.save()
        return redirect('plant_detail', pk=self.kwargs['pk'])

# For editing a plant (you need this view if you want users to update plants)
class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['name', 'description', 'category', 'stock', 'price']
    template_name = 'app/plant_form.html'
    success_url = reverse_lazy('plant_list')

# For deleting a plant (you need this view if you want users to delete plants)
class PlantDeleteView(LoginRequiredMixin, DeleteView):
    model = Plant
    template_name = 'app/plant_confirm_delete.html'
    success_url = reverse_lazy('plant_list')
