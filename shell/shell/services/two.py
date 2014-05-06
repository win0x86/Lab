# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "-two"


@cmd(CMD, "2", "help two")
class Two(CmdBase):
    pass




class TwoTest(object):
    pass


#@cmd(CMD, "test2", "help two")
class TwoTest2(object):
    pass
