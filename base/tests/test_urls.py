from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import *


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolves(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, index)
    
    def test_contact_url_is_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)
    
    def test_about_url_is_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)
    
    def test_register_url_is_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)
    
    def test_login_url_is_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_view)
    
    def test_logout_url_is_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)
    
    def test_profile_url_is_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_delete_review_url_is_resolves(self):
        url = reverse('delete_review', args=[2])
        self.assertEquals(resolve(url).func, delete_review)
    
    def test_recipes_url_is_resolves(self):
        url = reverse('recipes')
        self.assertEquals(resolve(url).func, recipes_list)
    
    def test_update_profile_url_is_resolves(self):
        url = reverse('update_profile')
        self.assertEquals(resolve(url).func, update_profile)
    
    def test_recipe_add_url_is_resolves(self):
        url = reverse('recipe_add')
        self.assertEquals(resolve(url).func, recipe_add)
    
    def test_recipe_url_is_resolves(self):
        url = reverse('recipe', args=[2])
        self.assertEquals(resolve(url).func, recipe)
    
    def test_recipe_edit_url_is_resolves(self):
        url = reverse('recipe_edit', args=[2])
        self.assertEquals(resolve(url).func, recipe_edit)