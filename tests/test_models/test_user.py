#!/usr/bin/python3
"""Module that Defines the Class User """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Defines Test Case for USer """

    def __init__(self, *args, **kwargs):
        """Test args and kwargs"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test User first name """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Tests the users last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """TEst the users email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test the useers password """
        new = self.value()
        self.assertEqual(type(new.password), str)
