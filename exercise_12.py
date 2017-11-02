from binary_search import make_word_list
from random import random
from structshape import structshape
from exercise_11 import invert_dict


def in_both_at_same_place(word1, word2):
    i = 0
    count = 0
    while i < len(word1):
        if word1[i] == word2[i]:
            count += 1
        i += 1
    if count == len(word1)-2:
        return True
    return False


def sumall(*args):
    print(sum(args))


def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


def enum_erate(t):
    for i, e in enumerate(t):
        print(i, e)


def sort_by_length(words):
    t = []
    for word in words:
        if len(word) > 0:
            t.append((len(word), random(), word))

    t.sort(reverse=True)
    res = []

    for length, _, word in t:
        res.append(word)

    return res


def most_frequent(wl1):
    d = {}
    for s in wl1:
        for letter in s:
            d[letter] = d.get(letter, 0) + 1

    res = []
    for letter, freq in d.items():
        res.append((freq, letter))

    res.sort(reverse=True)
    return res


def get_anagrams(wl2):
    d = {}

    for s in wl2:
        if len(s) > 1:
            d[s] = tuple(sorted(list(s)))

    dic = invert_dict(d)
    res = []

    for x in dic.values():
        if len(x) > 1:
            res.append(x)
    return res

word_list = make_word_list()
list_of_anagrams = get_anagrams(word_list)
list_anagrams_by_decr_length = sort_by_length(list_of_anagrams)


'''

# Sum function with more than 2 arguments
sumall(1, 2, 3, 4, 5, 34, 34, 54, 56, 68, 79)


# Zip built-in function takes any number of arguments
print(list(zip([1, 2, 3], 'abc', 'sbc', 'lkj', '123', (4, 5, 6))))


# Traversing two sequences at once using zip, for loop and tuple assignment
print(has_match([1, 2, 3], [5, 4, 3]))


# Enumerate function and tuple assignment for traversing
enum_erate(['dfhsd', 'fbhasbfh', 'gbjsd', 'bsfj'])


# DSU
print(sort_by_length(word_list)[:10])
print(structshape(sort_by_length(word_list)))


# Frequencies of letters - most_frequent
print(most_frequent(word_list))


# Anagrams in a list, and anagrams in decreasing order of possible words
word_list = make_word_list()
list_of_anagrams = get_anagrams(word_list)
list_anagrams_by_decr_length = sort_by_length(list_of_anagrams)
print(list_anagrams_by_decr_length)


# Bingo(scrabbles)
t = []
for x in list_anagrams_by_decr_length:
    for y in x:
        if len(y) == 8:
            t.append(x)
            break
for i in t:
    if len(i) == 7:
        print(i)


# Metathesis pairs - from anagrams
t = []
for x in list_anagrams_by_decr_length:
    i = 0
    while i < len(x)-1:
        if in_both_at_same_place(x[i], x[i+1]):
            t.append([x[i], x[i+1]])
        i += 1
print(t)

'''
