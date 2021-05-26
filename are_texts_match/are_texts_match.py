from difflib import SequenceMatcher
import numpy as np
import itertools

def match_texts(text1, text2):
    '''Returns true if the two texts match 70 percent or more'''
    similarity = lambda x: np.mean([SequenceMatcher(None, a,b).ratio() for a,b in itertools.combinations(x, 2)])
    text1, text2 = ' '.join(sorted(text1.lower().split())), ' '.join(sorted(text2.lower().split()))
    return similarity([text1, text2]) >= 0.7


def read_file(file):
	with open(file, encoding='utf-8') as f:
		return f.read().strip()


def main():
	input_or_path = input(
	'Do you want to input strings or specify the path to text files? 1-input, 2-path: '
	)
	if input_or_path == '1':
		text1 = input('Input string 1:')
		text2 = input('Input string 2:')
	else:
		text1 = read_file(input('Path to file 1:')) 
		text2 = read_file(input('Path to file 2:'))
	print('The texts math' if match_texts(text1, text2) else \
		  'The texts do not math')


if __name__ == '__main__':
	main()

