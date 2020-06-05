import unittest
import collatz_ju


class MyTestCase(unittest.TestCase):
    def test_coll_small(self):
        self.assertEqual(collatz_ju.coll(20), 7)

    def test_coll_big(self):
        self.assertEqual(collatz_ju.coll(1e+150), 876)

    def test_coll_negative(self):
        self.assertEqual(collatz_ju.coll(-20), 7)  # case will fail

    def test_coll_corner_infi(self):
        self.assertEqual(collatz_ju.coll(1e+300), 1245)

    def test_coll_zero(self):
        self.assertEqual(collatz_ju.coll(0), 0)  # case will fail


if __name__ == '__main__':
    unittest.main()