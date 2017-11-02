from pronounce import read_dictionary
from binary_search import make_word_list, in_bisect
from exercise_8 import rotate_word


def make_word_dict():
    dc = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        dc[word] = word
    return dc


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(h):
    for x in sorted(h.keys()):
        print(x, h[x])


def reverse_lookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)
    return l


def invert_dict(d):
    inverse = dict()
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse


# Global variable for fibonacci sequence
known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


known_ack = {(0, 0): 1, (1, 0): 2}


def ackermann(m, n):
    t = (m, n)

    if t in known_ack:
        return known_ack[t]

    else:
        if m == 0:
            known_ack[t] = n + 1
            return n + 1

        elif n == 0 and m > 0:
            known_ack[t] = ackermann(m - 1, 1)
            return ackermann(m - 1, 1)

        elif m > 0 and n > 0:
            known_ack[t] = ackermann(m - 1, ackermann(m, n - 1))
            return ackermann(m - 1, ackermann(m, n - 1))


def rotate_pairs(t, i):
    dic = {}
    for s in t:
        if in_bisect(t, rotate_word(s, i)):
            dic[s] = rotate_word(s, i)
    return dic


# Global variable
d = read_dictionary()


def homophone(dic):
    lt = []
    for s in dic:
        if len(dic[s]) >= 3:
            s2 = dic[s][1:]
            s3 = dic[s][0] + dic[s][2:]
            if s2 in dic and s3 in dic:
                if s2 in d.keys() and s3 in d.keys() and s in d.keys():
                    if d[s2] == d[s] and d[s3] == d[s]:
                        lt.append(s)
    return lt


word_map = make_word_dict()
word_list = make_word_list()


'''
# Traversal of a hash map or dictionary
for i in word_map:
    if has_no_e(word_map[i], 'e'):
        print(word_map[i])

# Keys and Values, respective frequencies
for i in word_map:
    x = histogram(word_map[i])
    if len(x) < 3:
        print(x)

# Printing reverse lookup
dict_sample = {'0': 'M', '1': 'V', '2': 'P', '3': 'S', '4': 'A', '5': 'M', '6': 'M'}
v = dict_sample.values()
print("Key(s) for value {} is {}".format(v[0], reverse_lookup(dict_sample, v[0])))

# To print the inverse of the dictionary
dict_sample = {'0': 'a', '1': 'b', '2': 'c', '3': 'a', '4': 'b', '5': 'c', '6': 'a', '7': 'a'}
print(invert_dict(dict_sample))

# Memoized fibonacci - quicker and easier
print(fibonacci(14))

# Memoized ackermann function - still no use
print(ackermann(3, 8))

# Fibonacci function call
print(fibonacci(99))
print(sqrt((ceil(sqrt(fibonacci(99))))**2 - fibonacci(99)))

# rotate pairs
word_list = make_word_list()
print(rotate_pairs(word_list, 11))

# homophones
print(homophone(word_map))

'''