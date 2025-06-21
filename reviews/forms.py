from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
