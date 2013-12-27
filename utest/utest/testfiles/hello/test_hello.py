# coding: utf-8


from unittest import TestCase



class TestHello(TestCase):
    def setUp(self):
        print "init ..."


    def tearDown(self):
        print "clean ..."


    def test_hello(self):
        a = "a"
        self.assertEqual(a, "a")



__all__ = ["TestHello"]
