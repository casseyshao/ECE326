# Lab 3

# Design a new utspell program similar to unix spell program.
# Use /usr/share/dict/words as the English dictionary.

import sys
import string

def utspell():

    english_dict = open('/usr/share/dict/words').read().split('\n')

    misspelled = set() # Initialize a set to hold the unique misspelled words.

    translate_punc = str.maketrans(string.punctuation, ' '*len(string.punctuation)) # Translator for replacing punctuation with spaces.

    if len(sys.argv) <= 1:
        print("No words supplied.")
        return

    if sys.argv[1] == "-f": # Read from file(s).
        i = 2
        while i < len(sys.argv):
            file_data = open(sys.argv[i], 'r').read().translate(translate_punc).split() # Replace punctuation.
            for word in file_data:
                if word not in english_dict:
                    misspelled.add(word)
            i += 1
    elif sys.argv[1] == "-c": # Read from command line.
        data = ' '.join(sys.argv[2:])
        data = data.translate(translate_punc) # Replace punctuation.
        data = data.split()
        for word in data:
            if word not in english_dict:
                misspelled.add(word)

    # Print each element in the set of misspelled words on its own line.
    for word in misspelled:
        print(word)

utspell()

