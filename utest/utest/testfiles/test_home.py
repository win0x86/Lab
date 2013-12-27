# coding: utf-8

"""Test Home

"""


from unittest import TestCase



class TestHome(TestCase):
    def test_home(self):
        a = "a"
        self.assertEqual(a, "a")



__all__ = ["TestHome"]
