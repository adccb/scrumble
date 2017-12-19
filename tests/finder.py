import unittest
import re

from lib.finder import Finder

finder = Finder()
class FinderTest(unittest.TestCase):
    def test_find(self):
        # test find is limited to just the letters we pass
        finder.set_hand('we')
        words = finder.find()

        self.assertTrue(all([
            re.match('^[we]+$', word)
            for word in words
        ]))

