# coding: utf-8

import logging
from datetime import datetime
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
        if DEBUG:
            ch =  self.get_stream_handler()
            fmt = "[%(module)s %(funcName)12s: %(lineno)4d] %(message)s"
        else:
            ch =  self.get_file_handler()
            fmt = "[%(asctime)s] %(message)s"
        log_format = logging.Formatter(fmt)
        ch.setFormatter(log_format)
        log.addHandler(ch)
        self.d = log.debug
        self.i = log.info
        self.e = log.error
        self._log = log


    def get_stream_handler(self):
        return logging.StreamHandler()


    def get_file_handler(self, f_name=None):
        if not f_name:
            f_name = "log%s.log" % datetime.now().strftime("%Y%m%d%H")
        return logging.FileHandler(f_name)



def get_logger():
    return Log.instance()
