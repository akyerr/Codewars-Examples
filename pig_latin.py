'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !'''
from string import punctuation
def pig_it(text):

    words = text.split(' ')
    # print(words)

    all_punc = punctuation
    # print(all_punc)
    result = []
    for word in words:
        if word in all_punc:
            result.append(word)
        else:
            result.append(word[1:] + word[0] + 'ay')
    return ' '.join([str(elem) for elem in result])
    # return result


print(pig_it('Hello World !'))

'''
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
'''
