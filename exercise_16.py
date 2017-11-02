class Time1(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
    hour = 0
    minute = 0
    second = 0


def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def print_time(time_obj):
    # I could have used tuple comparison for faster results
    print('%.2d:%.2d:%.2d' % (time_obj.hour, time_obj.minute, time_obj.second))


def is_after(t1, t2):
    return (t2.hour * 3600 + t2.minute * 60 + t2.second) > (t1.hour * 3600 + t1.minute * 60 + t1.second)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time1()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment_time_modifier(start_time, seconds):
    start_time.second += seconds
    total = start_time.hour * 3600 + start_time.minute * 60 + start_time.second

    start_time.hour = total // 3600
    start_time.minute = (total - start_time.hour * 3600) // 60
    start_time.second = total - start_time.hour * 3600 - start_time.minute * 60


def increment_time_pure_function(start_time, seconds):
    time = Time1()
    total = start_time.hour * 3600 + start_time.minute * 60 + start_time.second + seconds
    time.hour = total // 3600
    time.minute = (total - time.hour * 3600) // 60
    time.second = total - time.hour * 3600 - time.minute * 60

    return time


def increment_time(time, seconds):
    assert valid_time(time)
    new_time = time_to_int(time) + seconds
    return int_to_time(new_time)


def mul_time(time, n=10):
    total = time_to_int(time)
    return int_to_time(n * total)


def average_pace(fin_time, distance):
    time = mul_time(fin_time, 1/distance)
    return time


timey = Time1()
timey.hour = 2
timey.minute = 8
timey.second = 5

wimey = Time1()
wimey.hour = 3
wimey.minute = 58
wimey.second = 5

x = increment_time_pure_function(timey, 0)
y = add_time(timey, wimey)
z = increment_time(timey, 3601)
m = mul_time(timey, n=2)
ap = average_pace(timey, 5)

# print_time(timey)
# print_time(ap)

