from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search_results, name='search_results'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # path('search/', views.search, name='search'),
]
