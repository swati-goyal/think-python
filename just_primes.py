import dbm


db = dbm.open('primes.db', 'c')


def all_primes_till(x):
    n = 0
    for i in range(0, x+1):
        if is_prime(i):
            store_primes(n, i)
            n += 1


def is_prime(x):
    if x < 2 or x % 2 == 0:
        return False
    for n in range(2, int(x ** 0.5) + 1):
        if n % 2 == 0:
            continue
        if x % n == 0:
            return False
    return True


def semi_prime_factorization():
    pass


def power_of_two(num):
    prod = 1
    for i in range(num):
        prod *= 2
    return prod


def store_primes(i, prime):
    global db
    db[str(i)] = '\n' + str(prime)
    print(db[str(i)])


# print(len(str(power_of_two(11213))))
# print(all_primes_till(20))

