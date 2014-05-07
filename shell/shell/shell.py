#!/usr/bin/env python
# coding: utf-8

"""Shell

"""


from common.loader import loader

try:
    from settings import shell_path
except ImportError:
    shell_path = "services"



def run():
    loader(shell_path)



if __name__ == "__main__":
    run()
