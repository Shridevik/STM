# Write your code here

import math
import sys


def coll(n):
    if (n % 2) == 0:
        return n / 2
    else:
        n = (3 * n) + 1
        return n


c = 0
n = input()
print("The divisions goes as follows:")
while n != 1:
    n = coll(int(n))
    print(n)
    c = c + 1
print("The number of steps required to reach one is "+str(c))
