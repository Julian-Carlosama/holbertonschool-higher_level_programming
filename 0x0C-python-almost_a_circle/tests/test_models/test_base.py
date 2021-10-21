#!/usr/bin/python3
"""
Unittest for this project
"""


import unittest
from models.base import Base


class Testbaseclass(unittest.TestCase):
    """ test for base"""

    def test_all_base(self):
        """ All posible cases """

        string = Base("Juli")
        tup = Base((1, 2, 3))
        lista = Base([1, 2, 3])
        diccionario = Base({"key1": 1, "key2": 2, "key3": 3})
        none = Base(None)
        asertioErr = Base(0)
        negative = Base(-89)
        self.assertEqual(string.id, "Juli")
        self.assertEqual(tup.id, (1, 2, 3))
        self.assertEqual(lista.id, [1, 2, 3])
        self.assertEqual(diccionario.id, {"key1": 1, "key2": 2, "key3": 3})
        self.assertEqual(none.id, 1)
        self.assertEqual(asertioErr.id, 2)
        self.assertEqual(negative.id, -89)

if __name__ == "__main__":
    unittest.main()
