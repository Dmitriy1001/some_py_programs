def braces_status(string):
    string, lst = [i for i in string if i in('(','[','{',')',']','}')], []

    for i in string:
        if i in ('(','[','{'): 
            lst.append(i)
        else:
            if lst and lst[-1] + i in ('()', '[]', '{}'): lst = lst[:-1]
            else: return False

    else: return not lst


print(braces_status(input('input string: ')))