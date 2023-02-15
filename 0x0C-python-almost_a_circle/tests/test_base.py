import sys
import unittest
import pep8
from models.base import Base
import os
from models.rectangle import Rectangle
'''
    This module contains all unittest for Base class
'''


class TestBase(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
            Tests for pep8 test
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_base_for_id(self):
        """
            Test check for id
        """

        Base.__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)
        self.assertEqual(b4.id, 3)

    def test_docstrings(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(2, 10, 1, 1, 15)
        r4 = Rectangle(10, 10)
        self.assertEqual(r1.id, r2 - 1)
        self.assertNotEqual(r1.id, r2)
        self.assertEqual(r3.id, 15)
        self.assertEqual(r1.width(), r2.height())
