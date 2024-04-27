#!/usr/bin/python3
"""Module that deines test for Class Place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Defines  test case for Place """

    def __init__(self, *args, **kwargs):
        """Test *args and **kwargs """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Test id """
        alx = self.value()
        self.assertEqual(type(alx.city_id), str)

    def test_user_id(self):
        """ Test user id"""
        alx = self.value()
        self.assertEqual(type(alx.user_id), str)

    def test_name(self):
        """Test the str for name """
        alx = self.value()
        self.assertEqual(type(alx.name), str)

    def test_description(self):
        """Test description """
        alx = self.value()
        self.assertEqual(type(alx.description), str)

    def test_number_rooms(self):
        """Test room number """
        alx = self.value()
        self.assertEqual(type(alx.number_rooms), int)

    def test_number_bathrooms(self):
        """Test bethroom number """
        alx = self.value()
        self.assertEqual(type(alx.number_bathrooms), int)

    def test_max_guest(self):
        """Test maimum guest"""
        alx = self.value()
        self.assertEqual(type(alx.max_guest), int)

    def test_price_by_night(self):
        """Tests night price """
        alx = self.value()
        self.assertEqual(type(alx.price_by_night), int)

    def test_latitude(self):
        """Test latitude """
        alx = self.value()
        self.assertEqual(type(alx.latitude), float)

    def test_longitude(self):
        """Test longitude """
        alx = self.value()
        self.assertEqual(type(alx.latitude), float)

    def test_amenity_ids(self):
        """est new.amenity_ids """
        alx = self.value()
        self.assertEqual(type(alx.amenity_ids), list)
