import re


def password_validator(password):
    '''valid password criteria: at least six characters long, 
    contains a lowercase letter, contains an uppercase letter, contains a number'''
    regex = re.compile('''
                ^
                (?=.*?[a-z])
                (?=.*?[A-Z])
                (?=.*?[0-9])   # at least one number
                [A-Za-z\d]
                {6,}
                $
                ''', re.VERBOSE)
    return bool(re.search(regex, password))


print(password_validator(input('enter password: ')))    