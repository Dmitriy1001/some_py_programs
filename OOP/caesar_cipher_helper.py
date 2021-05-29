class CaesarCipher(object):
    '''    The class returns an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.
    If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leaves it.
    The shift must always be in range of [1, 26].'''
    def __init__(self, shift):
        self.shift = shift
        self.alph = [chr(i).upper() for i in range(ord('a'), ord('a')+26)]

    def encode(self, s):
        res = ''
        for i in s.upper():
            if i in self.alph:
                res += self.alph[self.alph.index(i) - (26-self.shift%26)]
            else:
                res += i
        return res            
        
    def decode(self, s):
        res = ''
        for i in s.upper():
            if i in self.alph:
                res += self.alph[self.alph.index(i) - (self.shift%26)]
            else:
                res += i
        return res


#c = CaesarCipher(5)
#c.encode('Codewars')  returns 'HTIJBFWX'
#c.decode('BFKKQJX')   returns 'WAFFLES'
