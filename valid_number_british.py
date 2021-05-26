import re

def validate_number(string):
	'''checks if the string is a valid UK mobile phone number or not'''
    numb = re.match(r'-*(0|\+44)-*7([\d-]+)', string)
    return numb and len([i for i in numb.group(2) if i.isdigit()]) == 9\
           and numb.group() == string


print(
	['Invalid', 'Valid'][validate_number(input('Input number: '))]
)    
    