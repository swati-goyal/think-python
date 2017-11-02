from timeit import timeit


known = {0: 0, 1: 1}


def fibonacci_h(n):
    if n in known:
        return known[n]

    res = fibonacci_h(n-1) + fibonacci_h(n-2)
    known[n] = res
    return res


def fibonacci_o(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_o(n-1) + fibonacci_o(n-2)

start_time = timeit()
print(fibonacci_o(14))
elapsed_time_o = timeit() - start_time
print("Original time consuming fibonacci: ", elapsed_time_o)

start_time = timeit()
print(fibonacci_h(14))
elapsed_time_h = timeit() - start_time
print("Memoized fibonacci: ", elapsed_time_h)