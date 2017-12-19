from collections import defaultdict

words = open('/usr/share/dict/words', 'r').read().splitlines()

class Finder():
    def __init__(self, hand=''):
        self.hand = list(hand.lower())
        self.words = words

    def set_hand(self, new_hand):
        self.hand = list(new_hand.lower())
        return self

    def find(self):
        return [
            word for word in self.words
            if all(letter in self.hand for letter in word)
        ]

