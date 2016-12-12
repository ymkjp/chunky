import sys, pprint
from chunky.logger import Logger
from chunky.parser import Parser
from chunky.sorter import Sorter
from chunky.filer import Filer
from chunky.error import Error


class Chunky:
    """Split subdirectories by cap sizes"""
    def __init__(self):
        self.logger = Logger()
        self.parser = Parser()
        self.sorter = Sorter()
        self.filer = Filer()

    def execute(self):
        try:
            self.logger.setup()
            args = self.parser.parse_args()
            dirs = self.sorter.execute(opts=args)
            result = self.filer.execute(dirs, opts=args)
            pprint.pprint(result)
            return 0
        except Error as e:
            sys.stderr.write("%s\n" % e)

if __name__ == '__main__':
    Chunky().execute()
