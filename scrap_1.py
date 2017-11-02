from exercise_6 import factorial
import math


def rotate_word(s):
    ns = []
    for c in s.lower():
         ns.append(str(ord(c)))
    return ns


def hailstone(n):
    """Print the terms of the 'hailstone sequence' from n to 1."""
    assert n > 0
    print(n)
    if n % 2 == 0:
        hailstone(n // 2)
    elif n > 1:
        hailstone((3*n) + 1)


def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15: break
        k += 1

    return 1 / total


# print(estimate_pi())
hailstone(10234)