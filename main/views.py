from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings # Import settings
from .forms import ContactForm, RegistrationForm
from .models import TeamMember, GalleryImage, Post

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def team(request):
    members = TeamMember.objects.all()
    return render(request, 'main/team.html', {'members': members})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'main/gallery.html', {'images': images})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Try to send an email
        try:
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email='your_email@example.com',  # Replace with your email
                recipient_list=['recipient@example.com'],  # Replace with recipient's email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'An error occurred while sending your message. Please try again later.')

    return render(request, 'contact.html')

def search_results(request):
    query = request.GET.get('q')
    results = [
        {'title': 'Example Result 1', 'description': 'Description of result 1.', 'url': '#'},
        {'title': 'Example Result 2', 'description': 'Description of result 2.', 'url': '#'},
        # Add your actual results here
    ] if query else []
    return render(request, 'main/search_results.html', {'query': query, 'results': results})

