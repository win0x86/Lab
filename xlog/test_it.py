#!/usr/bin/env python
# coding: utf-8


import logging

from xlog import init_xlog


def test_log():
    logging.debug("test debug message.")
    logging.info("test info message.")
    logging.warning("test warning message.")
    logging.error("test error message.")


def test():
    test_log()


if __name__ == "__main__":
    init_xlog()
    test()
