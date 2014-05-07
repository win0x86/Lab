# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("-f1", "5", "params: 5")
class FiveTest(CmdBase):
    def __call__(self):
        print "five"



class FiveTest2(object):
    pass
