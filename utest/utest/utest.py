#!/usr/bin/env python
# coding: utf-8

"""utest shell

"""


try:
    from settings import utest_path
except ImportError as ex:
    utest_path = "testfiles"


def main():
    from shell import run
    run()



def test():
    from unittest import TestCase
    from common.utility import get_members
    from pprint import pprint
    from utility import get_testcases
    path = "testfiles"
    #modules = get_members(path, lambda m: issubclass(m, TestCase) and not m is TestCase)
    modules = get_testcases(path, lambda v: issubclass(v, TestCase) and v is not TestCase)
    pprint(modules)
    print "\n"



if __name__ == "__main__":
    #main()
    test()
