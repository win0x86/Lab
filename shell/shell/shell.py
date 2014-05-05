#!/usr/bin/env python
# coding: utf-8

"""Shell

TODO:

    1. services get_members.
    2. example.

"""

from argparse import ArgumentParser
from services import *


def shell():
    parser = ArgumentParser(description="help this prog", epilog="Author: xi4nyu")
    parser.add_argument("-x", help="for the help")
    args = parser.parse_args()

    if args.x == "1":
        print "ok"
    elif args.x == "100":
        one = One()
        print one._cmd__
        print one._help__
        print one._arg__
    else:
        parser.print_help()



if __name__ == "__main__":
    shell()
