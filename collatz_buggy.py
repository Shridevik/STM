import sys

sys.setrecursionlimit(1000)


def coll(n: int) -> int:
    try:
        c = 1
        if n == 1:
            return c - 1
        if n % 2 == 0:
            c = (int(coll(int(n / 2))) + 1)
        elif n % 2 != 0:
            c = (int(coll(int(3 * n + 1))) + 1)
        return c
    except Exception as e:
        return 'RecursionLimit'


i = int(input("Enter a number: "))
print(coll(i))
# print(coll(1e+300))
# recursion error at 0 and <0
# input 1 to inf
# corner cases 0,1,1e+300
# basic cases 100, 1000,10000
# maybe 1e+150,-1,-10
# if RecursionLimit is reached, it means the num never reaches one or its way beyond set Recursion Limit
# need to add abs(), floor() and check for 0 to fix code
