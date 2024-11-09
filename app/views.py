from django.shortcuts import render

# Existing views for plant-related functionality

def home(request):
    return render(request, 'plants/home.html')

def about(request):
    return render(request, 'plants/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Here you can process the contact form, e.g., send an email or save to the database
        # For now, we'll just render a thank you message
        return render(request, 'plants/contact.html', {'message': 'Thank you for contacting us!'})
    return render(request, 'plants/contact.html')
