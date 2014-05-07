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
    exists_cmd = set()
    commands = {}
    parser = ArgumentParser(description="help this prog", epilog="Author: xi4nyu")

    for m in modules:
        o = m()
        if o.cmd in exists_cmd: raise ValueError("exists.")
        parser.add_argument(o.cmd, help=o.hlp, **o.kwargs)
        commands[o.cmd[o.cmd.rindex("-") + 1:]] = {o.arg: o}

    args = parser.parse_args()
    if not any(args.__dict__.values()):
        parser.print_help()
    else:
        cmds = filter(lambda k: not k[0].startswith("__") and k[1], args.__dict__.iteritems())
        for cmd, arg in cmds:
            if cmd in commands and arg in commands[cmd]:
                commands[cmd][arg]()
            else:
                print "%s invalid." % cmd


def execute(cmd, arg):
    pass
