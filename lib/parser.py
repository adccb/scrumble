from argparse import ArgumentParser

class Parser:
    def __init__(self):
        parser = ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            '--hand',
            help='Your current scrabble hand.'
        )
        group.add_argument(
            '--test',
            action='store_const',
            const=True,
            help='Run tests.'
        )

        self.parser = parser

    def get_args(self):
        args = self.parser.parse_args()
        return args

