# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("--ct1", "ct1", "params: ct1")
class Two(CmdBase):
    def __call__(self):
        print "child two"



class TwoTest(object):
    pass



@cmd("--ct2", "ct2", "params: ct2")
class TwoTest2(object):
    def __call__(self):
        print "child two"

