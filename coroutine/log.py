# coding: utf-8

import logging
from settings import DEBUG


class Log(object):
    _instance = None

    @staticmethod
    def instance():
        if getattr(Log, "_instance"):
            _instance = Log._instance
        else:
            _instance = Log()
            setattr(Log, "_instance", _instance)
        return _instance

    def __init__(self):
        log = logging.getLogger("Coroutine")
        log.setLevel(DEBUG and logging.DEBUG or logging.INFO)
        ch =  logging.StreamHandler()
        log_format = logging.Formatter(
            "[%(module)s %(funcName)12s: %(lineno)4d] - %(message)s")
        ch.setFormatter(log_format)
        log.addHandler(ch)
        self.d = log.debug
        self.i = log.info
        self.e = log.error
        self._log = log



def get_logger():
    return Log.instance()
