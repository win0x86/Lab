# coding: utf-8


def cmd(c, arg, hlp):
    def wrap(cls):
        cls._cmd__ = c
        cls._arg__ = arg
        cls._help__ = hlp
        return cls

    return wrap
