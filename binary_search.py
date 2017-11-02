from bisect import bisect_left


def make_word_list():
    y = []
    file_obj = open("words.txt", 'r')
    for line in file_obj:
        word = line.strip()
        y.append(word)
    return sorted(y)


def in_bisect(wl, word):
    i = bisect_left(wl, word)
    if i != len(wl) and wl[i] == word:
        return i


def has_no_e(word, ltr):
    for x in word:
        if x == ltr:
            return False
    return True


def avoids(word, fl):
    for letter in word:
        if letter in fl:
            return False
    return True


def find_reverse_pairs(word_list):
    t = {}
    for word in word_list:
        if in_bisect(word_list, word[::-1]) and word != word[::-1]:
            t[word] = word[::-1]
    return t


def interlocks_2(word):
    if len(word) % 2 == 0 and len(word) >= 2:
        str1 = ''
        str2 = ''
        i = 0
        while i < len(word)-1:
            str1 += word[i]
            str2 += word[i+1]
            i += 2

        return str1, str2, word


def interlocks_3(word):
    if len(word) % 3 == 0 and len(word) >= 3:
        str1 = ''
        str2 = ''
        str3 = ''
        i = 0
        while i < len(word)-2:
            str1 += word[i]
            str2 += word[i+1]
            str3 += word[i+2]
            i += 3

        return str1, str2, str3, word


# Read the word list from words.txt file
word_list = make_word_list()

'''
# Get the interlocked words in the word list made by three words
for word in word_list:
    strings = interlocks_3(word)
    if strings is not None:
        if in_bisect(word_list, strings[0]) and in_bisect(word_list, strings[1]) and in_bisect(word_list, strings[2]):
            print(strings)

# Get the interlocked words in the word list made by two words
for word in word_list:
    strings = interlocks_2(word)
    if strings is not None:
        if in_bisect(word_list, strings[0]) and in_bisect(word_list, strings[1]):
            print(strings)


# Go get the list of all words without 'letter'
letter = input("Enter letter which should not be present: ")
all_words_with_no_e = []
for word in word_list:
    if has_no_e(word, letter):
        all_words_with_no_e.append(word)


# Go get the words from list without forbidden letters
forbidden = input("Enter forbidden letters: ")
remaining_words = []
for word in word_list:
    if avoids(word, forbidden):
        remaining_words.append(word)

# Go get all the reverse pairs in the word list
print(len(find_reverse_pairs(word_list)))

'''