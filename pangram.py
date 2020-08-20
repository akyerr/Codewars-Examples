'''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.'''

import string


def is_pangram(s):

    lower_case = ''.join([i for i in s.lower() if not i.isdigit()])
    no_punc = "".join([i for i in lower_case if i not in string.punctuation])

    unique_str = set("".join(no_punc.split(' ')))

    return len(unique_str) == 26

# def is_pangram(s):
#     print(string.lowercase)

#     print(set(s.lower()))
#     return set(string.lowercase) <= set(s.lower())


print(is_pangram('Te quick, brown fox jumps over te lazy dog 1 2'))
