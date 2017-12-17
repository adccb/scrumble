from sys import exit
import unittest

from lib.parser import Parser
from lib.calculator import Calculator
from lib.finder import Finder

if __name__ == '__main__':
    p = Parser().get_args()

    if p.test:
        print('\nRunning all tests...\n')
        suite = unittest.TestLoader().discover('.', pattern='*.py')
        unittest.TextTestRunner(verbosity=2).run(suite)
        exit(0)

