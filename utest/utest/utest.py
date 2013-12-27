#!/usr/bin/env python
# coding: utf-8

"""utest shell

"""

from utility import get_testcase

try:
    from settings import utest_path
except:
    utest_path = "testfiles"


def main():
    # 1. cmd
    # 2. show
    files = get_testcase(d_name=utest_path)
    for k, v in files.iteritems():
        print k
        for i in v:
            print "\t{0}".format(i)



if __name__ == "__main__":
    main()
