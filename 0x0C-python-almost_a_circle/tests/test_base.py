import sys
import unittest
import pep8
from models.base import Base
import os
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
