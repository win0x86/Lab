# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("-th1", "3", "params: 3")
class Three(CmdBase):
    def __call__(self):
        print "three"



class ThreeTest(object):
    pass
