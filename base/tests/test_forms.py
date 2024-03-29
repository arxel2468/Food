from django.test import TestCase
from base.forms import *


class TestForms(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@gmail.com', password='secret')
        self.category1 = Category.objects.create(name='Spicy')
        self.category2 = Category.objects.create(name='Sweet')
    
    def test_registration_form_valid_data(self):
        form = RegistrationForm(data={
            'username': 'testuser',
            'first_name': 'test',
            'last_name': 'name',
            'email': 'test@gmail.com',
            'password': 'secret',
            'password_confirmation': 'secret',
        })
        
        self.assertTrue(form.is_valid())
        
    def test_registration_form_no_data(self):
        form = RegistrationForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)
    
    def test_contact_form_valid_data(self):
        form = ContactForm(data={
            'name': 'testuser',
            'email': 'test@gmail.com',
            'subject': 'Hello, this is a test',
            'message': 'Test Message',
        })
        
        self.assertTrue(form.is_valid())
        
    def test_contact_form_no_data(self):
        form = ContactForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
    
    def test_update_profile_form_valid_data(self):
        self.user = User.objects.create(username='testu', email='test@gmail.com', password='secret')
        form = UpdateProfileForm(data={
            'username': 'testuser1',
            'email': 'test1@gmail.com',
            'password': 'secret',
        })
        
        self.assertTrue(form.is_valid())
        
    def test_update_profile_form_no_data(self):
        form = UpdateProfileForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
    
    
    def test_review_form_valid_data(self):
        form = ReviewForm(data={
            'comment': 'test review'
        })
        
        self.assertTrue(form.is_valid())
        
    def test_review_form_no_data(self):
        form = ReviewForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)