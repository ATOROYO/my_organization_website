from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('MEMBER', 'Member'),
        ('STAFF', 'Staff'),
        ('ADMIN', 'Admin'),
    )
    
    role = models.CharField(max_length=10, choices=ROLES, default='MEMBER')
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    email_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

    def is_staff_member(self):
        return self.role in ['STAFF', 'ADMIN']