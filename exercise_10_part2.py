import timeit


def remove_duplicates(t):
    return set(t)

# print(remove_duplicates([21, 34, 56, 12, 23, 21, 21, 21, 21]))


def word_list():
    file_obj = open("words.txt", 'r')
    lines = file_obj.readlines()
    file = []
    for line in lines:
        t = line.split(' ')
        for x in t:
            file.append(x)
    return file


def word_list_2():
    file_obj = open("words.txt", 'r')
    lines = file_obj.readlines()
    file = []
    for line in lines:
        t = line.split(' ')
        for x in t:
            file += [x]
    return file

start_time = timeit.timeit()
t = word_list()
elapsed_time = timeit.timeit() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = timeit.timeit()
t = word_list_2()
elapsed_time = timeit.timeit() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')
