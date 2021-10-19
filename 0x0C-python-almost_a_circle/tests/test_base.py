#!/usr/bin/python3
"""
Test for all possible cases,
which may affect the Base class
"""


import unittest
from models.base import Base

class Base_test(unittest.TestCase):
    """C"""
    def base_None(self):
        self.Base = Base(None)
        self.assertEqual(Base)


if __name__ == "__main__":
    unittest.main()
