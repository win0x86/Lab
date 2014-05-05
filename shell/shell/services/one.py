# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("-x", "100", "help x")
class One(CmdBase):
    def execute(self):
        print "one run"
