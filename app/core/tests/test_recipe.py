"""
Test for Recipe Model
"""

from decimal import Decimal
from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import Recipe

class RecipeTests(TestCase):
    """Test models """

    def test_create_recipe(self):
        """Test creating a recipe is successful"""

        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='12345',
        )
        recipe = Recipe.objects.create(
            user=user,
            title="Sample Recipe",
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description',
            link="www.somelink.com"
        )

        self.assertEqual(str(recipe), recipe.title)