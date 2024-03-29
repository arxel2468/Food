from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.db import models
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import *

class RecipeAddForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None)
    class Meta:
        model = Recipe
        fields = ('title', 'category', 'ingredients', 'instructions', 'photo')
        
class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'category', 'ingredients', 'instructions', 'photo')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
    

class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
              

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Username"}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"First Name"}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Last Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Password"}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Confirm Password"}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")
        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data



class LoginForm(AuthenticationForm): 
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':"Comment..."}))
    class Meta:
        model = Review
        fields = ['comment']

    def save(self, commit=True):
        review = super().save(commit=False)
        if commit:
            review.save()
        return review
        