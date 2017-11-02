from binary_search import make_word_list


def uses_all(word, required_letters):
    return uses_only(required_letters, word)


def uses_only(word, given_letters):
    for letter in word:
        if letter not in given_letters:
            return False
    return True


def is_abecedarian(word):
    new_w = sorted(list(word))
    return ''.join(new_w) == word


word_list = make_word_list()


"""
# Get filter letters, word list from words.txt
letters = input("Enter letters which words should contain without spaces: ")

# Get the letters containing required letters at least once
list_uses_all = []
for words in word_list:
    if uses_all(words, letters):
        list_uses_all.append(words)
print("Word list contains {} words with letters '{}' ".format(len(list_uses_all), letters))

# Get the words containing given letters only
list_uses_only = []
for words in word_list:
    if uses_only(words, letters):
        list_uses_only.append(words)
print("Word list contains {} words with letters '{}' only".format(len(list_uses_only), letters))
print("List of words is: {}".format(list_uses_only))

# Get the list of words which are abecedarian
list_abecedarians = []
for words in word_list:
    if is_abecedarian(words):
        list_abecedarians.append(words)
print(list_abecedarians, len(list_abecedarians))

"""