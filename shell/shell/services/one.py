# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("-o1", "1", "params: 1")
class One(CmdBase):
    def __call__(self):
        print "one run"



@cmd("-o2", "v", "params: v")
class OneTest(CmdBase):
    def __call__(self):
        pass



class OneTest2(object):
    pass
