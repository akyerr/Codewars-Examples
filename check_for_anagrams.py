'''Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []'''


def anagrams(word, words):
    word = ''.join(sorted(word))
    result = []
    for ind, st in enumerate(words):
        st = ''.join(sorted(st))
        if st == word:
            result.append(ind)
    return [words[i] for i in result]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
