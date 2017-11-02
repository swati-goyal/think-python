known_sum = {0: [0], 1: [1, 2], 2: [2]}


def known_sum_of_dollars(n):
    global known_sum
    if n not in known_sum.keys():
        for i in range(n+1):
            if i not in known_sum.keys():
                known_sum[n - i] = game(n - i)
            else:
                continue
    return known_sum


def game(n):
    dic = known_sum_of_dollars(n)

    if n in dic.keys():
        return dic[n]

    else:
        sum1 = 0
        j = 1

        while j <= n:
            i = 1
            while i <= n:
                strng = str(i) + '/' + str(i + j)
                num = round(eval(strng), 2)
                sum1 += num
                i += 1
            j += 1

        if int(sum1) == sum1:
            return [sum1]

        x = round(sum1, 1)
        nume, deno = x.as_integer_ratio()

        if deno == 1:
            return [nume]

        return [nume, deno]

print(game(101))