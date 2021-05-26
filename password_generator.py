from random import shuffle, randint
from string import ascii_lowercase, ascii_uppercase

def password_gen():
	'''Password generator'''
    low, upp, dig = list(ascii_lowercase), list(ascii_uppercase), list('0123456789')
    shuffle(low), shuffle(upp), shuffle(dig)
    return ''.join(low[:randint(2, 8)]+upp[:randint(2, 6)]+dig[:randint(2, 6)])


print(password_gen())    