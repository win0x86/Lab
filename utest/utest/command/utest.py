# coding: utf-8

from unittest import TestCase

from common.utility import cmd
from common.base import CmdBase
try:
    from settings import utest_path
except ImportError as ex:
    utest_path = "testfiles"
from utility import get_testcases



@cmd("--show", "all", "all: show all utest.")
class UTestShow(CmdBase):
    def __call__(self):
        show()



def show():
    cases = get_testcases(utest_path, lambda v: issubclass(v, TestCase) and v is not TestCase)
    pprint(cases)
    no = 0
    blank = " "
    for k, v in cases.iteritems():
        no += 1
        print "[{1}] {0}".format(k, no)
        #no = old(v, no, blank)
        no = deep_case(v, no, blank)

    print "\nUTest count: {0}".format(no)



def old(v, no, blank):
    for i in v:
        for m, n in i.iteritems():
            no += 1
            print "{2}[{1}] {0}".format(m.__name__, no, blank * 4)
            for j in n:
                no += 1
                print "{2}[{1}] {0}".format(j, no, blank * 8)
    return no
    


def deep_case(cases, no=1, blank=" "):
    if isinstance(cases, list):
        for m in cases:
            if isinstance(m, dict):
                deep_case(m, no)
            else:
                no += 1
                print "{2}[{1}] {0}".format(m, no, blank * 8)
    elif isinstance(cases, dict):
        for k, v in cases.iteritems():
            no += 1
            print "{2}[{1}] {0}".format(k.__name__, no, blank * 4)
            deep_case(v, no)

    return no
