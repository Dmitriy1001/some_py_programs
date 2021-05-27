from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits 


def check_password(password):
    '''Strong password criteria. 8 to 20 characters, 
    Contains only the following symbols 
    (and at least one symbol from each category): 
    capital letters, lower case, numbers special characters from! @ # $% ^ & *?
    '''
    valid_char = ascii_letters + digits + '!@#$%^&*?'
    return any(i.islower() for i in password) and\
           any(i.isupper() for i in password) and\
           any(i.isdigit() for i in password) and\
           any(i in '!@#$%^&*?' for i in password) and\
           all(i in valid_char for i in password) and\
           8 <= len(password) <= 20


print('Strong' if \
    check_password(input('Input a password: ')) else \
    'Not strong'
    )           


