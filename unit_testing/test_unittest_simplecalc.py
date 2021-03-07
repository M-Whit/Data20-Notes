# import pyodbc

from simple_calc import SimpleCalc
import unittest
import pytest
# Can use pytest -v in the terminal for more information


class Calctests(unittest.TestCase):

    # Instance of SimpleCalc()
    calc = SimpleCalc()

    def test_add(self):
        # assertEqual() comes from unittest.TestCase
        # Takes input and expected output
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

# Always make sure the start of the file has test
# and that each class method begins with test
