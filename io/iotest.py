# coding: utf-8

"""Epoll test

"""

import errno
import socket
import select


class IO1(object):
    def __init__(self, host, port):
        self.connections = {}
        self.epoll = select.epoll()
        

    def run(self):
        pass


    def write(self, data):
        pass


    def read(self):
        pass
