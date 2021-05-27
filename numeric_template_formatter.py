import re


def numeric_formatter(template, num='1234567890'):
    formated_num = re.sub(r'[a-zA-Z]', '{}', template)
    len_template = len([i for i in template if i.isalpha()])
    while len(num) < len_template:
        num += num[:len_template]
    return formated_num.format(*num)


#numeric_formatter("xxx xxxxx xx","5465253289") == "546 52532 89"
#numeric_formatter("xxx xxxxx xx") == "123 45678 90"
#numeric_formatter("+555 aaaa bbbb", "18031978") == "+555 1803 1978"
#numeric_formatter("+555 aaaa bbbb") == "+555 1234 5678"
#numeric_formatter("xxxx yyyy zzzz") == "1234 5678 9012"


template = input('input template: ')
number = input('input number(press enter to leave the field empty): ')
print(
	numeric_formatter(template, number) if number else\
	numeric_formatter(template)
)    