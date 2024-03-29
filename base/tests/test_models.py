from django.test import TestCase
from base.models import *



class TestModels(TestCase):
    
    def setUp(self):
        
        self.user = User.objects.create(
            username= "testuser",
            email='test@gmail.com',
            password="secret"
        )
        
        self.category = Category.objects.create(
            name = 'Sweet',
        )        
        
        self.recipe = Recipe.objects.create(
            title= 'Test',
            user= self.user,
            category= self.category,
            ingredients="""test ingredients""",
            instructions="""test instructions""",
        )

        
        self.review = Review.objects.create(
            user = self.user,
            recipe = self.recipe,
            comment = 'test review',
            rating=3
        )

    def test_recipe_str(self):
        self.assertEqual(str(self.recipe), 'Test')
        
    def test_recipe_title(self):
        self.assertEqual(self.recipe.title, 'Test')
        
    def test_recipe_ingredients(self):
        self.assertEqual(self.recipe.ingredients, 'test ingredients')
        
    def test_recipe_instructions(self):
        self.assertEqual(self.recipe.instructions, 'test instructions')
        
    def test_recipe_category(self):
        self.assertEqual(self.recipe.category.name, 'Sweet')