'''
Dhruti Vadlamudi
Period 4
Spell Checker Project
'''

class WordInfo:

    def __init__(self, misspelled, line, word_number, suggestions=None):
        self._misspelled = misspelled
        self._line = line
        self._word_number = word_number
        self._suggestions = suggestions

    def get_word(self):
        return self._misspelled

    def get_line(self):
        return self._line

    def get_word_number(self):
        return self._word_number

    def get_suggestions(self):
        return self._suggestions

    def modify_suggestions(self, val):
        self._suggestions = val

    def __str__(self):
        so_far = f"{self._misspelled:>15}:  line:{self._line:>4}   word:{self._word_number:>3}"
        if self._suggestions:
            strin = ', '.join(self._suggestions)
            return f"{so_far}. Suggestions: [{strin}]"
        return so_far
