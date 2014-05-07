# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("--co1", "co1", "params: co1")
class One(CmdBase):
    def __call__(self):
        print "child one."



@cmd("--co2", "co2", "params: co2")
class OneTest(CmdBase):
    def __call__(self):
        print "child one test."



class OneTest2(object):
    pass
