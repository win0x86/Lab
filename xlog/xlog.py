# coding: utf-8

"""Initial root logger handler.

"""

import logging


class RootLogger(object):
    _DEFAULT_FORMAT = "[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s"

    def __init__(self, level=None, fmt=None):
        level = level or logging.INFO
        fmt = fmt or self._DEFAULT_FORMAT
        logger = logging.getLogger()
        logger.setLevel(level)
        channel = logging.StreamHandler()
        channel.setFormatter(logging.Formatter(fmt))
        logger.addHandler(channel)


def init_xlog(level=logging.DEBUG, fmt=None):
    assert level in (logging.DEBUG, logging.INFO, logging.WARN, logging.FATAL)
    RootLogger(level, fmt)
