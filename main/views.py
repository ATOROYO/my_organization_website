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

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    'Contact Form Submission', #Subject
                    f'Name: {name}\nEmail: {email}\nMessage: {message}', #Message
                    settings.EMAIL_HOST_USER, #From
                    [settings.EMAIL_HOST_USER], #To (You could use a different email here)
                    fail_silently=False,
                )
                return redirect('success') # Redirect to a success page
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(request, 'contact.html', {'form': form, 'error_message': 'There was an error sending your message. Please try again later.'})

        else:
            # Form is invalid, re-render with error messages
            return render(request, 'main/contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})

# def success(request):
#     return render(request, 'success.html') # Render a success page

def search_results(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'main/search_results.html', {'results': results})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database (handle password hashing etc.)
            user = form.save()
            # You can add logic for sending a welcome email or redirecting to a success page
            messages.success(request, 'You have registered successfully!')
            return redirect('login')  # Redirect to login page after successful registration
        else:
            # Form is invalid, re-render with error messages
            return render(request, 'main/register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in successfully.')
            return redirect('home')  # Redirect to the home page or dashboard
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')
    
    return render(request, 'main/login.html')

def search_results(request):
    query = request.GET.get('q')
    results = [
        {'title': 'Example Result 1', 'description': 'Description of result 1.', 'url': '#'},
        {'title': 'Example Result 2', 'description': 'Description of result 2.', 'url': '#'},
        # Add your actual results here
    ] if query else []
    return render(request, 'main/search_results.html', {'query': query, 'results': results})

