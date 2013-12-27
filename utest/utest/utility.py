# coding: utf-8
"""Some useful method for utest.

"""

from os.path import join as path_join, abspath
from pkgutil import walk_packages
from importlib import import_module
from inspect import getmembers, isclass, ismethod
from unittest import TestCase


def get_modules(d_name):
    modules = {}
    names = [x[1] for x in walk_packages([path_join(abspath("."), d_name)], "{0}.".format(d_name)) if not x[2]]
    imports = dict((n, import_module(n)) for n in names)
    for n, m in imports.iteritems():
        classes = [v for k, v in getmembers(m) if isclass(v) and issubclass(v, TestCase) and v is not TestCase]

        modules[n] = []
        for c in classes:
            modules[n].append({c: [k for k, v in getmembers(c) if k.startswith("test") and ismethod(v)]})

    return modules



def get_testcase(d_name="testfiles"):
    return get_modules(d_name)



def read_cmdline(line):
    pass
