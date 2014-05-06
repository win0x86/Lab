# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "-five"


@cmd(CMD, "5", "help five")
class FiveTest(CmdBase):
    pass



#@cmd(CMD, "test5", "help five")
class FiveTest2(object):
    pass
