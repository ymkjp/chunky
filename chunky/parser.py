import os, logging, tempfile, errno, argparse, uuid

import humanfriendly
from error import Error


class Parser:
    def __init__(self):
        self.logger = logging.getLogger()
        self.parser = argparse.ArgumentParser(description='Split subdirectories by cap sizes.')
        self.parser.add_argument('--source',
                                 dest='source',
                                 required=True,
                                 help='a source directory containing subdirectories')
        self.parser.add_argument('--destination',
                                 dest='destination',
                                 default=os.getcwd(),
                                 help='a target directory to output subdirectories (default: current directory)')
        self.parser.add_argument('--execute',
                                 dest='is_executable',
                                 action='store_true',
                                 default=False,
                                 help='To execute copy dirs (default: False)')
        self.parser.add_argument('--destination-prefix',
                                 dest='destination_prefix',
                                 type=str,
                                 default=uuid.uuid4(),
                                 help='a dir name prefix in dst directory (default: UUID)')
        self.parser.add_argument('--cap',
                                 dest='cap',
                                 metavar='N[B,KB,MB,GB]',
                                 default='2GB',
                                 help='Cap size (default: 2GB)')

    def parse_args(self):
        args = self.parser.parse_args()
        self.logger.debug(args)
        self.verify(args)
        return args

    def verify(self, args):
        if not os.path.exists(args.source):
            raise Error('Option --source dir `%s` does not exist' % args.source)
        if not os.path.exists(args.destination):
            raise Error('Option --destination dir `%s` does not exist' % args.destination)
        if not self.is_writable(args.destination):
            raise Error('Option --destination dir `%s` is not writable' % args.destination)
        if humanfriendly.parse_size(args.cap) <= 0:
            raise Error('Option --cap must be more than 0B (given %s)' % args.cap)

    def is_writable(self, path):
        try:
            testfile = tempfile.TemporaryFile(dir = path)
            testfile.close()
        except OSError as e:
            if e.errno == errno.EACCES:
                return False
            e.filename = path
            raise
        return True
