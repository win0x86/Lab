# coding: utf-8


from unittest import TestCase



class TestWorld(TestCase):
    def setUp(self):
        print "init ..."


    def tearDown(self):
        print "clean ..."


    def test_world(self):
        a = "a"
        self.assertEqual(a, "a")


    def test_world2(self):
        a = "a"
        self.assertEqual(a, "a")


class TestWorld2(TestCase):
    def setUp(self):
        print "init ..."


    def tearDown(self):
        print "clean ..."


    def test_world(self):
        a = "a"
        self.assertEqual(a, "a")


    def test_world2(self):
        a = "a"
        self.assertEqual(a, "a")

        

__all__ = ["TestWorld", "TestWorld2"]
