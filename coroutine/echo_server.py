#!/usr/bin/env python
# coding: utf-8

import os
import sys
import socket
import mimetypes


from httplib import responses
from coroutine import Scheduler, ReadWait, WriteWait, NewTask
from log import get_logger

log = get_logger()


class CoSocket(object):
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        yield ReadWait(self.sock)
        client, addr = self.sock.accept()
        yield CoSocket(client), addr

    def send(self, buf):
        while buf:
            yield WriteWait(self.sock)
            length = self.sock.send(buf)
            buf = buf[length:]

    def recv(self, maxbytes):
        yield ReadWait(self.sock)
        yield self.sock.recv(maxbytes)

    def close(self):
        yield self.sock.close()


def http_server(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(address)
    s.listen(50)
    s = CoSocket(s)

    while True:
        conn, addr = yield s.accept()
        yield NewTask(http_request(conn, addr))


def http_request(conn, addr):
    request = b""
    while True:
        data = yield conn.recv(8192)
        request += data
        if b"\r\n\r\n" in request: break

    header_data = request[:request.find(b"\r\n\r\n")]
    header_text = header_data.decode("latin-1")
    header_lines = header_text.splitlines()
    method, url, proto = header_lines[0].split()

    if method == "GET":
        if os.path.exists(url[1:]):
            yield serve_file(conn, url[1:])
        else:
            yield error_response(conn, 404, "File %s not found." % url)
    else:
        yield error_response(conn, 501, "%s method not implemented" % method)
    yield conn.close()


def serve_file(conn, filename):
    content, encoding = mimetypes.guess_type(filename)
    yield conn.send(b"HTTP/1.1 200 OK\r\n")
    yield conn.send(("Content-Type: %s\r\n" % content).encode("latin-1"))
    yield conn.send(("Content-Length: %d\r\n" % os.path.getsize(filename)).encode("latin-1"))
    yield conn.send(b"\r\n")
    f = open(filename, "rb")
    while True:
        data = f.read(8192)
        if not data: break
        yield conn.send(data)


def error_response(conn, code, message):
    yield conn.send(("HTTP/1.1 %d %s\r\n" % (code, responses[code])).encode("latin-1"))
    yield conn.send(b"Content-Type: text/plain\r\n")
    yield conn.send(b"\r\n")
    yield conn.send(message.encode("latin-1"))


def test1():
    port = 8080
    sched = Scheduler()
    sched.new(http_server(("", port)))
    log.i("Echo server on %d", port)
    sched.mainloop()


if __name__ == "__main__":
    test1()
