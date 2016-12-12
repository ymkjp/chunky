from os import listdir, path
import logging
import humanfriendly
from error import Error

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


class Sorter:
    def __init__(self):
        self.logger = logging.getLogger()

    def execute(self, opts=None):
        dirs = self.list_subdir_by_disk_usage(opts.source)
        self.logger.debug("Number of dirs: %d" % len(dirs))
        chunked_dirs = self.chunk(dirs, humanfriendly.parse_size(opts.cap))
        self.logger.debug("Number of chunks: %d" % len(chunked_dirs))
        return chunked_dirs

    def list_subdir_by_disk_usage(self, source_path=None):
        child_dirs = [path.join(source_path, child) for child in listdir(source_path)]
        disk_usages = [(d, self.get_tree_size(path.join(source_path, d))) for d in filter(path.isdir, child_dirs)]
        return sorted(disk_usages, key=lambda dir: dir[1], reverse=True)

    def get_tree_size(self, path):
        """Return total size of files in given path and subdirectories."""
        total = 0
        for entry in scandir(path):
            if entry.is_dir(follow_symlinks=False):
                total += self.get_tree_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size
        return total

    def chunk(self, dirs, cap_bytes):
        result = [[] for _ in range(len(dirs))]
        current_size = 0
        for dir in dirs:
            next_name = dir[0]
            next_size = dir[1]
            current_size += next_size
            pack_id = current_size / cap_bytes
            # print "\t".join(map(str, [pack_id, next_name, next_size, current_size, float(current_size) / cap_bytes]))
            if cap_bytes < next_size:
                raise Error("A size of `%s`(%s) is larger than cap size (%s)" % (
                    next_name,
                    humanfriendly.format_size(next_size),
                    humanfriendly.format_size(cap_bytes),
                ))

            result[pack_id].append(next_name)

        # print result
        return [dir for dir in result if len(dir) > 0]
