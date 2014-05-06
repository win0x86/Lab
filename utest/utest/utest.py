#!/usr/bin/env python
# coding: utf-8

"""utest shell

"""

from fp import runner

try:
    from settings import utest_path
except ImportError as ex:
    utest_path = "testfiles"


def main():
    runner(utest_path)


if __name__ == "__main__":
    main()
