from binary_search import make_word_list


def is_palindrome(word, start, length):
    new_w = str(word)[start:(start + length)]
    return new_w == new_w[::-1]


def has_three_consecutive_doubles(word):
    i = 0
    count = 0
    string = ''

    while i < len(word) - 1:
        letter = word[i]
        next_letter = word[i + 1]
        if letter == next_letter:
            count += 1
            string += letter + next_letter
        i += 1
    return count == 3 and string in word


def odometer_puzzle(num1):
    if is_palindrome(num1, 2, 4) and is_palindrome(num1 + 1, 1, 5) and is_palindrome(num1 + 2, 1, 4) and is_palindrome(
                    num1 + 3, 0, 6):
        return num1
    else:
        return "No such numbers found"


def age_diff_puzzle(my_age):
    new_my_age = str(my_age)
    if len(new_my_age) == 1:
        new_son_age = new_my_age.zfill(2)
        mom_age = int(new_son_age[::-1])
    else:
        mom_age = int(new_my_age[::-1])

    if mom_age - my_age == 18:
        return my_age
    else:
        return "Not found"


# Fetch standard word list
word_list = make_word_list()

'''

# Get words which have three consecutive double letters
new_list = []
for word in word_list:
    if has_three_consecutive_doubles(word):
        new_list.append(word)
print(len(new_list), new_list)


# Enumerates all 6 digit numbers
for i in range(100000, 1000000):
    if odometer_puzzle(i) == i:
        print(i)

for age in range(1, 100):
    if age_diff_puzzle(age) == age:
        print(age)

'''