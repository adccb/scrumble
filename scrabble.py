from sys import exit
import unittest

from lib.parser import Parser
from lib.calculator import Calculator
from lib.finder import Finder

def left_pad(string, length=2):
    if len(string) == length:
        return string

    return '{}{}'.format(
        '0' * (length - len(string)),
        string
    )

if __name__ == '__main__':
    p = Parser().get_args()

    if p.test:
        print('\nRunning all tests...\n')
        suite = unittest.TestLoader().discover('.', pattern='*.py')
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit(0)

    finder = Finder(p.hand)
    calculator = Calculator()
    words = [(word, calculator.calculate(word)) for word in finder.find()]

    # sort descending by t[1], the point value
    sorted_tuples = sorted(words, key=lambda t: t[1], reverse=True)
    for word, points in sorted_tuples:
        print('{} {}'.format(
            left_pad(str(points)),
            word
        ))

