# coding: utf-8


class CmdBase(object):
    _cmd__ = ""
    _hlp__ = ""
    _arg__ = ""
    _kwargs = {}


    @property
    def cmd(self):
        return self._cmd__


    @property
    def hlp(self):
        return self._hlp__


    @property
    def arg(self):
        return self._arg__


    @property
    def kwargs(self):
        return self._kwargs__
