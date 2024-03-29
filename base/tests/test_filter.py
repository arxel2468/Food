from django.test import TestCase
from django.urls import reverse
from django_filters.widgets import BooleanWidget

from base.models import *
from base.filters import *


class TestFilters(TestCase):
    
    def setUp(self):
        
        self.user = User.objects.create(username="testuser", email="test@gmail.com", password="secret")
        self.user1 = User.objects.create(username="testuser1", email="test1@gmail.com", password="secret1")
        
        self.category1 = Category.objects.create(name='Vegetarian')
        self.category2 = Category.objects.create(name='Non-Vegetarian')
        
        self.recipe1 = Recipe.objects.create(title="Vegetable Curry", category=self.category1, user=self.user)
        self.recipe2 = Recipe.objects.create(title="Beef Curry", category=self.category2, user=self.user)
        self.recipe3 = Recipe.objects.create(title="Vegetable Biryani", category=self.category1, user=self.user1)

    def test_filter_title(self):
        filter = RecipesFilter(data={'title':'curry'}, queryset = Recipe.objects.all()
        )
        
        self.assertEqual(len(filter.qs), 2)
        
    def test_filter_category(self):
        filter = RecipesFilter(data={'category': self.category2}, queryset = Category.objects.all()
        )
        
        self.assertEqual(len(filter.qs), 2)
        