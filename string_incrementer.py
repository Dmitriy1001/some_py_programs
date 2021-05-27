import re


def increment_string(s):
    '''Increments a string, to create a new string.'''
    if s:
        numbers = re.search(r'\d*$', s)

        if bool(numbers):
            letters = s[:numbers.start()]
            numbers = numbers.group()

            if not all(i == '0' for i in numbers):
                incremented = int(re.search(r'0*(\d*)', numbers).group(1)) + 1
                numbers = str(incremented) if len(str(incremented)) >= len(numbers)\
                else numbers[:-len(str(incremented))] + str(incremented)
                return letters + numbers
            else:
                return letters+numbers[:-1]+'1'

        else:
            return s + '1'

    else: return '1'   


# Examples
#foo -> foo1
#foobar23 -> foobar24
#foo0042 -> foo0043
#foo9 -> foo10
#foo099 -> foo100

print(
   increment_string(input('enter string: ')) 
)    