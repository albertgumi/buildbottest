import unittest
class DemoTest(unittest.TestCase):
    def test_passes(self):
        pass
    def test_fails(self):
        self.fail("I failed.")
