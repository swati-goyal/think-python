from datetime import *
from exercise_16 import *


def print_day_of_the_week():
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))


def days_to_year():
    pass


def age_and_next_birthday(birthdate):
    curr_date = datetime.today()
    age_in_days = (curr_date - birthdate)
    next_birthday = datetime(curr_date.year, 12, 30, 0, 0, 0)
    time_till_next = (next_birthday-curr_date)
    return 'You are {} years old and next birthday due in {}'.format(age_in_days.days//365, time_till_next)


def double_day(b1, b2, n):
    assert b1 > b2
    delta = b1 - b2
    nth_day = delta/(n-1) + b1
    return nth_day


b2 = datetime(1989, 12, 30)
b1 = datetime(2015, 7, 13)
x = double_day(b1, b2, 7)
print(x)


# bd = datetime(1989, 12, 30, 21, 24, 5)
# print(age_and_next_birthday(bd))
# print_day_of_the_week(date.today())
