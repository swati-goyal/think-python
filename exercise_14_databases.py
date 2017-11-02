from exercise_12 import get_anagrams
from binary_search import make_word_list
import shelve


def read_anagrams(s):
    words = make_word_list()
    loa = get_anagrams(words)
    list_of_words = []

    for t in loa:
        if sorted(s) == sorted(t[0]):
            list_of_words.extend(t)
        else:
            continue
    return s, list_of_words


def store_anagrams(s, list_of_string_anagrams):
    db = shelve.open('anagrams.db', 'c')
    db[s] = list_of_string_anagrams
    print(db[s])
    db.close()


if __name__ == '__main__':
    string, list_of_anagrams = read_anagrams('trader')
    store_anagrams(string, list_of_anagrams)