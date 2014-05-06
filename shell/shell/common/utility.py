# coding: utf-8

from pkgutil import walk_packages
from os.path import isfile, abspath, join as path_join
from inspect import getmembers, ismodule, isclass


def cmd(c, arg, hlp):
    def wrap(cls):
        cls._cmd__ = c
        cls._arg__ = arg
        cls._hlp__ = hlp
        return cls

    return wrap



def get_cmd(loc):
    return get_members(loc)



EXISTS = set()
def get_members(loc, filter_func=lambda s: s):
    modules = []
    
    for module, name, ispkg in walk_packages("."):
        if loc not in name: continue
        m = import_files(name, filter_func)
        if m: modules.append(m)

    return modules



def import_files(name, filter_func):
    ret = {}

    try:
        module_name = name
        modules = {n: m for n, m in getmembers(__import__(module_name)) if not n.startswith("__") and ismodule(m)}

        for name, module in modules.iteritems():
            if module in EXISTS: continue
            members = []
            for n, m in getmembers(module):
                if not n.startswith("__") and \
                        isclass(m) and filter_func(m):
                    EXISTS.add(module)
                    members.append(m)

            if members:
                if module_name in modules: 
                    ret[module_name] += members
                else:
                    ret[module_name] = members

    except Exception as ex:
        # continue
        raise

    return ret



def is_module(path):
    return isfile(path_join(abspath(path), "__init__.py"))
