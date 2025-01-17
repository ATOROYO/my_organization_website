from django.contrib import admin
from .models import ContactMessage
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(ContactMessage)
admin.site.register(CustomUser, UserAdmin)
