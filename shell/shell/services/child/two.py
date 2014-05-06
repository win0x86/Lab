# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "--ct"

@cmd(CMD, "ct", "help x")
class Two(CmdBase):
    pass



class TwoTest(object):
    pass


@cmd(CMD, "ctt", "help x")
class TwoTest2(object):
    pass
