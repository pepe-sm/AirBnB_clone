#!/usr/bin/python3
"""
    test_user module
"""
import unittest
from models.user import User


class test_User(unittest.TestCase):
    """ Tests User class """

    def test_created(self):
        """ check instance creation """
        user1 = User()
        self.assertIsInstance(user1, User)

    def test_attributes(self):
        """ check instance attributes """
        user2 = User()
        self.assertTrue(hasattr(user2, 'email'))
        self.assertTrue(hasattr(user2, 'password'))
        self.assertTrue(hasattr(user2, 'first_name'))
        self.assertTrue(hasattr(user2, 'last_name'))

    def test_attr_type_and_value(self):
        """ check attributes correct type & default value """
        user3 = User()
        self.assertEqual(type(user3.email), str)
        self.assertEqual(user3.email, "")

        self.assertEqual(type(user3.password), str)
        self.assertEqual(user3.password, "")

        self.assertEqual(type(user3.first_name), str)
        self.assertEqual(user3.first_name, "")

        self.assertEqual(type(user3.last_name), str)
        self.assertEqual(user3.last_name, "")


if __name__ == '__main__':
    unittest.main()
