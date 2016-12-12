import logging, shutil, os
from distutils.dir_util import copy_tree
from os import path


class Filer:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, dirs, opts=None):
        for index, dir_list in enumerate(dirs):
            dst_path = path.join(str(opts.destination), str(opts.destination_prefix), str(index))
            for src in dir_list:
                dst = path.join(dst_path, path.basename(src))
                result = len(copy_tree(src, dst)) if opts.is_executable else 0
                self.logger.info('%s\t%s\t%s' % (result, src, dst))

        return path.join(str(opts.destination), str(opts.destination_prefix))
