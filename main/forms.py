from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
        required=True,
        help_text='Username must be unique and cannot contain special characters.'  # Optional help text
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        required=True,
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        required=True,
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        required=True,
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another one.")
        return username

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match. Please try again.")
        return self

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name',
            'class': 'form-control',
        })
    )
    email = forms.EmailField(
        label='Your Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control',
        })
    )
    message = forms.CharField(
        label='Your Message',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Enter your message',
            'class': 'form-control',
        })
    )

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message.strip()) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.strip():
            raise forms.ValidationError("Name cannot be empty or contain only whitespace.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.strip():
            raise forms.ValidationError("Email cannot be empty or contain only whitespace.")
        return email