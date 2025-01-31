# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('services/', views.services, name='services'),
#     path('team/', views.team, name='team'),
#     path('gallery/', views.gallery, name='gallery'),
#     path('contact/', views.contact, name='contact'),
#     path('search/', views.search_results, name='search_results'),
#     path('register/', views.register, name='register'),
#     path('login/', views.login_view, name='login'),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('users/', include('users.urls')),
    path('services/', include('services.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
