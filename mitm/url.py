#!/usr/bin/env python
# coding: utf-8

import os
import sys
from base64 import b64decode


def get_log_files(path=None):
    path = path or "."
    files = os.listdir(path)
    ret = [f for f in files if f.startswith("log")]

    return ret


def split_log_line(line, wanted=None, decode=True):
    decode_fields = ["query", "url"]
    lst = ["time1", "time2", "method", "scheme", "host", "port", "path", "query", "url"]
    if not wanted:wanted = lst
    words = line.split(" ")
    if len(words) < 3:
        raise Exception("Error line %s." % line)
    elif words[2] not in ("GET", "POST", "OPTIONS"):
        raise Exception("Ignore line.")

    ret = []
    for want in wanted:
        if want not in lst: continue
        index = lst.index(want)
        if index > -1:
            w = words[index]
            if decode and want in decode_fields:
                try:
                    w = b64decode(w)
                except:
                    print "Decode error."
            ret.append(w)

    return ret


def analyze_log(f):
    with open(f, "r") as f:
        for i, line in enumerate(f):
            try:
                no = i + 1
                method, host, url = split_log_line(line, ["method", "host", "url"])
                print "%4d %s %s %s" % (no, method, host, (len(host + url) > 131) and "%s ..." % url[:(141 - len(host))] or url)
            except Exception as ex:
                print "%4d IGNORE %s" %(no, ex)


def run(code):
    log_files = get_log_files()

    for f in log_files:
        analyze_log(f)



#==============TEST ===========================

def test_get_log_files():
    print get_log_files()

def test_split_log_line():
    lines = """[2014-09-05 16:33:45,866] Proxy server on: 8000
[2014-09-05 16:33:53,180] GET http www.baidu.com 80 /  aHR0cDovL3d3dy5iYWlkdS5jb20v
[2014-09-05 16:33:53,611] GET http www.baidu.com 80 /index.php?tn=03009006_dg dG46IDAzMDA5MDA2X2RnDQo= aHR0cDovL3d3dy5iYWlkdS5jb20vaW5kZXgucGhwP3RuPTAzMDA5MDA2X2Rn
[2014-09-05 17:25:47,429] GET http www.baidu.com 80 /nocache/fesplg/s.gif?_screen=1600*900|1600*900&browser=30&wtt=669&dns=0&ct=0&st=0&tt=0&dct=0&olt=0&ht=163&vt=184&drt=406&tti=236&lt=0&fvt=4325&crt=4325&c_right=222&c_leftAD=223&c_results=235&let=4325&cus_q=qq&cus_tplp=&cus_stime=-1&cus_tti2=-1&cus_fs=-1&cus_srv=181.16&cus_net=-1&cus_fr=4324&cus_frdom=236&cus_frext=4088&cus_app=undefined&cus_srcid=6728_6729_20824_6835_91_16743_11170&cus_sid=5014_8544_5228_1430_7801_8235_8677_8488_8056_8558_6505_8504_6018_8592_8626_7825_8579_8549_7799_8483_8548_8509_8435_8566&cus_eid=&cus_qid=f546c3fa0000d161&cus_ic=33&cus_extic=27&cus_icl=9&cus_icr=24&cus_ck=undefined&cus_b64=1&cus_lfs=-1&cus_rfs=-1&cus_bpu=150&cus_tape=80&cus_cusval=b64_1_552&cache=0&user=0&product_id=45&page_id=101&special_id=[40]&pf=Linux%20x86_64&_t=1409909148396 X3NjcmVlbjogMTYwMCo5MDB8MTYwMCo5MDANCmJyb3dzZXI6IDMwDQp3dHQ6IDY2OQ0KZG5zOiAwDQpjdDogMA0Kc3Q6IDANCnR0OiAwDQpkY3Q6IDANCm9sdDogMA0KaHQ6IDE2Mw0KdnQ6IDE4NA0KZHJ0OiA0MDYNCnR0aTogMjM2DQpsdDogMA0KZnZ0OiA0MzI1DQpjcnQ6IDQzMjUNCmNfcmlnaHQ6IDIyMg0KY19sZWZ0QUQ6IDIyMw0KY19yZXN1bHRzOiAyMzUNCmxldDogNDMyNQ0KY3VzX3E6IHFxDQpjdXNfdHBscDogDQpjdXNfc3RpbWU6IC0xDQpjdXNfdHRpMjogLTENCmN1c19mczogLTENCmN1c19zcnY6IDE4MS4xNg0KY3VzX25ldDogLTENCmN1c19mcjogNDMyNA0KY3VzX2ZyZG9tOiAyMzYNCmN1c19mcmV4dDogNDA4OA0KY3VzX2FwcDogdW5kZWZpbmVkDQpjdXNfc3JjaWQ6IDY3MjhfNjcyOV8yMDgyNF82ODM1XzkxXzE2NzQzXzExMTcwDQpjdXNfc2lkOiA1MDE0Xzg1NDRfNTIyOF8xNDMwXzc4MDFfODIzNV84Njc3Xzg0ODhfODA1Nl84NTU4XzY1MDVfODUwNF82MDE4Xzg1OTJfODYyNl83ODI1Xzg1NzlfODU0OV83Nzk5Xzg0ODNfODU0OF84NTA5Xzg0MzVfODU2Ng0KY3VzX2VpZDogDQpjdXNfcWlkOiBmNTQ2YzNmYTAwMDBkMTYxDQpjdXNfaWM6IDMzDQpjdXNfZXh0aWM6IDI3DQpjdXNfaWNsOiA5DQpjdXNfaWNyOiAyNA0KY3VzX2NrOiB1bmRlZmluZWQNCmN1c19iNjQ6IDENCmN1c19sZnM6IC0xDQpjdXNfcmZzOiAtMQ0KY3VzX2JwdTogMTUwDQpjdXNfdGFwZTogODANCmN1c19jdXN2YWw6IGI2NF8xXzU1Mg0KY2FjaGU6IDANCnVzZXI6IDANCnByb2R1Y3RfaWQ6IDQ1DQpwYWdlX2lkOiAxMDENCnNwZWNpYWxfaWQ6IFs0MF0NCnBmOiBMaW51eCB4ODZfNjQNCl90OiAxNDA5OTA5MTQ4Mzk2DQo= aHR0cDovL3d3dy5iYWlkdS5jb20vbm9jYWNoZS9mZXNwbGcvcy5naWY/X3NjcmVlbj0xNjAwKjkwMHwxNjAwKjkwMCZicm93c2VyPTMwJnd0dD02NjkmZG5zPTAmY3Q9MCZzdD0wJnR0PTAmZGN0PTAmb2x0PTAmaHQ9MTYzJnZ0PTE4NCZkcnQ9NDA2JnR0aT0yMzYmbHQ9MCZmdnQ9NDMyNSZjcnQ9NDMyNSZjX3JpZ2h0PTIyMiZjX2xlZnRBRD0yMjMmY19yZXN1bHRzPTIzNSZsZXQ9NDMyNSZjdXNfcT1xcSZjdXNfdHBscD0mY3VzX3N0aW1lPS0xJmN1c190dGkyPS0xJmN1c19mcz0tMSZjdXNfc3J2PTE4MS4xNiZjdXNfbmV0PS0xJmN1c19mcj00MzI0JmN1c19mcmRvbT0yMzYmY3VzX2ZyZXh0PTQwODgmY3VzX2FwcD11bmRlZmluZWQmY3VzX3NyY2lkPTY3MjhfNjcyOV8yMDgyNF82ODM1XzkxXzE2NzQzXzExMTcwJmN1c19zaWQ9NTAxNF84NTQ0XzUyMjhfMTQzMF83ODAxXzgyMzVfODY3N184NDg4XzgwNTZfODU1OF82NTA1Xzg1MDRfNjAxOF84NTkyXzg2MjZfNzgyNV84NTc5Xzg1NDlfNzc5OV84NDgzXzg1NDhfODUwOV84NDM1Xzg1NjYmY3VzX2VpZD0mY3VzX3FpZD1mNTQ2YzNmYTAwMDBkMTYxJmN1c19pYz0zMyZjdXNfZXh0aWM9MjcmY3VzX2ljbD05JmN1c19pY3I9MjQmY3VzX2NrPXVuZGVmaW5lZCZjdXNfYjY0PTEmY3VzX2xmcz0tMSZjdXNfcmZzPS0xJmN1c19icHU9MTUwJmN1c190YXBlPTgwJmN1c19jdXN2YWw9YjY0XzFfNTUyJmNhY2hlPTAmdXNlcj0wJnByb2R1Y3RfaWQ9NDUmcGFnZV9pZD0xMDEmc3BlY2lhbF9pZD1bNDBdJnBmPUxpbnV4JTIweDg2XzY0Jl90PTE0MDk5MDkxNDgzOTY="""
    for line in lines.split("\n"):
        try:
            method, host, path = split_log_line(line, ["method", "host", "path"])
            print "%s %s %s" % (method, host, path)
        except Exception as ex:
            print "Test func Error: %s" % ex.message

def test_analyze_log():
    f = "log2014090517.log"
    analyze_log(f)


def test():
    #test_get_log_files()
    test_split_log_line()
    #test_analyze_log()
#===========TEST END===========================


if __name__ == "__main__":
    code = sys.argv[-1]
    if code == "test":
        test()
    else:
        run(code)
