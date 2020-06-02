import unittest
import collatz

class MyTestCase(unittest.TestCase):
    def test_something(self):
        exp_c = 25
        c = 0
        n = 100
        while n != 1:
            n = collatz.coll(int(n))
            # print(n)
            c = c + 1
        self.assertEqual(c, exp_c)



if __name__ == '__main__':
    unittest.main()


