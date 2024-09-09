'''
Dhruti Vadlamudi
Spell Checker Project
'''

from spell_checker import SpellChecker
import time


def main():
    dictionary_path = input("Dictionary: ")
    essay_path = input("Essay to check: ")
    start = time.time()
    s = SpellChecker(dictionary_path)
    misspelled_words = s.spell_check(essay_path)
    suggestions = {wi.get_word(): s.suggest_corrections(wi.get_word()) for wi in misspelled_words}
    end = time.time()
    elapsed = end - start
    print(f'Time to spellcheck: {elapsed:.3f}')
    print("Misspelled Words:")
    for word_info in misspelled_words:
        print(word_info)
    print("\nSuggested Corrections:")
    for item in suggestions:
        word = item
        suggestion_list = suggestions[item]
        # Used Github code for help with formatting
        print("{0:15} -> {1}".format(word, ', '.join(suggestion_list)))


if __name__ == '__main__':
    main()
