import unittest

from lib.calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_wwf(self):
        calc = Calculator(variant='words_with_friends')
        words = {
            'coccyx': 24,
            'hello': 9,
            'sister': 6,
            'yoga': 8
        }

        for word, val in words.items():
            self.assertTrue(calc.calculate(word) == val)

    def test_scr(self):
        calc = Calculator(variant='scrabble')
        words = {
            'coccyx': 22,
            'hello': 8,
            'sister': 6,
            'yoga': 8
        }

        for word, val in words.items():
            self.assertTrue(calc.calculate(word) == val)

