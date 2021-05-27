from random import shuffle, randint
from string import ascii_lowercase, ascii_uppercase


def password_gen():
	'''Generator meets the following criteria: 6 - 20 characters long, 
	contains at least one lowercase letter, one uppercase letter, one number,
	contains only alphanumeric characters (no special characters)'''
    low, upp, dig = list(ascii_lowercase), list(ascii_uppercase), list('0123456789')
    shuffle(low), shuffle(upp), shuffle(dig)
    return ''.join(low[:randint(2, 8)]+upp[:randint(2, 6)]+dig[:randint(2, 6)])


print(password_gen())    