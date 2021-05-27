import re


def change_case(s, target_case):
    '''Converts between camelCase, snake_case, and kebab-case'''
    types = {
    'snake': re.match(r'[a-z](_?[a-z]+_?[a-z]+)*', s),
    'camel': re.match(r'[a-z][a-zA-Z]+', s),
    'kebab': re.match(r'[a-z](-?[a-z]+-?[a-z]+)*', s),
    }
    # First, we find out the case type of the input string
    current_case = [[None] + [i for i in types if bool(types[i]) and types[i].group() == s]][-1][-1]
    convert = {
    'camel_to_snake': re.sub(r'([A-Z])', lambda x: '_'+x.group().lower(), s),
    'kebab_to_snake': re.sub(r'-|[A-Z]', '_', s),
    'snake_to_camel': re.sub(r'_\w', lambda x: x.group().upper()[1:], s),
    'kebab_to_camel': re.sub(r'-\w', lambda x: x.group().upper()[1:], s),
    'snake_to_kebab': re.sub(r'_|[A-Z]', '-', s),
    'camel_to_kebab': re.sub(r'([A-Z])', lambda x: '-'+x.group().lower(), s)
    }
    # Then we convert the string according to its case type to the required type
    if s:
        return convert.get(f'{current_case}_to_{target_case}') if current_case != target_case else s
    else:
        return ''


# Examples
# change_case("snakeCase", "snake") == "snake_case"
# change_case("some-lisp-name", "camel") == "someLispName"
# change_case("map_to_all", "kebab") == "map-to-all"
# change_case("doHTMLRequest", "kebab") == "do-h-t-m-l-request"
# change_case("invalid-inPut_bad", "kebab") == None
# change_case("valid-input", "huh???") == None
# change_case("", "camel") == ""


string = input('enter string: ')
case = input('enter case(snake, camel, kebab): ')
print(change_case(string, case))