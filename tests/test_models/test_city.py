#!/usr/bin/python3
"""
    Is the test_city module
"""
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """ This Tests for City class """

    def test_created(self):
        """ This will check if an instance is correctly created """
        city1 = City()
        self.assertIsInstance(city1, City)

    def test_attributes(self):
        """ This checks if the instance has the proper attributes """
        city2 = City()
        self.assertTrue(hasattr(city2, 'name'))
        self.assertTrue(hasattr(city2, 'state_id'))

    def test_attr_type_and_value(self):
        """ This checks if the attributes have the correct type & default value """
        city3 = City()
        self.assertEqual(type(city3.name), str)
        self.assertEqual(type(city3.state_id), str)
        self.assertEqual(city3.name, "")
        self.assertEqual(city3.state_id, "")


if __name__ == '__main__':
    unittest.main()
