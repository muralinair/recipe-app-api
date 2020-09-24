from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """Test for two numbers"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """test for subtractions"""
        self.assertEqual(subtract(11, 6), 5)
