#!/usr/bin/env python
# coding: utf-8

"""Test dust

Example:

"""

from unittest import TestCase, main, skip
from tornado.ioloop import IOLoop

from dustlib import SMTPClient


class SMTPClientTest(TestCase):
    def setUp(self):
        self.client = SMTPClient("localhost", 8025)


    def _start(self):
        IOLoop.current().start() 


    def _stop(self):
        IOLoop.current().stop()


    @skip("skip")
    def test_connect(self):
        self._start()


    @skip("skip")
    def test_fmt_replay(self):
        line = "220 cc Python SMTP proxy version 0.2"
        code, msg = SMTPClient.fmt_reply(line)
        self.assertEqual(code, 220)
        self.assertEqual(msg, "cc Python SMTP proxy version 0.2")


    @skip("skip")
    def test_get_hostname(self):
        n = self.client._get_hostname()
        self.assertEqual(n, "127.0.1.1")


    @skip("skip")
    def test_cmd_helo(self):
        self.client.cmd_helo()
        self._start()


    def test_cmd_ehlo(self):
        self.client.cmd_ehlo()
        self._start()


    def test_send_mail(self):
        self.client.send_mail("cc@cc", "cc@cc", "Hello from dust.")



if __name__ == "__main__":
    main()
