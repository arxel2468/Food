from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.db import models
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    ingredients = models.TextField()
    instructions = models.TextField()
    photo = models.ImageField(upload_to='recipes/')
    slug = models.SlugField(null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title)
        
            has_slug = Recipe.objects.filter(slug=slug).exists()
            count = 1
            
            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)
                has_slug = Recipe.objects.filter(slug=slug).exists()
                
            self.slug = slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return self.comment

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name