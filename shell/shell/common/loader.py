# coding: utf-8

"""Loader

"""

from inspect import isclass
from argparse import ArgumentParser
from utility import get_members
from base import CmdBase


def loader(path):
    modules = get_members(path, lambda m: issubclass(m, CmdBase) and not m is CmdBase)
    modules = [j for i in modules for k, v in i.iteritems() for j in v if isclass(j)]
    add_argument(modules)


def add_argument(modules):
    cmdargs = {}
    parser = ArgumentParser(description="help this prog", epilog="Author: xi4nyu")
    for m in modules:
        o = m()
        parser.add_argument(o.cmd, help=o.hlp)
        cmdargs[m.cmd] = m.arg

    args = parser.parse_args()
    print args
    parser.print_help()
