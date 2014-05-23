# coding: utf-8

"""Dust实现.

通过Tornado的IOStream可以写出方便的事件驱动模型, 完全封装了低层的
epoll(Linux)的事件，我们可以把我们请求交由IOStream处理, 而且是异步非阻塞的.

"""


import socket

from tornado.iostream import IOStream


SMTP_PORT = 25
CRLF = "\r\n"

class SMTPClientBaseException(Exception):
    pass


class SMTPClientConnectError(SMTPClientBaseException):
    def __init__(self, code, msg):
        self.code = code
        self.error = msg
        self.args = (code, msg)





class SMTPClient(object):
    def __init__(self, host, port, hostname=None,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.hostname = hostname
        self.timeout = timeout
        self.connect(self.host, self.port)


    def _get_socket(self, host, port, timeout):
        return socket.create_connection((host, port), timeout)


    def _get_hostname(self):
        fqdn = socket.getfqdn()
        if "." in fqdn: return fqdn

        return socket.gethostbyname(socket.gethostname())


    def _on_connect(self, data):
        code, msg = SMTPClient.fmt_reply(data)
        print "on_connect: ", code, msg

        if code != 220: raise SMTPClientConnectError(code, msg)
        if not self.hostname: self.hostname = self._get_hostname()
        # self.cmd_helo()


    def _on_cmd_helo(self, data):
        code, msg = SMTPClient.fmt_reply(data)
        print "helo resp:", code, msg
        self.close()


    def _on_cmd_ehlo(self, data):
        # TODO implement.
        code, msg = SMTPClient.fmt_reply(data)
        print "helo resp:", code, msg
        self.close()


    def _on_close(self, data):
        print "close:", data
        self.stream.close()
        self.sock.close()

    
    def auth(self, user, passwd):
        pass


    def connect(self, host=None, port=None):
        host = host or "localhost"
        port = port or SMTP_PORT
        self.sock = self._get_socket(host, port, self.timeout)
        self.stream = IOStream(self.sock)
        # TODO multiline
        self.stream.read_until("\n", self._on_connect)


    def cmd_helo(self, hostname=""):
        self.execute("helo", self._on_cmd_helo, hostname or self.hostname)


    def cmd_ehlo(self, hostname=""):
        self.execute("ehlo", self._on_cmd_ehlo, hostname or self.hostname)


    def execute(self, cmd, callback, params="", end=CRLF):
        cmdline = "%s %s" % (cmd, params)
        cmdline = "%s%s" % (cmdline.strip(), end)
        print "cmdline:", repr(cmdline)
        self.stream.write(cmdline)
        self.stream.read_until(end, callback)


    def send_mail(self, frm, to, msg, options=None):
        options = options or []
        yield self.cmd_helo(self.hostname)
        # FIXME.


    @classmethod
    def fmt_reply(cls, line):
        code, msg = line[:3], line[4:].strip()
        try:
            code = int(code)
        except:
            code = -1
        return code, msg


    def close(self):
        self.execute("quit", self._on_close)
