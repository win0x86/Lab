#!/usr/bin/env python
# coding: utf-8

"""Shell

TODO:

    1. services get_members.
    2. example.
    3. load all services.

"""


from common.loader import loader

try:
    from settings import services_path
except ImportError:
    services_path = "services"


def run():
    loader(services_path)



if __name__ == "__main__":
    run()
