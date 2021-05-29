# A prototype that supports the version control system,
# which will allow to save different versions of the text
# and restore any one of them.

class Text:
    '''Works with texts (adding, font changing, etc.)'''
    def __init__(self):
        self.current_text = ''
        self.current_font = ''

    def write(self, new_text):
        '''adds (text) to the current text;font is applied to the whole text,
        even if it’s added after the font is set;
        the font is displayed in the square brackets before and after the text: "[Arial]...example...[Arial]";
        Font can be specified multiple times but only the last variant is displays'''
        self.current_text += new_text

    def set_font(self, new_font):
        ''' sets the chosen font'''
        self.current_font = new_font

    def show(self):
        '''returns the current text and font (if is was set)'''
        if not self.current_font:
            return f"{self.current_text}"
        else:
            return f"[{self.current_font}]{self.current_text}[{self.current_font}]"    

    def restore(self, saved_text_version):
        '''restores the text of the chosen version'''
        self.current_text = saved_text_version[0]
        self.current_font = saved_text_version[1]


class SavedText:
    '''Controls the versions and save them.'''
    def __init__(self):
        self.versions = {}
        self.count = 0

    def save_text(self, text):
        '''saves the current text and font;
        the first saved version has the number 0, the second - 1, and so on'''
        self.versions[self.count] = [text.current_text, text.current_font]
        self.count += 1

    def get_version(self, number):
        '''this method works with the 'restore' method
        and is used for choosing the needed version of the text'''
        return self.versions[number]


# Example

text = Text()
saver = SavedText()
    
text.write("At the very beginning ")
saver.save_text(text)
text.set_font("Arial")
saver.save_text(text)
text.write("there was nothing.")
text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
text.restore(saver.get_version(0))
text.show() == "At the very beginning "
