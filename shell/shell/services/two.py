# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("-t1", "2", "params: 2")
class Two(CmdBase):
    def __call__(self):
        print "two"



class TwoTest(object):
    pass



@cmd("-t2", "test2", "params: test2")
class TwoTest2(object):
    def __call__(self):
        print "two"

