import os

line1 = "This is first line \n"
line2 = "This is second line \n"

fout = open("test-file.txt", 'w')
fout.write(line1)
fout.write(line2)
fout.close()


def walk(dir_name):
    for name in os.listdir(dir_name):
        path = os.path.join(dir_name, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dir_name):
    for root, dirs, files in os.walk(dir_name):
        for filename in files:
            print(os.path.join(root, filename))


def sed(ps, rs, f1, f2):
    try:
        fin = open(f1, 'r')
        fout = open(f2, 'w')
        data = fin.readlines()
        for lines in data:
            fout.write(lines.replace(ps, rs))
        fin.close()
        fout.close()
    except:
        print("Something went wrong")


def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('exercise_14.py'))
#    sed('the', 'eht', 'emma.txt', 'eht-emma.txt')
#    walk2('.')
#    walk('.')
