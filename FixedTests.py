import math
import unittest
import collatz_fixed


class MyTestCase(unittest.TestCase):
    def test_coll_small(self):
        self.assertEqual(collatz_fixed.coll(20), 7)

    def test_coll_big(self):
        self.assertEqual(collatz_fixed.coll(1e+150), 876)

    def test_coll_negative(self):
        self.assertEqual(collatz_fixed.coll(-20), 7)

    def test_coll_corner_infi(self):
        self.assertEqual(collatz_fixed.coll(1e+300), 1245)

    def test_coll_zero(self):
        self.assertEqual(collatz_fixed.coll(0), "InvalidInput")

    def test_coll_float(self):
        self.assertEqual(collatz_fixed.coll(1024.5678), 10)

    def test_coll_neg_float(self):
        self.assertEqual(collatz_fixed.coll(-1055.24), 31)

    def test_coll_very_small(self):
        self.assertEqual(collatz_fixed.coll(1e-300), "InvalidInput")

    def test_coll_neg_infi(self):
        self.assertEqual(collatz_fixed.coll(-(1e+300)), 1245)

    def test_coll_large(self):
        self.assertEqual(collatz_fixed.coll(1e+500), "Overflow")

    def test_coll_large_recur(self):
        self.assertEqual(collatz_fixed.coll(1e+309), "Overflow")

    def test_coll_irrat(self):
        self.assertEqual(collatz_fixed.coll(math.sqrt(2)), 0)

    def test_coll_pie(self):
        self.assertEqual(collatz_fixed.coll(math.pi), 7)


if __name__ == '__main__':
    unittest.main()
