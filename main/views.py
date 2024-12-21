from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
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
    return render(request, 'main/contact.html')

def search_results(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'main/search_results.html', {'results': results})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
