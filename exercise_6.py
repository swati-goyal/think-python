import math


def hypotenuse(l, b):
    h = l ** 2 + b ** 2
    return math.sqrt(h)


# print(hypotenuse(13, 41))


def is_between(x, y, z):
    return x <= y <= z


# print(is_between(3, 4, 5))


def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def is_power(a, b):
    if a % b == 0 and is_power(a/b, b):
        return True
    else:
        return False


# print("Fibonacci-th : {}".format(fibonacci(int(num))))
# print("Factorial : {}".format(factorial(num)))
# print(is_power(int(a), int(b)))

