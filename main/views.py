# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.core.mail import send_mail
# from django.conf import settings # Import settings
# from .forms import ContactForm, RegistrationForm
# from .models import TeamMember, GalleryImage, Post

# def home(request):
#     return render(request, 'main/home.html')

# def about(request):
#     return render(request, 'main/about.html')

# def services(request):
#     return render(request, 'main/services.html')

# def team(request):
#     members = TeamMember.objects.all()
#     return render(request, 'main/team.html', {'members': members})

# def gallery(request):
#     images = GalleryImage.objects.all()
#     return render(request, 'main/gallery.html', {'images': images})

# from django.shortcuts import render
# from django.core.mail import send_mail
# from django.contrib import messages
# from .forms import ContactForm

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
            
#             try:
#                 send_mail(
#                     subject=f"Contact Form Submission from {name}",
#                     message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
#                     from_email='davidatoroyosika@gmail.com',  # Replace with your email
#                     recipient_list=['sharonlove'],  # Replace with recipient's email
#                     fail_silently=False,
#                 )
#                 messages.success(request, 'Your message has been sent successfully!')
#             except Exception as e:
#                 messages.error(request, 'An error occurred while sending your message. Please try again later.')
#         else:
#             messages.error(request, 'Please correct the errors in the form.')
#     else:
#         form = ContactForm()

#     return render(request, 'main/contact.html', {'form': form})


# def search_results(request):
#     query = request.GET.get('q')
#     results = [
#         {'title': 'Example Result 1', 'description': 'Description of result 1.', 'url': '#'},
#         {'title': 'Example Result 2', 'description': 'Description of result 2.', 'url': '#'},
#         # Add your actual results here
#     ] if query else []
#     return render(request, 'main/search_results.html', {'query': query, 'results': results})

#################################
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import ContactMessage  # Assuming you have a model for contact form messages
from .models import TeamMember, GalleryImage, Post

# def home(request):
#     return render(request, 'main/home.html')

# def about(request):
#     return render(request, 'main/about.html')

# def services(request):
#     return render(request, 'main/services.html')

# def team(request):
#     members = TeamMember.objects.all()
#     return render(request, 'main/team.html', {'members': members})

# def gallery(request):
#     images = GalleryImage.objects.all()
#     return render(request, 'main/gallery.html', {'images': images})

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, "Username already exists.")
#             elif User.objects.filter(email=email).exists():
#                 messages.error(request, "Email already registered.")
#             else:
#                 User.objects.create_user(username=username, email=email, password=password1)
#                 messages.success(request, "Account created successfully. Please log in.")
#                 return redirect('login')
#         else:
#             messages.error(request, "Passwords do not match.")
#     return render(request, 'main/register.html')

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Logged in successfully!")
#             return redirect('home')  # Redirect to your homepage
#         else:
#             messages.error(request, "Invalid username or password.")
#     return render(request, 'main/login.html')

# def logout_view(request):
#     logout(request)
#     messages.success(request, "Logged out successfully.")
#     return redirect('main/login')

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         ContactMessage.objects.create(name=name, email=email, message=message)
#         messages.success(request, "Message sent successfully.")
#         return redirect('contact')
#     return render(request, 'main/contact.html')

# def search_results(request):
#     query = request.GET.get('q')
#     results = [
#         {'title': 'Example Result 1', 'description': 'Description of result 1.', 'url': '#'},
#         {'title': 'Example Result 2', 'description': 'Description of result 2.', 'url': '#'},
#         # Add your actual results here
#     ] if query else []
#     return render(request, 'main/search_results.html', {'query': query, 'results': results})

from django.shortcuts import render
from .models import Service, TeamMember, GalleryItem, ContactMessage
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    services = Service.objects.all()[:3]
    team_members = TeamMember.objects.filter(is_active=True)[:3]
    gallery_items = GalleryItem.objects.filter(is_featured=True)[:6]
    
    context = {
        'services': services,
        'team_members': team_members,
        'gallery_items': gallery_items,
    }
    return render(request, 'main/home.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            
            # Send email
            send_mail(
                'New Contact Form Submission',
                f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def search_view(request):
    query = request.GET.get('q', '')
    results = []
    
    if query:
        # Search across multiple models
        services = Service.objects.filter(title__icontains=query)
        team = TeamMember.objects.filter(name__icontains=query)
        gallery = GalleryItem.objects.filter(title__icontains=query)
        
        results = list(services) + list(team) + list(gallery)
    
    context = {
        'results': results,
        'query': query,
        'results_count': len(results)
    }
    return render(request, 'main/search_results.html', context)
