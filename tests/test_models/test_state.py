#!/usr/bin/python3
"""
    test_state module
"""
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """ Tests for State class """

    def test_created(self):
        """ check correctly created """
        state1 = State()
        self.assertIsInstance(state1, State)

    def test_attributes(self):
        """ check instance attribute """
        state2 = State()
        self.assertTrue(hasattr(state2, 'name'))

    def test_attr_type_and_value(self):
        """ check ittribute correct type & default value """
        state3 = State()
        self.assertEqual(type(state3.name), str)
        self.assertEqual(state3.name, "")


if __name__ == '__main__':
    unittest.main()
