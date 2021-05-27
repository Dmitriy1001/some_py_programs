import re


def is_valid_coordinates(coords):
    '''Validates if given parameters are valid geographical coordinates.'''
    match = re.match(r'-?[0-9]{1,2}(\.?\d+)?\b, -?[0-9]{1,3}(\.?\d+)?\b', coords)
    try:
        coord1, coord2 = match.group().split(', ')
        return match.group() == coords and \
        eval(f'-90 <= {float(coord1)} <= 90') and eval(f'-180 <= {float(coord2)} <= 180')
    except:
        return False


#Here are some valid coordinates:
# -23, 25
# 24.53525235, 23.45235
# 04, -23.234235
# 43.91343345, 143
# 4, -3

#And some invalid ones:
# 23.234, - 23.4234
# 2342.43536, 34.324236
# N23.43345, E32.6457
# 99.234, 12.324
# 6.325624, 43.34345.345
# 0, 1,2
# 0.342q0832, 1.2324


coord1, coord2 = input('input coordinate 1: '), input('input coordinate 2: ')
print(
    is_valid_coordinates(f'{coord1}, {coord2}')
)