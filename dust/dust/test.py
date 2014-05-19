#!/usr/bin/env python
# coding: utf-8

"""Test dust

Example:

"""

from unittest import TestCase, main
from tornado.ioloop import IOLoop

from dustlib import SmtpClient


class SmtpClientTest(TestCase):
    def _start(self):
        IOLoop.current().start() 


    def _stop(self):
        IOLoop.current().stop()


    def test_connect(self):
        client = SmtpClient("localhost", 8025)
        self._start()



if __name__ == "__main__":
    main()
