#!/usr/bin/env python
# coding: utf-8

from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient

done = 0
all_task = 0

def callback(r):
    print r.code, r.request.url, "Response body:", r.body

    global done
    done += 1

    if all_task == done:
        IOLoop.instance().stop()


def fetch(url):
    http = AsyncHTTPClient()
    http.fetch(url, callback)


def run():
    host = "http://localhost:8080"
    urls = ["/client.py", "/echo_server.py"]
    global all_task
    all_task = len(urls)

    for url in urls:
        fetch(host + url)
        print "fetch url:", url
    IOLoop.instance().start()


if __name__ == "__main__":
    run()
