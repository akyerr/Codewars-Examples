"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""

def count(input_str):
	return (input_str.count('a') +  input_str.count('e') +  input_str.count('i') +  input_str.count('o') +  input_str.count('u'))


print(count("o a kak ushakov lil vo kashu kakao"))