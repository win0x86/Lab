# coding: utf-8

"""???

"""

from unittest import TextTestRunner
from utility import get_testcases


def runner(utest_path):
    cases = get_testcases(utest_path)
    no = 0
    blank = " "
    for k, v in cases.iteritems():
        no += 1
        print "[{1}] {0}".format(k, no)
        for i in v:
            for m, n in i.iteritems():
                no += 1
                print "{2}[{1}] {0}".format(m.__name__, no, blank * 4)
                for j in n:
                    no += 1
                    print "{2}[{1}] {0}".format(j, no, blank * 8)


    print "\nUTest count: {0}".format(no)


