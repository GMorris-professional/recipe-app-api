"""
Unit tests for Calc
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module."""

    def test_add_numbers(self):
        """Test adding two numbers together."""
        x = 1
        y = 2
        result = calc.add(x, y)
        self.assertEquals(result, 3)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        x = 2
        y = 1
        result = calc.subtract(x, y)
        self.assertEquals(result, 1)
