'''
Dhruti Vadlamudi
Period 4
Spell Checker Project
'''

import re
from levenshtein import lev_distance
from word_info import WordInfo


class SpellChecker:

    def __init__(self, dictionary):
        with open(dictionary) as f:
            self.dictionary = set(f.read().split())

    def spell_check(self, file_name):
        '''
        This will check the spelling of everyword in the file_name.
        It will return a list of WordInfo objects that describe the words misspelled.
        '''
        word_info_list = []
        with open(file_name) as f:
            line_count = 0
            for line in f:
                line_count += 1
                words = line.split()
                word_count = 0
                for word in words:
                    word_count += 1
                    word = normalize_token(word)
                    if self.misspelled(word):
                        word_info_list.append(WordInfo(word, line_count, word_count))
        return word_info_list

    def misspelled(self, word):
        '''
        This method MUST deal with hyphenated words.
        If any part of a hyphenated word is misspelled, then the whole word
        is misspelled.

        word   is not normalized and may or may not be hyphenated.
        return True if the word is misspelled, False if spelled correctly.
        '''
        word = normalize_token(word)
        if '-' in word:
            word = word.split('-')
            for letter in word:
                if letter not in self.dictionary:
                    return True
            return False
        else:
            return word not in self.dictionary

    def suggest_corrections(self, word):
        '''
        word : the misspelled word to find suggestions for

        Return a list of all the suggested words that share the same minimum
        distance from word using the levenshtein distance algorithm.
        '''
        word = normalize_token(word)
        if '-' in word:
            parts = word.split('-')
            suggestions = [self._process_word(part) for part in parts]
            # initialize with first list of suggestions wrapped in list
            combined = [[letter] for letter in suggestions[0]] if suggestions else []
            # combines the suggestions from the initialized list of suggestions
            # with the combined list of suggestions offset by one
            for suggests in suggestions[1:]:
                combined = [before + [now] for before in combined for now in suggests]
            # Join back all of the combined suggestions
            combined = ['-'.join(suggest) for suggest in combined]
            return sorted(set(combined))
        else:
            return self._process_word(word)

    def _process_word(self, word):
        minimum = None
        main_words = []
        for item in self.dictionary:
            distance = lev_distance(word, item)
            if minimum is None or distance < minimum:
                minimum = distance
                main_words = [item]
            elif distance == minimum:
                main_words.append(item)
        return sorted(main_words)

    def suggest_mismisspellings(self, word, max=6):
        '''
        word : the misspelled word to find suggestions for
        max : the max size of the list returned

        Return a list of all the suggested words by using the mis-misspelled
        approach. See instructions.
        '''
        if word in self.dictionary:
            return [word]
        words = set()
        for word_ins in self._insert_letters(word):
            for word_del in self._remove_letters(word_ins):
                for word_swap in self._swap_letters(word_del):
                    if word_swap in self.dictionary and len(words) < max:
                        words.add(word_swap)
                    if len(words) >= max:
                        break
                if len(words) >= max:
                    break
            if len(words) >= max:
                break
        return list(words)

    def _insert_letters(self, word):
        '''
        This is a generator that will insert a-z at all location in the word
        '''
        yield word
        for num in range(len(word)+1):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                yield word[:num] + letter + word[num:]

    def _remove_letters(self, word):
        '''
        This is a generator that will remove each letter one at a time
        '''
        yield word
        for num in range(len(word)):
            yield word[:num] + word[num + 1:]

    def _swap_letters(self, word):
        '''
        This is a genertor that will replace each letter with a-z.
        This is sort of like a composition of insert & remove letters
        '''
        yield word
        for num in range(len(word)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter != word[num]:
                    yield word[:num] + letter + word[num + 1:]


def normalize_token(token):
    '''
    remove non-alphabetic characters using a regular expression
    don't forget to handle upper vs lowercase letters. Let's go lowercase.
    The hyphen is NOT removed. It remains.
    '''
    return re.sub(r"[^A-Za-z\-]", "", token.lower())
