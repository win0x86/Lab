# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "-three"

@cmd(CMD, "3", "help three")
class Three(CmdBase):
    pass



class ThreeTest(object):
    pass
