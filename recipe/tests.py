from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Desserts")
        self.assertEqual(str(self.category), "Desserts")
    
    def test_category_iteration(self):
        category_iter = list(iter(self.category))
        self.assertEqual(category_iter, ["Desserts"])

class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Delicious chocolate cake",
            instructions="Mix ingredients and bake",
            ingredients="Flour, sugar, cocoa powder, eggs, butter",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "Chocolate Cake")
        self.assertEqual(self.recipe.description, "Delicious chocolate cake")
        self.assertEqual(self.recipe.instructions, "Mix ingredients and bake")
        self.assertEqual(self.recipe.ingredients, "Flour, sugar, cocoa powder, eggs, butter")
        self.assertEqual(self.recipe.category, self.category)
        self.assertEqual(str(self.recipe), "Chocolate Cake")
    
    def test_recipe_category_relationship(self):
        recipes_in_category = self.category.recipe_set.all()
        self.assertIn(self.recipe, recipes_in_category)