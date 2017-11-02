def is_prime(x):
    for n in range(2, int(x**.5 + 1)):
        if x % n == 0:
            return False
    return True


print(is_prime(2993))

