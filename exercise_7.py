from math import *

from exercise_6 import factorial


def hailstone_sequence(n):
    count = 1
    while n != 1:
        print("{}. ".format(count), n)
        count += 1
        if n % 2 == 0:  # n is even
            n //= 2
        else:  # n is odd
            n = n * 3 + 1

# hailstone_sequence(73)


def test_square_root(x, a):
    while True:
        y = (a + x / a) / 2
        if y == a:
            break
        a = y
    z = sqrt(x)
    print(x, y, z, abs(z-y))

# test_square_root(4, 1)


def eval_loop(exp):
    if exp != 'done':
        print(eval(exp))
        expr = input("Please enter expression for calculation: ")
        eval_loop(expr)
    else:
        print('Hope it helped')

# expr = input("Please enter expression for calculation: ")
# eval_loop(expr)


def estimate_pi():
    i = 0
    r_const = (2 * sqrt(2)) / 9801
    while True:
        one_by_pi = r_const * (factorial(4 * i) * (1103 + 26390 * i)) / ((factorial(i) ** 4) * (396 ** (4 * i)))
        if one_by_pi < 1e-15:
            break
        i += 1

    return 1/one_by_pi

# print(estimate_pi())


def gcd(a, b):
    r = a % b
    if r != 0:
        x = gcd(b, r)
        return x
    else:
        return b


print(gcd(48, 18))
