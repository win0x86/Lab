#!/usr/bin/env python
# coding: utf-8

import os
import sys
import traceback
from base64 import b64encode
from util import get_logger
from libmproxy import proxy, flow


PORT = 8000
log = get_logger()

class MyFlowMaster(flow.FlowMaster):
    def run(self):
        try:
            flow.FlowMaster.run(self)
        except KeyboardInterrupt:
            self.shutdown()
            log.i("Exit.")
            sys.exit(-1)
        except Exception as e:
            log.e("Error: %s", e.message)
            t = traceback.format_exc(sys.exc_info())
            log.e(t)
            sys.exit(-1)

    def handle_request(self, r):
        f = flow.FlowMaster.handle_request(self, r)
        if f: r.reply()
        return f

    def handle_response(self, r):
        f = flow.FlowMaster.handle_response(self, r)
        self.log_it(f.request, f.response)
        if f: r.reply()
        return f

    def log_it(self, req, resp):
        try:
            query = repr(req.get_query())
            url = req.get_url()
            content_type = resp.get_content_type() or ""
            if " " in content_type:
                content_type = content_type[:content_type.index(" ")].strip()
            query = b64encode(query)
            url = b64encode(url)
        except Exception as ex:
            log.e("Except message: %s", ex.message)
        else:
            log.i("%s %s %s==%s %d %s %s %s", req.method, req.scheme, content_type, req.host, req.port, req.path, query, url)



def start_proxy(port=PORT):
    state =  flow.State()
    cerfile = os.path.expanduser("cert.pem")
    server = proxy.ProxyServer(proxy.ProxyConfig(certfile=cerfile, cacert="/home/vm/.mitmproxy/mitmproxy-ca.pem"), port)
    m = MyFlowMaster(server, state)
    log.i("Proxy server on: %d", port)
    m.run()


if __name__ == "__main__":
    start_proxy()
