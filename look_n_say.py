# The look and say sequence is a sequence in which each element 
# is the result of a "look and say" operation on the previous element.

def look_and_say_sequence(first_element, n):
    '''Takes a starting string (not necessarily the classical "1") 
    and return the nth element of the series.'''
    a = [first_element+'.']
    while len(a) < n:
        s, number, x = '', '', a[-1]
        for i in range(len(x)-1):
            if x[i] == x[i+1]:
                s += x[i]
            else:
                s += x[i]; number += (str(len(s))+s[0]); s = ''
        a.append(number+'.')
    return a[n-1][:-1]


string = input('input the starting string: ')
n = int(input('input the series item number: '))
print(look_and_say_sequence(string, n))