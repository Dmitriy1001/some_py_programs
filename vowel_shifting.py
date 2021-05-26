import re

def vowel_shift(string, n):
	'''The function shifts the vowels by "n" positions to the right.
	   (if n is negative - to the left.)'''
	vowels = re.findall(r'[aeiouAEIOU]', string)
	string = re.sub(r'[aeiouAEIOU]', '{}', string)
	n = n % len(vowels) if vowels else 0 
	return string.format(*vowels[len(vowels)-n:]+vowels[:len(vowels)-n])


# Example

#text = "This is a test!"
#n = 1
#output = "Thes is i tast!"

#text = "This is a test!"
#n = 3
#output = "This as e tist!"


string = input('input string: ')
n = int(input('how many positions to shift the vowels: '))

print(vowel_shift(string, n))