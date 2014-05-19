# coding: utf-8

"""Dust实现.

通过Tornado的IOStream可以写出方便的事件驱动模型, 完全封装了低层的
epoll(Linux)的事件，我们可以把我们请求交由IOStream处理, 而且是异步非阻塞的.

"""


import os
import socket

from tornado.iostream import IOStream


SMTP_PORT = 25
CRLF = os.linesep


class SmtpClient(object):
    def __init__(self, host, port, hostname=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.hostname = hostname
        self.timeout = timeout
        self.connect(self.host, self.port)


    def _get_socket(self, host, port, timeout):
        return socket.create_connection((host, port), timeout)


    def _on_connect(self, data):
        print "_on_connect:", data

    
    def auth(self, user, passwd):
        pass


    def connect(self, host=None, port=None):
        host = host or "localhost"
        port = port or SMTP_PORT
        self.sock = self._get_socket(host, port, self.timeout)
        self.stream = IOStream(self.sock)
        self.stream.read_until("\n", self._on_connect)


    def execute(self, cmd, callback, args="", end=os.linesep):
        cmdline = "%s %s" % (cmd, args)
        self.stream.write("%s%s" % (cmdline.strip(), end))
        self.stream.read_until(end, callback)


    def send_mail(self, frm, to, msg, options=None):
        options = options or []

