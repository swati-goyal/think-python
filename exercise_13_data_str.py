from string import whitespace, punctuation
from exercise_11 import make_word_dict
import random
from exercise_10 import cumulative_sum
from bisect import bisect_left
from math import log

word_dict = make_word_dict()


def strip_book(f_name):
    all_words = dict()

    fin = open(f_name, 'r+', encoding='UTF8')
    skip_gutenberg_header(fin, s="***START")
    data = fin.readlines()
    fin.close()

    for lines in data:
        lines.replace(whitespace+punctuation, '')
        lines.strip(punctuation)
        for word in lines.split():
            if word.isalpha():
                word = word.lower().strip(punctuation)
                all_words[word] = all_words.get(word, 0) + 1

    fout = open("Output of - {}".format(f_name), "w+")
    for word, number in all_words.items():
        fout.write(word + ' ')

    return all_words


def skip_gutenberg_header(fp, s):
    for line in fp:
        if line.startswith(s):
            break


def subtract_dict(t, dictionary):
    x = []
    for word in t:
        if word not in dictionary:
            x.append(word)
    return x


def subtract_dict_set(words_in_the_book, dictionary):
    t1 = set(words_in_the_book)
    dictionary = set(dictionary)
    return t1.difference(dictionary)


def total_words(dic):
    return sum(dic.values())


def most_common(d, num=5):
    t = []
    for key, value in d.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t[:num]


def choose_from_hist(d):
    words = []

    for word, number in d.items():
        words.extend([word]*number)

    return random.choice(words)


def random_word(hist):
    words = list(hist.keys())
    freq = [vals for vals in hist.values()]
    t = (cumulative_sum(sorted(freq)))
    n = total_words(hist)
    indx = bisect_left(t, random.randint(0, n+1))
    return words[indx]


hist = strip_book("A story of seven years' wars.txt")


'''
# Comparing vocabulary of two books
words_of_a_book = strip_book("History of Historians.txt")
print(words_of_a_book)
words_of_a_book = strip_book("A story of seven years' wars.txt")
print(words_of_a_book)

# Comparing words in the book with word_dictionary
print(special_words)

# Book data
print("Words which are not there in the dictionary: ", len(additional_words))
print("Different words in the book: ", len(hist))
print("Total words in the book: ", total_words(hist))
print("Five Topmost words in the book: ", most_common(hist))
for i in range(1):
    print("Random word chosen: '{}'".format(choose_from_hist(hist)))

# Faster random word
print("Random word from the word list: ", random_word(hist))
OR
for i in range(10):
    print(random_word(hist),)

# Subtracting words of the book from dictionary
additional_words = subtract_dict_set(hist.keys(), word_dict)

# Zipf's Law representation of word, freq, log(freq), log(word_rank)
total_words_in_book = len(hist)
words_in_rev_order = most_common(hist, total_words_in_book)
for item in words_in_rev_order:
    word = item[1]
    word_rank = words_in_rev_order.index(item)+1
    freq = item[0]
    print(word, freq, str(log(freq)), str(log(word_rank)))

'''

d1 = {'set', 'me', 'up'}
d2 = {'set', 'me', 'not'}

print(subtract_dict_set(d2, d1))
