''''Fermat’s Last Theorem says that there are no positive integers a, b, and c such that: a^n + b^n = c^n for any
values of n greater than 2.'''


from math import *


def check_fermat(a, b, c, n):

    if n > 2:
        if pow(a, n) + pow(b, n) == pow(c, n):
            print("Holy smokes, Fermat was wrong!")

        else:
            print("No, that doesn't work!")
    else:
        if pow(a, n) + pow(b, n) == pow(c, n):
            print("Fermat holds good!")

print("To verify if fermat's last theorem holds good for your combination of numbers, enter these values")
a = input("Enter first operand: ")
b = input("Enter second operand: ")
c = input("Enter third operand: ")
n = input("Enter the value of power: ")
print("\n")
print("----------RESULT--------- \n")

check_fermat(int(a), int(b), int(c), int(n))

print("\n")
