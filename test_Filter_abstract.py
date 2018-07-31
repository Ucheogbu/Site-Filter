import unittest
from Filter_abstract import *


class FilterTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_host_paths(self):

        self.assertEqual(get_host_paths(r'C:\Windows\System32\etc'), r"C:\Windows\System32\etc")
