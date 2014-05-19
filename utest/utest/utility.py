# coding: utf-8
"""Some useful method for utest.

"""

from unittest import TestCase
from pkgutil import walk_packages
from importlib import import_module
from os.path import join as path_join, abspath
from inspect import getmembers, isclass, ismethod


def get_modules(d_name, filter_func):
    modules = {}
    names = [x[1] for x in walk_packages([path_join(abspath("."), d_name)], "{0}.".format(d_name)) if not x[2]]
    imports = dict((n, import_module(n)) for n in names)
    from pprint import pprint
    #pprint(imports)
    print
    for n, m in imports.iteritems():
        classes = [v for k, v in getmembers(m) if isclass(v) and filter_func(v)]

        modules[n] = []
        print
        print classes
        print
        for c in classes:
            modules[n].append({c: [k for k, v in getmembers(c) if k.startswith("test") and ismethod(v)]})

    return modules



def get_testcases(d_name, filter_func=lambda s: s):
    return get_modules(d_name, filter_func)
