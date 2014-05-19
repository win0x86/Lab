# coding: utf-8

from common.utility import cmd
from common.base import CmdBase
try:
    from settings import utest_path
except ImportError as ex:
    utest_path = "testfiles"
from utility import get_testcases


@cmd("--exec", "1", "1: number 1.")
class UTestExec(CmdBase):
    def __call__(self):
        execute()



def execute():
    print "execute"
