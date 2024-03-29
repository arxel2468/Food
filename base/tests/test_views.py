from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from base.models import *
from django.contrib.auth.models import User
import json

class TestViews(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        
        
    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        
    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        # self.assertTemplateUsed(response, 'register.html')
        
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        # self.assertTemplateUsed(response, 'login.html')
        
    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        
    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        # self.assertRedirects(response, reverse('login'))
        
    
        