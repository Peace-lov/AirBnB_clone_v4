#!/usr/bin/python3
"""Module that tests for Class Review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Defines test Case for Clas Review"""

    def __init__(self, *args, **kwargs):
        """tests for args and kwargs"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """tests id for place"""
        alx = self.value()
        self.assertEqual(type(alx.place_id), str)

    def test_user_id(self):
        """test for usr id"""
        alx = self.value()
        self.assertEqual(type(alx.user_id), str)

    def test_text(self):
        """test for text"""
        alx = self.value()
        self.assertEqual(type(alx.text), str)

