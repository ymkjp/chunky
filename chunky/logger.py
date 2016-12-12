import logging
import logging.config


class Logger:
    def __init__(self):
        pass

    def setup(self):
        return logging.config.fileConfig('logging.conf')
