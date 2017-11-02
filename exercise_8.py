def rotate_word(s, i):
    ns = ''
    for c in s.lower():
        f = ord(c) + i
        if 97 <= f <= 122:
            ns += chr(f)
        elif f >= 122:
            ns += chr(f-26)
        else:
            ns += chr(f + 26)
    return ns


# print(rotate_word('kosla', 8))

# 'swati' + 18 = 'kosla'