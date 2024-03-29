from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView
from .models import *
from .forms import *

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout, name="logout"),
    
    path("profile/", views.profile, name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("profile/delete_review/<int:pk>/", views.delete_review, name="delete_review"),
    
    path("recipes/", views.recipes_list, name="recipes"),
    path("recipes/<slug:slug>/", views.recipe, name="recipe"),
    path("recipe/add/", views.recipe_add, name="recipe_add"),
    path("recipes/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    path("recipes/<slug:slug>/delete/", views.recipe_delete, name="recipe_delete"),
    
    # path("recipes/<int:pk>/", views.recipe, name="recipe"),
    # path("recipes/<int:pk>/edit/", views.recipe_edit, name="recipe_edit"),
    # path("recipes/<int:pk>/delete/", views.recipe_delete, name="recipe_delete"),
]

