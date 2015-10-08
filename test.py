import unittest
import warnings

class DemoTest(unittest.TestCase):
    def test_passes(self):
        warnings.warn("Warning...........Message")
        pass
    def test_fails(self):
        self.fail("I failed.")
