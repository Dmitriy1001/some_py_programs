import re


def life_path_number(birthday):
    '''A person's Life Path Number is calculated by adding each individual number in that person's date of birth,
    until it is reduced to a single digit number.'''
    birthday = re.findall(r'\d+', birthday)
    sum_n = lambda n: sum([int(i) for i in str(n)])
    all_sum = 0
    for i in birthday:
        while len(str(i)) > 1:
            i = sum_n(i)
        all_sum += i
    while len(str(all_sum)) > 1:
        all_sum = sum_n(all_sum)
    return all_sum


# For example 1879-03-14
# year  :  1 + 8 + 7 + 9 = 25  -->  2 + 5 = 7
# month :  0 + 3 = 3
# day   :  1 + 4 = 5
# result:  7 + 3 + 5 = 15  -->  1 + 5 = 6


print(life_path_number("input date of birth(yyyy-mm-dd): "))        