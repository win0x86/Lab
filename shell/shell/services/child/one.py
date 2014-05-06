# coding: utf-8

from common.utility import cmd
from common.base import CmdBase

CMD = "--co"


@cmd(CMD, "c1", "help co")
class One(CmdBase):
    def execute(self):
        print "one run"



#@cmd(CMD, "ct", "help ct")
class OneTest(object):
    pass



class OneTest2(object):
    pass
