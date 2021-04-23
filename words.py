def print_upper_words (words_in):
    '''this function takes a list of words and prints each word on a separate line in all caps'''
    for word in words_in:
        print(word.upper())
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
        
def print_upper_words_e (words_in):
    '''this function takes a list of words and only prints the ones that start with an upper of lower case "e"'''
    for word in words_in:
        if  word.startswith('e') or word.startswith('E'):
            print(word.upper())      
print_upper_words_e(["hello", "Eddie", "hey", "goodbye", "eat","yo", "yes"])

def print_upper_words_starts_with(words_in, starts_with):
    '''this function takes a list of words and only prints the ones that start with a set of passed in letters'''
    for word in words_in:
        for starts in starts_with:
            if word.startswith(starts):
                print(word.upper())
print_upper_words_starts_with(["hello", "Eddie", "hey", "goodbye", "eat","yo", "yes"], ['y', 'e', 'E', 'Y'])


