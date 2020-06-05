import math
import sys

sys.setrecursionlimit(2000)


def coll(n: int) -> int:
    try:
        n = abs(math.floor(float(n)))
    except (Exception) as e:
        return 'Overflow'

    if n == 0 or n < 0:
        return 'InvalidInput'
    else:
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
            return 'Overflow'

# print(coll(1e-300))
# i = math.floor(float(input("Enter a number: ")))
# i = abs(i)
# if i < 0 or i == 0:
#     print("Invalid input")
# else:
#     print(coll(i))

