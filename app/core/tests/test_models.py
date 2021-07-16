from unittest.mock import patch

from django.db import models
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@example.com', password='testpass'):
    """ Create a sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_emaill_successful(self):
        """ Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'Test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized"""
        email = 'test@Example.com'
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'Test@123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        # is_superuser và is_staff được quy định trong class PermissionsMixin của django.contrib.auth.models

    # Test recipe model
    def test_tag_str(self):
        """ test the tag string """
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )
        self.assertEqual(str(tag), tag.name)

    # Test ingredient model
    def test_ingredient_str(self):
        """ Test the ingredient string """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )
        self.assertEqual(str(ingredient), ingredient.name)

    # Test recipe model

    def test_recipe_str(self):
        """ Test the recipe string """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Banh xeo',
            time_minute=5,
            price=10000
        )
        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """ Test that image in saved in correct location """
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
