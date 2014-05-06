# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "-one"

@cmd(CMD, "1", "help one")
class One(CmdBase):
    def execute(self):
        print "one run"



#@cmd(CMD, "test1", "help one")
class OneTest(object):
    pass



class OneTest2(object):
    pass
