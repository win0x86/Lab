# coding: utf-8

from common.utility import cmd
from common.base import CmdBase


@cmd("-f", "4", "params: 4")
class Four(CmdBase):
    def __call__(self):
        print "four"
