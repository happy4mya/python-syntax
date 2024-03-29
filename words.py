def print_upper_words(words):
    """Print each word in uppercase on a separate line"""
    for word in words:
        print(word.upper())

# words = ['orion', 'cassiopeia', 'crux', 'ursa', 'eridanus', 'hydra', 'pegasus', 'centaurus']
# print_upper_words(words)                   

def print_upper_words_e(words):
    """Print each word in uppercase on a separate line starting with either 'e' or 'E' """ 
    for word in words:
        if word.startswith('E') or word.startswith('e'):
            print(word.upper())

# words = ['orion', 'cassiopeia', 'crux', 'ursa', 'eridanus', 'hydra', 'pegasus', 'centaurus']
# print_upper_words_e(words)       
            

def print_upper_words_letters(words, must_start_with):
    for word in words:
        lower_word = word.lower()
        if any(lower_word.startswith(letter) for letter in must_start_with):
            print(word.upper())

        
#  words = ['orion', 'cassiopeia', 'crux', 'ursa', 'eridanus', 'hydra', 'pegasus', 'centaurus']
# must_start_with = ["o", "c"]
# print_upper_words_letters(words, must_start_with)        








