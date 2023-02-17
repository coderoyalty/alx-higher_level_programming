import sys
import unittest
import pep8
from models.base import Base
import os
from models.rectangle import Rectangle
from models.square import Square
'''
    This module contains all unittest for Base class
'''


class TestBase(unittest.TestCase):
    def test_pep8_model(self):
        """
            Tests for pep8 model
        """
        files = []
        files.append('models/base.py')
        files.append('models/rectangle.py')
        files.append('models/square.py')
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(files)
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
        self.assertEqual(r1.id, r2.id - 1)
        self.assertNotEqual(r1.id, r2.id)
        self.assertEqual(r3.id, 15)

    def test_rect_area(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 10)
        self.assertEqual(r1.width, r2.height)
        self.assertEqual(r1.area(), r2.area())
        self.assertNotEqual(r1.area(), r3.area())

    def test_rect_exception_error(self):
        with self.assertRaises((TypeError, ValueError)):
            Rectangle(10, 2.5)
            Rectangle(0, 10)

    def test_rect_update(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r1.update(89, 15, 30)
        r2.update(90, 30, 30)
        self.assertNotEqual(r1.area(), r2.area())

    def test_rect_dict(self):
        r1 = Rectangle(10, 2, 5, 10, 50)
        r2 = Rectangle(10, 5, 2, 10, 50)

        rdict1 = r1.to_dictionary()
        rdict2 = r2.to_dictionary()

        self.assertNotEqual(rdict1, rdict2)
        r1.update(width=4, height=3, x=5, y=5)
        r2.update(width=4, height=3, x=5, y=5)
        rdict1 = r1.to_dictionary()
        rdict2 = r2.to_dictionary()
        self.assertEqual(rdict1, rdict2)

    def test_square(self):
        s1 = Square(10)
        s2 = Square(20)
        s3 = Square(30)
        self.assertNotEqual(s1.size, s2.size)
        self.assertEqual(s3.size, 30)

    def test_square_area(self):
        s1 = Square(10)
        s2 = Square(20)
        self.assertEqual(s1.area(), 100)
        self.assertEqual(s2.area(), 400)
        self.assertNotEqual(s1.area(), s2.area())

    def test_square_update(self):
        s1 = Square(10)
        s2 = Square(20)
        self.assertNotEqual(s1.area(), s2.area())
        s1.update(2, 20)
        self.assertEqual(s1.area(), s2.area())
        s1.update(size=10)
        self.assertNotEqual(s1.area(), s2.area())

    def test_square_dictionary(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)

        sdict1 = s1.to_dictionary()
        s2.update(**sdict1)
        self.assertEqual(sdict1, s2.to_dictionary())
