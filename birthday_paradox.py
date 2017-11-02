from random import *


def has_duplicates(t):
    for x in t:
        if t.count(x) > 1:
            return True


# print(has_duplicates(['a', 'e', 'b', 'l', 'l', 'l']))


def get_month():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    rm = choice(months)
    return rm


def generate_birthday():

    bdl = []

    for i in range(23):
        mon = get_month()
        if mon != 'Feb':
            bdl.append(mon + ' ' + str(randint(1, 32)))
        else:
            bdl.append(mon + ' ' + str(randint(1, 30)))

    return bdl


def calc_probability_birthday_paradox():

    pbp = []

    for i in range(0, 1000):
        t = str(has_duplicates(generate_birthday()))
        pbp.append(t)

    for x in pbp:
        if x == 'True':
            return pbp.count(x)/1000

total = 0
for i in range(50):
    total += float(calc_probability_birthday_paradox())

print(total/50)