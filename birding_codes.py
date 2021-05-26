import re

def bird_code(lst):
    '''The function  takes an array of strings of common bird names
    from North America, and create the codes for those names.'''
    one_w = [(lst[i][:4].upper(), i) for i in range(len(lst)) if re.match(r'^[a-zA-Z\']+$', lst[i])]
    two_w = [(re.sub(r"([a-zA-Z\']+)[-\s]([a-zA-Z\']+)", lambda x: x.group(1)[:2]+x.group(2)[:2], lst[i]).upper(), i) for i in range(len(lst)) if re.match(r'^[a-zA-Z\']+[\s-][a-zA-Z\']+$', lst[i])]
    three_w = [(re.sub(r'([a-zA-Z\']+)[-\s]([a-zA-Z\']+)[-\s]([a-zA-Z\']+)', lambda x: x.group(1)[0]+x.group(2)[0]+x.group(3)[:2], lst[i]).upper(), i) for i in range(len(lst)) if re.match(r'^[a-zA-Z\']+[\s-][a-zA-Z\']+[\s-][a-zA-Z\']+$', lst[i])]
    four_w = [(re.sub(r'([a-zA-Z\']+)[-\s]([a-zA-Z\']+)[-\s]([a-zA-Z\']+)[-\s]([a-zA-Z\']+)', lambda x: x.group(1)[0]+x.group(2)[0]+x.group(3)[0]+x.group(4)[0], lst[i]).upper(), i) for i in range(len(lst)) if re.match(r'^[a-zA-Z]+[\s-][a-zA-Z]+[\s-][a-zA-Z]+[\s-][a-zA-Z]+$', lst[i])]
    return [i[0] for i in sorted(one_w+two_w+three_w+four_w, key=lambda x: x[1])]


# Example
# bird_code(["Common Tern", "Black-Capped Chickadee"]) == ["COTE","BCCH"]

birds_list = input('input a list of birds separated by commas: ').split(',')
print(bird_code(birds_list))
