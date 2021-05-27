from string import ascii_lowercase as alphabet


def rot13(s):
    '''Encrypts and decrypts the string with ROOT13 cipher'''
    alph = list(alphabet)
    res, low_upper = [], 0
    for i in s:
        low_upper = 1 if i.isupper() else 0
        if i.isalpha():
            i = alph[alph.index(i.lower())-13]
            if low_upper == 1: res.append(i.upper())
            else: res.append(i)
        else:
            res.append(i)
    return ''.join(res)


print(rot13("This is my first ROT13 excercise!"))     