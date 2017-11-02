def nested_sum(t):
    total = 0
    for x in t:
        if type(x) == list:
            total += nested_sum(x)
        else:
            total += x

    return total


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(t):
    res = []
    for s in t:
        if type(s) != list:
            res.append(s.capitalize())
        else:
            res.append(capitalize_nested(s))
    return res


def cumulative_sum(t):
    res = []
    i = 0
    while i <= len(t):
        x = sum(t[:i+1])
        res.append(x)
        i += 1
    return res


def middle(t):
    if len(t) >= 2:
        t.pop(0)
        t.pop(-1)
    else:
        t.pop(0)
    return t


def chop(t):
    if len(t) >= 2:
        del t[0]
        del t[-1]


def is_sorted(t):
    if type(t) == list:
        return t == sorted(t)
    else:
        return "Not a list!"


def is_anagram(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))


# print(nested_sum([81, [72, [64, [55, [46, [37, [28, [19]]]]]]]]))
# print(capitalize_nested(['s', ['w', ['a', ['t', ['i', ['p', ['i', ['u']]]]]]]]))
# print(cumulative_sum([1, 1, 1, 2, 3, 5, 6]))
# print(middle(['a','b','c', 'd', 'e']))
# print(chop(['a','b','c', 'd', 'e']))
# print(is_sorted(['a','a']))
# print(is_anagram('firf', 'rif'))
