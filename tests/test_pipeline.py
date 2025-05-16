import unittest
from bess.pipeline import is_feasible


class TestPipeline(unittest.TestCase):
    def test_example_address(self):
        self.assertTrue(is_feasible("123 Example St, City, ST 00000"))

    def test_commerce_address(self):
        self.assertTrue(is_feasible("5300 Sheila St, Commerce, CA 90040"))



if __name__ == "__main__":
    unittest.main()
