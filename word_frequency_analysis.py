from exercise_13_data_str import skip_gutenberg_header
from string import whitespace
import random


# MARKOV ANALYSIS
suffix_map = dict()
prefix = tuple()


def read_file(f_name):
    # read the file from its crude form
    fin = open(f_name, 'r+', encoding='UTF8')
    skip_gutenberg_header(fin, "*END*")
    data = fin.readlines()
    fin.close()

    # write the file on your own terms
    fout = open("Output of - {}".format(f_name), "w+", encoding='UTF8')
    for line in data:
        line = line.replace('-', ' ')
        line = line.strip(whitespace)
        fout.write(line + ' ')
    fout.close()


def process_file(f_name, order=2):
    read_file(f_name)
    f_obj = open("Output of - {}".format(f_name), "r+", encoding='UTF8')
    t = []

    for line in f_obj.readlines():
        for word in line.split():
            t.append(word.strip(whitespace))

    for word in t:
        process_word(word, order)


def process_word(word, order=2):
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def shift(t, word):
    return t[1:] + (word,)


def random_text(n=100):
    excerpt = ''
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes is None:
            random_text(n - i)
            return

        word = random.choice(suffixes)
        excerpt += word + ' '
        start = shift(start, word)
    return excerpt

if __name__ == '__main__':
    process_file(f_name="emma.txt", order=4)
    print(random_text(20))




